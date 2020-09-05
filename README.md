# GachiBot-Discord
Gachibot for discord, old version)
## How to use:
<br/>
Change database in kachalochka.py
<br/>


    def __init__(self):
        self.mysql_c = pymysql.connect(
                             host='HOST',
                             user='USER',
                             password='PASSWORD',
                             db='DATABASE',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        try:
            with self.mysql_c.cursor() as cursor:
<br/>
Change bot token in start.py
<br/>

        embed_obj.description ="Используй **/гачи [команда] [аргументы...]**"
        await channel.send(embed=embed_obj)

    gachi.discord.run('TOKEN')
    
Add bot in channel and start script (start.py)
write 'гачи помоги'
