import telegram

bot = telegram.Bot(token="5705202999:AAGZAyzcFBnIFGcLaqPFO0wopevJo_f9M-4 ")

# Function to handle when a user sends a message
def handle_message(message):
    # Send a message back to the user
    bot.send_message(chat_id=message.chat.id, text="•──────────────•")

# Set the bot to listen for messages
bot.set_update_listener(handle_message)
