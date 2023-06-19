import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

facts_list = [
    'Найди людное место и попробуй поискать мусора. Не забудь взять пакет!',
    'Попробуй пойти вместе со своими друзьями. Вместе интересней',
    'Если вы найдете какие-нибудь батарейки, несите их на переработку.'
]

infa_list = [
    'Железная банка - 10 лет',
    'синтетическая одежда - 30-40 лет',
    'жестяная банка - до 90 лет',
    'окурок (сигаретный фильтр) - до 3 лет',
    'металлические контейнеры разрушаются в морской среде за 10 лет',
    'а бетонированные - 30 лет',
    'обувь из искусственной кожи - 40-50 лет',
    'жевательная резинка (в теплых климатических условиях) - 30 лет, на холоде - сотни лет',
    'губка для мытья посуды - 200 лет',
    'одноразовый подгузник - около 500 лет',
    'обломки кирпича и бетона - 100 лет',
    'аккумуляторы, батарейки - 100 лет',
    'фольга - 100 лет',
    'резина - 100 лет',
    'пластик - 100 лет',
    'автомобильные покрышки - 120-140 лет',
    'полиэтилен - 100-200 лет',
    'алюминиевая тара - 500 лет',
    'стекло - более 1000 лет'
]

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот захостился!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот, который следит за экосистемой!')

@bot.command()
async def facts(ctx):
    fact = random.choice(facts_list)
    await ctx.send(fact)

@bot.command()
async def infa(ctx):
    info = random.choice(infa_list)
    await ctx.send(info)

@bot.command()
async def ecosystem(ctx):
    await ctx.send(f'О, все таки ты заинтересован в экосистеме! Я рад за тебя. Пропиши команду $howtodo, чтобы узнать рекомендации.')

@bot.command()
async def mem(ctx):
    mge = os.listdir('mge')
    img_name = random.choice(mge)
    with open(f'mge/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

bot.run('token')
