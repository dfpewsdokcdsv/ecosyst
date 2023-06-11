import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Привет, дорогие пользователи. Вот мои команды: howtodo, hello, about')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот который следит за экосистемой!')


@bot.command()
async def ecosystem(ctx):
    await ctx.send(f'О, все таки ты заинтересован в экосистеме! Я рад за тебя, пропиши комманду $howtodo чтобы узнать рекомендации')


@bot.command()
async def howtodo(ctx):
    await ctx.send(f'1. Найди людное место и попробуй поискать мусора. Не забудь взять пакет! 2. Попробуй пойти вместе со своими друзьями.',
                  f'Вместе интересней.' ,
                  f'3. Если вы найдете какие-нибудь батарейки, несите их на переработку.')
                  
@bot.command()
async def about(ctx):
    await ctx.send(f'Железная банка - 10 лет' ,
f'синтетическая одежда - 30-40 лет',
f'жестяная банка - до 90 лет' ,
f'окурок (сигаретный фильтр) - до 3 лет',
f'металлические контейнеры разрушаются в морской среде за 10 лет',
f'а бетонированные - 30 лет', 
f'обувь из искусственной кожи - 40-50 лет', 
f'жевательная резинка (в теплых климатических условиях) - 30 лет, на холоде - сотни лет', 
f'губка для мытья посуды - 200 лет',
f'одноразовый подгузник - около 500 лет',
f'обломки кирпича и бетона - 100 лет',
'аккумуляторы, батарейки - 100 лет',
f'фольга - 100 лет',
f'резина - 100 лет',
f'пластик - 100 лет',
f'автомобильные покрышки - 120-140 лет',
f'полиэтилен - 100-200 лет',
f'алюминиевая тара - 500 лет',
f'стекло - более 1000 лет')

@bot.command()
async def ecomem(ctx):
    images = os.listdir('images')
    img_name = random.choice()
    with open(f'images/мге.png', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

bot.run('token')
