import requests
from bs4 import BeautifulSoup
import time

# 스팀의 특정 게임 리뷰 페이지 URL
game_id = '570'  # 예: 도타 2 (게임 ID는 Steam store URL에서 확인 가능)
url = f"https://store.steampowered.com/appreviews/{game_id}?json=1&filter=recent"

# 요청 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# API 호출 및 JSON 응답 파싱
params = {
    "json": "1",
    "filter": "recent",
    "language": "korean",
    "num_per_page": "100"
}

response = requests.get(url, headers=headers, params=params)
reviews = response.json()

# 리뷰 출력
for review in reviews['reviews']:
    print("리뷰 내용:", review['review'])
    print("추천 여부:", "추천" if review['voted_up'] else "비추천")
    print("리뷰 날짜:", review['timestamp_created'])
    print("="*50)

# 딜레이 추가 (스팀 서버에 과부하를 방지)
time.sleep(1)
