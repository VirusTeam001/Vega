import aiohttp
import asyncio
from termcolor import colored
import sys
import os
import requests

async def get_roles(session, guild_id, headers):
    url = f'https://discord.com/api/v9/guilds/{guild_id}/roles'

    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            roles_data = await response.json()
            role_ids = [role['id'] for role in roles_data]
            return role_ids
        elif response.status == 429:
            print("Слишком много запросов, ожидаем 0.2 секунды...")
            await asyncio.sleep(0.2)
            return []
        else:
            print(f"Не удалось получить список ролей. Код состояния: {response.status}")
            return []

async def remove_roles(session, guild_id, headers):
    role_ids = await get_roles(session, guild_id, headers)
    
    if not role_ids:
        return
    
    url = f'https://discord.com/api/v9/guilds/{guild_id}/roles'

    for role_id in role_ids:
        role_url = f'{url}/{role_id}'
        async with session.delete(role_url, headers=headers) as response:
            if response.status == 204:
                print(colored(f"Роль с ID {role_id} успешно удалена.", 'green'))
            elif response.status == 429:
                print("Слишком много запросов, ожидаем 0.2 секунды...")
                await asyncio.sleep(0.2)
            else:
                print(f"Не удалось удалить роль с ID {role_id}. Код состояния: {response.status}")

async def main():
    with open("token.txt", "r") as file:
        bot_token = file.readline().strip()

    if not bot_token:
        print("Пустой токен бота в файле token.txt.")
        sys.exit(1)

    headers = {'Authorization': f'Bot {bot_token}', 'Content-Type': 'application/json'}
    guild_id = input("ID сервера (Guild ID): ")

    async with aiohttp.ClientSession() as session:
        await remove_roles(session, guild_id, headers)

if __name__ == '__main__':
    asyncio.run(main())
