
import gachi
import discord
import functions
import kachalochka

commands = functions.commands()
gachi = gachi.gachi() #gachi class

kachalaka = kachalochka.kachalka()

################################################################
##                      FUNCS INITIALIZATION                  ##
################################################################

def setup_functions():
    gachi.register("помоги",commands.show_help,"`- Показать все доступные команды")    
    gachi.register("цитата",commands.show_citate,"`- Попросить великую цитату от гачи-бота")  
    gachi.register("шар",commands.predirect_ball,"[вопрос]` - Спросить что-либо у бота") 
    gachi.register("стата",commands.gachi_stata,"[пользователь]` - Узнать статистику") 
    gachi.register("имя",commands.gachi_changename,"[имя]` - Сменить имя") 
    gachi.register("борьба",commands.gachi_punch,"[пользователь]` - Сделать fisting другому пользователю") 
    gachi.register("создатель",commands.show_creators,"` - узнать создателей") 
################################################################
##                      BOT INITIALIZATION                    ##
################################################################

@gachi.discord.event
async def on_ready():
    gachi.msg('We have logged in as {0.user}'.format(gachi.discord))
    setup_functions()
    activity = discord.Game(name="anal fisting")
    await gachi.discord.change_presence(status=discord.Status.idle, activity=activity)

@gachi.discord.event
async def on_message(message):

    #Ignoring self
    if message.author == gachi.discord.user:
        return

    channel = message.channel
    messa = message.content
    
    command = messa.split(' ')

    kachalaka.user_strong_up(message.author.id,1)

    if not command[0].lower().startswith('гачи'):
        return

    try:
        if gachi.has(command[1].lower()):
            await channel.send(embed=gachi.activate(message,command[1],command))
        else:
            embed_obj = discord.Embed()
            embed_obj.description = "Я не знаю такой команды, пиши **/гачи помоги** для подробностей!"
            embed_obj.color=0xff00d4
            await channel.send(embed=embed_obj)
    except:
        embed_obj = discord.Embed()
        embed_obj.color=0xff00d4
        embed_obj.description ="Используй **/гачи [команда] [аргументы...]**"
        await channel.send(embed=embed_obj)

gachi.discord.run('TOKEN')
