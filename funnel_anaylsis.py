import pandas as pd
import os

# 데이터 폴더 경로 설정
data_path = "data/"

# 데이터 폴더 내 모든 CSV 파일 가져오기
file_names = [f for f in os.listdir(data_path) if f.endswith(".csv")]

# 데이터 불러오기 및 기본 정보 출력
dataframes = {}
for file in file_names:
    file_path = os.path.join(data_path, file)
    df = pd.read_csv(file_path)
    
    # 데이터 저장 (딕셔너리 형태로 저장)
    dataframes[file] = df
    
    # 기본 정보 출력
    print(f"📎{file} 데이터셋 개요")
    print(df.info(), "\n")  # 데이터 타입 및 결측치 확인
    print(df.head(), "\n")  # 상위 5개 행 출력
    print("="*50, "\n")  # 가독성을 위해...