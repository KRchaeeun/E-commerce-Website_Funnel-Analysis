import pandas as pd
import os

# 데이터 폴더 경로 설정
data_path = "data/"

# CSV 파일 불러오기
home = pd.read_csv(os.path.join(data_path, "home_page_table.csv"))
search = pd.read_csv(os.path.join(data_path, "search_page_table.csv"))
payment = pd.read_csv(os.path.join(data_path, "payment_page_table.csv"))
confirmation = pd.read_csv(os.path.join(data_path, "payment_confirmation_table.csv"))
users = pd.read_csv(os.path.join(data_path, "user_table.csv"))

# 단계별 방문 여부 컬럼 추가
home["home_visited"] = 1
search["search_visited"] = 1
payment["payment_visited"] = 1
confirmation["payment_confirmed"] = 1

# 병합 (user_id 기준으로 LEFT 조인)
merged_df = users.merge(home[["user_id", "home_visited"]], on="user_id", how="left")
merged_df = merged_df.merge(search[["user_id", "search_visited"]], on="user_id", how="left")
merged_df = merged_df.merge(payment[["user_id", "payment_visited"]], on="user_id", how="left")
merged_df = merged_df.merge(confirmation[["user_id", "payment_confirmed"]], on="user_id", how="left")

# 결측치(방문하지 않은 경우 NaN으로 입력됨) 
# → 0으로 채우기
merged_df.fillna(0, inplace=True)

# 데이터 타입 정리 (int 변환) 
# → 병합 과정에서 생긴 NaN 값이 0으로 변환되었지만 기본적으로 float 타입임
merged_df[["home_visited", "search_visited", "payment_visited", "payment_confirmed"]] = merged_df[["home_visited", "search_visited", "payment_visited", "payment_confirmed"]].astype(int)

# 결과 확인
print("📎 병합된 데이터 개요")
print(merged_df.info(), "\n")
print(merged_df.head(), "\n")

# 병합된 데이터 저장
merged_df.to_csv(os.path.join(data_path, "merged_data.csv"), index=False)
print("✅ 병합된 데이터 저장 완료: merged_data.csv")

# 병합된 데이터 define
merged_df = pd.read_csv(os.path.join(data_path, "merged_data.csv"))

# 비정상적인 funnel 흐름 데이터 확인
invalid_cases = {
    "검색 페이지 방문 but 홈페이지 미방문": merged_df[(merged_df["search_visited"] == 1) & (merged_df["home_visited"] == 0)],
    "결제 페이지 방문 but 검색 페이지 미방문": merged_df[(merged_df["payment_visited"] == 1) & (merged_df["search_visited"] == 0)],
    "결제 완료 but 결제 페이지 미방문": merged_df[(merged_df["payment_confirmed"] == 1) & (merged_df["payment_visited"] == 0)]
}

# 결과 출력
for case, df in invalid_cases.items():
    print(f"\n❗ {case}: {len(df)}건 발견")
    if not df.empty:
        print(df[["user_id", "home_visited", "search_visited", "payment_visited", "payment_confirmed"]].head())