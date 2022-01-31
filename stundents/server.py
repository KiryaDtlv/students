from quart import Quart

app = Quart(__name__)


dev = True

if dev:
    from quart_cors import cors
    app = cors(app, allow_origin='')

async def asyncio_run():
    await app.run_task(host='0.0.0.0', port=911)
