import discord
import responses
from discord.ext import commands
import os 
import random

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await (message.author.send(response) if is_private else message.channel.send(response))

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)
    bot.remove_command("help")

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running..')

    @bot.command()
    async def hello(ctx):
        await responses.handle_command(ctx, "Hello!", "Hey there!", discord.Color.green())

    @bot.command()
    async def roll(ctx):
        await responses.handle_command(ctx, "Dice Roll", f"The dice rolled: {random.randint(1, 6)}", discord.Color.blue())

    @bot.command()
    async def coin(ctx):
        await responses.handle_command(ctx, "Coin Flip", f"The result is: {random.choice(['Head', 'Tail'])}", discord.Color.gold())

    @bot.command()
    async def help(ctx):
        await responses.handle_command(ctx, "Help Section", "I will add the help section here.", discord.Color.orange())

    # @bot.event
    # async def on_message(message):
    #     if message.author == bot.user:
    #         return
        
    #     username = str(message.author)
    #     user_message = str(message.content)
    #     channel = str(message.channel)
    #     print(f"{username} said: '{user_message}' {channel}")

    #     if user_message[0] == '?':
    #         user_message = user_message[1:]
    #         await send_message(message, user_message, is_private=True)
    #     else:
    #         await send_message(message, user_message, is_private=False)

    bot.run(os.getenv('TOKEN'))