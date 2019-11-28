import asyncio
import logging

# 1. Start the server and listen -> start talking to it
# 2. Client connects -> read and reply
# 3. Client connects

connected_clients = 0

async def client_connected_handler(reader, writer):
    global connected_clients
    connected_clients += 1
    print(f"New client connected: {connected_clients}")
    line = await reader.readline()
    writer.write(line)
    await writer.drain()
    writer.close()
    connected_clients -= 1
    print(f"client left: {connected_clients}")

# Coroutine
async def tcp_echo_server():
    print("Starting a server")
    server = await asyncio.start_server(
            client_connected_handler,
            host='0.0.0.0',
            port='8080'
    )
    # .... ?

    await server.serve_forever()
    # .... 2 -> server_forerver will finish

# Main Loop
logging.basicConfig(level=logging.DEBUG)
asyncio.run(tcp_echo_server(), debug=True)

