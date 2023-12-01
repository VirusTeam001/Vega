from pystyle import Write, Colors, Colorate
from colorama import Fore, init
import colorama
import requests
import time
import os
import subprocess
import sys
sys.dont_write_bytecode = True

init()

def banner():
    banner_text = """\n 
                                                                                                          
                                                                                                          
                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                            ┃ dP     dP  88888888b  .88888.   .d888888  ┃
                            ┃ 88     88  88        d8'   `88 d8'    88  ┃
                            ┃ 88    .8P a88aaaa    88        88aaaaa88a ┃
                            ┃ 88    d8'  88        88   YP88 88     88  ┃
                            ┃ 88  .d8P   88        Y8.   .88 88     88  ┃
                            ┃ 888888'    88888888P  `88888'  88     88  ┃
                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                                    
                                    \n"""
    print(Colorate.Diagonal(Colors.red_to_purple, banner_text, 8))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f"title Создал - VirusTeam")

    with open("token.txt", "r") as file:
        token = file.readline().strip()

    if token == "":
        print("Пустой токен в файле 'token.txt'. Замените его на свой токен Discord бота .")
        sys.exit(1)
    elif token == "single token here":
        print("Вы не изменили файл 'token.txt'. Замените его на свой токен Discord бота .")
        sys.exit(1)

    headers = {'Authorization': f'Bot {token}'}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

    if response.status_code == 200:
        options = f"""
        
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ https://github.com/VirusTeam001 ┃  https://discord.gg/DdX9GnNfXT    ┃                                 ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃  [1] Menu                       ┃  [10] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [2] Mass delete channels       ┃  [11] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [3] Mass create channels       ┃  [12] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [4] Mass delete role           ┃  [13] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [5] Mass create roles          ┃  [14] Spam all channels           ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [6] Rename server              ┃  [15] Spam channels ( ID )        ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [7] . . . . . . . . . . . . .  ┃  [16] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [8] . . . . . . . . . . . . .  ┃  [17] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [9] . . . . . . . . . . . . .  ┃  [18] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        
        """
        banner()
        print(Colorate.Vertical(Colors.purple_to_red, options, 1))
    else:
        optionsi = """
        
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ https://github.com/VirusTeam001 ┃  https://discord.gg/DdX9GnNfXT    ┃                                 ┃
        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ┃  [1] Menu                       ┃  [10] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [2] Mass delete channels       ┃  [11] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [3] Mass create channels       ┃  [12] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [4] Mass delete role           ┃  [13] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [5] Mass create roles          ┃  [14] Spam all channels           ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [6] Mass create webhooks       ┃  [15] Spam channels ( ID )        ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [7] . . . . . . . . . . . . .  ┃  [16] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [8] . . . . . . . . . . . . .  ┃  [17] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┃  [9] . . . . . . . . . . . . .  ┃  [18] . . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        
        """
        banner()
        print(Colorate.Vertical(Colors.purple_to_red, optionsi, 1))

    while True:
        user_input = Write.Input(
            f"\n\n     Choose: ", Colors.blue_to_red, interval=0.03)
        user_input = user_input.lower()

        if user_input == "1":
            subprocess.run(["python", "main.py"])
            time.sleep(1.9)
            main()
        elif user_input == "":
            print("Ошибка, введите что-то")
            time.sleep(0.7)
            main()
        elif user_input == "2":
            subprocess.run(["python", "commands/massdelch.py"])
            time.sleep(1.9)
            main()
        elif user_input == "3":
            subprocess.run(["python", "commands/masschannel.py"])
            time.sleep(1.9)
            main()
        elif user_input == "4":
            subprocess.run(["python", "commands/massdelrole.py"])
            time.sleep(1.9)
            main()
        elif user_input == "6":
            subprocess.run(["python", "commands/webhooks.py"])
            time.sleep(1.9)
            main()
        elif user_input == "5":
            subprocess.run(["python", "commands/massrole.py"])
            time.sleep(1.9)
        elif user_input == "14":
            subprocess.run(["python", "commands/massspam.py"])
            time.sleep(1.9)
            main()
        elif user_input == "15":
            subprocess.run(["python", "commands/spam.py"])
            time.sleep(1.9)
            main()
        elif user_input == "exit":
            sys.exit()
        else:
            print(Fore.RED + "Ошибка 404: Команда не найдена")
            time.sleep(0.7)
            main()

if __name__ == "__main__":
    main()
