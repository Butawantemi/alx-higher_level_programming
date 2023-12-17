#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    # Connect database using command-line arguments
    my_db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
    )

    # Create cursor obj to interact with database
    my_cursor = my_db.cursor()

    # Execute a SELECT query to fetch data
    my_cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id"""
    )

    # fetch all the database
    my_data = my_cursor.fetchall()

    # Fetched data and print each row
    for row in my_data:
        print(row)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()
