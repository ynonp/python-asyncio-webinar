import asyncio, aiofiles, logging

async def create_file(filename):
    async with aiofiles.open(filename, mode='w') as f:
        for _ in range(10_000):
            f.write('Hello\n')

        print(f"Created file {filename}")

async def main():
    await create_file('one.txt')
    await create_file('two.txt')
    await create_file('three.txt')

logging.basicConfig(level=logging.DEBUG)
asyncio.run(main(), debug=True)
