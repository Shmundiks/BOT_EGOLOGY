import discord
import random
from discord.ext import commands
import os
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен!')

def get_duck_image_url():    
    url = 'https://ecoportal.su/'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animal(ctx):
    animals_name = random.choice(os.listdir("Animals"))
    with open(f'Animals/{animals_name}', 'rb') as f:
        
        picture = discord.File(f)
   
    await ctx.send(file=picture)


@bot.command()
async def egology(ctx):
    '''Показывает картинку об экологии'''
    egology_name = random.choice(os.listdir("Egology"))
    with open(f'Egology/{egology_name}', 'rb') as f:
        
        picture = discord.File(f)
   
    await ctx.send(file=picture)


@bot.command()
async def rubbish(ctx): 
     '''Сайт об экологии'''
     eco = "https://ecoportal.su/" 
     ego = ("Это сайт об экологии поможет нам узнать все новости о природе!")
     await ctx.send(eco)   
     await ctx.send(ego)
@bot.command()
async def Save_egology(ctx): 
     '''Как спасти нашу планету'''
     Save = "https://turclub-pik.ru/blog/chto-ya-mogu-sdelat-dlya-ehkologii-30-sposobov/"
     Answer = ("Давайте посмотрим как спасти нашу планету!")
     await ctx.send(Save)
     await ctx.send(Answer)


bot.run("MTE0NzgyOTQzNTE5MDQ5NzI4MA.Gl0gb1.cmIFVZwWYdqIJ34DmQKp6LcsyXkoYv25AOyYFw")