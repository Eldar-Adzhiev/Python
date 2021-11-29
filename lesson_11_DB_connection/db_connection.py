import psycopg2  #Библиотека для работы с Базой данных

# Коннекшин с базой

conn = psycopg2.connect(dbname = 'qa_ddl_24_140',
                        user = 'user_24_140',
                        password = '123',
                        host = '159.69.151.133',
                        port = '5056')

cursor = conn.cursor()

# Cначала нужно проверить коннект с базой!!!

# Select

# if conn:
#     print('Connection is ok')
#
#     select_query = 'select * from public.salary_2'
#     execute_q= cursor.execute(select_query)
#
#
#     get_query_result = cursor.fetchall() # Команда которая fetchall компует
#     # все что прилетело с базы. Без этой команды ничего не прилетит
#     print('execute_q', get_query_result)
#
#     for i in get_query_result:
#         print(i)

# insert   Добавление данных в таблицу

for i in range(0,10):

    if conn:
        print('Connction Insert qa_ddl_24_140')

        salary = str(40 + i*100)

        insert_query = 'insert into public.salary_2(monthly_salary)'\
                   'values(' + salary + ')'

        cursor.execute(insert_query)

        conn.commit()
cursor.close


