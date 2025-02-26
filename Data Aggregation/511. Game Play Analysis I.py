Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 

Write a solution to find the first login date for each player.

Return the result table in any order.


Solution:
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_logins = activity.groupby("player_id")["event_date"].min().reset_index()
    return first_logins.rename(columns = {'event_date' : 'first_login'})
