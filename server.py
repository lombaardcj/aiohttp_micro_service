from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes([web.get('/', hello)])

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
