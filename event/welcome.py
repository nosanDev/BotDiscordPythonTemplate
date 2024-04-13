###################################################################################################################################################################################
###################################################################################################################################################################################
############################################################################  welcome.py for Template  ############################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################


"""" Importations """
from discord import *
import json

""" Code """
class welcome_def:
    def welcome(client, tree):

        @client.event
        async def on_member_join(member):

            with open("data/join_sys.json") as file:
                server_info = json.load(file)
                info = server_info[f"{member.guild.id}"]
            
            etat = info[0]
            channel = client.get_channel(info[1])
            if info[2] == None:
                msg = f""
            else:
                msg = info[2]
            
            print(etat)
            if etat:

                embed = Embed(color=0x0000D6, description=f"Bienvenue à {member.name} sur {member.guild.name}\n{msg}")
                embed.set_author(name=f"Bienvenue sur {member.guild.name}", icon_url=member.guild.icon_url)

                await channel.send()