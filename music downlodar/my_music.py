import sqlite3


conn = sqlite3.connect("music_downloader.db", check_same_thread=False)
 
cursor = conn.cursor()
 
# cursor.execute("Drop table users")
 
cursor.execute('''CREATE TABLE IF NOT EXISTS Data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username STRING ,
                    email STRING UNIQUE ,
                    password STRING 
                )''')


def add_entry(username,Email,password,):
    cursor.execute(f"""INSERT INTO Data (username,email, password) VALUES (?, ?, ?)""",(username,Email, password))
 
    conn.commit()


conn.commit()

