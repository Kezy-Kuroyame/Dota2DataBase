from connection.connection import connection


def create_indexes():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
            INSERT INTO tournament (name, price_win, win_team) 
                VALUES 
                   ('The International 2023', 3148799, 1),
                   ('DreamLeague Season 21', 1000000, 1),
                   ('Riyadh Masters 2023', 15000000, 1),
                   ('The Bali Major 2023', 500000, 2),
                   ('DreamLeague Season 21', 1000000, 2),
                   ('ESL One Berlin Major 2023', 500000, 2);               
       """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()