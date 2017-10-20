import inspect
import os

import logging

from jupiter_http.RequestHandler import RequestHandlerC


class RouteC():
    @classmethod
    def init(cls, app, fold_path, packet_path):
        handlerList = [x for x in os.listdir(fold_path) if
                       os.path.splitext(x)[0] != '__init__' and os.path.splitext(x)[1] == '.py']
        for handler in handlerList:
            n = handler.rfind('.')
            mod = __import__(packet_path + handler[:n], globals(), locals(), ['py'])
            for attr in dir(mod):
                if attr.startswith('_'):
                    continue
                fn = getattr(mod, attr)
                if callable(fn):
                    method = getattr(fn, '__method__', None)
                    path = getattr(fn, '__route__', None)
                    if method and path:
                        RouteC.addApp(app, fn)

    @classmethod
    def addApp(cls, app, fn):
        method = getattr(fn, '__method__', None)
        path = getattr(fn, '__route__', None)
        if path is None or method is None:
            raise ValueError('@get or @post not defined in %s.' % str(fn))
        logging.info('add route %s %s => %s(%s)' % (
            method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
        requestHandler = RequestHandlerC(app, fn)
        if app is not None:
            app.router.add_route(method, path, requestHandler)

    @classmethod
    def initStatic(cls, app, path):
        logging.info('add static %s => %s' % ('/static/', path))
        if app is not None:
            app.router.add_static('/static/', path)
