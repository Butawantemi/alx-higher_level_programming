#!/usr/bin/python3

"""
script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Connect the db using command-line arguments
    my_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    # Create the cusror && execute the query
    my_cursor = my_db.cursor()
    my_cursor.execute(
        """SELECT * FROM states WHERE name LIKE
        BINARY 'N%'ORDER BY states.id ASC
        """
        )

    # Fetch the data queried
    my_data = my_cursor.fetchall()

    # Iterate to print a tuple
    for data in my_data:
        print(data)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()
