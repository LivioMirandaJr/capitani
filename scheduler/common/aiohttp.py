import aiohttp


class SingletonAiohttp:
    aiohttp_client: aiohttp.ClientSession | None = None

    @classmethod
    async def get_aiohttp_client(cls) -> aiohttp.ClientSession:
        if cls.aiohttp_client is None:
            # timeout = aiohttp.ClientTimeout(total=10)
            connector = aiohttp.TCPConnector(keepalive_timeout=30)
            # cls.aiohttp_client = aiohttp.ClientSession(timeout=timeout, connector=connector)
            cls.aiohttp_client = aiohttp.ClientSession(connector=connector)
        return cls.aiohttp_client

    @classmethod
    async def close_aiohttp_client(cls) -> None:
        if cls.aiohttp_client:
            await cls.aiohttp_client.close()
            cls.aiohttp_client = None

    @classmethod
    async def post(cls, url: str, body: any) -> dict | list | set:
        client = await cls.get_aiohttp_client()
        response = await client.post(url, data=body)
        json_result = await response.json()
        return json_result
