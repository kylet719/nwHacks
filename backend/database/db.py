import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_songs_by_mood(mood):
    try:
        connection = psycopg2.connect(os.getenv('DB_CONNECTION_STRING'))
        cursor = connection.cursor()

        # Query songs where mood matches the parameter (case insensitive)
        cursor.execute("SELECT name, author FROM songs WHERE LOWER(mood) = LOWER(%s)", (mood,))
        rows = cursor.fetchall()
        
        # Create list of songs with name and author
        songs = [{"title": row[0], "artist": row[1]} for row in rows]
        
        cursor.close()
        connection.close()
        
        return songs
        
    except Exception as e:
        print(f"Error: {e}")
        return []

# try:
#     connection = psycopg2.connect(os.getenv('DB_CONNECTION_STRING'))
#     print("Connected to Neon PostgreSQL database successfully!")

#     cursor = connection.cursor()

#     cursor.execute("SELECT * FROM songs")
    

#     rows = cursor.fetchall()
    
#     for row in rows:
#         print(row)
        
#     cursor.close()
#     connection.close()
    
# except Exception as e:
#     print(f"Error: {e}")

# songs = get_songs_by_mood("happy")
# for song in songs:
#     print(f"Name: {song['name']}, Author: {song['author']}")   