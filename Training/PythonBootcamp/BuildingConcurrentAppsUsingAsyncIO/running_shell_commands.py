import asyncio


# creating a coroutine that takes as argument the command that will run asynchronously
async def run(cmd):
    #  To run the command I'll use the create_subprocess_shell() function of the asyncio library.
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    # Each Linux command returns a status code which is zero if there was no error and different from zero if there was error.
    print(f'{cmd} exited with status code: {proc.returncode}]')

    # if the command has generated any output we can access it by using stdout.decode()
    if stdout:
        print(f'STDOUT:\n{stdout.decode()}')

    if stderr:
        print(f'STDERROR:\n{stderr.decode()}')


# defining the top level coroutine which is the async application starting point.
# this coroutine will take a list of commands as argument and spawn a task asynchronously for each command.
async def main(commads):
    tasks = []
    for cmd in commads:
        tasks.append(run(cmd))

    # and we schedule the coroutines to run asap by gathering the tasks.
    await asyncio.gather(*tasks)


# running some random Linux commands asynchronously.
commands = ('ifconfig', 'ls', 'who', 'ping -c 1 8.8.8.8')
asyncio.run(main(commands))