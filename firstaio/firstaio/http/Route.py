import os


class RouteC():
    @classmethod
    def init(cls, app, foldpath, packet_path):
        handlerList = [x for x in os.listdir(foldpath) if
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
                        print(fn)


if __name__ == '__main__':
    RouteC.init(None, 'C:\\Users\\admin\\Desktop\\github\\firstaio\\trunk\\firstaio\\firstaio\\http\\handler',
                'firstaio.http.handler.')
