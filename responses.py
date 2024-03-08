import random
import discord

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