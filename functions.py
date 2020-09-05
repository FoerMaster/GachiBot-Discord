import random
import discord
import pymysql.cursors
import kachalochka

kachalaka = kachalochka.kachalka()

class commands:

    def show_help(self,obj,mobject,args):
        return obj.def_help()

    def show_citate(self,obj,mobject,args):

        citates = ["Я, как яйца - участвую, но не вхожу.","Никто не сделает первый шаг, потому что каждый думает, что это не взаимно"]
        embed_obj = discord.Embed(colour=0xff00d4)
        embed_obj.title = '**Великая цитата**'
        embed_obj.description = random.choice(citates)

        obj.msg("Showing citate")

        return embed_obj

    def predirect_ball(self,obj,mobject,args):

        simple = ["Да","Нет","Возможно","Вероятно","Не может быть","Мало вероятно","Может быть"]
        where = ["В раздевалке", "В качалочке","У шкафчика","На вокзале","Дома","На улице","В машине","В гачи-клубе","В гей-клубе","В клубе"]
        
        embed_obj = discord.Embed(colour=0xff00d4)


        if args[0].lower() == "где" or args[0].lower() == "в каком месте":
            embed_obj.description = random.choice(where)
        elif args[0].lower() == "когда" or args[0].lower() == "в какое время" or args[0].lower() ==  "во сколько":
            rtime = int(random.random()*86400)

            hours   = int(rtime/3600)
            minutes = int((rtime - hours*3600)/60)
            seconds = rtime - hours*3600 - minutes*60

            time_string = '%02d:%02d:%02d' % (hours, minutes, seconds)
            embed_obj.description = "По дате я не знаю, но вермя было " + time_string
        else:
            embed_obj.description = random.choice(simple)
            

        obj.msg("Showing predirect ball")

        return embed_obj

    def gachi_stata(self,obj,mobject,args):
        
        if args and len(args[0]) > 0:
            user = args[0]
            ListS = list(user)
            ListS.pop(0)
            ListS.pop(0)
            ListS.pop(0)

            if ("".join(ListS)) == "744679451505197108>":
                embed_obj = discord.Embed(colour=0xff00d4)
                embed_obj.title = '**Статистика**'
                embed_obj.description = "Лол, тупа бог"

                obj.msg("Showing gachi stata")

                return embed_obj
            stata = kachalaka.get_stata("".join(ListS))
        else:
            stata = kachalaka.get_stata(mobject.author.id)
        
        if stata:
 
            embed_obj = discord.Embed(colour=0xff00d4)
            embed_obj.title = '**Статистика**'
            embed_obj.description = "Прозвище: `" + stata['name'] + "`\nРанк: `" + kachalaka.get_rank(int(stata['level'])) + "`\nСила: `" + str(stata['strong']) + "/"+ str(int(stata['level'])*53) +"`\nРейтинг: `" + str(stata['rating']) + "`"

            obj.msg("Showing gachi stata")

            return embed_obj
        else:
            if not args or len(args[0]) <= 0:
                kachalaka.register_user(mobject.author.id)
            
            embed_obj = discord.Embed(colour=0xff00d4)
            embed_obj.title = '**Статистика**'
            embed_obj.description = "Ты зарегистрирован в гачи!"

            obj.msg("Showing gachi stata")

            return embed_obj

    def gachi_changename(self,obj,mobject,args):
        stata = kachalaka.get_stata(mobject.author.id)
        newname = (" ".join(args))
        if len(newname) < 4:
            embed_obj = discord.Embed(colour=0xff00d4)
            embed_obj.description = "Слишком короткое имя"

            obj.msg("Setting name")

            return embed_obj
        if len(newname) > 25:
            embed_obj = discord.Embed(colour=0xff00d4)
            embed_obj.description = "Слишком длинное имя"

            obj.msg("Setting name")

            return embed_obj
        if stata:

            embed_obj = discord.Embed(colour=0xff00d4)
            embed_obj.description = "Теперь тебя зовут *" + newname + "*"

            obj.msg("Setting name")

            kachalaka.set_name(mobject.author.id,newname)
            return embed_obj

        else:

            kachalaka.register_user(mobject.author.id)
            embed_obj = discord.Embed(colour=0xff00d4)
            embed_obj.description = "Ты еще не создан, напиши *гачи стата*"

            obj.msg("Setting name")

            return embed_obj


    def gachi_punch(self,obj,mobject,args):

        victim = 0
        attaker = kachalaka.get_stata(mobject.author.id)

        if args and (len(args[0]) > 0):
            user = args[0]
            ListS = list(user)
            ListS.pop(0)
            ListS.pop(0)
            ListS.pop(0)
            print("".join(ListS))
            victim = kachalaka.get_stata("".join(ListS))
        else:
            embed_obj = discord.Embed(colour=0xff00d4)
            embed_obj.description = "Ты забыл указать того, с кем ты будешь делать fisting!"
            return embed_obj 


        if not victim:
            kachalaka.register_user(mobject.author.id)
            embed_obj = discord.Embed(colour=0xff00d4)
            embed_obj.description = "Твой противник еще не знает о гачи, пусть напишет *гачи стата*"

            return embed_obj

        if attaker:

            winner = 0
            a_points = 0
            v_points = 0

            attaker_points = random.randint(0, attaker["strong"])
            victim_points = random.randint(0, victim["strong"])

            if attaker_points > victim_points:
                winner = attaker
                a_points = float('{:.2f}'.format((attaker["strong"] / victim["strong"]) / 5))
                kachalaka.user_rating_up(attaker["id"],a_points)
            else:
                winner = victim 
                v_points = float('{:.2f}'.format((victim["strong"] / attaker["strong"]) / 5))
                kachalaka.user_rating_up(victim["id"],a_points)

            

            

            embed_obj = discord.Embed(colour=0xff00d4)
            embed_obj.title = "**Итоги боя**"
            embed_obj.description = "**" + attaker["name"] + "**: Hey, **" + victim["name"] +"**, давай выясним, кто босс этой качалки! Снимай свои побрякушки и выясним это прямо здесь!\n Порванные трусы увозились из качалки на камазах, и в этом сражении победителем вышел **" + winner["name"] + "**\n Слава новому боссу качалки!\n\n ```Рейтинг:\n" + attaker["name"] + ": " + str(attaker["rating"]) + " (+" + str(a_points) + ")" + "\n" + victim["name"] + ": " + str(victim["rating"]) + " (+" + str(v_points) + ")```"

            return embed_obj

        else:

            kachalaka.register_user(mobject.author.id)
            embed_obj = discord.Embed(colour=0xff00d4)
            embed_obj.description = "Ты еще не создан, напиши *гачи стата*"

            return embed_obj

    def show_creators(self,obj,mobject,args):

        embed_obj = discord.Embed(colour=0xff00d4)
        embed_obj.title = '**Создатели Gachi-бота**'
        embed_obj.description = "Главный кодер: **Foer**\nИдея/вдохновитель: **vk.com/gachibots**\nЕсли есть баги пишите `Foer#7777`\n*И да, бот сделан за один день, багов может быть уйма)*"

        obj.msg("Showing creators")

        return embed_obj