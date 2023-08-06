#from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL 연결 설정
db = mysql.connector.connect(
    host='your_database_host',
    user='your_database_user',
    password='your_database_password',
    database='your_database_name'
)
cursor = db.cursor()

# 지역별 식당 목록 조회 API
@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    query = "SELECT DISTINCT location FROM restaurants;"
    cursor.execute(query)
    locations = [row[0] for row in cursor.fetchall()]
    return jsonify(locations)

# 선택한 지역의 식당 목록 조회 API
@app.route('/api/restaurants/<string:location>', methods=['GET'])
def get_restaurants_by_location(location):
    query = f"SELECT * FROM restaurants WHERE location='{location}';"
    cursor.execute(query)
    restaurants = cursor.fetchall()
    return jsonify(restaurants)

# 선택한 식당의 상세 정보와 후기 조회 API
@app.route('/api/restaurant/<int:restaurant_id>', methods=['GET'])
def get_restaurant_detail(restaurant_id):
    query = f"SELECT * FROM restaurants WHERE restaurant_id={restaurant_id};"
    cursor.execute(query)
    restaurant = cursor.fetchone()

    query = f"SELECT * FROM reviews WHERE restaurant_id={restaurant_id};"
    cursor.execute(query)
    reviews = cursor.fetchall()

    return jsonify({
        'restaurant': restaurant,
        'reviews': reviews
    })

if __name__ == '__main__':
    app.run(debug=True)
