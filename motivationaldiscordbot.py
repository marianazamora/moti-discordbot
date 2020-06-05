import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot


client = discord.Client()
bot = commands.Bot(command_prefix="!") #allows bot to take commands. 

#commands
@bot.command()
async def quote(ctx): #gives a random quote from the list
        await ctx.send("Here's a quote:")
        motquote = open("motivationalquotes.txt")
        quotecont = motquote.read().splitlines()
        line = random.choice(quotecont)
        await ctx.send(line)
        motquote.close()

@bot.command()
async def compliment(ctx): #gives random compliments from the document
        await ctx.send("Hey!")
        compl = open("compliments.txt")
        cont = compl.read().splitlines()
        line = random.choice(cont)
        await ctx.send(line)
        compl.close()
        
@bot.command()
async def encourage(ctx): 
        await ctx.send("Here's some courage:")
        encourage = open("encouragement.txt")
        enc = encourage.read().splitlines()
        line = random.choice(enc)
        await ctx.send(line)
        encourage.close()

@bot.command()
async def cuteanimal(ctx):
        await ctx.send("Here's a cute animal:")
        cuteanimal = open("cuteanimals.txt")
        cute = cuteanimal.read().splitlines()
        line = random.choice(cute)
        await ctx.send(line)
        cuteanimal.close()
       

#events triggered by messages
@bot.event
async def on_ready(ready):
        print("Moti is ready to partay!")

@bot.event      
async def on_message(message):
        message.content = message.content.lower()
        if message.content.startswith("hello moti"):
                channel = message.channel
                await channel.send("Hello I'm Moti! The motivator bot. \
I'm here to give you support. \nChoose one of this actions:\
\n!quote\n!compliment\n!encourage\n!cuteanimal")
        await bot.process_commands(message) #This line will prevent on_message from blocking the commands.


bot.run("YOUR TOKEN")

