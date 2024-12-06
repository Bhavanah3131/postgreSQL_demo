
import psycopg2
from datetime import datetime
database="human", 
user="postgres", 
password="Bhavana@31", 
host="localhost", 
port=5432
try:
    connection = psycopg2.connect(
        database="human", 
        user="postgres", 
        password="Bhavana@31", 
        host="localhost", 
        port=5432)

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS car_sold(sale_id SERIAL PRIMARY KEY, 
                   sale_date date NOT NULL, total_sold int NOT NULL,
                   car_id int REFERENCES car(id),
                   UNIQUE (sale_date, total_sold, car_id));""")
    connection.commit()
    
    
    car_sold_data = [
    (datetime(2024, 1, 1).date(), 10, 1),
    (datetime(2024, 4, 27).date(), 5, 2),
    (datetime(2024, 7, 31).date(), 4, 3),
    (datetime(2024, 9, 21).date(), 8, 4),
    (datetime(2024, 4, 4).date(), 0, 5)
    ]
    
    for sale_date, total_sold, car_id in car_sold_data:
        cursor.execute("""INSERT INTO car_sold(sale_date, total_sold, car_id) VALUES 
                   (%s, %s, %s)
                   ON CONFLICT (sale_date, total_sold, car_id) DO NOTHING;""",
                   (sale_date, total_sold, car_id))
    connection.commit()
    
    cursor.execute("""SELECT car.make, car.model, car.price, car_sold.sale_date, car_sold.total_sold,
                   car_sold.car_id fROM car JOIN car_sold ON car_sold.car_id=car.id""")
    res=cursor.fetchall()
    
    cursor.execute("SELECT MAX(total_sold) FROM car_sold;")
    car_sold=cursor.fetchone()
    cursor.execute("SELECT * FROM car_sold;")
    car_sold=cursor.fetchall()
  
  
    cursor.execute("SELECT * from car;")
    car=cursor.fetchall()
    cursor.execute("SELECT * FROM person;")
    person=cursor.fetchall()
# Fetch all rows from database
    cursor.execute("""
                   
                   SELECT person.first_name, person.last_name, car.make, car.model,
                   car.price FROM person JOIN
                   car ON person.car_id=car.id""")
    result=cursor.fetchall()
        
    print("car data:- ")
    for row in car:
        print(row)
        
    print("person data: ")
    for row in person:
        print(row)
        
    print("Person and car data:")
    for row in result:
        print(row)
        
        
    print("car_sold data: ")
    for row in car_sold:
        print(row)
        
    print("car nd car_sold data: ")
    for row in res:
        print(row)
    
    connection.commit()
except Exception as error:
    print(error)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()