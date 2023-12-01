import aiohttp
import asyncio
import sys

async def get_channels(guild_id, session, headers):
    try:
        async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers) as response:
            response.raise_for_status()
            channels = await response.json()
            return channels
    except aiohttp.ClientError as e:
        print(f"Произошла ошибка при получении списка каналов: {e}")
        sys.exit(1)

async def send_message(channel_id, message, num, session, headers):
    try:
        for _ in range(num):
            async with session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json={"content": message}) as response:
                response.raise_for_status()
                await asyncio.sleep(0.5)
        return True
    except aiohttp.ClientError as e:
        print(f"Произошла ошибка при отправке сообщения: {e}")
        return False

async def spam_all_channels(guild_id, message, num, headers):
    async with aiohttp.ClientSession() as session:
        channels = await get_channels(guild_id, session, headers)

        tasks = [send_message(channel['id'], message, num, session, headers) for channel in channels]
        results = await asyncio.gather(*tasks)

        successful = sum(results)
        print(f"Отправлено {successful} сообщений в каждый из {len(channels)} каналов.")

if __name__ == "__main__":
    with open("token.txt", "r") as file:
        token = file.readline().strip()
        if not token or token == "single token here":
            print("Токен не указан или не отредактирован в файле 'token.txt'.")
            sys.exit(1)

    headers = {'Authorization': f'Bot {token}'}

    message = input("Сообщение? ")
    try:
        num = int(input("Сколько сообщений в каждый канал? (Советуем 10 макс) "))
        if num <= 0:
            raise ValueError("Число сообщений должно быть положительным.")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
        sys.exit(1)

    guild_id = input("ID сервера (Guild ID)? ")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(spam_all_channels(guild_id, message, num, headers))
