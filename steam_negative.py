import requests
import csv
import pandas as pd
import time

# 스팀의 특정 게임 리뷰 페이지 URL
game_id = '1245620'  # 예: 특정 게임 ID
url = f"https://store.steampowered.com/appreviews/{game_id}"

# 요청 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# CSV 파일로 저장
with open('negative_reviews.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["리뷰 내용", "추천 여부", "리뷰 날짜", "플레이 시간(분)"])  # 헤더 작성
    
    cursor = '*'
    review_count = 0  # 리뷰 수를 추적

    while review_count < 500:  # 원하는 리뷰 수까지 반복
        # API 호출 및 JSON 응답 파싱
        params = {
            "json": "1",
            "filter": "recent",
            "language": "korean",
            "num_per_page": "100",
            "cursor": cursor
        }

        response = requests.get(url, headers=headers, params=params)
        reviews = response.json()

        # 리뷰 데이터가 없는 경우 루프 종료
        if 'reviews' not in reviews or len(reviews['reviews']) == 0:
            break

        # 각 부정적 리뷰를 CSV에 쓰기
        for review in reviews['reviews']:
            if not review['voted_up']:  # 부정적 리뷰만 선택
                review_text = review['review']
                recommendation = "비추천"
                review_date = review['timestamp_created']
                playtime = review['author']['playtime_forever']  # 플레이 시간 가져오기 (분 단위)

                writer.writerow([review_text, recommendation, review_date, playtime])
                review_count += 1  # 리뷰 수 증가

                # 수집한 리뷰 표시
                print("리뷰 내용:", review_text)
                print("추천 여부:", recommendation)
                print("리뷰 날짜:", review_date)
                print("플레이 시간(분):", playtime)
                print("="*50)

            if review_count >= 500:  # 지정한 리뷰 수에 도달하면 종료
                break

        # 다음 페이지로 이동하기 위해 cursor 값 업데이트
        cursor = reviews.get('cursor', '*')
        time.sleep(1)  # API 호출 제한을 피하기 위해 딜레이 추가

print("부정적 리뷰가 'negative_reviews.csv' 파일에 저장되었습니다.")

# CSV 파일 읽기
data = pd.read_csv('negative_reviews.csv', low_memory=False)
data.head(2)
