import discord
from discord.ext import commands
import random
import asyncio
import csv

intents = discord.Intents.default()
mosh=418342181619761163
lily=700635398006898758
kev=398883942515867653
rom=710103820272926807
azmog=307762856487550976
stib=493467201769308161
brebre=460125845176975369
lixlix=756563934533779497
jaune=606507587307044895

pays={}
with open('capitale.csv') as toto:
	toto_csv=csv.reader(toto)
	en_tetes=next(toto_csv)
	for ligne in toto_csv:
		pays[ligne[0]]=ligne[1]

bote=777199204099424277
bot = commands.Bot(command_prefix='?',intents=intents)
@bot.event
async def on_ready():
	print("Je suis prêt à travailler")

@bot.event
async def on_disconnect():
	print("je suis déconnecté")

@bot.event
async def on_message_delete(message):
	print("Le message de "+str(message.author)+" a été supprimé et ce message est:"+message.content)

@bot.event
async def on_typing(channel, user, when):
    global couldown_dm
    if user.id == None:
        if user.dm_channel == None:
            await user.create_dm()
        await user.dm_channel.send("Tu peux fermer ta gueule ?")






@bot.command(pass_context=True)
async def dodo(ctx):
	if ctx.author.id == mosh:
		await bot.logout()
		await bot.close()
	else:
		await ctx.channel.send("***<@"+str(ctx.author.id)+"> tu n'es pas la personne qui peut m'apporter le repos éternel.***")


@bot.command(pass_context=True)
async def choose(ctx,liste:str):
	"""Pour utiliser cette commande, il faut mettre la liste des choses entre lesquels vous n'arrivez pas à choisir, chaque élément est espacé par une virgule, et si vous voulez mettre un espace, il faut utiliser _"""
	choix= []
	mot=''
	liste=liste+","
	for lettre in liste:
		if lettre != ",":
			mot=mot+lettre
		else:
			choix.append(mot)
			mot=''

	await ctx.channel.send("<@"+str(ctx.author.id)+">"", je choisis parmi ce que tu me proposes : "+choix[random.randint(0,len(choix)-1)])



@bot.command(pass_context=True)
async def r34(ctx, tags:str):
	"""Cette commande sert à chercher des images à caractère pornographique, avec le tags de votre choix. Si c'est en plusieurs mot, les espaces sont remplacés par des _"""
	async def getter(txt,start):
		cpt = txt.index(start)+len(start)+2
		chara = txt[cpt:cpt+1]
		tot = ""
		while chara != '"':
			tot = tot + chara
			cpt = cpt + 1
			chara = txt[cpt:cpt+1]
			return tot
	await ctx.channel.send("\\"+await getter(str(requests.get("https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=1&tags=-animated%20"+tags+"&pid="+str(random.randint(0,int(await getter(str(requests.get("https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=1&tags=-animated%20"+tags).text),"posts count"))))).text),"file_url"))
liste=[""]
abandonne=[]
@bot.command(pass_context=True)
async def capital(ctx):
	"""Cette commande vous affiche un pays dont vous devez devinez la capitale"""
	del abandonne[:]
	pay, capi = random.choice(list(pays.items()))
	await ctx.channel.send("<@"+str(ctx.author.id)+">, le pays dont lequel tu dois chercher la capitale est: "+str(pay))
	liste[0]=pay
	await ctx.message.delete()


@bot.command(pass_context=True)
async def rep(ctx,*,reponse:str):
	"""cette commande permet de répondre à la commande ?capital pour donner votre réponse."""
	for i in range(len(abandonne)):
		if ctx.author.id==abandonne[i] and reponse==pays[liste[0]]:
			return await ctx.channel.send("T'as pas honte <@"+str(ctx.author.id)+">? Tu vas demander la réponse et tu oses répondre avec, t'es une sacrée merde :slight_smile:.")
		else:
			return await ctx.channel.send("Jamais vue une aussi grosse merde que toi, <@"+str(ctx.author.id)+">, tu vas demander la réponse et t'es même pas capable de mettre la bonne réponse.")
	if reponse==pays[liste[0]]:
		await ctx.channel.send("Bravo, <@"+str(ctx.author.id)+">, tu as réussi à trouver la capitale de ce pays !")
	else:
		await ctx.channel.send("Bravo, <@"+str(ctx.author.id)+">, t'es une énorme merde !")

@bot.command(pass_context=True)
async def answer(ctx):
	"""Si vous n'arrivez pas à trouver la capitale que le bot vous a donné, vous pouvez l'utilisez pour qu'il vous donne la réponse en mp"""
	await ctx.author.send("La réponse est "+str(pays[liste[0]]+" mais chut, faut pas dire aux autres :eyes:"))
	abandonne.append(ctx.author.id)
	await ctx.message.delete()


#await bot.process_commands(message) ça sert quand je voudrait mettre des event on_message


file = open("payement.txt","r")
token = file.read()
file.close()
bot.run(token)