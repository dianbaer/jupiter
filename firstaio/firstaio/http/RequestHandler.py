import inspect
import logging

from aiohttp import web


class RequestHandlerC():
    def __init__(self, app, fn):
        self._app = app
        self._fn = fn
        # 是否有request
        self._has_request_arg = RequestHandlerC.has_request_arg(fn)
        # 是否有**kw
        self._has_var_kw_arg = RequestHandlerC.has_var_kw_arg(fn)
        # 是否有 *,xxx
        self._has_named_kw_args = RequestHandlerC.has_named_kw_args(fn)
        # 是否有*args
        self._has_positional_kw_args = RequestHandlerC.has_positional_kw_args(fn)
        # *,xxx后面的参数
        self._named_kw_args = RequestHandlerC.get_named_kw_args(fn)
        # *,xxx后面的参数并且没有默认值
        self._required_kw_args = RequestHandlerC.get_required_kw_args(fn)

    async def __call__(self, request):
        kw = None
        if self._has_named_kw_args:
            if request.method == 'POST':
                if not request.content_type:
                    return web.HTTPBadRequest('Missing Content-Type.')
                ct = request.content_type.lower()
                if ct.startswith('application/json'):
                    params = await request.json()
                    if not isinstance(params, dict):
                        return web.HTTPBadRequest('JSON body must be object.')
                    kw = params
                elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
                    params = await request.post()
                    kw = dict(**params)
                else:
                    return web.HTTPBadRequest('Unsupported Content-Type: %s' % request.content_type)
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

    @classmethod
    def get_named_kw_args(cls, fn):
        args = []
        sig = inspect.signature(fn)
        params = sig.parameters
        for name, param in params.items():
            if param.kind == inspect.Parameter.KEYWORD_ONLY:
                args.append(name)
        if len(args) > 0:
            logging.info('get_named_kw_args:%s(%s),args%s' % (fn.__name__, ', '.join(params.keys()), str(args)))
        return tuple(args)

    @classmethod
    def get_required_kw_args(cls, fn):
        args = []
        sig = inspect.signature(fn)
        params = sig.parameters
        for name, param in params.items():
            if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
                args.append(name)
        if len(args) > 0:
            logging.info('get_required_kw_args:%s(%s),args%s' % (fn.__name__, ', '.join(params.keys()), str(args)))
        return tuple(args)
