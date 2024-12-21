import pandas as pd
import mysql.connector


##############
# MAKE SURE TO INSTALL DOLT from brew AND
# pip install mysql-connector-python dolt
##############

##############
# CLONE THE DATASET LOCALLY
##############

##############
# MAKE SURE TO HAVE A SQL-server running in another terminal
# dolt sql-server
##############


connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    port=3306,
    database='transparency-in-pricing' # Database name
)

# Read query directly into a pandas DataFrame
query = "SELECT * FROM hospital LIMIT 10"
df = pd.read_sql(query, connection)

# Now you can work with the data in the DataFrame
print(df)

connection.close()
