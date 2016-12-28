import asyncio

PERIOD = 2

@asyncio.coroutine
def readline(f):
    while True:
        #yield from asyncio.sleep(PERIOD)
        data = f.readline()
        if data:
            return data
        else:
            return None
        

@asyncio.coroutine
def test(filename):
    with open(filename) as f:
        while True:
            line = yield from readline(f)
            print('Got {}: {!r}'.format(filename,line))
            if not line: break

loop = asyncio.get_event_loop()
tasks = [test(filename) for filename in ['asyncio_hello_world.py', 'test.txt', 'wget.py']]
loop.run_until_complete(asyncio.wait(tasks))
#loop.run_until_complete(test())
loop.close()
