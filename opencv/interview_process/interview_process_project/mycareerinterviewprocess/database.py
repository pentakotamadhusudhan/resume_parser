# import psycopg2

# #establishing the connection
# conn = psycopg2.connect(
#    database="postgres", user='postgres', password='Madhu@12', host='localhost', port= '5432'
# )
# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Executing an MYSQL function using the execute() method
# cursor.execute("select version()")

# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print("Connection established to: ",data)

# #Closing the connection
# conn.close()



database_config = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'madhu',
        'USER': 'postgres',
        'PASSWORD': 'Madhu@12',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



database_config = {
    'default': {
        'ENGINE': 'djongo',
        'NAME':  'interview process',
        
    }
}