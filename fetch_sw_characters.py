import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[
            fetch(session, f'http://swapi.co/api/people/{i}') for i in range(1, 5)
            ])

        print([x['name'] for x in results])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

