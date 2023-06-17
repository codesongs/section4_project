import psycopg2
import psycopg2.extras
import csv

host = 'drona.db.elephantsql.com'
user = 'rsegildw'
password = 'HIMBRYn1_CQEjaiwBQFvNZ0m3CaLhpzT'
database = 'rsegildw'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

# 중복테이블 제거
cursor.execute("DROP TABLE IF EXISTS baseball_data;")

# 테이블 생성
create_table_query = """
CREATE TABLE baseball_data (
    war FLOAT,
    k_per_9 FLOAT,
    bb_per_9 FLOAT,
    ops FLOAT,
    whip FLOAT,
    fastball_velocity FLOAT,
    slider_velocity FLOAT,
    curve_velocity FLOAT,
    changeup_velocity FLOAT,
    splitter_velocity FLOAT,
    sinker_velocity FLOAT,
    knuckle_velocity FLOAT,
    other_velocity FLOAT,
    fastball_percentage FLOAT,
    slider_percentage FLOAT,
    curve_percentage FLOAT,
    changeup_percentage FLOAT,
    splitter_percentage FLOAT,
    sinker_percentage FLOAT,
    knuckle_percentage FLOAT,
    other_percentage FLOAT,
    zone_percentage FLOAT
);
"""

cursor.execute(create_table_query)
connection.commit()

# CSV 파일에서 데이터 읽기 및 삽입
with open('baseball.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        insert_query = """
        INSERT INTO baseball_data (
            war, k_per_9, bb_per_9, ops, whip, fastball_velocity, slider_velocity, curve_velocity, 
            changeup_velocity, splitter_velocity, sinker_velocity, knuckle_velocity, other_velocity, 
            fastball_percentage, slider_percentage, curve_percentage, changeup_percentage, 
            splitter_percentage, sinker_percentage, knuckle_percentage, other_percentage, zone_percentage
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (
            row['WAR'], row['K/9'], row['BB/9'], row['OPS'], row['WHIP_y'], row['직구구속'], row['슬라구속'], 
            row['커브구속'], row['첸졉구속'], row['스플구속'], row['싱커구속'], row['너클구속'], row['기타구속'], 
            row['직구구사율'], row['슬라구사율'], row['커브구사율'], row['첸졉구사율'], row['스플구사율'], 
            row['싱커구사율'], row['너클구사율'], row['기타구사율'], row['Zone%']
        ))

connection.commit()