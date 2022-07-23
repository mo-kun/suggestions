import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="-")
bot.remove_command("help")

my_secret = "MTAwMDQyMzE5NDI5MDgxNTE4MA.GEnyJs.WVb_MyArpE8387RUNa2IIIjJeB2lSua1HiQBtw"



@bot.listen()
async def on_message(message):
  if message.channel.id ==999823889653846060 and message.content.startswith("-suggest") : 
      if  len(message.content)>8:
          await message.delete()
          embed = discord.Embed(    
          title="suggestion made by "+message.author.name,  description=message.content[9:], color = 0xf1c40f) 
          await message.channel.send(embed=embed)
      
      elif 0<=len(message.content)<=8:
          await message.delete()







bot.run(my_secret)
