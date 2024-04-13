###################################################################################################################################################################################
###################################################################################################################################################################################
############################################################################  welcome_set.py for Template  ########################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################


""" Importations """
from discord import *
import json


""" Class """
class welcome_def:
    """ Def pour Import """
    def commande(client, tree):
        @app_commands.default_permissions(administrator=True)
        @app_commands.command(description="C'est pour configurer le salon de bienvenue.") # Defini la fonction async def test 
        async def welcome_set(interaction : Interaction, channel : TextChannel, état : bool = None): # Creation de la commande Test avec definition de l'interaction
            with open("data/set_bienv.json") as file :
                data = json.load(file)
            data[f"{interaction.guild.id}"] = [channel.id, état]
            with open("data/set_bienv.json", "w") as file :
                json.dump(data, file)
            embed1 = Embed(colour=0x1de9b6, title="Bienvenue", description=f" > Le système de message de bienvenue a bien été configurer !")
            embed1.add_field(name="Salon", value=f"{channel}", inline=True)
            embed1.add_field(name="État", value=f"{état}", inline=True)
            await interaction.response.send_message(embed=embed1, delete_after=20)
        tree.add_command(welcome_set)