import discord
from discord.ext import commands
TOKEN = 'NzI2MTYxNzU5NDEyNjgyODYy.XvZRVw.8WS1Wrx1OPOpBoGNGTu6esX93IM'
bot = commands.Bot(command_prefix='!')
@bot .command(pass_context=True)
async def test(ctx, arg):
	await ctx.send(arg)
	
bot.run(TOKEN)