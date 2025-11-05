import asyncio
import time

async def send_email(num):
    print(f'Email sended {num}')
    await asyncio.sleep(1)
    print(f'Email {num} dostavleno')


start_time = time.time()

async def main():
    task = [send_email(i) for i in range(10)]
    await asyncio.gather(*task)
    print(f'Time elasped: {time.time() - start_time} s')

asyncio.run(main())
