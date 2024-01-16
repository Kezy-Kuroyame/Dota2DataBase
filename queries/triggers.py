from connection.connection import connection


def main_triggers():
    matches_insert_trigger_fnc()


def matches_insert_trigger_fnc():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
            CREATE OR REPLACE FUNCTION matches_insert_trigger_fnc()
                RETURNS trigger AS
            $$
            DECLARE
                i INT := 1;
                j INT := 1;
                list_id INT[];
                list_hero_id INT[];
                players_items_in_match INT[];
                count_items INT;
            BEGIN
                list_id := ARRAY(
                    SELECT id_player
                    FROM PLAYERS
                    ORDER BY random()
                    LIMIT 10
                );
                
                 
                list_hero_id := ARRAY(
                    SELECT id_hero
                    FROM hero
                    ORDER BY random()
                    LIMIT 10
                );
                
                FOR i IN 1..array_length(list_id, 1)
                LOOP
                    IF i <= 5 THEN
                        UPDATE PLAYERS
                        SET count_wins = count_wins + 1,
                            mmr = 
                                CASE 
                                    WHEN count_wins > count_defeats THEN mmr - 27
                                 END
                        WHERE id_player = list_id[i];
                        
                        INSERT INTO matches_history (id_player, id_match, team, id_hero) 
                        VALUES
                            (list_id[i], NEW.id_match, NEW.win_team, list_hero_id[i]);
                    ELSE
                        UPDATE PLAYERS
                        SET count_defeats = count_defeats + 1,
                            mmr = 
                            CASE 
                                WHEN count_wins > count_defeats THEN mmr - 27
                             END
                        WHERE id_player = list_id[i];
                        
                        INSERT INTO matches_history (id_player, id_match, team, id_hero) 
                        VALUES
                            (list_id[i], NEW.id_match, NOT(NEW.win_team), list_hero_id[i]);
                    END IF; 
                END LOOP;
                i := 1;
                WHILE i <= 10
                LOOP
                    j := 1;
                    players_items_in_match := ARRAY(
                        SELECT id_item FROM item
                        ORDER BY random()
                        LIMIT 6
                    );
                    
                    count_items := floor(random() * 6 + 1)::INTEGER;
                    WHILE j <= count_items
                    LOOP
                         INSERT INTO items_in_match (id_match, id_item, id_hero) 
                         VALUES 
                            (NEW.id_match, players_items_in_match[j], list_hero_id[i]);
                        j := j + 1;
                    END LOOP;
                    i := i + 1;
                END LOOP;   
                RETURN NEW; 
            END;
            $$ LANGUAGE plpgsql;            
            """

    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def matches_insert_trigger():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
         CREATE TRIGGER matches_insert_trigger
         AFTER INSERT ON match
         FOR EACH ROW
         EXECUTE FUNCTION matches_insert_trigger_fnc();
         """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def tournament_insert_trigger_fnc():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
            CREATE OR REPLACE FUNCTION tournament_matches_insert_trigger_fnc()
                RETURNS trigger AS
            $$
            DECLARE
                i INT := 1;
                j INT := 1;
                list_id INT[];
                list_hero_id INT[];
                players_items_in_match INT[];
                count_items INT;
            BEGIN
                list_id := ARRAY(
                    SELECT id_player
                    FROM PLAYERS
                    ORDER BY random()
                    LIMIT 10
                );


                list_hero_id := ARRAY(
                    SELECT id_hero
                    FROM hero
                    ORDER BY random()
                    LIMIT 10
                );

                FOR i IN 1..array_length(list_id, 1)
                LOOP
                    IF i <= 5 THEN
                        UPDATE PLAYERS
                        SET count_wins = count_wins + 1
                        WHERE id_player = list_id[i];

                        INSERT INTO matches_history (id_player, id_match, team, id_hero) 
                        VALUES
                            (list_id[i], NEW.id_match, NEW.win_team, list_hero_id[i]);
                    ELSE
                        UPDATE PLAYERS
                        SET count_defeats = count_defeats + 1
                        WHERE id_player = list_id[i];

                        INSERT INTO matches_history (id_player, id_match, team, id_hero) 
                        VALUES
                            (list_id[i], NEW.id_match, NOT(NEW.win_team), list_hero_id[i]);
                    END IF; 
                END LOOP;
                i := 1;
                WHILE i <= 10
                LOOP
                    j := 1;
                    players_items_in_match := ARRAY(
                        SELECT id_item FROM item
                        ORDER BY random()
                        LIMIT 6
                    );

                    count_items := floor(random() * 6 + 1)::INTEGER;
                    WHILE j <= count_items
                    LOOP
                         INSERT INTO items_in_match (id_match, id_item, id_hero) 
                         VALUES 
                            (NEW.id_match, players_items_in_match[j], list_hero_id[i]);
                        j := j + 1;
                    END LOOP;
                    i := i + 1;
                END LOOP;   
                RETURN NEW; 
            END;
            $$ LANGUAGE plpgsql;            
            """

    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def tournament_matches_insert_trigger():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
         CREATE TRIGGER matches_insert_trigger
         AFTER INSERT ON match
         FOR EACH ROW
         EXECUTE FUNCTION matches_insert_trigger_fnc();
         """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()
