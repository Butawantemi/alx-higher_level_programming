#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    
    import MySQLdb
    from sys import argv
    
    #connect db using command-line argurments
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    #obj to interact with database
    my_cursor = my_db.cursor()

    #query to fetch data
    my_cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    #data returned by the query
    my_data = my_cursor.fetchall()

    #fetched data and print each row
    for row in my_data:
        print(row)

    #close cursor
    my_cursor.close()
    
    #close db
    my_db.close()
