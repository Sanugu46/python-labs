import asyncio
import aiofiles

# async function to read the file
async def read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        content = await file.read()
        print(content)

# main function to run to call the async function to read the files in parallel
async def main(): 
    file_paths = ['requirements.txt', 'LICENSE']
    tasks =[asyncio.create_task(read_file(f_path)) for f_path in file_paths]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())