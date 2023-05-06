import discord
import requests
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.content.startswith('$monero'):
        response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=monero')
        json_response = response.json()
        price = json_response[0]['current_price']
        await message.channel.send(f'Current Monero Price: ${price}')

client.run('')
