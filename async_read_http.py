import asyncio
import aiohttp

# async function to perform http get requests asynchronously
async def read_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

# main function to run to call the async function to perform http get requests asynchronously
async def main():
    urls = ['http://www.google.com', 'https://www.prudential.com']
    tasks = [asyncio.create_task(read_url(url)) for url in urls]
    await asyncio.wait(tasks)
    for task in tasks:
        print(task.result())

if __name__ == '__main__':
    asyncio.run(main())