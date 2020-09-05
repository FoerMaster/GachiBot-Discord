import discord
import pymysql.cursors

class kachalka:

    ranks = {
        0:"NoName",
        1:"BOY NEXTDOOR",
        2:"Lather man",
        3:"Dungeon master",
    }

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
                sql = "CREATE TABLE IF NOT EXISTS `users` (`id` bigint(255) NOT NULL,`name` longtext CHARACTER SET utf8 NOT NULL,`level` int(255) NOT NULL,`strong` int(255) NOT NULL,`rating` int(255) NOT NULL)"
                cursor.execute(sql)
            self.mysql_c.commit()
            print("[GachiSQL] Table generated")
        except: print("")

    def get_rank(self,level):
        if level in self.ranks:
            return self.ranks[level]
        elif level > 3:
            return "Billy"
    


    def register_user(self,id):
        try:
            with self.mysql_c.cursor() as cursor:
                sql = "INSERT INTO `users`(`id`, `name`, `level`, `strong`, `rating`) VALUES (%s,%s,%s,%s,%s)"
                cursor.execute(sql, (int(id),"noname",1,1,0))

            self.mysql_c.commit()

            print("[GachiSQL] User registred")
        except: return 0

    def set_name(self,id,name):
        try:
            with self.mysql_c.cursor() as cursor:
                sql = "UPDATE `users` SET `name`=%s WHERE `id` = %s"
                cursor.execute(sql, (name,int(id)))

            self.mysql_c.commit()

            print("[GachiSQL] User name changed")
        except: return 0   

    def set_level(self,id,level):
        try:
            print(level)
            with self.mysql_c.cursor() as cursor:
                sql = "UPDATE `users` SET `level`=%s WHERE `id` = %s"
                cursor.execute(sql, (int(level),int(id)))

            self.mysql_c.commit()

            print("[GachiSQL] User level changed")
        except: return 0   

    def get_stata(self,id):
        try:
            with self.mysql_c.cursor() as cursor:

                # sql = "INSERT INTO `users`(`id`, `name`, `level`, `strong`, `rating`) VALUES (%s,%s,%s,%s,%s)"
                self.mysql_c.commit()

                sql = "SELECT * FROM `users` WHERE `id`=%s"
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
                #result['level'] =
                return result

            print("[GachiSQL] User getting")
        except: return 0

    def user_strong_up(self,id,count):
        try:
            with self.mysql_c.cursor() as cursor:
                sql = "UPDATE users SET strong = strong + %s WHERE id = %s"
                cursor.execute(sql, (count,id))
                self.mysql_c.commit()

            
            with self.mysql_c.cursor() as cursor:

                sql = "SELECT * FROM `users` WHERE `id`=%s"
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
                if result:
                    try:
                        calc_exp = int(result['level']) * 53
                        if result['strong'] >= calc_exp:
                            self.set_level(id,result['level'] + 1)
                    except: print("")
            self.mysql_c.commit()

            print("[GachiSQL] User strong up")
        except: return 0

    def user_rating_up(self,id,count):
        try:
            with self.mysql_c.cursor() as cursor:
                sql = "UPDATE users SET rating = rating + " + str(count) + " WHERE id = %s"
                cursor.execute(sql, (id,))

            self.mysql_c.commit()

            print("[GachiSQL] User rating up")

        except: return 0