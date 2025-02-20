import pandas as pd

# 병합된 데이터 define
merged_df = pd.read_csv("merged_data.csv")

# 각 단계별 사용자 수 계산
home_users = merged_df["home_visited"].sum()
search_users = merged_df["search_visited"].sum()
payment_users = merged_df["payment_visited"].sum()
confirmed_users = merged_df["payment_confirmed"].sum()

# 전환율(Conversion Rate) 계산 
# → 분모가 0명이면 연산할 때 0으로 나누는 오류 즉, ZeroDivisionError이 발생할 수 있으므로 if절 추가
search_conversion = (search_users / home_users) * 100 if home_users > 0 else 0
payment_conversion = (payment_users / search_users) * 100 if search_users > 0 else 0
confirmed_conversion = (confirmed_users / payment_users) * 100 if payment_users > 0 else 0

# 이탈률(Drop-off Rate) 계산
search_dropoff = 100 - search_conversion
payment_dropoff = 100 - payment_conversion
confirmed_dropoff = 100 - confirmed_conversion

# 데이터프레임 생성
funnel_data = pd.DataFrame({
    "단계": ["홈페이지 방문", "검색 페이지 방문", "결제 페이지 방문", "결제 완료"],
    "사용자 수": [home_users, search_users, payment_users, confirmed_users],
    "전환율(%)": [100, search_conversion, payment_conversion, confirmed_conversion],  # 첫 단계는 100%
    "이탈률(%)": [0, search_dropoff, payment_dropoff, confirmed_dropoff]  # 첫 단계는 0%
})

# 결과 출력
print("\n📌 단계별 Funnel 분석 결과")
print(funnel_data)


# CSV 저장 (Excel 한글 깨짐 방지)
funnel_data.to_csv("funnel_analysis.csv", index=False, encoding="utf-8-sig")
print("\n✅ Funnel 분석 데이터 저장 완료: funnel_analysis.csv")