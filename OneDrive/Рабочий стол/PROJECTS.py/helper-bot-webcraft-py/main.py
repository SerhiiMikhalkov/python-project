import sqlite3
import telebot
import logging
import time

bot = telebot.TeleBot('6067883998:AAFC3syNThOQjtQvEOu2vjtJj61SXeBP8yg')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}! \n Вітаємо в боті каналу WebCraft. Щоб побачити список доступних команд впишіть в чат /help', parse_mode='html')
    print(f'Користувач {message.from_user.id}, {message.from_user.first_name} запустив бота')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'От список команд які можуть тобі знадобитись: \n /info - остання інформація о нас \n /id - показує твоє айді в боті \n /contacts - способи звязку з нами \n /help_channel - допомогти каналу')

@bot.message_handler()
def info(message):
    if message.text.lower() == '/id':
        bot.send_message(message.chat.id, f'ID: {message.from_user.id}')
        bot.send_message(message.chat.id, f'От список команд які можуть тобі знадобитись: \n /info - остання інформація о нас \n /id - показує твоє айді в боті \n /contacts - способи звязку з нами \n /help_channel - допомогти каналу')
        print(f'Користувач {message.from_user.id}, {message.from_user.first_name} {message.from_user.username} запросив ID користувача')
    elif message.text.lower() == '/perevirka':
        bot.send_message(message.chat.id, message)
    # elif message.text.lower() == '/info':
    #     bot.send_message(message.chat.id, 'Останню інформацію по нашій спільноті можете побачити в нашому телеграм каналі t.me/WebCraftChanel')
    #     bot.send_message(message.chat.id, f'От список команд які можуть тобі знадобитись: \n /info - остання інформація о нас \n /id - показує твоє айді в боті \n /contacts - способи звязку з нами \n /help_channel - допомогти каналу')
    #     print(f'Користувач {message.from_user.id}, {message.from_user.first_name} {message.from_user.username} запросив останню інформацію')
    elif message.text.lower() == '/contacts':
        bot.send_message(message.chat.id, 'Для контакту з нашою тімою напиши до (@WEBCRAFTcreator)')
        bot.send_message(message.chat.id, f'От список команд які можуть тобі знадобитись: \n /info - остання інформація о нас \n /id - показує твоє айді в боті \n /contacts - способи звязку з нами \n /help_channel - допомогти каналу')
        print(f'Користувач {message.from_user.id}, {message.from_user.first_name} {message.from_user.username} запросив контакти')
    elif message.text.lower() == '/help_channel':
        bot.send_message(message.chat.id, 'Посилання щоб нас підтримати: \n https://send.monobank.ua/jar/xCdqgRnnP')
        bot.send_message(message.chat.id, f'От список команд які можуть тобі знадобитись: \n /info - остання інформація о нас \n /id - показує твоє айді в боті \n /contacts - способи звязку з нами \n /help_channel - допомогти каналу')
        print(f'Користувач {message.from_user.id}, {message.from_user.first_name} {message.from_user.username} запросив підтримку каналу')


bot.polling(none_stop=True)