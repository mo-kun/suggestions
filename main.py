import discord
from discord.ext import commands
from time import sleep

bot = commands.Bot(command_prefix="-")
bot.remove_command("help")

my_secret = "MTAwMDQyMzE5NDI5MDgxNTE4MA.Gzwyob.vqZY4ZADJu87g-Z36mdezrPIdz2HElLbkxVYnM"



@bot.listen()
async def on_message(message):
  if message.channel.id ==1004884958713753610 and message.content.startswith("-suggest ") : 
      if  len(message.content)>8 and message.author!=bot.user:
          embed = discord.Embed(    
          title="suggestion made by "+message.author.name,  description=message.content[9:], color = 0xf1c40f) 
          await message.channel.send(embed=embed)
          await message.delete()


  elif  message.channel.id ==1004884958713753610 and message.author!=bot.user:
    await message.delete()
    await message.channel.send("-suggest <your suggestion>")
    
    
  
  if message.content=="-suggest <your suggestion>":
    sleep(3)
    await message.delete()






bot.run(my_secret)
