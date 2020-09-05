import discord

class gachi:

    functions = {}

    def __init__(self):
        self.discord = discord.Client()

    def register(self,command,function,desc):
        self.functions[command] = {}
        self.functions[command]['func'] = function
        self.functions[command]['desc'] = desc

    def has(self,command):
        try:
            if command in self.functions:
                return self.functions[command]
            else:
                return 0
        except:return 0

    def msg(self,message):
        print("[GachiBot] "+message)

    def def_help(self):
        embed_obj = discord.Embed(colour=0xff00d4)

        embed_obj.title = '**Все доступные команды**'
        embed_obj.description = " "
        for i in self.functions:
            embed_obj.description = embed_obj.description + "`гачи " + i + " " + self.functions[i]['desc'] + '\n'
        self.msg("Showing help")
        return embed_obj


    def activate(self,mobject,command,args):
        try:
            args.pop(0) #Removing /gachi
            args.pop(0) #Removing command
            if self.has(command):
                return self.functions[str(command)]['func'](self,mobject,args)
        except:
            embed_obj = discord.Embed()
            embed_obj.color=0xff00d4
            embed_obj.description = 'Произошла ошибка при выполнении команды, напишите фоеру о ней!'
            return embed_obj