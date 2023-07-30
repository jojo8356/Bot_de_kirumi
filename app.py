import os
from dotenv import load_dotenv
import random
import discord
from discord.ext import commands
from discord import app_commands
import json

load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.tree.sync()
    return print("Bot pret")

"""
@bot.tree.command(name="test")
@app_commands.describe(user="Qui ?", texte="Texte à afficher")
async def test(i: discord.Interaction, user: discord.Member, texte: str):
    await i.response.send_message(f"{user.mention} a dit : {texte}")
"""


def random_bool():
    return random.choice([True, False])


def choice_true(i, lien, haki):
    choice = random_bool()
    user = i.user.mention
    if choice:
        return f"{user} vous avez eu {haki}\n{lien}"
    else:
        return f"{user} vous n'avez pas eu {haki}"


def random_typefruit():
    return random.choice(["logia", "pharamecia", "zoan"])


async def add_role_to_user(i, id):
    role = i.guild.get_role(int(id))
    await i.user.add_roles(role)


"""
@bot.tree.command(name="test")
async def test(i: discord.Interaction):
    await add_role_to_user(i,1127241431942172774)
    await i.response.send_message("c'est bon")
"""


@bot.tree.command(name="haki", description="Création du haki")
async def haki(i: discord.Interaction):
    user = i.user.mention
    choice1 = random_bool()
    choice2 = random_bool()
    if choice1 and choice2:
        await add_role_to_user(i, 1126885409041944678)
        await add_role_to_user(i, 1126885201860120626)
        text = f"Qu'est ce que j'entend !? {user} possède les deux haki ? Ça doit ètre un signe d'avenir prometteur !\nhttps://media.tenor.com/YR4vMPF4NZsAAAAC/luffy.gif"
    elif choice1:
        await add_role_to_user(i, 1126885409041944678)
        text = f"Toutes mes félicitations {user} tu possèdes le haki de l'observation !\nhttps://media.tenor.com/3VW1ZYi3JsQAAAAC/one-piece-luffy.gif"
    elif choice2:
        await add_role_to_user(i, 1126885201860120626)
        text = f"Oh , {user} a eu le haki de l'armement felicitations !\nhttps://media.tenor.com/uU4IefaDKwoAAAAC/haki-do.gif"
    else:
        text = "Oh.. dommage.. tu manques d'entraînement pour apprendre le Haki.. mais ne relache pas tes efforts tu finira par y arriver !"
    await i.response.send_message(text, ephemeral=False)


@bot.tree.command(
    name="depart",
    description="Création de l'inventaire, et début d'une nouvelle aventure",
)
async def depart(i: discord.Interaction):
    user = i.user.mention
    choice1 = random_bool()
    choice2 = random_bool()
    if choice1 and choice2:
        await add_role_to_user(i, 1126887751145488444)
        await add_role_to_user(i, "1126887867902337026")
        text = "Wow , {user} tu vient de voler un bateau remplis d'argent , bien joué !"
    elif choice1:
        await add_role_to_user(i, 1126887751145488444)
        text = f"{user} tu commences avec un bateau , felicitations !\nhttps://media.tenor.com/EqJbEe-SIkoAAAAS/one-piece-strawhats.gif"
    elif choice2:
        await add_role_to_user(i, "1126887867902337026")
        text = f"Oh , je vois que {user} a trouvé de l'argent en son début d'aventure !\nhttps://media.tenor.com/OzdknS29eaoAAAAC/%E0%B8%94%E0%B8%B5%E0%B9%83%E0%B8%88-nami.gif"
    else:
        text = "Oh.. tu n'a pas de bateau , ni d'argent , dommage.."
    await i.response.send_message(text, ephemeral=False)


@bot.tree.command(name="sabre", description="Donnation du sabre")
async def sabre(i: discord.Interaction):
    haki = "le sabre"
    choice = random_bool()
    user = i.user.mention
    if choice:
        text = f"{user} tu a un sabre , bien joué !\nhttps://media.tenor.com/EDY38R79tmAAAAAC/yoru-onepiece.gif"
        await add_role_to_user(i, "1126887901028954223")
    else:
        text = f"{user} tu n'a pas de sabre.. mais tu a trouvé une branche par terre !\nhttps://media.tenor.com/a_UuRf9IUPIAAAAC/tony-tony-chopper-chopper-crying.gif"
    await i.response.send_message(text, ephemeral=False)


@bot.tree.command(name="fruit", description="Donnation du fruit")
async def fruit(i: discord.Interaction):
    choice = random_bool()
    user = i.user.mention
    if choice:
        text = f"Wow , {user} a trouvé un fruit du demon , je me demande du quel il s'agit.. effectue /typefruit pour le voir !\nhttps://media.tenor.com/MJpeivM4mGIAAAAC/devil-fruit-fruit-du-demon.gif"
        await add_role_to_user(i, "1126887977226879088")
    else:
        text = f"Malhereusement {user} tu n'a pas de fruit ..\nhttps://media.tenor.com/f2Kz0-oJsbsAAAAd/tony-tony-chopper-cotton-canday.gif"
    await i.response.send_message(text, ephemeral=False)

@bot.tree.command(name="typefruit", description="Définition du type de fruit")
async def typefruit(i: discord.Interaction):
    roles = list(i.user._roles)
    roles = [str(x) for x in roles]
    if "1126887977226879088" in roles:
        user = i.user.mention
        dictio = {
            "logia": "https://media.tenor.com/yM3nmMmAtHQAAAAS/akainu-one-piece.gif",
            "pharamecia": "https://media.tenor.com/nrnBObPMpcIAAAAS/trafalgar-law-law.gif",
            "zoan": "https://media.tenor.com/m1r7DIpqpMgAAAAS/marco-one-piece.gif",
        }
        ids = {
            "logia": "1126887091960303767",
            "pharamecia": "1126887239574634526",
            "zoan": "1126887340099522580",
        }
        choice = random_typefruit()
        await add_role_to_user(i, ids[choice])
        if choice == "logia":
            text = f"{user} ton fruit est un fruit de type Logia , il te rendra insensible aux attaques physiques contre les adversaires sans haki de l'armement !"
        if choice == "pharamecia":
            text = f"{user} tu a un fruit de type paramecia , c'est un fruit qui permet entre autre de modifier ton corps !"
        if choice == "zoan":
            text = f"Ouah ! {user} ton fruit est un Zoan , tu a le pouvoir de te changer en animal !"
        text = f"{text}\n{dictio[choice]}"
        await i.response.send_message(text, ephemeral=False)
    else:
        await i.response.send_message("Tu n'as pas de fruit")

@bot.tree.command(name="zoan", description="création du type de zoan")
async def zoan(i: discord.Interaction):
    user = i.user.mention
    zoans = ["naturel", "antique", "mythologique"]
    choice = random.choice(zoans)
    roles = list(i.user._roles)
    roles = [str(x) for x in roles]
    if "1126887340099522580" in roles:
        if choice == "naturel":
            await add_role_to_user(i, "1127530100762624120")
            await i.response.send_message(
                f"{user} tu as un Zoan naturel , un fruit qui te permet de te changer en animal qui existe , un incecte , ou un renne par exemple..\nhttps://media.discordapp.net/attachments/1126524575165980835/1127292301652275301/chopper-dancing.gif"
            )
        elif choice == "antique":
            await add_role_to_user(i, "1127530651684458588")
            await i.response.send_message(
                f"{user} tu a un fruit vraiment surprenant.. ton Zoan te permet de te changer en animal préhistorique.. comme un Dinosaure !\nhttps://media.discordapp.net/attachments/1126524575165980835/1127292849868787723/3287860780_1_16_bUvXDVs9.gif"
            )
        elif choice == "mythologique":
            await add_role_to_user(i, "1127530882878681171")
            await i.response.send_message(
                f"Ben ça alors.. {user} a eu un Zoan mythologique apparement ce fruit vaudrait de l'or , il permet de se changer en creature mythologique comme le phœnix ou le dragon !\nhttps://media.discordapp.net/attachments/1126524575165980835/1127293415139332096/kaido-dragon-one-piece_480x480.gif"
            )
    else:
        await i.response.send_message("Tu n'as pas le type de fruit Zoan")


bot.run(token)
