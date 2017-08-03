import inspect
import logging


class RequestHandlerC():
    def __init__(self, app, fn):
        self._app = app
        self._fn = fn
        self._has_request_arg = RequestHandlerC.has_request_arg(fn)
        self._has_var_kw_arg = RequestHandlerC.has_var_kw_arg(fn)
        self._has_named_kw_args = RequestHandlerC.has_named_kw_args(fn)
        self._has_positional_kw_args = RequestHandlerC.has_positional_kw_args(fn)

    async def __call__(self, request):
        kw = dict()
        kw['request'] = request
        logging.info('%s RequestHandlerC call start next handler %s ' % (request.__uuid__, self._fn))
        r = await self._fn(**kw)
        logging.info('%s RequestHandlerC call end ' % (request.__uuid__))
        return r

    @classmethod
    def has_request_arg(cls, fn):
        sig = inspect.signature(fn)
        params = sig.parameters
        found = False
        for name, param in params.items():
            if name == 'request':
                found = True
                logging.info('has_request_arg:%s(%s)' % (fn.__name__, ', '.join(params.keys())))
                continue
            if found and (
                                param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
                raise ValueError(
                    'request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
        return found

    @classmethod
    def has_var_kw_arg(cls, fn):
        sig = inspect.signature(fn)
        params = sig.parameters
        for name, param in params.items():
            if param.kind == inspect.Parameter.VAR_KEYWORD:
                logging.info('has_var_kw_arg:%s(%s)' % (fn.__name__, ', '.join(params.keys())))
                return True

    @classmethod
    def has_named_kw_args(cls, fn):
        sig = inspect.signature(fn)
        params = sig.parameters
        for name, param in params.items():
            if param.kind == inspect.Parameter.KEYWORD_ONLY:
                logging.info('has_named_kw_args:%s(%s)' % (fn.__name__, ', '.join(params.keys())))
                return True

    @classmethod
    def has_positional_kw_args(cls, fn):
        sig = inspect.signature(fn)
        params = sig.parameters
        for name, param in params.items():
            if param.kind == inspect.Parameter.VAR_POSITIONAL:
                logging.info('has_positional_kw_args:%s(%s)' % (fn.__name__, ', '.join(params.keys())))
                return True
