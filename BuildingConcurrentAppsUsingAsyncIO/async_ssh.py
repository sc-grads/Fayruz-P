import asyncio
import asyncssh


# the first coroutine I'm gonna define will connect and authenticate using ssh to the ssh server and run a command
async def run_client(host, username, password, command):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        return await connection.run(command)


# I'm defining the top-level coroutine which will be the async application starting point.
# this coroutine will take a list of hosts and call or await the run_client() coroutine for each host.
async def run_multiple_clients(hosts):  # in previous asyncio examples the name of the top-level coroutine was main,
    # but this is not mandatory

    tasks = list()
    for host in hosts:
        task = run_client(host['host'], host['username'], host['password'], host['command'])
        tasks.append(task)
    results = await asyncio.gather(*tasks, return_exceptions=True)  # I want it to raise an Exception if it's the case.

    i = 0
    for result in results:
        i += 1
        # if the result was an Exception then I'll print it out
        if isinstance(result, Exception):
            print(f'Task {i} failed: {str(result)}')
        # if the command' exist status was not zero that means there was an error and I'll print it out
        elif result.exit_status != 0:
            print(f'Task {i} exited with status {result.exit_status}:')
            print(result.stderr, end='')
        else:  # and the else branch for the case where was neither an Exception was raised nor an error occurred.
            print(f'Task {i} succeeded:')
            print(result.stdout, end='')

        print(50 * '#')


hosts = [
    {'host': '192.168.0.105', 'username': 'u1', 'password': 'test123', 'command': 'ifconfig'},
    # I have a single linux vm so I'm gonna spawn an ssh task that runs a command on the same host
    {'host': '192.168.0.105', 'username': 'u1', 'password': 'test123', 'command': 'whox -a'},
    {'host': '192.168.0.105', 'username': 'u1', 'password': 'test1234', 'command': 'uname -a'}
]

asyncio.run(run_multiple_clients(hosts))