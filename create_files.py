import asyncio, aiofiles, logging

async def create_file(filename):
    async with aiofiles.open(filename, mode='w') as f:
        for _ in range(1_000):
            await f.write('Hello\n')

        print(f"Created file {filename}")

async def main():
    t1 = asyncio.create_task(create_file('one.txt'))
    t2 = asyncio.create_task(create_file('two.txt'))
    t3 = asyncio.create_task(create_file('three.txt'))

    for t in [t1, t2, t3]:
        await t

logging.basicConfig(level=logging.DEBUG)
asyncio.run(main(), debug=True)
