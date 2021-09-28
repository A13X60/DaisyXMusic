import asyncio

from pyrogram import Client

print("Enter your app information from my.telegram.org/apps below.")


async def main():
    async with Client(
        ":memory:", api_id=int(input("8965144:")), api_hash=input("357b13c12870043a009356a3fb3f0366:")
    ) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
