import mysql.connector

# MySQL 연결 설정
db = mysql.connector.connect(
    host='your_database_host',
    user='your_database_user',
    password='your_database_password',
    database='your_database_name'
)
cursor = db.cursor()

# 식당 테이블에 데이터 삽입
insert_query = "INSERT INTO restaurants (name, location, address, additional_info, card) VALUES (%s, %s, %s, %s, %s)"
restaurant_data = ('Restaurant A', 'Seoul, South Korea', '123 Main St', 'Menu: Korean BBQ, Open Hours: 10am - 10pm', 5)
cursor.execute(insert_query, restaurant_data)

# 리뷰 테이블에 데이터 삽입
insert_query = "INSERT INTO reviews (restaurant_id, keywords, content) VALUES (%s, %s, %s)"
review_data = (1, 'Delicious, Friendly Staff', 'I had a great experience at Restaurant A. The food was delicious and the staff was very friendly.')
cursor.execute(insert_query, review_data)

# 변경 사항을 커밋
db.commit()

# 식당 테이블의 데이터 수정
update_query = "UPDATE restaurants SET card = %s WHERE restaurant_id = %s"
new_card_value = 6
restaurant_id = 1
cursor.execute(update_query, (new_card_value, restaurant_id))
db.commit()

# 리뷰 테이블의 데이터 삭제
delete_query = "DELETE FROM reviews WHERE review_id = %s"
review_id = 1
cursor.execute(delete_query, (review_id,))
db.commit()
