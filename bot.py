import requests
import json
import asyncio
import os, sys
import time
from datetime import datetime
from time import gmtime, strftime
from colorama import init, Fore, Back, Style
from discord.ext import commands
from discord.ext.commands import Bot
os.system('cls')
print(f'''
{Fore.RED}
████████╗██╗███╗░░░███╗███████╗
╚══██╔══╝██║████╗░████║██╔════╝
░░░██║░░░██║██╔████╔██║█████╗░░
░░░██║░░░██║██║╚██╔╝██║██╔══╝░░
░░░██║░░░██║██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝ Developer : kasra001{Fore.RESET}
''')
print(f"""
			{Fore.LIGHTCYAN_EX}Discord: !001#4612 Rz Discord :https://discord.gg/bSfKWsVzPW {Fore.RESET}
""")

Bot = commands.Bot(command_prefix='>', self_bot=True)
Bot.remove_command('help')

with open('token.txt','r') as f:
    token = f.readline()


@Bot.event
async def on_ready():
    print('')
    print('[=========================================================================================]')
    print('')
    print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] man Godrat mandam connect dadam hora [{Fore.LIGHTMAGENTA_EX}{Bot.user}{Fore.RESET}]')
    print('')
    print('[=========================================================================================]')
    print('')
    a = input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] shoro be kar konam ya na =/? [are / na kos mathar] ')
    print('')
    if a == 'are':
        print("are arvare ba dota ajor pare to kos matharet =/")
        time.sleep(2)
        while True:
            await asyncio.sleep(0)
            now = datetime.now()
            second = now.second
            minute = now.minute
            hour = now.hour
            if now.second < 10:
                second = f'0{now.second}'
            if now.minute < 10:
                minute = f'0{now.minute}'
            if now.hour < 10:
                hour = f'0{now.hour}'
            text = f'{hour}:{minute}:{second} :)'
            status_data = json.dumps(
                {
                    "custom_status":
                        {
                            "text": text
                        }
                }
            )
            sys.stdout.write("\r" + f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] {text}')
            sys.stdout.flush()
            r = requests.patch("https://discordapp.com/api/v6/users/@me/settings",headers={"Authorization": token, "Content-Type": "application/json"}, data=status_data)
    else:
        print(f'[{Fore.RED}Rz na system{Fore.RESET}] na o niyze to kos matharet goh mikhori migi na khar kose kir kol Rz Team to kos matharet =/')
        await asyncio.sleep(8)
        os._exit(8)

Bot.run(token,bot=False)
