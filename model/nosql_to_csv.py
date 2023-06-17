import csv
from pymongo import MongoClient

HOST = 'cluster0.osfxs85.mongodb.net'
USER = 'whaleuser'
PASSWORD = 'whale1234'
DATABASE_NAME = 'Cluster0'
COLLECTION_NAME = 'baseball'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

# MongoDB에 연결
client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

# MongoDB에서 데이터 쿼리
cursor = collection.find()


# CSV 파일 경로
csv_file_path = 'model/output.csv'

# CSV 파일 열기
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 컬럼 헤더 작성
    headers = ['WAR', 'K/9', 'BB/9', 'OPS', 'WHIP', '직구구속', '슬라구속', '커브구속', '첸졉구속', '스플구속', '싱커구속', '너클구속', '기타구속',
               '직구구사율', '슬라구사율', '커브구사율', '첸졉구사율', '스플구사율', '싱커구사율', '너클구사율', '기타구사율', 'Zone']
    writer.writerow(headers)

    # 데이터 쓰기
    for document in cursor:
        row = [
            float(document.get('WAR', '')),
            float(document.get('K/9', '')),
            float(document.get('BB/9', '')),
            float(document.get('OPS', '')),
            float(document.get('WHIP', '')),
            float(document.get('직구구속', '')),
            float(document.get('슬라구속', '')),
            float(document.get('커브구속', '')),
            float(document.get('첸졉구속', '')),
            float(document.get('스플구속', '')),
            float(document.get('싱커구속', '')),
            float(document.get('너클구속', '')),
            float(document.get('기타구속', '')),
            float(document.get('직구구사율', '')),
            float(document.get('슬라구사율', '')),
            float(document.get('커브구사율', '')),
            float(document.get('첸졉구사율', '')),
            float(document.get('스플구사율', '')),
            float(document.get('싱커구사율', '')),
            float(document.get('너클구사율', '')),
            float(document.get('기타구사율', '')),
            float(document.get('Zone', ''))
        ]
        writer.writerow(row)

print(f"데이터를 CSV 파일로 추출하였습니다: {csv_file_path}")

