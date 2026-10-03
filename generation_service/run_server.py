import asyncio
import sys

import uvicorn


def run_server():
    config = uvicorn.Config(
        'src.main:app',
        host='localhost',
        port=8000,
        reload=True,
    )
    server = uvicorn.Server(config)

    try:
        if sys.platform == 'win32':
            asyncio.run(server.serve(), loop_factory=asyncio.SelectorEventLoop)
        else:
            asyncio.run(server.serve())
    except KeyboardInterrupt:
        print('Сервер остановлен.\n')


if __name__ == '__main__':
    run_server()
