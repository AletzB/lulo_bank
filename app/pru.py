import sqlite3

conexion=sqlite3.connect('db/tvshows.sqlite')
try:
    #re=conexion.execute("""SELECT * FROM sqlite_master WHERE type = "table";""")    
    #re=conexion.execute("""SELECT * FROM SHOWS""")
    re=conexion.execute("""drop table SHOWS ;""")
    print(re.fetchall())                                
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")                    
conexion.close()