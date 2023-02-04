import mysql.connector
import os
query = os.environ.get('a').lower()
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
conn = mysql.connector.connect(
    host=os.environ['MYSQL_HOST'],
    port=os.environ['MYSQL_PORT'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD']
)
cursor = conn.cursor()
try:
    cursor.execute(f'''
               {query}
                    ''')
    with open('data.txt','w') as f:    
        for row in cursor.fetchall():
            
            f.write(str(row))
            print(row)

       
except Exception as e:
    if str(e).__contains__('no results'):
            data = f'{query} concluida' 
    else : 
        
        data = str(e)
        with open('data.txt','w') as f:
            f.write("ERROR")
            f.write(data)

conn.commit()
