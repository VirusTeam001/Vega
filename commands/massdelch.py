import aiohttp
import asyncio
from termcolor import colored

async def delete_channel(session, channel_id, headers, channel_name=None):
    url = f'https://discord.com/api/v9/channels/{channel_id}'
    async with session.delete(url, headers=headers) as response:
        if response.status == 200:
            print(colored(f"Канал '{channel_name}' успешно удален.", 'green'))
        elif response.status == 429:
            print("Слишком много запросов, ожидаем 0.8 секунды...")
            await asyncio.sleep(0.8)
        else:
            print(f"Не удалось удалить канал '{channel_id}'. Код состояния: {response.status}")

async def delete_category(session, category_id, headers):
    url = f'https://discord.com/api/v9/channels/{category_id}'
    async with session.delete(url, headers=headers) as response:
        if response.status == 200:
            print(f"Категория '{category_id}' успешно удалена.")
        elif response.status == 429:
            print("Слишком много запросов, ожидаем 0.2 секунды...")
            await asyncio.sleep(0.2)
        else:
            print(f"Не удалось удалить категорию '{category_id}'. Код состояния: {response.status}")

async def main():
    with open("token.txt", "r") as file:
        bot_token = file.readline().strip()

    if bot_token == "":
        print("Пустой токен бота в файле token.txt")
        print("Игнорируйте ошибку ниже, я не знаю, как ее исправить. Если вы знаете, как ее исправить, создайте запрос на добавление изменений (pull request).")
        return

    headers = {'Authorization': f'Bot {bot_token}', 'Content-Type': 'application/json'}
    target_id = input("ID сервера: ")

    async with aiohttp.ClientSession() as session:
        channels_url = f'https://discord.com/api/v9/guilds/{target_id}/channels'
        async with session.get(channels_url, headers=headers) as response:
            if response.status == 200:
                channels_data = await response.json()

                tasks = []
                for channel in channels_data:
                    channel_id = channel['id']
                    channel_type = channel['type']
                    channel_name = channel.get('name', None)

                    if channel_type == 4: 
                        tasks.append(delete_category(session, channel_id, headers))
                    else:  
                        tasks.append(delete_channel(session, channel_id, headers, channel_name))

                await asyncio.gather(*tasks)

            elif response.status == 429:
                print("Слишком много запросов, ожидаем 0.8 секунды...")
                await asyncio.sleep(0.8)
            else:
                print(f"Не удалось получить список каналов. Код состояния: {response.status}")

if __name__ == '__main__':
    asyncio.run(main())
