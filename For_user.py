from pyrogram import Client, filters

api_id = 23013698
api_hash = 'a02e867cc4e2e27b289437956c9e2049'

app = Client("session_name", api_id=api_id, api_hash=api_hash)

group_id_1 = -1002116274028
group_for_parsing_id = -1002100150828
group_for_parsing_id_2 = -1002105785999

async def get_last_message_id(client, chat_id):
    async for message in client.get_chat_history(chat_id, limit=1):
        return int(message.id)

@app.on_message(filters.group & ~filters.forwarded)
async def forward_message(client, message):
    try:
        if message.chat.id == group_for_parsing_id:
            last_message_id = await get_last_message_id(client, group_for_parsing_id)
            print(last_message_id)
            if last_message_id:
                await client.forward_messages(group_id_1, group_for_parsing_id, last_message_id)
        if message.chat.id == group_for_parsing_id_2:
            last_message_id_2 = await get_last_message_id(client, group_for_parsing_id_2)
            print(last_message_id_2)
            if last_message_id_2:
                await client.forward_messages(group_id_1, group_for_parsing_id_2, last_message_id_2)
    except Exception as e:
        print(f"An error occurred: {e}")

app.run()