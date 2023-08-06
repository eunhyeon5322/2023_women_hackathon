#식당 테이블 (restaurants):
#restaurant_id: 식당의 고유 식별자 (Primary Key)
#name: 식당 이름
#location: 식당 위치 (나라, 도시 등을 문자열로 저장)
#address: 식당 주소 (상세 주소까지 문자열로 저장)
#additional_info: 추가 사항 및 설명 (메뉴, 운영 시간, 연락처 등을 문자열로 저장)
#card: 추천카드 장수
CREATE TABLE restaurants (
    restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    additional_info TEXT,
    card INT NOT NULL
);

#리뷰 테이블 (reviews):
#review_id: 후기의 고유 식별자 (Primary Key)
#restaurant_id: 해당 후기가 속한 식당의 고유 식별자 (Foreign Key)
#keywords: 후기에 해당하는 키워드들을 저장하는 컬럼 (여러 개의 키워드를 저장하기 위해 문자열로 저장, 쉼표 등으로 구분)
#content: 후기 내용 (후기의 긴 내용을 저장하기 위해 TEXT 타입으로 저장)
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    keywords VARCHAR(255),
    content TEXT NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);
