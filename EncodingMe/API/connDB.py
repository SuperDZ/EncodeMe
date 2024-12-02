import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="1234",
            host="192.168.31.10",
            port="5432",
            database="postgres"
        )
        return connection
    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None

def insert_data(connection, table, data):
    try:
        cursor = connection.cursor()
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        insert_query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        cursor.execute(insert_query, list(data.values()))
        connection.commit()
        cursor.close()
    except Exception as error:
        print(f"Error inserting data: {error}")

def delete_data(connection, table, condition):
    try:
        cursor = connection.cursor()
        delete_query = f"DELETE FROM {table} WHERE {condition}"
        cursor.execute(delete_query)
        connection.commit()
        cursor.close()
    except Exception as error:
        print(f"Error deleting data: {error}")

def update_data(connection, table, updates, condition):
    try:
        cursor = connection.cursor()
        set_clause = ', '.join([f"{column} = %s" for column in updates.keys()])
        update_query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        cursor.execute(update_query, list(updates.values()))
        connection.commit()
        cursor.close()
    except Exception as error:
        print(f"Error updating data: {error}")

# Example usage:
if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        # Insert data example
        insert_data(conn, 'your_table', {'column1': 'value1', 'column2': 'value2'})
        
        # Delete data example
        delete_data(conn, 'your_table', "column1 = 'value1'")
        
        # Update data example
        update_data(conn, 'your_table', {'column1': 'new_value'}, "column2 = 'value2'")
        
        conn.close()


