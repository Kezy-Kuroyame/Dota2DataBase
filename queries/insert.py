import random
import datetime
import string

from connection.connection import connection


HEROES = 10
TEAMS = 2000
TOURNAMENTS = 1006
ITEMS = 30
PLAYERS = 2000
TOURNAMENT_MATCHES = 20
MATCHES = 29999


def insertHeroes():
    conn = connection()
    cursor = conn.cursor()

    # data = pd.read_csv("csv/heroes.csv")
    # data = data[['localized_name', 'base_str', 'base_agi', 'base_int']]
    # for index, row in data.iterrows():
    #     print(index)
    #     sql_query = f"""
    #     INSERT INTO heroes (name_hero, strength, agility, intelligence)
    #                 VALUES('{row['localized_name'].replace("'", "")}', {row['base_str']}, {row['base_agi']}, {row['base_int']});
    #     """
    #     cursor.execute(sql_query)

    sql_query = f"""
        INSERT INTO hero (name_hero, strength, agility, intelligence) 
            VALUES 
                ('Axe', 25, 20, 18),
                ('Bane', 23, 23, 23),
                ('Earthshaker', 22, 12, 18),
                ('Juggernaut', 20, 34, 14),
                ('Mirana', 20, 24, 22),
                ('Morphling', 23, 23, 19),
                ('Puck', 17, 22, 23),
                ('Pudge', 25, 14, 16),
                ('Razor', 22, 24, 21),
                ('Sven', 22, 21, 16);
        """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def insertAbilities():
    conn = connection()
    cursor = conn.cursor()
    sql_query = f"""
           INSERT INTO Heroes_abilities (ability_type, id_hero, ability_name) 
               VALUES 
                   ('Active', 1, 'BERSERKERS CALL'),
                   ('Active', 1, 'BATTLE HUNGER'),
                   ('Passive', 1, 'COUNTER HELIX'),
                   ('Active', 1, 'CULLING BLADE'),
                   ('Active', 2, 'ENFEEBLE'),
                   ('Active', 2, 'BRAIN SAP'),
                   ('Active', 2, 'NIGHTMARE'),
                   ('Active', 2, 'FIENDS GRIP'),
                   ('Active', 3, 'FISSURE'),
                   ('Active', 3, 'ENCHANT TOTEM'),
                   ('Passive', 3, 'AFTERSHOCK'),
                   ('Active', 3, 'ECHO SLAM'),
                   ('Active', 4, 'BLADE FURY'),
                   ('Active', 4, 'HEALING WARD'),
                   ('Passive', 4, 'BLADE DANCE'),
                   ('Active', 4, 'OMNISLASH'),
                   ('Active', 5, 'STARSTORM'),
                   ('Active', 5, 'SACRED ARROW'),
                   ('Active', 5, 'LEAP'),
                   ('Active', 5, 'MOONLIGHT SHADOW'),
                   ('Active', 6, 'WAVEFORM'),
                   ('Active', 6, 'ADAPTIVE STRIKE'),
                   ('Active', 6, 'ATTRIBUTE SHIFT'),
                   ('Active', 6, 'MORPH'),
                   ('Active', 7, 'ILLUSORY ORB'),
                   ('Active', 7, 'WANING RIFT'),
                   ('Active', 7, 'PHASE SHIFT'),
                   ('Active', 7, 'DREAM COIL'),
                   ('Active', 8, 'MEAT HOOK'),
                   ('Active', 8, 'ROT'),
                   ('Passive', 8, 'FLESH HEAP'),
                   ('Active', 8, 'DISMEMBER'),
                   ('Active', 9, 'PLASMA FIELD'),
                   ('Active', 9, 'STATIC LINK'),
                   ('Passive', 9, 'STORM SURGE'),
                   ('Active', 9, 'EYE OF THE STORM'),
                   ('Active', 10, 'STORM HAMMER'),
                   ('Passive', 10, 'GREAT CLEAVE'),
                   ('Active', 10, 'WARCRY'),
                   ('Active', 10, 'GODS STRENGTH');        
           """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def insertItems():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
           INSERT INTO ITEM (item_price, item_description, name) 
               VALUES 
                   (1900, 'Каждая атака может с вероятностью в 30% нанести 160% урона.', 'Crystalys'),
                   (2500, 'Если включена, увеличивает урон на 35, силу на 25, сопротивление замедлениям на 35% и броню на 4, но отнимает 45 здоровья в секунду. Вы не можете умереть ни от потери здоровья из-за способности, ни от спада бонуса к силе после её выключения.', 'Armlet of Mordiggian'),
                   (2875, 'Каждая атака может оглушить цель на 1,2 сек. и нанести 100 физического урона. Вероятность зависит от типа атаки владельца: 25% в ближнем бою, 10% — в дальнем.', 'Skull Basher'),
                   (3000, 'Делает героя невидимым на 14 сек. или до момента, когда он совершит атаку или применит способность. Также увеличивает скорость передвижения на 20% и позволяет проходить сквозь существ.', 'Shadow Blade'),
                   (3500, 'Атаки уменьшают броню цели на -6. Эффект длится 7 сек', 'Desolator'),
                   (4800, 'Атаки героя прорубают жертву, нанося врагам в радиусе 650 вокруг неё физический урон (только в ближнем бою)', 'Battle Fury'),
                   (4650, 'Придаёт цели бесплотный облик, который полностью защищает от физического урона, но не позволяет атаковать и увеличивает получаемый магический урон на -40%.', 'Ethereal Blade'),
                   (4375, 'Развеивает положительные эффекты с цели в момент применения и следующие 5 сек', 'Nullifier'),
                   (4900, 'Каждая атака может с вероятностью в 80% пройти сквозь уклонение и нанести 70 дополнительного магического урона.', 'Monkey King Bar'),
                   (4975, 'Этот клинок могут обуздать лишь самые могучие и опытные воины, но владельцу он даёт невероятное проворство в бою.', 'Butterfly'),
                   (1700, 'С вероятностью в 60% блокирует 50 урона от атак, если владелец — герой ближнего боя, или 25 урона, если герой дальнего боя.', 'Vanguard'),
                   (2800, 'Возвращает 20 + 20% урона от каждой атаки атакующим вас существам.', 'Blade Mail'),
                   (3000, 'Если здоровье владельца упадёт ниже 70%, он получит магический щит, который сильным очищением развеет большинство эффектов, а также на 2,5 сек. увеличит сопротивление эффектам на 75% и не даст наносить или получать урон. Срабатывает только от урона игроков. Перезарядка увеличивается после каждого срабатывания.', 'Aeon Disk'),
                   (3800, 'Восстанавливает ману в размере 30% от урона, наносимого вражескими заклинаниями.', 'Eternal Shroud'),
                   (3725, 'На 8 сек. даёт героям и постройкам поблизости шанс в 100% заблокировать урон от каждой атаки в размере 70 + 50% от силы владельца. Способность действует на одно и то же существо не чаще, чем раз в 35 секунд.', 'Crimson Guard'),
                   (3850, 'Создаёт вокруг цели щит, отражающий большинство направленных заклинаний обратно во врага. Действует 6 сек.', 'Lotus Orb'),
                   (4050, 'Применяет на владельца нормальное развеивание. Даёт +50% к сопротивлению магии и невосприимчивость к чистому и отражённому урону. Защищает владельца от действия отрицательных эффектов.', 'Black King Bar'),
                   (4600, 'Создаёт 2 иллюзии вашего героя, которые существуют 20 сек.', 'Manta Style'),
                   (5200, 'Сохранившееся сердце вымершего монстра, которое укрепляет стойкость владельца.', 'Heart of Tarrasque'),
                   (1900, 'Увеличивает дальность атаки героев дальнего боя.', 'Dragon Lance'),
                   (2500, 'Позволяет героям ближнего боя совершить двойную атаку, которая на 0,8 секунд уменьшает скорость передвижения жертвы на 100%.', 'Echo Sabre'),
                   (2700, 'Каждая атака с вероятностью в 30% может создать разряд цепной молнии, которая 4 раза перескочит между случайными врагами в радиусе 650, нанося каждому по 135 магического урона. От атаки с цепной молнией нельзя уклониться. Наносит 150% урона иллюзиям.', 'Maelstrom'),
                   (2500, 'Замедляет противника на 4 сек.', 'Diffusal Blade'),
                   (2500, 'Атакуемые враги наносят на 35% меньше урона заклинаниями. Действует 6 сек.', 'Mage Slayer'),
                   (2375, 'Следующая способность, направленная на врага, отдельно нанесёт ему ещё 150 урона и замедлит его на 50%. Длительность: 1,5 сек.', 'Phylactery'),
                   (5050, 'Увеличивает эффект вампиризма до 175% на 6 сек.', 'Satanic'),
                   (5300, 'Каждая атака на 3 сек. замедляет передвижение и атаку цели, а также уменьшает её лечение, восстановление здоровья, вампиризм и вампиризм способностями на 40%. Замедление зависит от типа атаки жертвы: у существ дальнего боя замедляет передвижение на 50%, атаку — на 60. У существ ближнего боя замедляет передвижение на 20%, атаку — на 30.', 'Eye of Skadi'),
                   (5500, 'На 15 сек. окружает выбранное существо заряженным щитом, который с вероятностью в 20% может нанести 225 магического урона атакующему врагу и 4 другим.', 'Mjollnir'),
                   (6800, 'После перемещения мгновенно наносит урон, равный 100 + 50% от силы владельца и дополнительный урон в размере 100% от силы героя постепенно, всем врагам в радиусе 800 и замедляет их передвижение на 50%, а атаку — на 50. Замедление действует 6 сек.', 'Overwhelming Blink'),
                   (4500, 'Выстреливает в выбранного врага гарпун, который тянет владельца и цель друг к другу на расстояние до 35% от изначального. Если владелец сражается в ближнем бою, притягивает его и цель на расстояние атаки', 'Harpoon');
           """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def insertPlayers():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
            INSERT INTO players (name, count_wins, count_defeats, mmr) 
                VALUES 
                    ('kezy', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('kepasta', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('morkovka', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('jast', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('pacan', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('loogika', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('polyak', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('Monkey', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('pomelo', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('lucy', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('zarevo', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0),
                    ('collapse', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('yatoro', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('larl', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('mira', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('miposhka', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('nightfall', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('torontotokyo', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('gpk', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Pure', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Save', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('RAMZES666', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('kiyotaka', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Antares', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Solo', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Miero', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('dyrachyo', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Ace', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Quinn', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('tOfu', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Seleri', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('miCKe', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Nisha', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('33', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Boxi', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('iNSaNiA', {random.randint(1000, 1000)}, {random.randint(500, 800)}, 0),
                    ('Timado', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Bryle', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Kasane', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Immersion', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Whitemon', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Crystallis', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('MidOne', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('BOOM', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('yamich', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('Puppey', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
                    ('SabeRLighT', {random.randint(800, 1000)}, {random.randint(500, 800)}, 0),
            UPDATE players
            SET mmr = (count_wins - count_defeats) * 27
            WHERE count_wins > count_defeats
            """

    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def insertTeam():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
         INSERT INTO Team (name, count_wins, total_price) 
             VALUES 
                ('Team Spirit', {random.randint(100, 1000)}, {random.randint(10000, 10000000)}),
                ('Gaimin Gladiators', {random.randint(100, 1000)}, {random.randint(10000, 10000000)}),
                ('9 Pandas', {random.randint(100, 1000)}, {random.randint(10000, 10000000)}),
                ('BetBoom Team', {random.randint(100, 1000)}, {random.randint(10000, 10000000)}),
                ('Liquid Team', {random.randint(100, 1000)}, {random.randint(10000, 10000000)}),
                ('Team Secret', {random.randint(100, 1000)}, {random.randint(10000, 10000000)});
                ('Team Tundra', {random.randint(100, 1000)}, {random.randint(10000, 10000000)});
         """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def insertPlayersInTeam():
    conn = connection()
    cursor = conn.cursor()

    sql_query = f"""
         INSERT INTO Players_in_team (id_player, id_team) 
             VALUES 
                (12, 1),
                (13, 1),
                (14, 1),
                (15, 1),
                (16, 1),
                (17, 4),
                (18, 4),
                (19, 4),
                (20, 4),
                (21, 4),
                (22, 3),
                (23, 3),
                (24, 3),
                (25, 3),
                (26, 3),
                (27, 2),
                (28, 2),
                (29, 2),
                (30, 2),
                (31, 2),
                (32, 5),
                (33, 5),
                (34, 5),
                (35, 5),
                (36, 5),
                (37, 7),
                (38, 7),
                (39, 7),
                (40, 7),
                (41, 7),
                (42, 6),
                (43, 6),
                (44, 6),
                (45, 6),
                (46, 6);
                
    """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def insertTournament():
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


def insertItemsInMatches():
    conn = connection()
    cursor = conn.cursor()
    match = 29
    for index_match in range(1, match + 1):
        heroes = []
        for _ in range(10):
            hero = random.randint(1, HEROES)
            while hero in heroes:
                hero = random.randint(1, HEROES)
            heroes.append(hero)

        for hero in heroes:
            for item in range(random.randint(1, 6)):
                sql_query = f"""
                     INSERT INTO items_in_match (id_match, id_item, id_hero) 
                         VALUES 
                         ({index_match}, {random.randint(1, 30)}, {hero});        
                """
                cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def insertTournamentMatch():
    conn = connection()
    cursor = conn.cursor()
    match_id = 21
    matches = []

    for tournament in range(1, TOURNAMENTS):
        for match in range(1, 6):
            team1 = random.randint(1, TEAMS)
            team2 = random.randint(1, TEAMS)
            while [team1, team2] in matches or [team2, team1] in matches:
                team1 = random.randint(1, TEAMS)
                team2 = random.randint(1, TEAMS)
            matches.append([team1, team2])
        for match in matches:
            sql_query = f"""
                 INSERT INTO tournament_match (id_match, id_team1, id_team2, id_tournament) 
                     VALUES 
                     ({match_id}, {match[0]}, {match[1]}, {tournament});            
            """
            match_id += 1
            cursor.execute(sql_query)
        matches.clear()
    conn.commit()
    cursor.close()
    conn.close()


def insertMatch():
    conn = connection()
    cursor = conn.cursor()

    id = []
    duration = []
    time_end = []
    win_team = []

    for i in range(1, 30000):
        id.append(i)
        duration.append(random.randint(900, 5100))
        days = random.randint(10, 1000)
        time_end.append((datetime.datetime.now() - datetime.timedelta(days=days, hours=duration[i - 1] / 60 / 60,
                                                                      minutes=duration[i - 1] / 60 % 60,
                                                                      seconds=duration[i - 1] % 60)))
        win_team.append(random.randint(0, 1))

    for i in range(len(id)):
        query = f"""
                INSERT INTO Match
                    (time_end, duration, win_team)
                VALUES ('{time_end[i].strftime('%Y-%m-%d %H:%M:%S')}', {duration[i]}, {bool(win_team[i])});
            """
        cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def insertHistory():
    conn = connection()
    cursor = conn.cursor()
    for match_index in range(1, MATCHES + 1):
        players = []
        heroes = []

        for _ in range(10):
            player = random.randint(1, PLAYERS)
            hero = random.randint(1, HEROES)
            while player in players:
                player = random.randint(1, PLAYERS)
            while hero in heroes:
                hero = random.randint(1, HEROES)
            players.append(player)
            heroes.append(hero)

        for i in range(10):
            sql_query = f"""
                     INSERT INTO matches_history (id_player, id_match, team, id_hero) 
                         VALUES 
                         ({players[i]}, {match_index}, {False if i >= 5 else True}, {heroes[i]});            
            """
            cursor.execute(sql_query)

    conn.commit()
    cursor.close()
    conn.close()


def insertItemsRandom():
    conn = connection()
    cursor = conn.cursor()
    letters = string.ascii_letters
    for i in range(10000):
        description = "".join(random.choice(letters) for _ in range(100))
        name = "".join(random.choice(letters) for _ in range(20))
        sql_query = f"""
            INSERT INTO ITEM (item_price, item_description, name)
            VALUES
            ({random.randint(1000, 6000)}, '{description}', '{name}')
        """
        cursor.execute(sql_query)

    conn.commit()
    cursor.close()
    conn.close()


def insertPlayersRandom():
    conn = connection()
    cursor = conn.cursor()
    letters = string.ascii_letters
    for i in range(10000):
        name = "".join(random.choice(letters) for _ in range(15))
        sql_query = f"""
             INSERT INTO players (name, count_wins, count_defeats, mmr) 
                VALUES 
                    ('{name}', {random.randint(500, 1000)}, {random.randint(0, 500)}, 0)
        """
        cursor.execute(sql_query)
    sql_query = f"""
    UPDATE players
            SET mmr = (count_wins - count_defeats) * 27
            WHERE count_wins > count_defeats
    """
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def insertTeamsRandom():
    conn = connection()
    cursor = conn.cursor()
    letters = string.ascii_letters
    for i in range(2000):
        name = "".join(random.choice(letters) for _ in range(15))
        sql_query = f"""
             INSERT INTO Team (name, count_wins, total_price) 
                VALUES 
                    ('{name}', {random.randint(200, 1000)}, {random.randint(0, 1500000)})
        """
        cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def insertPlayersTeamRandom():
    conn = connection()
    cursor = conn.cursor()
    for team in range(1, 2000 + 1):
        for player in range(5):
            sql_query = f"""
                 INSERT INTO players_in_team (id_player, id_team) 
                    VALUES 
                        ({10048 - (team * 5 + player)}, {team})
            """
            cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()


def insertTournamentRandom():
    conn = connection()
    cursor = conn.cursor()
    letters = string.ascii_letters

    for i in range(1000):
        name = "".join(random.choice(letters) for _ in range(25))
        sql_query = f"""
             INSERT INTO tournament (name, price_win, win_team) 
                 VALUES 
                    ('{name}', {random.randint(100000, 1000000)}, {random.randint(1, 2000)})               
        """
        cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()



