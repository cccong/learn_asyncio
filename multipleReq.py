import requests
import asyncio

async def req1():
    print('req 1')
    print(requests.get('http://checkip.amazonaws.com').text)

async def req2():
    print('req 2')
    print(requests.get('http://checkip.amazonaws.com').text)
    
async def req3():
    print('req 3')
    print(requests.get('http://checkip.amazonaws.com').text)
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    #loop.call_soon(req1)
    #print(1)
    #loop.call_soon(req2)
    #print(2)
    #loop.call_soon(req3)
    #print(3)
    #loop.stop()
    #loop.run_forever()
    tasks = [req1(),req2(),req3()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
