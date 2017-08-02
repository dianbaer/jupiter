import logging

from aiohttp import web


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
        return r

    return response
