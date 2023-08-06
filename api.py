import requests

# 공공데이터포털 API 키
api_key = "J265MSRmiYjx8Kxn4g3rk9YK0oiKEEoxTpQTxv7AYF%2FYB4MNNLWtmS7yspYtjz1l48VThsFFwoOUV44yUS6oVw%3D%3D"

# API 엔드포인트와 파라미터 설정
base_url = "http://api.odcloud.kr/api"  # API 기본 주소
endpoint = "http://infuser.odcloud.kr/oas/docs?namespace=15076742/v1"  # 원하는 API 엔드포인트
query_params = {
    "page": 1,       # 페이지 번호
    "perPage": 10,   # 페이지 당 결과 수
    "returnType": "json",  # 응답 데이터 타입 (json 형식으로 설정)
    "serviceKey": api_key,  # API 키
}

# API 요청 보내기
response = requests.get(base_url + endpoint, params=query_params)

# 응답 확인 및 데이터 추출
if response.status_code == 200:
    data = response.json()
    # 데이터 가공 및 활용
    for restaurant in data['data']:
        # 식당 정보 출력 예시
        print("식당 ID:", restaurant['식당ID'])
        print("식당명:", restaurant['식당명'])
        print("업종(메뉴)정보:", restaurant['업종(메뉴)정보'])
        # 필요한 정보를 원하는 방식으로 가공하여 활용하면 됩니다.
else:
    print("API 요청 실패:", response.status_code)
