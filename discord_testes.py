import discord
from discord.ext import commands,tasks
import os
import youtube_dl
import socket
# hostname = socket.gethostname()
# ip = socket.gethostbyname(hostname)
DISCORD_TOKEN = "MTA3MTEwMTg0NDczMTk5ODMyOQ.G-YcSa.gn3C6dY1MjfoLA4vzLvl80df20RuwBbEpAyekk"

intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$run'):
        a = str(message.content).strip('$run')
        os.environ["a"] = a
        await message.channel.send(f'Rodando a query {a}!\n\n\n')
        os.system("python teste.py")
        with open('data.txt') as f:
            query = f.read()
        if str(query).__contains__('Bad ERROR') == True:
            await message.channel.send(f'Results with Error: {query}!')
        else:
            await message.channel.send(f'Results: {query}!')

if __name__ == "__main__" :
    client.run(DISCORD_TOKEN)