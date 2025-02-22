Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).



Solution:
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
  employee["rank"] = employee["salary"].rank(ascending = False, axis = 0, method='dense')
  sechighest = employee[employee["rank"] == 2]
  return pd.DataFrame({'SecondHighestSalary' : [None if len(sechighest) == 0 else sechighest['salary'].iloc[0]]})
