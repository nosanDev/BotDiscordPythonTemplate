""" Importations """

from discord import *

class ping_class:
    def commande(ctx, client):
        async def ping(ctx):
            latency = client.latency * 1000 # Convertir la latence de secondes en millisecondes
            await ctx.send(f'Pong! Latency: {latency:.2f}ms')

        
                