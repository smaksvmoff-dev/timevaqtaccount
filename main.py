from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION_STRING")

TZ = ZoneInfo("Asia/Tashkent")

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

async def update_name():
    await client.start()
    print("✅ Ishga tushdi!")
    while True:
        now = datetime.now(TZ).strftime("%H:%M")
        await client(UpdateProfileRequest(first_name=f"> time: {now}"))
        print(f"✔ {now}")
        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(update_name())
