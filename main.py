import load
import telebot


TOKEN = '1964614455:BAH7HooGg8eeqS3jN1q2mMukLwUFBJDwe2v'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	text = message.text
	if text.count('https://fex.net/') != 0:
		bot.send_message(message.chat.id, load.dounload(text))
	else:
		bot.send_message(message.chat.id, f'{text}: uncorrect message')

if __name__ == '__main__':
	bot.infinity_polling()