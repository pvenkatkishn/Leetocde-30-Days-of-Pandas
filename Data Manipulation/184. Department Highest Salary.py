Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.


Solution:
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, department, left_on = "departmentId", right_on = "id", suffixes = ("_emp","_dept"))
    max_sal = df.groupby(by= "name_dept")["salary"].max().reset_index()
    df1 = df[df["salary"].isin(max_sal["salary"])]
    return df1.rename(columns= {
        "name_emp" : "Employee",
        "name_dept" : "Department",
        "salary" : "Salary"
    })[["Department", "Employee", "Salary"]]
