from dotenv import load_dotenv
from flask import Flask, request
load_dotenv()
import os
import telebot
import openai
OPENAI_KEY = os.environ["OPENAI_KEY"]
openai.api_key = OPENAI_KEY

<<<<<<< HEAD
app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
=======
BOT_TOKEN = os.environ["BOT_TOKEN"]
>>>>>>> origin/main

# bot instance
bot = telebot.TeleBot(BOT_TOKEN)

def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK', 200


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

if __name__ == '__main__':
    app.run()
