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

    @bot.command()
    async def select_account(ctx):
        options = ["Prop account -1", "Prop account -2"]  # List of options
        prompt = "\n".join(f"{index + 1}. {option}" for index, option in enumerate(options))

        # Send prompt to the user
        await responses.handle_command(ctx, "Please select an option by typing its number:\n", prompt, discord.Color.green())

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.isdigit() and 1 <= int(message.content) <= len(options)

        try:
            message = await bot.wait_for('message', check=check, timeout=30)
            selected_option = options[int(message.content) - 1]

            role_id = None
            for role in ctx.author.roles:
                role_id = role.id
                break  

            await responses.handle_command(ctx, "You selected:", f"{selected_option} and your role ID is: {role_id}", discord.Color.green())
        except Exception as e:
            await ctx.send("You took too long to respond.")



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