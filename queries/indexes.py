from connection.connection import connection


def create_indexes():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
            CREATE INDEX ind_items_for_heroes_items_in_match on items_in_match USING hash(id_hero); 
            CREATE INDEX ind_id_team1_tournament_match on tournament_match USING hash(id_team1);
            CREATE INDEX ind_id_team2_tournament_match on tournament_match USING hash(id_team2);
            CREATE INDEX ind_matches_history on matches_history USING hash(id_player); 
            """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()