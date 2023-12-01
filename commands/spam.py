import aiohttp
import asyncio
import time
import sys

successful = 0

async def spam(session, num, channel_id, headers, json_data):
    global successful

    while successful < num:
        try:
            if not json_data['content']:
                print("Сообщение не может быть пустым.")
                sys.exit(1)

            async with session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data, timeout=5) as response:
                response.raise_for_status()

                successful += 1
                print(f"Сообщение отправлено! ({successful}/{num})")
        except aiohttp.ClientError as e:
            print(f"Произошла ошибка: {e}")

        await asyncio.sleep(0.6)

async def main():
    with open("token.txt", "r") as file:
        token = file.readline().strip()
        if not token:
            print("Пустой токен")
            sys.exit(1)
        elif token == "single token here":
            print("Вы не отредактировали файл 'token.txt'.")
            sys.exit(1)

    headers = {'Authorization': f'Bot {token}'}

    message = input("Сообщение? ")
    try:
        num = int(input("Сколько сообщений? "))
        if num <= 0:
            raise ValueError("Число сообщений должно быть положительным.")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
        sys.exit(1)

    channel_id = input("ID канала? ")
    json_data = {"content": message}

    async with aiohttp.ClientSession() as session:
        await spam(session, num, channel_id, headers, json_data)

if __name__ == "__main__":
    asyncio.run(main())
