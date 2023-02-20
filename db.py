from mysql.connector import connect, Error
from configurebot import cfg


connection = connect(
        host=cfg['db_host'],
        port=3306,
        user=cfg['user'],
        password=cfg['password'],
        database=cfg['db_name'],
    )


def db_profile_exist(uid):
    select_users = "SELECT _id FROM users"
    with connection.cursor() as cursor:
        cursor.execute(select_users)
        result = cursor.fetchall()
        if (any(uid in i for i in result)):
            return True
        else:
            return False

def db_profile_insertone(query):
    with connection.cursor() as cursor:
        _id = query.get("_id", None)
        Read_like = 0
        Read_unlike = 0
        Unread_like = 0
        Unread = 0
        page = 0
        cursor.execute("INSERT INTO `users` (_id, Read_like, Read_unlike, Unread_like, Unread, page) VALUES (%s, %s, %s, %s, %s, %s)", (_id, Read_like, Read_unlike, Unread_like, Unread, page))
        connection.commit()

def db_profile_info(uid):
    page_info = "SELECT _id, page FROM users"
    with connection.cursor() as cursor:
        cursor.execute(page_info)
        result = cursor.fetchall()
        for i, j in result:
            if i == uid:
                return(j)

def db_book_pages():
    page_broke = "SELECT book_id FROM books"
    with connection.cursor() as cursor:
        cursor.execute(page_broke)
        result = cursor.fetchall()
        m = 0
        for i in result:
            m += 1
        print(m)
        return(m)

def db_page_next(query, uid):
    print(query)
    query += 1
    page_next = f"""UPDATE users SET page {query} WHERE _id = uid"""
    with connection.cursor() as cursor:
        cursor.execute(page_next)
        connection.commit()
        


# def db_profile_updateone(query, query2):
#     us_id = query.get("_id", None)
#     us_ban = query2.get("$set", None).get("ban", None)
#     us_access = query2.get("$set", None).get("access", None)
#     if us_ban != None:
#         try:
#             with connection.cursor() as cursor:
#                 sql_update_query = """UPDATE users SET ban = %s WHERE _id = %s"""
#                 input_data = (us_ban, us_id)
#                 cursor.execute(sql_update_query, input_data)
#                 connection.commit()
#         except Exception as e:
#             print(e)
#     else:
#         try:
#             with connection.cursor() as cursor:
#                 sql_update_query = """UPDATE users SET access = %s WHERE _id = %s"""
#                 input_data = (us_access, us_id)
#                 cursor.execute(sql_update_query, input_data)
#                 connection.commit()
#         except Exception as e:
#             print(e)
#     connection.commit()