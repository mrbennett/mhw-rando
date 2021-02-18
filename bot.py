import discord
import random
import requests
import os
from bs4 import BeautifulSoup

client = discord.Client()

weapons = [ 
    'Greatsword',
    'Insect Glaive',
    'Longsword',
    'Hunting Horn',
    'Dual Blades',
    'Hammer',
    'Lance',
    'Gun Lance',
    'Heavy Bowgun',
    'Light Bowgun',
    'Sword and Shield',
    'Charge Blade',
    'Switch Axe',
    'Bow'
]

def generate_monster_list_from_kiranico():
    kira_url = 'https://mhworld.kiranico.com/monsters'

    r = requests.get(kira_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    monsters_table = soup.table.find_all('tr')

    return [monsters_row.td.span.a.get_text() for monsters_row in monsters_table]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(f'{message.content}')

    if message.author == client.user:
        return

    if message.content.startswith('!rando'):
        await message.channel.send(f'You should fight {random.choice(monsters)} with the {random.choice(weapons)}!')


monsters = generate_monster_list_from_kiranico()
client.run(os.environ['DISCORD_BOT_TOKEN'])

