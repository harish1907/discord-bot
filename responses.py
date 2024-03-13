import random
import discord
from discord.ui import Select , View

def handle_response(message):
    p_message = message.lower()

    if p_message == "hello":
        return "Hye there!"
    
    elif p_message == "roll":
        return str(random.randint(1,6))
    
    elif p_message == "!help":
        return "I will help section after all the use cases."
    
    elif p_message == "coin":
        return random.choice(["Head", "Tail"])
    
async def handle_command(ctx, title, description, color):
    embed = discord.Embed(title=title, description=description, color=color)
    await ctx.send(embed=embed)


# select options dropdown cases.
def selectInputs():
    select = Select(
        placeholder="Choose an input option!",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="A", description="Initial prop fund balance USD."),
            discord.SelectOption(label="B", description="Day starting balance USD."),
            discord.SelectOption(label="C", description="Day ending balance USD."),
            discord.SelectOption(label="D", description="Name of the prop firm."),
            discord.SelectOption(label="E", description="Daily draw down percent."),
            discord.SelectOption(label="F", description="Max draw down percent."),
            discord.SelectOption(label="G", description="Phase 1 target percent."),
            discord.SelectOption(label="H", description="Phase 2 target percent."),
        ]
    )

    async def my_callback(interaction):
        await interaction.response.send_message(f"Awesome! I like {select.values[0] } too!")

    select.callback = my_callback
    return select

# select account dropdown cases.
def selectAccount(ctx):
    print(ctx.author, ctx.author.id)
    select = Select(
        placeholder="Choose an Account!",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="Account 1"),
            discord.SelectOption(label="Account 2"),
        ]
    )

    async def my_callback(interaction):
        await interaction.response.send_message(f"You selected {select.values[0] }.\nPlease select input one by one and fill accordingly.")
        channel = interaction.channel
        await channel.send("Please choose another option", view=discord.ui.View().add_item(selectInputs()))

    select.callback = my_callback
    return select