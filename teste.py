import mysql.connector
import os
query = os.environ.get('a').lower()
conn = mysql.connector.connect(
        host = '192.168.18.8',
        user = 'daniel',
        password ='',
        database = 'mysql'

)
cursor = conn.cursor()
try:
    cursor.execute(f'''
                {query}
                    ''')
    with open('data.txt','w') as f:    
        for row in cursor.fetchall():
            
            f.write(str(row))

       
except Exception as e:
    if str(e).__contains__('no results'):
            data = f'{query} concluida' 
    else : 
        
        data = str(e)
        with open('data.txt','w') as f:
            f.write("ERROR")
            f.write(data)

conn.commit()
