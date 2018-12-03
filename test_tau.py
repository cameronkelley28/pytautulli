"""Example usage of pytautulli."""
import asyncio
import json
import aiohttp
from pytautulli import Tautulli

HOST = 'thebananastand.mynetgear.com'
PORT = '8083'
API_KEY = '18b83e60fb5e4717854430b6c678bea3'
SSL_ON = 'False'


async def test():
    """Example usage of pytautulli."""
    async with aiohttp.ClientSession() as session:
        data = Tautulli(HOST, PORT, API_KEY, LOOP, session, False)
        await data.test_connection()
        await data.get_data()

        print("Connection status:", data.connection_status)
        print(json.dumps(data.session_data, indent=4, sort_keys=True))
        print(json.dumps(data.home_data, indent=4, sort_keys=True))


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(test())
