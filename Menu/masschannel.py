import aiohttp
import asyncio
import json
from sys import exit
from termcolor import colored

async def create_channel(session, target_id, channel_name, channel_type, headers):
    data = {'name': channel_name, 'type': channel_type}
    url = f'https://discord.com/api/v9/guilds/{target_id}/channels'
    async with session.post(url, json=data, headers=headers) as response:
        if response.status == 201:
            print(colored(f"Канал '{channel_name}' успешно создан.", 'green'))
        elif response.status == 429:
            print(colored("Достигнут лимит запросов, ждем 0.4 секунды...", 'yellow'))
            await asyncio.sleep(0.4)
        else:
            print(
                colored(f"Не удалось создать канал '{channel_name}'. Код состояния: {response.status}", 'red'))

async def main():
    try:
        with open("token.txt", "r") as file:
            token = file.readline().strip()

        if token == "":
            print(colored("Пустой токен в файле token.txt", 'red'))
            print(colored("Игнорируйте ошибку ниже, я не знаю, как ее исправить. Если вы знаете, как исправить, создайте запрос на объединение изменений (pull request).", 'yellow'))
            return

        if not token.startswith("Bot "):
            headers = {'Authorization': f'Bot {token}',
                       'Content-Type': 'application/json'}
        else:
            headers = {'Authorization': token,
                       'Content-Type': 'application/json'}

        target_id = input(colored("ID сервера: ", 'white'))
        channel_name = input(colored("Имя канала: ", 'white'))

        while True:
            try:
                how_many = int(input(colored("Количество создаваемых каналов: ", 'white')))
                break
            except ValueError:
                print(colored("Введите корректное число.", 'red'))

        vc_or_text = input(colored("Текстовой канал, голосовой канал или категория? [t|vc|c] ", 'white'))

        if vc_or_text == "t":
            channel_type = 0
        elif vc_or_text == "vc":
            channel_type = 2
        elif vc_or_text == "c":
            channel_type = 4
        else:
            print(colored("Неверный вариант...", 'red'))
            return

        async with aiohttp.ClientSession() as session:
            tasks = []
            for _ in range(how_many):
                tasks.append(create_channel(session, target_id, channel_name, channel_type, headers))

            await asyncio.gather(*tasks)

    except FileNotFoundError:
        print(colored("Файл 'token.txt' не найден.", 'red'))

if __name__ == '__main__':
    asyncio.run(main())
