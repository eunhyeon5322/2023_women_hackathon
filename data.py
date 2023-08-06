import pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='restaurantDB',
    charset='utf8mb4'
)
cur = conn.cursor()

#테이블 생성
cur.execute("Create Table restaurantTable(id int, name char(255), address char(255), phone int)")

# 데이터 삽입
def insert_data(id, name, address, phone):
    query = "INSERT INTO restaurantTable (id, name, address, phone) VALUES (%s, %s, %s, %s)"
    values = (id, name, address, phone)
    cur.execute(query, values)
    conn.commit()

#데이터 수정
def update_data(id, new_name, new_address, new_phone):
    query = "UPDATE restaurantTable SET name=%s, address=%s, phone=%s WHERE id=%s"
    values = (new_name, new_address, new_phone, id)
    cur.execute(query, values)
    conn.commit()
    
#데이터 삭제
def delete_data(id):
    query = "DELETE FROM restaurantTable WHERE id=%s"
    value = (id,)
    cur.execute(query, value)
    conn.commit()

#데이터 조회
def get_restaurant_by_id(id):
    query = "SELECT * FROM restaurantTable WHERE id=%s"
    value = (id,)
    cur.execute(query, value)
    result = cur.fetchone()
    return result

def get_all_restaurants():
    query = "SELECT * FROM restaurantTable"
    cur.execute(query)
    result = cur.fetchall()
    return result

#cur.execute("Insert into restaurantTable values(1, 'ㅇㅇ식당', '서울시 영등포구', 01000000000)")
#conn.commit()

# 기타 필요한 데이터베이스 쿼리 함수들을 작성

# 연결 종료
#cur.close()
conn.close()
