import psycopg2
import csv

host = 'drona.db.elephantsql.com'
user = 'rsegildw'
password = 'HIMBRYn1_CQEjaiwBQFvNZ0m3CaLhpzT'
database = 'rsegildw'

# 데이터베이스 연결
connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

# CSV 파일 경로
csv_file_path = 'model/data.csv'

# 테이블 이름
table_name = 'baseball_data'

# SQL 쿼리 실행하여 데이터 가져오기
query = f'SELECT * FROM {table_name}'
cursor.execute(query)
rows = cursor.fetchall()

# 컬럼 이름 가져오기
columns = [desc[0] for desc in cursor.description]

# CSV 파일로 데이터 저장
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(columns)  # 컬럼 이름을 첫 번째 행에 쓰기
    writer.writerows(rows)  # 데이터 행 쓰기

# 연결 닫기
cursor.close()
connection.close()

print('데이터를 CSV 파일로 내보내었습니다.')