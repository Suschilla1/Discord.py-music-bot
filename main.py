import discord
from discord.ext import commands


from music_cog import music_cog

bot = commands.Bot(command_prefix='.')

bot.remove_command('help')

bot.add_cog(music_cog(bot))


bot.run(TOKEN)
