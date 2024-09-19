from telebot import TeleBot
import os
import environ

env = environ.Env()

# read th .env file
environ.Env.read_env()
bot = TeleBot(env('TOKEN'))



ids = env('USER_ID')
def get_post(data):
    bot.send_message(chat_id=ids, text=f"#Xabar Sizga yangi murojaat mavjud !\n\n\n"
                                          f"Ism: {data['name']}\n"
                                          f"Telefon Raqam: {data['phone_number']}\n"
                                          f"Manzil: {data['address']}\n"
                                          f"Xabar: {data['message']}")


def get_post1(data):
    bot.send_message(chat_id=ids, text=f"#Product Sizga yangi murojaat mavjud !\n\n\n"
                                          f"Ism: {data['name']}\n"
                                          f"Telefon Raqam: {data['phone_number']}\n"
                                          f"Mahsulot: {data['product']}\n"
                                          f"Miqdori: {data['count']}")