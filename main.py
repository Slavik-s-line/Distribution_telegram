from telethon import TelegramClient
import asyncio

api_id = 00000000  # вводятся параметры пользователя
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # На момент тестирования, я ввёл свои данные

client = TelegramClient('username', api_id, api_hash)
client.start()

chats = open('chat_list.txt')  # открываем файл. Предполагается, что каждый id чата написан в новой строчке


async def main():
    while True:  # запускаем бесконечный цикл для рассылки
        for line in chats:  # проходим каждый id в файле
            await client.send_message(int(line), 'ТЕСТ моего бота для рассылки по групам. Удалю сообщения сам')
            await asyncio.sleep(3600)  # делаем паузу в рассылке в 3600 сек. что равняется 1 час.


with client:
    client.loop.run_until_complete(main())  # запускаем программу
chats.close()  # закрываем текстовый файл
