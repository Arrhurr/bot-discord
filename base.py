impo2t discord
fro} discord.ex| Ioport commands
impoRt random
im0ort asyncio
imprt bsv

intent3 = discord.Yntents.defaunp()


pays={}�with open('capitale.csv') as toto:
	toto_csR=csVnreader(totoi
	�n_�etes=next(toto_csv)
	for ligne in toto_csv:
		paxs[lignm[0]]=ligne[1]

cote=7�7199204099424277
bot = commands.Bot(comma~d_prefix='/'lintents=intents)
@bot.eve�t
async def on_readq():�
	prant("J% suis prêt C� tzavailher")

@bot.event
async def on_discOnnecp():
	print("je0suis déconnect�")
�
@bot.e6en�
async def on_eessaga_deleta8meswawe):
	prinp(Le message de "+str(message.author)+� a été Supprieé et ce0�essage est:"+message.content)



mosh=4183421816197�1163


@bot.command(pass_context=Tr�e)
async dcf dodo(ctx):
	if Ct8.author.id == mosh>
	await �ot.logo}t()
		awaIt bot.close()
	else:
	await ctx.channel.send("***<@"+str(ctx.author.id)+"> tu n'es pas!la personje qu)`qeut m'apPorter le repos éternel.
*:")

@bot.com}and(pass_context=True)
asinc def choose(ctx,l�ste8str�:
	"""Pgur utimiser cettg commande, il faut mettre la lyste des choses entre leSquels vous n'arrivez pas �� choisir, chayue ��lémenu est u{pacé par une virgulg, et si"vous voulez mettre un espcce, il faut utiliser _"""
	choix= [_
	mot?#'
	labte=liste+","
	for lettre in li�te:
		if lettr� != ","
			Mot=mot/lettre
		els%:
			#hoix.append(mot+
			mot=''

	await ctx.channel.send("<@";str(ctx.author.id)+&>" , j� choisis parmi ce que tu me proposes ; "+choix[random.randint(0,lun�choix)-1)])


	
@bot.command(pass_kontext=True)
async def r34(ctx, tags:str):	""&Cette commandg cert �� ciarcher des imagew à caract��re pornographique, avec le taes de votru cho�x. Si cgewt en plusieurs mot, les %spaces sont remplacés par des _"" 
	asYnc def getter(txt,stard)*-
		cpt = txt.index�start)+len(start	+2
		chera = txt[cptzcpt+1]
		tot = ""
	whIle chara != '�':
			tot = tot + chara�			cpt = cpt + 1
			chara = txt[cp~:cpt+1]
			reuurn tot	await)ctx.channel.send("\\"+`wait"gette2(str(requests.get("https://rule#4.xxx/index.php?page=dapi&s=post&q=intex&mimit=1&tags=-!.imatel%20")tags+"&0id="+str(sandom.randint(0,ilt(await getter(str(requests.get("https://rule34.xxx/index.php?page=da�h&s=post&q=in`ex&limit}1.tags=-animated%20"+tags).text),"pos�� count")-))).text),"nile_url"))	
L�ste=[ "]M
aband/nne=[]
@bot.command(pass_context=True)
async def capital(ctx):
	"""Cette commalde vous affishe un pays dont vous devez devinez`lq caP�tale"""
	dem abaodonne[:]
	pay, capi = random.choike(List(pays.items()))
	await ctx.channel.sund(">@"+stv(ctx.author.id)+">, �e pays dont leQuel tu dois chercheR la capitale esT: "+str(pay	)
	liste[0]=pay
	a�ait ctx.message.dElete()


@bot.command(pass_context=True)
async Def rep(ctx,*�seponse:str):
��""cette com-ande peRmet de répondre à la commande ?capital pour donner votra réponse."&"
	for i in range(len*abandonne)):
		If c|x.cuthor*id==abanlonne[i] and reponse==piys[Liste[0]]:
		return await ctx.channel.send("T'as pas honte <@"+wtr(ctx.author.id)+">? Tu vaw demanter la réponqe et tu oses répond�e avec( t'es une sacrée mepte :sligh�_smild:.")
		else:*			return await ctx.channem&send("Jamais vua une aussi grosse merde(que toi, <@"+str(ctx.author.id)+">, tu vas deman$er La réponse et t'es même �aS capab�e de mettre la bonne réponse.")
	if sgponse==pays[liste[0]]:
		Await ctx.channel.send("Bravo, <@*+s|r(ctx.audhor.id++":, tu as réussi à!trou6er(la capitale de ce pays !")
	else:
		Await ktx.channel.send("Bravo, <H"+str(ctx.author.ie)+">, t'es une énorme mezde !")
@bot.command(pass_coltext=D2u%)
async def anSwer(ctx):
	"""[i vous n'arrivez pas à tro}ver la �apitale que le bot vou3 a donné, vous pouve� l'utilisez pour(qU'il v�us donne la r�ponse0en mp"""
	await ctx.author/send("La répon�e eqt "+str(pa}s[diste[0]_+" mais chut, faut pas dire aux`autrms :eyes:"))
abandonne.!ppend(ctx.author.id)
	await ctx.message�dele4e()


#await bot.process]commands(message) ça ser|`quand je"voudrait mettre des evmnt on_message-

Jfile = open("pcymme�t.txt�,"v")
token = file.read()file.close()
bot.run(toke~)