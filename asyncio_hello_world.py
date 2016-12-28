import asyncio
import time

def hello_world(loop):
    time.sleep(3)
    print('hello world')
    

loop = asyncio.get_event_loop()
loop.call_soon(hello_world, loop)
#loop.stop()
loop.run_forever()
loop.close()
