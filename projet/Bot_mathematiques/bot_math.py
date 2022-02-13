import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")
bot = commands.Bot(command_prefix="!", description="Bot pour Réviser")

@bot.event
async def on_ready():
    print("Ready!")

#lien utiles pour réviser
@bot.command()
async def link(ctx):
    embed = discord.Embed(title = "Les Liens utiles", color = 0x334FFF, description='[maths-et-tiques](https://www.maths-et-tiques.fr/)\n[autre site](https://nirbose.fr/)')
    embed.set_footer(text = "fin de la leçon !")
    await ctx.send(embed = embed)

#aller sur l'ent de stephane hesssel
@bot.command()
async def ent(ctx):
    embed = discord.Embed(title = "mon Etablissement", color = 0x334FFF, description='[ENT Stephane_Hessel](https://stephane-hessel.mon-ent-occitanie.fr/)')
    embed.set_image(url="https://stephane-hessel.mon-ent-occitanie.fr/lectureFichiergw.do?ID_FICHIER=1506290041830")
    await ctx.send(embed = embed)

#automatismes
@bot.command()
async def base(ctx):
    embed = discord.Embed(title = "Les automatismes",url="https://www.maths-et-tiques.fr/index.php/cours-maths/niveau-terminalet#A1",color = 0x334FFF)
    embed.set_image(url="https://i.ytimg.com/vi/QJwGIDnFKnA/maxresdefault.jpg")
    embed.set_footer(text = "fin de la leçon !")
    await ctx.send(embed = embed)

#suite
@bot.command()
async def suite(ctx):
    embed = discord.Embed(title = "Les suites",url="https://www.maths-et-tiques.fr/telech/19Suites1TM.pdf",color = 0x334FFF)
    embed.set_image(url="https://cdn.discordapp.com/attachments/752135228528787486/922930626603143198/Capture_decran_2021-12-21_201534.png")
    embed.set_footer(text = "fin de la leçon !")
    await ctx.send(embed = embed)

#
# @bot.command()
# async def suite(ctx):
#     embed = discord.Embed(title = "Les suites",url="https://www.maths-et-tiques.fr/telech/19Suites1TM.pdf",color = 0x334FFF)
#     embed.set_image(url="https://cdn.discordapp.com/attachments/752135228528787486/922930626603143198/Capture_decran_2021-12-21_201534.png")
#     embed.set_footer(text = "fin de la leçon !")
#     await ctx.send(embed = embed)


bot.run(os.getenv("TOKEN"))