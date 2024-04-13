""" Importations """
from discord import *
import json

""" Code """
class server_info_class:
    def command(client, tree):
        with open("data/client.json") as file:
            client_data = json.load(file)
        color = client_data[1]
        color = int(color.lstrip("0x"), 16)

        @app_commands.command(description="Donne des informations sur le serveur.")
        async def server_info(interaction : Interaction):
            embed = Embed(title=f"{interaction.guild.name} Info", description="Information sur le Serveur", color=color)
            embed.add_field(name='🆔Serveur ID', value=f"{interaction.guild.id}", inline=True)
            embed.add_field(name='📆Créer le', value=interaction.guild.created_at.strftime("%b %d %Y"), inline=True)
            embed.add_field(name='👑Owner', value=f"{interaction.guild.owner.mention}", inline=True)
            embed.add_field(name='👥Members', value=f'{interaction.guild.member_count} Members', inline=True)
            embed.add_field(name='💬Channels', value=f'{len(interaction.guild.text_channels)} Texte | {len(interaction.guild.voice_channels)} Vocale', inline=True)
            try:
                embed.set_thumbnail(url=interaction.guild.icon.url)   
            except:
                pass
            embed.set_author(name=f"{client.user.name}", icon_url=client.user.avatar.url)

            await interaction.response.send_message(embed=embed)
        
        tree.add_command(server_info)