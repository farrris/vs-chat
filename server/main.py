from aiohttp import web
import aiohttp_cors

app = web.Application()

async def index(request):
  res = {"msg": "Init"}
  return web.json_response(res)

app.router.add_get('/', index)

cors = aiohttp_cors.setup(app, defaults={
   "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*"
    )
  })

for route in list(app.router.routes()):
  cors.add(route)

if __name__ == "__main__":
  web.run_app(app, port=4000)