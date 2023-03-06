from dotenv import load_dotenv
load_dotenv()
import os
import telebot
import openai
OPENAI_KEY = os.getenv("OPENAI_KEY")
openai.api_key = OPENAI_KEY

BOT_TOKEN = os.getenv("BOT_TOKEN")

# bot instance
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Open Kay-I, created by kester. Do well to ask reasonable questions and dont you"
                          " dare try to say shit...LOL")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": message.text
            }
        ]
    )
    bot.reply_to(message, completion.choices[0].message["content"].strip())


bot.infinity_polling()
