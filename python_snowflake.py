import snowflake.connector

# Establish the connection
conn = snowflake.connector.connect(
    user='Vajay8679',
    password='Vajay8679@',
    account='jhpmgzi-xt72971',  # e.g., abc12345.us-east-1
    warehouse='COMPUTE_WH',
    database='TEST_DB',
    schema='TEST_SCHEMA'
)

# Create a cursor object
cursor = conn.cursor()

try:
    # Execute a query
    # cursor.execute("SELECT CURRENT_VERSION();")
    cursor.execute("SELECT * from employee1;")

    
    # Fetch results
    # result = cursor.fetchone()
    # print("Snowflake version:", result[0])

    results = cursor.fetchall()

    print("Employee Table Data:")
    for row in results:
        print(row)
    
finally:
    # Clean up
    cursor.close()
    conn.close()
