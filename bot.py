import discord
import responses
from discord.ext import commands
import os 

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await (message.author.send(response) if is_private else message.channel.send(response))

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="--", case_insensitive=True, intents=intents)
    bot.remove_command("help")

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running..')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username} said: '{user_message}' {channel}")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    bot.run(os.getenv('TOKEN'))