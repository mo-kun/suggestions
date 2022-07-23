import discord
from discord.ext import commands
from time import sleep

bot = commands.Bot(command_prefix="-")
bot.remove_command("help")

my_secret = "MTAwMDQyMzE5NDI5MDgxNTE4MA.GEnyJs.WVb_MyArpE8387RUNa2IIIjJeB2lSua1HiQBtw"



@bot.listen()
async def on_message(message):
  if message.channel.id ==1000467738738823319 and message.content.startswith("-suggest ") and message.author!=bot.user : 
      if  len(message.content)>8:
          embed = discord.Embed(    
          title="suggestion made by "+message.author.name,  description=message.content[9:], color = 0xf1c40f) 
          await message.channel.send(embed=embed)
          await message.delete()


  elif  message.channel.id ==1000467738738823319 and message.author!=bot.user:
    await message.delete()
    x = await message.channel.send("-suggest <your suggestion>")
    sleep(3)
    await bot.delete_message(x)
    







bot.run(my_secret)
