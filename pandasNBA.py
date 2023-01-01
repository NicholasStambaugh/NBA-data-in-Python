import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Read Data
df = pd.read_csv(r"C:\Program Files\JetBrains\nba.csv")
df.head()
df.describe()

#Column names
print(df.columns)

#Top Scorers
df.groupby('player')['total_points'].max() \
    .sort_values(ascending=False) \
    .head(10) \
    .sort_values() \
    .plot(kind='barh',
          figsize=(10, 5),
          title='Top Ten Scorers All Time',
          color='teal')
plt.show()

#Top PPG
df.groupby('player')['points_per_game'].max() \
    .sort_values(ascending=False) \
    .head(10) \
    .sort_values() \
    .plot(kind='barh',
          figsize=(5, 10),
          title='Top Ten PPG All Time',
          color='darkgreen')
plt.show()

#Top free shots
df.groupby('player')['free_shots'].max() \
    .sort_values(ascending=False) \
    .head(5) \
    .sort_values() \
    .plot(kind='barh',
          figsize=(5, 10),
          title='Top 5 Free Shots All Time',
          color='purple')
plt.show()

#Top 5 Three Point Shooters
df.groupby('player')['three_points_goals'].max() \
    .sort_values(ascending=False) \
    .head(5) \
    .sort_values() \
    .plot(kind='barh',
          figsize=(5, 10),
          title='Top 5 3-Point Shooters All Time',
          color='purple')
plt.show()

#mean
df.points_per_game.mean()
#quantiles
df.total_points.quantile([0.25,0.75])
#median
df.free_shots.median()
#new column
df['threes_per_Game'] = df.three_points_goals/df.total_games
#query basics
df.query('threes_per_Game > 1.3 and free_shots > 100')
#rename
df = df.rename(columns = {'points_per_game':'Points Per Game'})
#std & var & mean
df.std()
df.mean()
df.var()

#unique values
df['teams'].nunique()

#3s made a game. graph
df.groupby('player')['threes_per_Game'].max() \
    .sort_values(ascending=False) \
    .head(7) \
    .sort_values() \
    .plot(kind='barh',
          figsize=(15, 6),
          title='Three Pointers Made per Game, Top 7',
          color='grey')
plt.show()

#3s by team
df.groupby('teams')['threes_per_Game'].max() \
    .sort_values(ascending=False) \
    .head(5) \
    .sort_values() \
    .plot(kind='barh',
          figsize=(15, 8),
          title='Three Pointers Made per Game, Top 15 Teams',
          color='grey')
plt.show()

#basic scatterplot
df.plot.scatter(x='Points Per Game', y='free_shots', title='PPG by Free Shots')

#seaborn plotting
import seaborn as sns
sns.regplot(data=df, x='Points Per Game', y='free_shots')
sns.jointplot(data=df, x='total_points', y='total_games', hue='hall_of_fame')
sns.jointplot(data=df, x='total_points', y='total_games', hue='country')

sns.catplot(data=df, x='active_player', y='total_points', hue='country')
sns.catplot(data=df, x='position', y='total_points', kind='box')
sns.catplot(data=df, x='position', y='points_per_game', kind='box')