import psycopg2
conn = psycopg2.connect(database='clientdb', user='postgres', password='1111')

with conn.cursor() as cur:
    def create_db(cursor):
        cursor.execute("DROP TABLE client, phone")
        cursor.execute("CREATE TABLE client "
                       "(id SERIAL PRIMARY KEY, "
                       "first_name VARCHAR (10) NOT NULL,"
                       "second_name VARCHAR(20) NOT NULL,"
                       "email VARCHAR(30) NOT NULL UNIQUE);")
        cursor.execute("CREATE TABLE phone"
                       "(id SERIAL PRIMARY KEY,"
                       "client_id INTEGER REFERENCES client(id) ON DELETE CASCADE,"
                       "phone_number INTEGER UNIQUE);")
        conn.commit()
    create_db(cur)

    def new_client(cursor):
        f_n = input('Имя клиента:')
        s_n = input('Фамилия клиента:')
        e_m = input('Email клиента')
        cursor.execute(f"""INSERT INTO client(first_name,second_name,email) VALUES('{f_n}','{s_n}','{e_m}')
                             RETURNING id, first_name, second_name, email;""")
        conn.commit()
        print(cursor.fetchall())

    def add_phone(cursor):
        phone = int(input('Введите телефон нового клиента: '))
        id_check = int(input('Введите id клиента: '))
        cursor.execute(f"""INSERT INTO phone(client_id,phone_number) VALUES('{id_check}','{phone}')
                             RETURNING id, client_id,phone_number;""")
        conn.commit()
        print(cursor.fetchall())

    def change_data(cursor):
        id_check = int(input('Введите id клиента: '))
        f_n = input('Имя клиента: ')
        s_n = input('Фамилия клиента: ')
        e_m = input('Email клиента: ')
        cursor.execute(f"""UPDATE client
                              SET first_name = '{f_n}',second_name = '{s_n}',email = '{e_m}'
                            WHERE id = '{id_check}'
                        RETURNING id, first_name, second_name, email;""")
        conn.commit()
        print(cursor.fetchall())

    def del_phone(cursor):
        id_check = int(input('Введите id клиента: '))
        cursor.execute(f"""DELETE FROM phone
                            WHERE client_id = '{id_check}';""")
        conn.commit()

    def del_client(cursor):
        id_check = int(input('Введите id клиента: '))
        cursor.execute(f"""DELETE FROM client
                                    WHERE id = '{id_check}';""")
        conn.commit()

    def search(cursor):
        print("Выберите атрибут поиска клиента:\n"
              "1. Имя\n"
              "2. Фамилия\n"
              "3. email\n"
              "4. Телефон")
        choice = int(input())
        if choice == 1:
            name = input('Введите имя клиента: ')
            cursor.execute(f"""
                        SELECT * FROM client 
                        WHERE first_name = '{name}';""")
            print(cursor.fetchall())
        elif choice == 2:
            s_name = input('Введите фамилию клиента: ')
            cursor.execute(f"""
                        SELECT * FROM client 
                        WHERE second_name = '{s_name}';""")
            print(cursor.fetchall())
        elif choice == 3:
            email = input('Введите email клиента: ')
            cursor.execute(f"""
                        SELECT * FROM client 
                        WHERE email = '{email}';""")
            print(cursor.fetchall())
        elif choice == 4:
            phone = input('Введите телефон клиента: ')
            cursor.execute(f"""
                        SELECT * FROM client c
                        JOIN phone p ON p.client_id = c.id
                        WHERE phone_number = '{phone}';""")
            print(cursor.fetchall())

    while True:
        print('Выберите желаемое действие:\n'
              '1. Внести нового клиента\n'
              '2. Добавить телефон для существующего клиента\n'
              '3. Изменить данные о клиенте\n'
              '4. Удалить телефон клиента\n'
              '5. Удалить клиента\n'
              '6. Найти клиента по его имени, фамилии, email или телефону\n'
              '0. ЗАВЕРШИТЬ РАБОТУ'
              '')
        num = int(input())
        if num == 0:
            break
        elif num == 1:
            new_client(cur)
        elif num == 2:
            add_phone(cur)
        elif num == 3:
            change_data(cur)
        elif num == 4:
            del_phone(cur)
        elif num == 5:
            del_client(cur)
        elif num == 6:
            search(cur)

conn.close()
