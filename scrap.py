import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import time

def init_selenium():
    """
    해당 함수는 원활한 Selenium 사용을 위해 설정을 진행하는 함수입니다.
    첨부된 주석을 통해 해당 코드의 기능을 확인할 수 있습니다.
    """
    driver_options = Options()
    
    #---
    # driver_options.add_argument("--disable-extensions")
    # driver_options.add_argument('--headless')
    # driver_options.add_argument('--no-sandbox')
    # driver_options.add_argument('--disable-dev-shm-usage')
    #---
    
    # 하기 코드는 False로 설정시 자동으로 웹 브라우저가 종료될 수 있게 설정합니다.
    driver_options.add_experimental_option("detach", True) 
    # 하기 코드는 불필요한 경고 메시지가 출력되지 않게 설정합니다.
    driver_options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
    # 하기 코드는 WebDriver를 자동으로 관리하는 모듈을 호출하여 설치합니다.
    auto_driver = Service(ChromeDriverManager().install())

    # 설정과 WebDriver를 이용해 크롤러를 driver 변수에 선언합니다.
    driver = webdriver.Chrome(service = auto_driver, options = driver_options)
    return driver

driver = init_selenium()

# 사용할 URL
URL = 'http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=1&ys=2014&ye=2022&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR&o2=OutCount&de=1&lr=0&tr=&cv=&ml=1&sn=3000&si=&cn=' 
driver.get(URL) 

#element = driver.find_element(By.ID, 'mytable')
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mytable')))
rows = element.find_elements(By.TAG_NAME, 'tr')

# 기본탭(투수)

column_names = ['순', '이름', '팀', 'WAR', '출장', '완투', '완봉', '선발', '승', '패', '세이브', '홀드', '이닝', '실점', '자책',
                 '타자', '안타', '2루타', '3루타', '홈런', '볼넷', '고의사구', '사구', '삼진', '보크', '폭투', 'ERA', 'FIP', 'WHIP', 'ERA+', 'FIP+', 'WAR_dup', 'WPA']
data = []
for i in range(2, len(rows), 12):
    subset = rows[i:i+10]
    data.extend(subset)
    if i+12 < len(rows):
        data.append(rows[i+12])
# for row in data:
#     print(row.text)

data_rows = [row.text.split() for row in data]
df1 = pd.DataFrame(data_rows, columns=column_names)
print(df1.head())

time.sleep(10)


# 사용할 URL
URL2 = 'http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=1&ys=2014&ye=2022&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=2&o1=FIP&de=0&o2=WAR&lr=0&tr=&cv=&ml=1&sn=3000&si=&cn=' 
driver.get(URL2) 

# 확장탭(투수)

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mytable')))
rows = element.find_elements(By.TAG_NAME, 'tr')

column_names2 = ['순', '이름', '팀', 'FIP', '출장', '이닝', 'ERA', 'FIP', 'K/9', 'BB/9', 'K/BB', 'HR/9', 'K%', 'BB%', 'K-BB%', 
                'PFR', 'BABIP', 'LOB%', '타율', '출루율', '장타율', 'OPS', 'WHIP', 'WHIP+', '투구', 'IP/G', 'P/G', 'P/IP', 'P/PA', 'CYP']
data2 = []
for i in range(2, len(rows), 12):
    subset = rows[i:i+10]
    data2.extend(subset)
    if i+12 < len(rows):
        data2.append(rows[i+12])
   
data_rows2 = [row.text.split() for row in data2]
df2 = pd.DataFrame(data_rows2, columns=column_names2)
print(df2.head())

time.sleep(10)

# 사용할 URL
URL3 = 'http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=1&ys=2014&ye=2022&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=14&o1=FVval&o2=WAR&de=1&lr=0&tr=&cv=&ml=1&sn=3000&si=&cn=' 
driver.get(URL3)

# 구종(투수)
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mytable')))
rows = element.find_elements(By.TAG_NAME, 'tr')

column_names3 = ['순', '이름', '팀', '직구구속_dup', '출장', '이닝', '직구구속', '슬라구속', '커브구속', '첸졉구속', '스플구속', '싱커구속', '너클구속', '기타구속', 
                '직구구사율', '슬라구사율', '커브구사율', '첸졉구사율', '스플구사율', '싱커구사율', '너클구사율', '기타구사율', 
                '스윙IZ', '스윙OZ', '스윙All', '컨택IZ', '컨택OZ', '컨택All', 'Zone%']
data3 = []
for i in range(2, len(rows), 12):
    subset = rows[i:i+10]
    data3.extend(subset)
    if i+12 < len(rows):
        data3.append(rows[i+12])
        
# for row in data3:
#     row_data = [cell.text if cell.text.strip() != '' else -1 for cell in row.find_elements(By.TAG_NAME, 'td')]
#     print(row_data)

data_rows3 = []
for row in data3:
    row_data = [cell.text if cell.text.strip() != '' else '-1' for cell in row.find_elements(By.TAG_NAME, 'td')]
    data_rows3.append(row_data)

df3 = pd.DataFrame(data_rows3, columns=column_names3)
df3 = df3.replace('-1', -1)  # -1을 실제 -1 값으로 대체
print(df3.head())


# 데이터프레임 복사
df1_modified = df1.copy()
df2_modified = df2.copy()
df3_modified = df3.copy()

# '순' 컬럼 제거
df1_modified.drop('순', axis=1, inplace=True)
df2_modified.drop('순', axis=1, inplace=True)
df3_modified.drop('순', axis=1, inplace=True)

def drop_duplicates(df):
    """
    이름과 팀 컬럼을 제외한 중복 컬럼들을 삭제하는 함수
    """
    duplicates = df.columns[df.columns.duplicated()].tolist()
    duplicates = [dup for dup in duplicates if dup not in ['이름', '팀']]

    return df.drop(columns=duplicates)

# 각 데이터프레임에서 중복된 컬럼 제거
df1_modified = drop_duplicates(df1_modified)
df2_modified = drop_duplicates(df2_modified)
df3_modified = drop_duplicates(df3_modified)

# '이름'과 '팀'을 기준으로 데이터프레임 합치기
merged_df = pd.merge(df1_modified, df2_modified, on=['이름', '팀'])
merged_df = pd.merge(merged_df, df3_modified, on=['이름', '팀'])

# 병합된 데이터프레임에서 중복된 컬럼 제거
merged_df = drop_duplicates(merged_df)


save_folder = os.getcwd()  # 현재 실행된 폴더 경로를 가져옵니다.

# merged_df를 CSV 파일로 저장할 파일 경로
save_path = os.path.join(save_folder, 'baseball.csv')

# merged_df를 CSV 파일로 저장
merged_df.to_csv(save_path, index=False)

print(f"baseball 이 {save_path}에 저장되었습니다.")
