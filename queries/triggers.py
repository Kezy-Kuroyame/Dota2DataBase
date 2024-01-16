from connection.connection import connection


def main_triggers():
    tournament_insert_trigger_fnc()
    tournament_insert_trigger()


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
                team_ids INT[];
                tournament_id INT;
            BEGIN
                IF NOT(NEW.isTournament) THEN
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
                                mmr = mmr + 27
                            WHERE id_player = list_id[i];
    
                            INSERT INTO matches_history (id_player, id_match, team, id_hero) 
                            VALUES
                                (list_id[i], NEW.id_match, NEW.win_team, list_hero_id[i]);
                        ELSE
                            UPDATE PLAYERS
                            SET count_defeats = count_defeats + 1,
                            mmr = 
                                CASE 
                                    WHEN mmr >= 27 THEN mmr - 27
                                    WHEN mmr < 27 THEN 0
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
                ELSE
                    team_ids := ARRAY(
                        SELECT id FROM team
                        ORDER BY random()
                        LIMIT 2
                        );
                    SELECT id INTO tournament_id
                        FROM tournament
                        ORDER BY random()
                        LIMIT 1;
                    INSERT INTO tournament_match (id_match, id_team1, id_team2, id_tournament)
                    VALUES
                    (NEW.id_match, team_ids[1], team_ids[2], tournament_id);
                END IF;
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


def tournament_matches_insert_trigger_fnc():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
            CREATE OR REPLACE FUNCTION tournament_matches_insert_trigger_fnc()
                RETURNS trigger AS
            $$
            DECLARE
                i INT;
                j INT;
                team_win BOOLEAN;
                list_players_id INT[];
                list_hero_id INT[];
                players_items_in_match INT[];
                count_items INT;
            BEGIN
                select win_team into team_win
                FROM match
                WHERE (id_match = NEW.id_match);
                
                list_hero_id := ARRAY(
                    SELECT id_hero
                    FROM hero
                    ORDER BY random()
                    LIMIT 10
                );
                
                IF (team_win) THEN
                    UPDATE TEAM
                    SET count_wins = count_wins + 1
                    WHERE (id = NEW.id_team1);
                    
                    UPDATE TEAM
                    SET count_defeats = count_defeats + 1
                    WHERE (id = NEW.id_team2);
                    
                    list_players_id := ARRAY(
                        SELECT id_player FROM players_in_team
                        WHERE id_team = NEW.id_team1
                    );
                    i := 1;
                    WHILE i <= 5
                    LOOP
                        UPDATE PLAYERS
                        SET count_wins = count_wins + 1
                        WHERE id_player = list_players_id[i];
                        
                        INSERT INTO matches_history (id_player, id_match, team, id_hero) 
                        VALUES
                            (list_players_id[i], NEW.id_match, team_win, list_hero_id[i]);
                        
                        players_items_in_match := ARRAY(
                            SELECT id_item FROM item
                            ORDER BY random()
                            LIMIT 6
                        );
                        count_items := floor(random() * 6 + 1)::INTEGER;
                        j := 1;
                        WHILE j <= count_items
                        LOOP
                             INSERT INTO items_in_match (id_match, id_item, id_hero) 
                             VALUES 
                                (NEW.id_match, players_items_in_match[j], list_hero_id[i]);
                            j := j + 1;
                        END LOOP;
                        i := i + 1;
                    END LOOP;
                    
                    list_players_id := ARRAY(
                        SELECT id_player FROM players_in_team
                        WHERE id_team = NEW.id_team2
                    );
                    i := 1;
                    WHILE i <= 5
                    LOOP
                        UPDATE PLAYERS
                        SET count_defeats = count_defeats + 1
                        WHERE id_player = list_players_id[i];
                        
                        INSERT INTO matches_history (id_player, id_match, team, id_hero) 
                        VALUES
                            (list_players_id[i], NEW.id_match, NOT(team_win), list_hero_id[i + 5]);
                        
                        players_items_in_match := ARRAY(
                            SELECT id_item FROM item
                            ORDER BY random()
                            LIMIT 6
                        );
                        count_items := floor(random() * 6 + 1)::INTEGER;
                        j := 1;
                        WHILE j <= count_items
                        LOOP
                             INSERT INTO items_in_match (id_match, id_item, id_hero) 
                             VALUES 
                                (NEW.id_match, players_items_in_match[j], list_hero_id[i + 5]);
                            j := j + 1;
                        END LOOP;
                        i := i + 1 ;
                    END LOOP;    
                ELSE
                    UPDATE TEAM
                    SET count_wins = count_wins + 1
                    WHERE (id = NEW.id_team2);
                    
                    UPDATE TEAM
                    SET count_defeats = count_defeats + 1
                    WHERE (id = NEW.id_team1);
                    
                    list_players_id := ARRAY(
                        SELECT id_player FROM players_in_team
                        WHERE id_team = NEW.id_team2
                    );
                    i := 1;
                    WHILE i <= 5
                    LOOP
                        UPDATE PLAYERS
                        SET count_wins = count_wins + 1
                        WHERE id_player = list_players_id[i];
                        
                        INSERT INTO matches_history (id_player, id_match, team, id_hero) 
                        VALUES
                            (list_players_id[i], NEW.id_match, team_win, list_hero_id[i]);
                    
                         players_items_in_match := ARRAY(
                            SELECT id_item FROM item
                            ORDER BY random()
                            LIMIT 6
                        );
                        count_items := floor(random() * 6 + 1)::INTEGER;
                        j := 1;
                        WHILE j <= count_items
                        LOOP
                             INSERT INTO items_in_match (id_match, id_item, id_hero) 
                             VALUES 
                                (NEW.id_match, players_items_in_match[j], list_hero_id[i]);
                            j := j + 1;
                        END LOOP;
                        i := i + 1;
                    END LOOP;
                    
                    list_players_id := ARRAY(
                        SELECT id_player FROM players_in_team
                        WHERE id_team = NEW.id_team1
                    );
                    i := 1;
                    WHILE i <= 5
                    LOOP
                        UPDATE PLAYERS
                        SET count_defeats = count_defeats + 1
                        WHERE id_player = list_players_id[i];
                        
                        INSERT INTO matches_history (id_player, id_match, team, id_hero) 
                        VALUES
                            (list_players_id[i], NEW.id_match, NOT(team_win), list_hero_id[i]);
                        
                        players_items_in_match := ARRAY(
                            SELECT id_item FROM item
                            ORDER BY random()
                            LIMIT 6
                        );
                        count_items := floor(random() * 6 + 1)::INTEGER;
                        j := 1;
                        WHILE j <= count_items
                        LOOP
                             INSERT INTO items_in_match (id_match, id_item, id_hero) 
                             VALUES 
                                (NEW.id_match, players_items_in_match[j], list_hero_id[i + 5]);
                            j := j + 1;
                        END LOOP;
                        i := i + 1;
                    END LOOP;    
                END IF;
                return new;     
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
         CREATE TRIGGER tournament_matches_insert_trigger
         AFTER INSERT ON tournament_match
         FOR EACH ROW
         EXECUTE FUNCTION tournament_matches_insert_trigger_fnc();
         """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def tournament_insert_trigger_fnc():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
            CREATE OR REPLACE FUNCTION tournament_insert_trigger_fnc()
            RETURNS trigger AS
            $$
            DECLARE
            BEGIN
                UPDATE TEAM
                SET total_price = total_price + NEW.price_win
                WHERE (id = NEW.win_team);
                
                RETURN NEW; 
            END;
            $$ LANGUAGE plpgsql;            
            """

    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def tournament_insert_trigger():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
         CREATE TRIGGER tournament_insert_trigger
         AFTER INSERT ON tournament
         FOR EACH ROW
         EXECUTE FUNCTION tournament_insert_trigger_fnc();
         """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()
