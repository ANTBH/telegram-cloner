from telethon import TelegramClient

# استخدام بياناتك
api_id = '12847352'  # ضع هنا API ID الخاص بك
api_hash = '19b76e60ee49e2356497d361cabcf7a8'  # ضع هنا API Hash الخاص بك
session_name = '+212652935228'  # اسم الجلسة الجديدة

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    print("Logged in successfully!")

with client:
    client.loop.run_until_complete(main())
