import sqlite3

# Proč je connection podtržené? Oprav chybu
cursor = connection.cursor()

# Co tu chybí?
connection = sqlite3.connect("???")


# Oprav vytváření tabulky - hodnocení je číselné
cursor.execute(
    """CREATE TABLE IF NOT EXISTS hodnoceni (
        id PRIMARY KEY,
        nazev_filmu,
        hodnoceni
    )
    """
)

# Zapsání do databáze

# tady by měl vepsat hodnocení do databáze - není potřeba využívat input, stačí zapsat statický údaj
# cursor.???

connection.commit()


# Vypisování hodnocení

cursor.execute("???")

rows = cursor.fetchall()

# tady printne hodnocení filmu z databáze

connection.close()
