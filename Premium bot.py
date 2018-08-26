import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

Clinet = discord.Client()
bot = commands.Bot(command_prefix="!")
lines = open(r'Premium.txt').read().splitlines()

@bot.event
async def on_ready():
    print("The bot is online!")

@bot.command(pass_context=True)
async def gen(ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.ID

    if ctx.message.server:
        await bot.delete_message(ctx.messgae)
        myline = random.choice(lines)
        split = myline.partition(":")


        embed=discord.Embed(title="Minecraft Account", description="Deine Minecraft Account daten")
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/bIdnrpy_luwj1vN-vpTjJXgL3KtxQOLZRa_5G4KefxAhliq-cB_m2tEtIvlgg3RztLU6NjVDVSsCVV4xA9Qb_w=s400")
        embed.add_field(name="Email", value=split[0], inline=False)
        embed.add_field(name="Passwort", value=split[2], inline=False)
        embed.set_footer(text="Viel Spaß!!!!")
        await bot.send_message(ctx.message.author,embed=embed)

        print("{} Typed !alt3".format(userName))
        
bot.run("NDgzMjgxMzI2ODEyOTU0NjI0.DmRKdg.8KGFittjXLWK9HsYczskM_xM0dM")#bots token!
