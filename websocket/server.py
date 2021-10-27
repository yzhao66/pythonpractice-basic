import asyncio
import websockets
import time


async def echo(websocket, path):
    async for message in websocket:
        result_message = "I got your message: {}".format(message)
        await websocket.send(result_message)

        while True:
             t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
             if str(t).endswith("0"):
                 await websocket.send(t)
                 break


asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
