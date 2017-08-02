import logging

from aiohttp import web
import json


async def response_factory(app, handler):
    async def response(request):
        logging.info('%s response_factory response start next handler %s ' % (request['first_aio_uuid'], handler))
        r = await handler(request)
        logging.info('%s response_factory response end ' % (request['first_aio_uuid']))
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            template = r.get('__template__')
            if template is not None:
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
            else:
                resp = web.Response(
                    body=json.dumps(r, ensure_ascii=False).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
        return r

    return response
