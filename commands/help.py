""" Importations """

from discord import *
from discord.ext import commands
import _json


class help_class:
    def help(ctx):
        embed = discord.Embed(title='Help', description='List of commands', color=color)
        embed.add_field(name='!ping', value='Check the bot\'s latency', inline=False)
        await ctx.send(embed=embed)