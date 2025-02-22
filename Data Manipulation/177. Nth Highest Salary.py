Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.



Solution:
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
  employee["rank"] = employee["salary"].rank(ascending = False, axis = 0, method="dense")
  nthhighest = employee[employee["rank"] == N]
  return pd.DataFrame({ f'getNthHighestSalary({N})':[None if len(nthhighest) == 0 else nthhighest['salary'].iloc[0]]})
