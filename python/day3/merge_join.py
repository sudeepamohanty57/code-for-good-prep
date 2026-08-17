import pandas as pd

employees = pd.DataFrame({
    "employee_id": [1, 2, 3, 4],
    "name": ["A", "B", "C", "D"],
    "department_id": [101, 102, 101, 103]
})

departments = pd.DataFrame({
    "department_id": [101, 102, 104],
    "department": ["IT", "HR", "Finance"]
})

""" Inner merge """

print(
    pd.merge(
        employees,
        departments,
        on="department_id",
        how="inner"
    )
)

print(
    pd.merge(
        employees,
        departments,
        on="department_id",
        how="left"
    )
)

"""SQL equivalent"""

""" SELECT *
FROM employees
LEFT JOIN departments
ON employess.department_id= departments.department_id
"""

