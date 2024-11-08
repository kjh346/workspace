import requests
import csv
import pandas as pd
import time

# 스팀의 특정 게임 리뷰 페이지 URL
game_id = '1245620'  # 예: 도타 2 (게임 ID는 Steam store URL에서 확인 가능)
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

# CSV 파일로 저장
with open('reviews.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["리뷰 내용", "추천 여부", "리뷰 날짜", "플레이 시간(분)"])  # 헤더 작성
    
    # 각 리뷰를 CSV에 쓰기
    for review in reviews['reviews']:
        review_text = review['review']
        recommendation = "추천" if review['voted_up'] else "비추천"
        review_date = review['timestamp_created']
        playtime = review['author']['playtime_forever']  # 플레이 시간 가져오기 (분 단위)
        
        writer.writerow([review_text, recommendation, review_date, playtime])

        print("리뷰 내용:", review_text)
        print("추천 여부:", recommendation)
        print("리뷰 날짜:", review_date)
        print("플레이 시간(분):", playtime)
        print("="*50)

    # 딜레이 추가 (스팀 서버에 과부하를 방지)
    time.sleep(1)

print("리뷰가 'reviews.csv' 파일에 저장되었습니다.")

# CSV 파일 읽기
data = pd.read_csv('reviews.csv', low_memory=False)
data.head(2)
