import sqlite3

class sqllite_db(object):

        def __init__(self, table= 'SHOWS'):
                self.table = table                


        def  get_connection(self):
                conn = None
                try:
                        conn = sqlite3.connect('db/tvshows.sqlite')
                except sqlite3.error as e:
                        print(e)      
                return conn
                

        def init_table(self):
                con = self.get_connection()
                c = con.cursor()
                c.execute(""" CREATE TABLE IF NOT EXISTS {t} (
                        Id text, 
                        Url text,
                        Name text,
                        Season text,
                        Number text,
                        Type text,
                        Airdate text,
                        Airtime text,
                        Airstamp text,
                        Runtime text,
                        Image text,
                        Summary text,
                        Link text,
                        Average_rating text,
                Embedded_show text)""".format(t= self.table))
                con.commit()
                con.close()

        def bulk_data(self, data):
                data.to_sql(self.table, con=self.get_connection(), if_exists = "replace")
        
        def validate(self):
                con = self.get_connection()
                c = con.cursor()
                c.execute(""" SELECT count(*) from {t} """.format(t = self.table))
                count = c.fetchone()[0]
                con.commit()
                con.close()
                return count
