import pandas as pd

df = pd.read_csv("exercices/module 4/csv/fictitious_basketball_league_players_1200_v2 - fictitious_basketball_league_players_1200_v2.csv")
top_salary = df.nlargest(10, "salary")[["Team", "salary"]]
print(top_salary)