import discord
from discord.ext import commands
import requests
import json

# Inicjalizacja bota z odpowiednimi intencjami
intents = discord.Intents.all()
intents.messages = True
intents.message_content = True  # Wymagane do odczytu treści wiadomości
bot = commands.Bot(command_prefix="!", intents=intents)

# URL serwera Flask
with open("config.json", "r") as f:
    config = json.load(f)
    DISCORD_BOT_TOKEN = config["DISCORD_BOT_TOKEN"]
    AUTHORIZED_CHANNEL_ID = config["AUTHORIZED_CHANNEL_ID"]
    FLASK_SERVER_URL = config["FLASK_SERVER_URL"]  # Zmień na adres serwera Flask, jeśli inny


@bot.event
async def on_ready():
    print(f"Bot zalogowany jako {bot.user}")

@bot.event
async def on_message(message):
    # Ignoruj wiadomości od bota
    if message.author == bot.user:
        return

    # Wypisanie każdej wiadomości w konsoli
    print(f"{message.author}: {message.content}")

    # Przetwarzaj wiadomości w kontekście komend
    await bot.process_commands(message)

# Komenda !dzwonek
@bot.command()
async def dzwonek(ctx):
    try:
        # Wysyłanie zapytania POST do serwera Flask z channel_id
        payload = {'channel_id': str(ctx.channel.id)}
        response = requests.post(FLASK_SERVER_URL, json=payload)
        
        # Sprawdzenie odpowiedzi serwera
        if response.status_code == 200:
            await ctx.send("🔔 Dzwonek został uruchomiony!")
        else:
            await ctx.send(f"```⚠️ Błąd: serwer Flask zwrócił status {response.status_code}```")
    except requests.exceptions.RequestException as e:
        await ctx.send(f"```⚠️ Błąd połączenia z serwerem Flask: {e}```")

# Uruchomienie bota
bot.run(DISCORD_BOT_TOKEN) # Wstaw tutaj token swojego bota