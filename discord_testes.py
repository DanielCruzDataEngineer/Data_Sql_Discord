import discord
from discord.ext import commands,tasks
from discord.ext.commands import Bot
import os
import pandas as pd
import time
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# hostname = socket.gethostname()
# ip = socket.gethostbyname(hostname)

intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$run'):
        a = str(message.content).strip('$run')
        os.environ["a"] = a
        start = time.time()
        await message.channel.send(f'Olá,{message.author}!Rodando a query {a}!\n\n\n')

        os.system("python teste.py")

        end = time.time()

        print(f"Tempo de execução da query: {end - start:.2f} segundos")
        df = pd.read_csv('data.txt', sep=" ",encoding='utf-8',encoding_errors='ignore')
        df.to_csv("results.csv", index=False)
        if str(df).__contains__('ERROR') == True:
            
            await message.channel.send(f'Results with Error: {str(df)}!')
        else:
            with open("results.csv", "rb") as file:
                await message.channel.send(file=discord.File(file))
                await message.channel.send(f'Tempo de execução da query: {end - start:.2f} segundos!')

if __name__ == "__main__" :
    client.run(DISCORD_TOKEN)

