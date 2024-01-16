from connection.connection import connection

query_players = """
    CREATE TABLE IF NOT EXISTS Players (
      id_player SERIAL PRIMARY KEY,
      name VARCHAR(30),
      count_wins INTEGER CHECK (count_wins >= 0),
      count_defeats INTEGER CHECK (count_defeats >= 0),
      mmr INTEGER CHECK (mmr >= 0)
    );
    """

query_history = """
    CREATE TABLE IF NOT EXISTS Matches_history (
      match_history_id SERIAL PRIMARY KEY,
      id_player INTEGER,
      id_match INTEGER,
      team BOOLEAN,
      id_hero INTEGER,
      FOREIGN KEY(id_player) REFERENCES Players(id_player),
      FOREIGN KEY(id_match) REFERENCES Match(id_match),
      FOREIGN KEY(id_hero) REFERENCES Hero(id_hero)
    );
    """
query_hero = """
    CREATE TABLE IF NOT EXISTS Hero (
      id_hero SERIAL PRIMARY KEY,
      name_hero VARCHAR(30),
      strength INTEGER CHECK (strength > 0),
      agility INTEGER CHECK (agility > 0),
      intelligence INTEGER CHECK (intelligence > 0)
    );
    """
query_match = """
    CREATE TABLE IF NOT EXISTS Match (
      id_match SERIAL PRIMARY KEY,
      time_end TIME,
      duration TIME,
      win_team BOOLEAN
    );
    """

query_items_in_match = """
    CREATE TABLE IF NOT EXISTS items_in_match (
      id_items_match SERIAL PRIMARY KEY,
      id_match INTEGER,
      id_item INTEGER,
      id_hero INTEGER,
      FOREIGN KEY(id_match) REFERENCES Match(id_match),
      FOREIGN KEY(id_item) REFERENCES Item(id_item),
      FOREIGN KEY(id_hero) REFERENCES Hero(id_hero)
    );
    """
query_item = """
    CREATE TABLE IF NOT EXISTS Item (
      id_item SERIAL PRIMARY KEY,
      item_price INTEGER CHECK (item_price >= 0),
      item_description VARCHAR(500),
      name VARCHAR(30)
    );
    """

query_abilities = """
    CREATE TABLE IF NOT EXISTS Heroes_abilities (
      id_ability SERIAL PRIMARY KEY,
      ability_type VARCHAR(30) CHECK (ability_type IN ('Active', 'Passive')),
      id_hero INTEGER,
      ability_name VARCHAR(50),
      FOREIGN KEY(id_hero) REFERENCES Hero(id_hero)
    );
    """

query_tournament_match = """
    CREATE TABLE IF NOT EXISTS Tournament_match (
      id_tournament_match SERIAL PRIMARY KEY,
      id_match INTEGER NOT NULL UNIQUE,
      id_Team1 INTEGER,
      id_Team2 INTEGER,
      id_tournament INTEGER,
      FOREIGN KEY(id_match) REFERENCES match(id_match),
      FOREIGN KEY(id_Team1) REFERENCES Team(id),
      FOREIGN KEY(id_Team2) REFERENCES Team(id),
      FOREIGN KEY(id_tournament) REFERENCES Tournament(id)
    );
    """

query_team = """
    CREATE TABLE IF NOT EXISTS Team (
      id SERIAL PRIMARY KEY,
      name VARCHAR(30),
      count_wins INTEGER CHECK (count_wins >= 0),
      total_price INTEGER CHECK (total_price >= 0)
    );
    """

query_tournament = """
    CREATE TABLE IF NOT EXISTS tournament (
      id SERIAL PRIMARY KEY,
      name VARCHAR(30),
      price_win INTEGER CHECK (price_win >= 0),
      win_team INTEGER CHECK (win_team >= 0)
    );
    """

query_players_in_team = """
    CREATE TABLE IF NOT EXISTS Players_in_team (
      id SERIAL PRIMARY KEY,
      id_player INTEGER,
      id_team INTEGER,
      FOREIGN KEY(id_team) REFERENCES Team(id),
      FOREIGN KEY(id_player) REFERENCES Players(id_player)
    );
    """


def createBD():
    conn = connection()
    cursor = conn.cursor()
    queries = [query_players, query_match, query_hero, query_item, query_abilities, query_team, query_tournament, query_history, query_items_in_match, query_tournament_match, query_players_in_team]
    for func in queries:
        cursor.execute(func)
    conn.commit()
    cursor.close()
    conn.close()