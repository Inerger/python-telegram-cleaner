from telethon import TelegramClient

# Enter your API ID and API Hash
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'

# List of offensive words
offensive_words = ["offensive_word1", "offensive_word2", "offensive_word3"]

# Create the client
client = TelegramClient('session_name', api_id, api_hash)

def contains_offensive_word(text):
    # Convert the text to lowercase
    text = text.lower()
    for word in offensive_words:
        if word.lower() in text:
            return True
    return False

async def delete_offensive_private_messages():
    await client.start(phone_number)
    dialogs = await client.get_dialogs()

    for dialog in dialogs:
        if dialog.is_user:  # Check if the dialog is a private chat
            async for message in client.iter_messages(dialog, limit=None):  # Gradually fetch all messages
                if message.out and message.message and contains_offensive_word(message.message):
                    try:
                        await client.delete_messages(dialog.entity, [message.id], revoke=True)
                        print(f"Message {message.id} deleted.")
                    except Exception as e:
                        print(f"Error deleting message {message.id}: {e}")

    print("Offensive messages deleted.")

with client:
    client.loop.run_until_complete(delete_offensive_private_messages())
    