Table: Courses

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
 

Write a solution to find all the classes that have at least five students.

Return the result table in any order.



Solution:
import pandas as pd
import numpy as np

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = (courses.groupby('class')['student'].count().reset_index())
    df_1 = df[df["student"] >= 5]
    return df_1[["class"]]
