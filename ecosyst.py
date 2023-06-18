import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

facts = [
'Найди людное место и попробуй поискать мусора. Не забудь взять пакет!,
'Попробуй пойти вместе со своими друзьями. Вместе интересней,
'Если вы найдете какие-нибудь батарейки, несите их на переработку.
]

infa = [
'Железная банка - 10 лет' ,
'синтетическая одежда - 30-40 лет',
'жестяная банка - до 90 лет' ,
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
    print(f'Привет, дорогие пользователи. Вот мои команды: howtodo, hello, about')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот который следит за экосистемой!')

@bot.command()
async def facts(ctx):
    facts = random.choice(facts)
    await ctx.send(facts)


@bot.command()
async def infa(ctx):
    infa = random.choice(infa)
    await ctx.send(infa)


@bot.command()
async def ecosystem(ctx):
    await ctx.send(f'О, все таки ты заинтересован в экосистеме! Я рад за тебя, пропиши комманду $howtodo чтобы узнать рекомендации')
                  
@bot.command()
async def cat(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

bot.run('token')
