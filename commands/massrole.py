import asyncio
import json
import aiohttp
import sys

success = 0
with open("token.txt", "r") as file:
    token = file.readline().strip()
    if token == "":
        print("Пустой токен")
        sys.exit(1)
    elif token == "single token here":
        print("Вы не отредактировали файл 'token.txt'.")
        sys.exit(1)
    headers = {'Authorization': f'Bot {token}'}

    guild_id = input("ID сервера? ")
    rname = input("Название роли? ")
    num_role = int(input("Количество ролей? "))

    async def start_bot():
        async with aiohttp.ClientSession(headers=headers) as session:
            await create_roles(session)
            await session.close()

    async def create_roles(session):
        global success  
        print("Создание ролей...")
        create_role_url = f'https://discord.com/api/v9/guilds/{guild_id}/roles'
        create_tasks = []
        max_retries = 3

        for i in range(num_role):
            create_role_payload = {
                'name': f'{rname}',
                'color': 0xffffff,
                'hoist': True,
                'mentionable': True
            }
            create_tasks.append(create_role_with_retries(session, create_role_url, create_role_payload, max_retries))

        create_responses = await asyncio.gather(*create_tasks)
        for response in create_responses:
            if response is not None:
                if response[0] == 200:
                    print(f"Роль {rname} успешно создана ({success}/{num_role})")
                    success += 1
                else:
                    print(f"Не удалось создать роль. Код ошибки:{response[0]} ({success}/{num_role})")

    async def create_role_with_retries(session, url, payload, max_retries):
        retries = 0
        while retries <= max_retries:
            try:
                response = await session.post(url, json=payload)
                if response.status == 429:
                    print(f"Ограничение запросов. Ожидание 0.5 секунды... ({success}/{num_role})")
                    await asyncio.sleep(0.5)
                    retries += 1
                else:
                    return response.status, response 
            except Exception:
                retries += 1
            await asyncio.sleep(1)

        print(f"Не удалось выполнить запрос {max_retries} раз, пропускаем...")
        return None

    asyncio.run(start_bot())
