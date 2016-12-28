import asyncio
import datetime

def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()

loop = asyncio.get_event_loop()

# Schedule the first call to display_date()
end_time = loop.time() + 5.0
print(end_time)
#loop.call_soon(display_date, end_time, loop)
loop.call_later(1, display_date, end_time, loop)
loop.stop()
# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
