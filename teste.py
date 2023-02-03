import psycopg2
import pandas as pd
import os
query = os.environ.get('a').lower()
# query = 'CREATE TABLE testes_v3 as (select 1+1 as var)'

def execute_sql():
    conn = psycopg2.connect(host='localhost', port='5432',database='postgres',user='postgres', password='changeme')
    cursor = conn.cursor()
    try:
        cursor.execute(f'''
                {query}
                    ''')
        
        for row in cursor.fetchall():
            print(row)
            data = row
       
    except Exception as e:
        if str(e).__contains__('no results'):
                data = f'{query} concluida' 
        else : 
            data = str(e)
    print(data)
    with open('data.txt','w') as f:
        f.write(str(data))
        f.close()

    conn.commit()
execute_sql()		   