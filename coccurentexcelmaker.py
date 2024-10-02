import pandas as pd
import json
import datetime

with open("leagues/leagues.txt", "r") as f:
    leagues = json.load(f)

for i in leagues:
    file_path = f"datatxt/{i}.txt"
    print(i)
    try:     
        with open(file_path, "r") as f:
            content = json.load(f)
    except:
        pass    
    objects = []
    try:
        for match in content:
            home_teams_list = []
            away_teams_list = []
            bookmakers_list = []
            team_home_quotes_list = []
            team_away_quotes_list = []
            team_x_quotes_list = []
            commence_time = match['commence_time']

            home_team = match['home_team']
            away_team = match['away_team']
            for bookmakers in match['bookmakers']:

                bookmakers_list.append(bookmakers['key'])
                
                for markets in bookmakers['markets']:
                    
                    for outcomes in markets['outcomes']:
                        if markets['key'] == "h2h_lay":
                            continue
                        elif outcomes['name'] == home_team:
                            home_teams_list.append(home_team)
                            team_home_quotes_list.append(outcomes['price'])
                        elif outcomes['name'] == match['away_team']:
                            away_teams_list.append(away_team)
                            team_away_quotes_list.append(outcomes['price'])
                        else:
                            team_x_quotes_list.append(outcomes['price'])
            obj = {
                "Team Home": home_teams_list,
                "Team Away": away_teams_list,
                "Bookmakers": bookmakers_list,
                "1": team_home_quotes_list,
                "2": team_away_quotes_list,
                "x": team_x_quotes_list
            }
            objects.append(obj)
    except:
        print(i) 

    output_file = f"dataxlsx/{i}.xlsx"
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:

        for j, match in enumerate(objects):
            sheet_name = f"Match_{j+1}"
            df = pd.DataFrame(match)
            sorted_df = df.sort_values("1", ascending=False)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
