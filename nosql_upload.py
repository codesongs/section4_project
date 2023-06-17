
import csv
import os
import json
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

# CSV 파일의 경로
csv_file_path = os.path.join(os.getcwd(), 'baseball.csv')

# CSV 파일 열기
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    documents = []
    for row in reader:
        # 데이터를 dictionary 형태로 변환
        document = {
            'WAR': float(row['WAR']),
            'K/9': float(row['K/9']),
            'BB/9': float(row['BB/9']),
            'OPS': float(row['OPS']),
            'WHIP': float(row['WHIP_y']),
            '직구구속': float(row['직구구속']),
            '슬라구속': float(row['슬라구속']),
            '커브구속': float(row['커브구속']),
            '첸졉구속': float(row['첸졉구속']),
            '스플구속': float(row['스플구속']),
            '싱커구속': float(row['싱커구속']),
            '너클구속': float(row['너클구속']),
            '기타구속': float(row['기타구속']),
            '직구구사율': float(row['직구구사율']),
            '슬라구사율': float(row['슬라구사율']),
            '커브구사율': float(row['커브구사율']),
            '첸졉구사율': float(row['첸졉구사율']),
            '스플구사율': float(row['스플구사율']),
            '싱커구사율': float(row['싱커구사율']),
            '너클구사율': float(row['너클구사율']),
            '기타구사율': float(row['기타구사율']),
            'Zone': float(row['Zone%'])
            
        }
        documents.append(document)
        
# 중복 테이블 삭제
if COLLECTION_NAME in database.list_collection_names():
    database.drop_collection(COLLECTION_NAME)
    
collection.insert_many(documents)