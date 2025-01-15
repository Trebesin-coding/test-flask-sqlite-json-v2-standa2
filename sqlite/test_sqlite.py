import sqlite3

# Proč je connection podtržené? Oprav chybu

# Co tu chybí?
connection = sqlite3.connect("filmy.db")

cursor = connection.cursor()

# Oprav vytváření tabulky - hodnocení je číselné
cursor.execute(
    """CREATE TABLE IF NOT EXISTS hodnoceni (
        id INT PRIMARY KEY,
        nazev_filmu TXT,
        hodnoceni INT
    )
    """
)

# Zapsání do databáze

# tady by měl vepsat hodnocení do databáze - není potřeba využívat input, stačí zapsat statický údaj
cursor.execute("""INSERT INTO hodnoceni (id, nazev_filmu, hodnoceni) VALUES (1,'cars', 10)""")

connection.commit()


# Vypisování hodnocení

cursor.execute("SELECT * FROM hodnoceni")

rows = cursor.fetchall()

# tady printne hodnocení filmu z databáze
print(rows[0][2])

connection.close()
