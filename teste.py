import psycopg2
import pandas as pd
import os
query = os.environ.get('a')
def execute_sql():
    conn = psycopg2.connect(host='localhost', port='5432',database='postgres',user='postgres', password='changeme')
    cursor = conn.cursor()
    try:
        cursor.execute(f'''
                {query}
                    ''')
        
        data = 'SUCESS\n ' + str(cursor.fetchall())
    except Exception as e:
        if query.__contains__('CREATE') and query.__contains__('INSERT') and query.__contains__('DROP') == False:
                data = 'Bad ERROR ' + str(e) 
    
    with open('data.txt','w') as f:
        f.write(data)
        f.close()

    conn.commit()
execute_sql()		   