import psycopg2
from config import CONNECTION_STRING

try:
    connection = psycopg2.connect(CONNECTION_STRING)
    print("Connected to Neon PostgreSQL database successfully!")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM songs")
    

    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
    cursor.close()
    connection.close()
    
except Exception as e:
    print(f"Error: {e}")   