from constants import *
import discord

from discord.ext import commands
from google_api import GoogleApi

intens = discord.Intents.default()
intens.message_content = True
intens.members = True

bot = commands.Bot(command_prefix="$", intents=intens)


@bot.event
async def on_ready():
    print("Bot está pronto")

# commands
@bot.command()
async def whoami(ctx: commands.Context):
    user = ctx.author
    await ctx.reply(f"Ola, {user.display_name}. Eu sou o bot gemini, estou aqui pra te ajudar no que for preciso")

@bot.command()
async def gemini(ctx: commands.Context, *,prompt:str):
    go_api = GoogleApi()
    prompt = go_api.max_line_prompt(prompt=prompt)
    res = go_api.chat_response(prompt=prompt)
    await ctx.reply(res)
    # await ctx.reply(f"Infelizmente o limite de caracteres é {limit} tente encurtar a sua questão")

bot.run(get_id_bot())
