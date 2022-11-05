import mysql.connector
from config import USER, PASSWORD, HOST


# This is the database connector
class DbConnectionError(Exception):
    pass


# Connect to the database
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# Add one to the score stored in the database
def update_score(player):
    try:
        db_name = 'toptrumps'
        # Database engine
        db_connection = _connect_to_db(db_name)
        # Cursor
        cur = db_connection.cursor()


        query = 'UPDATE toptrumps.TotalScores SET score=score+1 WHERE player = "{}"'.format(player)
        cur.execute(query)
        db_connection.commit()
        cur.close()
    except Exception:
        raise DbConnectionError

    finally:
        if db_connection:
            db_connection.close()



# View a players score
def view_score(player):
    try:
        db_name = 'toptrumps'
        # Database engine
        db_connection = _connect_to_db(db_name)
        # Cursor
        cur = db_connection.cursor()


        query = 'SELECT score FROM TotalScores WHERE player = "{}"'.format(player)
        cur.execute(query)
        result = cur.fetchall()
        return int(result[0][0])
    except Exception:
        raise DbConnectionError

    finally:
        if db_connection:
            db_connection.close()


# Function to reset the database after a game
def clear_scores():
    try:
        db_name = 'toptrumps'
        # Database engine
        db_connection = _connect_to_db(db_name)
        # Cursor
        cur = db_connection.cursor()

        query = 'UPDATE TotalScores SET score=0;'
        cur.execute(query)
        db_connection.commit()
    except Exception:
        raise DbConnectionError

    finally:
        if db_connection:
            db_connection.close()

