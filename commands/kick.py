""" Importations """

from discord import *
import json

class kick_class:
    def commande(client, tree):

        with open("data/client.json") as file:
            client_data = json.load(file)
            color = client_data[1]
            color = int(color.lstrip("0x"), 16)

        @app_commands.default_permissions(kick_members=True)
        @app_commands.describe(member="Membre à expulser.", raison="Raison du kick.")
        @app_commands.command(description="Kick un membre.")
        async def kick(interaction : Interaction, member : Member, raison : str = "Aucune raison."):
            if member == interaction.user:
                await interaction.response.send_message("Vous ne pouvez pas vous kick.", ephemeral=True)
            else:
                embed = Embed(color=color, description=f"{member.mention} vient d'être kick par {interaction.user.mention}\n**Raison :** {raison}")
                embed.set_author(name=client.user.name, icon_url=client.user.avatar.url)

                await member.kick(reason=raison)
                await interaction.response.send_message(embed=embed)

        tree.add_command(kick)