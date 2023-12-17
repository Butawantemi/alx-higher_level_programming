#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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

    # Execute a SELECT query 
    my_cursor.execute(
        """SELECT * FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id"""
    )

    print(", ".join([city[2]
                     for city in my_cursor.fetchall()
                     if city[4] == argv[4]])

          )

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()
