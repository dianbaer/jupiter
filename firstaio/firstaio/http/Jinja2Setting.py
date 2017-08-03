import logging
import os

from jinja2 import Environment, FileSystemLoader

from firstaio.http.Jinja2Filter import datetime_filter


class Jinja2SettingC():
    @classmethod
    def init(cls, app, **kwargs):
        logging.info('init jinja2...')
        options = dict(
            autoescape=kwargs.get('autoescape', True),
            block_start_string=kwargs.get('block_start_string', '{%'),
            block_end_string=kwargs.get('block_end_string', '%}'),
            variable_start_string=kwargs.get('variable_start_string', '{{'),
            variable_end_string=kwargs.get('variable_end_string', '}}'),
            auto_reload=kwargs.get('auto_reload', True)
        )
        path = kwargs.get('path', None)
        if path is None:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
        logging.info('set jinja2 template path: %s' % path)
        env = Environment(loader=FileSystemLoader(path), **options)
        filters = kwargs.get('filters', None)
        if filters is not None:
            for name, f in filters.items():
                env.filters[name] = f
        if app is not None:
            app['__templating__'] = env


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    Jinja2SettingC.init(None,
                        path='C:\\Users\\admin\\Desktop\\github\\firstaio\\trunk\\firstaio\\firstaio\\http\\templates',
                        filters=dict(datetime=datetime_filter))
