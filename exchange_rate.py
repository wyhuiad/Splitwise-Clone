import aiohttp
import asyncio
import ssl
import certifi

import pandas as pd

async def main(url):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            print("Content:", response.content)

        async with session.request('GET',url) as req:
            assert req.status == 200
            return await req.text()
            
url = 'https://api.hkma.gov.hk/public/market-data-and-statistics/monthly-statistical-bulletin/er-ir/er-eeri-daily?offset=0'

loop = asyncio.get_event_loop()
data = loop.run_until_complete(main(url))

df = pd.read_json(data)

exchangerate_df = pd.DataFrame.from_dict(df.at['records','result'])
print(exchangerate_df.head())

exchangerate_df.to_csv("exchange_rate.csv")