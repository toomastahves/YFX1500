# INNER JOIN
SELECT t1.*, t2.*
FROM Table1 t1
INNER JOIN Table2 t2 
ON t1.ID = t2.ID;

# LEFT OUTER JOIN
SELECT t1.ID AS T1ID, t1.Value AS T1Value, t2.ID as T2ID, t2.Value as T2Value
FROM Table1 t1
LEFT JOIN Table2 t2 
ON t1.ID = t2.ID;

# RIGHT OUTER JOIN
SELECT t1.ID AS T1ID, t1.Value AS T1Value, t2.ID as T2ID, t2.Value as T2Value
FROM Table1 t1
RIGHT JOIN Table2 t2 
ON t1.ID = t2.ID;

# Simulate FULL OUTER JOIN
SELECT t1.ID AS T1ID, t1.Value AS T1Value, t2.ID as T2ID, t2.Value as T2Value
FROM Table1 t1
LEFT JOIN Table2 t2 
ON t1.ID = t2.ID
UNION
SELECT t1.ID AS T1ID, t1.Value AS T1Value, t2.ID as T2ID, t2.Value as T2Value
FROM Table1 t1
RIGHT JOIN Table2 t2 
ON t1.ID = t2.ID;

# CROSS JOIN
SELECT t1.ID AS T1ID, t1.Value AS T1Value, t2.ID as T2ID, t2.Value as T2Value
FROM Table1 t1
CROSS JOIN Table2 t2;

# SELF JOIN
SELECT e1.name AS EmployeeName, e2.name AS ManagerName
FROM Employee e1
INNER JOIN Employee e2
ON e1.managerid = e2.employeeid;

SELECT e1.name AS EmployeeName, IFNULL(e2.name, 'boss') AS ManagerName
FROM Employee e1
LEFT JOIN Employee e2
ON e1.managerid = e2.employeeid;

# NATURAL JOIN
SELECT t1.ID AS T1ID, t1.Value AS T1Value, t2.ID as T2ID, t2.Value as T2Value
FROM Table1 t1
NATURAL JOIN Table2 t2;

SELECT t1.ID AS T1ID, t1.Value AS T1Value, t2.ID as T2ID, t2.Value as T2Value
FROM Table1 t1
NATURAL LEFT JOIN Table2 t2;

# USING
SELECT t1.ID AS T1ID, t1.Value AS T1Value, t2.ID as T2ID, t2.Value as T2Value
FROM Table1 t1
INNER JOIN Table2 t2 
USING (ID, Value);

# UNION
SELECT t1.ID AS T1ID, t1.Value AS T1Value
FROM Table1 t1
UNION ALL
SELECT t2.ID AS T2ID, t2.Value AS T2Value
FROM Table2 t2;

SELECT t1.ID AS T1ID, t1.Value AS T1Value
FROM Table1 t1
UNION
SELECT t2.ID AS T2ID, t2.Value AS T2Value
FROM Table2 t2;
