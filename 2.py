# from pyrogram import Client
# from typing import AsyncGenerator
# from pyrogram.types import Message
# import asyncio
# api_id = 28556510
# api_hash = 'e6544881e867e4a7d92295ffd67d11b7'
#
#
# async def reversed_messages(messages: AsyncGenerator):
#     reverse_message = [message async for message in messages]
#     return reverse_message[::-1]
#
#
# async def clone_content(donor_channel_id: int, my_channel_id: int):
#     client = Client("session_name", api_id, api_hash)
#     await client.start()
#
#     messages: AsyncGenerator[Message, None] = client.get_chat_history(donor_channel_id, limit=1000)
#
#     reversed_message = await reversed_messages(messages=messages)
#     for message in reversed_message:
#         await message.copy(chat_id=my_channel_id)
#
# if __name__ == "__main__":
#     asyncio.run(clone_content(donor_channel_id=-4118104135, my_channel_id=-4199732341))


