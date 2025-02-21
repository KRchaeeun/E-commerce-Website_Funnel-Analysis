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

# 날짜 변환
merged_df["date"] = pd.to_datetime(merged_df["date"])
merged_df["month"] = merged_df["date"].dt.to_period("M")

# 성별, 기기별 사용자 수 계산
def get_user_counts(df, column, value):
    return [
        df[df[column] == value]["home_visited"].sum(),
        df[df[column] == value]["search_visited"].sum(),
        df[df[column] == value]["payment_visited"].sum(),
        df[df[column] == value]["payment_confirmed"].sum()
    ]
    
# 성별 사용자 수 계산
male_users = get_user_counts(merged_df, "sex", "Male")
female_users = get_user_counts(merged_df, "sex", "Female")

# 기기별 사용자 수 계산
desktop_users = get_user_counts(merged_df, "device", "Desktop")
mobile_users = get_user_counts(merged_df, "device", "Mobile")

# 월별 사용자 수 계산
monthly_users = merged_df.groupby("month")[["home_visited", "search_visited", "payment_visited", "payment_confirmed"]].sum().reset_index()

# Funnel Summary 데이터프레임 생성
funnel_data = pd.DataFrame({
    "STEP": ["홈페이지 방문", "검색 페이지 방문", "결제 페이지 방문", "결제 완료"],
    "USERS": [home_users, search_users, payment_users, confirmed_users],
    "MALE_USERS": [male_users[0], male_users[1], male_users[2], male_users[3]],
    "FEMALE_USERS": [female_users[0], female_users[1], female_users[2], female_users[3]],
    "DESKTOP_USERS": [desktop_users[0], desktop_users[1], desktop_users[2], desktop_users[3]],
    "MOBILE_USERS": [mobile_users[0], mobile_users[1], mobile_users[2], mobile_users[3]]
})

# Funnel Monthly 데이터프레임 생성
funnel_monthly = pd.DataFrame({
    "STEP": ["홈페이지 방문", "검색 페이지 방문", "결제 페이지 방문", "결제 완료"]
})

# 월별 데이터 변환
for month in monthly_users["month"].astype(str).unique():
    values = [
        monthly_users.loc[monthly_users["month"].astype(str) == month, "home_visited"].values[0],
        monthly_users.loc[monthly_users["month"].astype(str) == month, "search_visited"].values[0],
        monthly_users.loc[monthly_users["month"].astype(str) == month, "payment_visited"].values[0],
        monthly_users.loc[monthly_users["month"].astype(str) == month, "payment_confirmed"].values[0]
    ]
    funnel_monthly[month] = values

# 결과 출력
print("\n📌 단계별 Funnel 분석 결과")
print(funnel_data)

# CSV 저장 (Excel 한글 깨짐 방지를 위한 encoding)
funnel_data.to_csv("funnel_analysis.csv", index=False, encoding="utf-8-sig")

# 월별 사용자 수 저장
funnel_monthly.to_csv("funnel_monthly_analysis.csv", index=False, encoding="utf-8-sig")

print("\n✅ Funnel 분석 데이터 저장 완료: funnel_analysis.csv")
print("✅ 월별 분석 데이터 저장 완료: funnel_monthly_analysis.csv")