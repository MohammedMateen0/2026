CREATE TABLE Employees(
    EmployeeID INT,
    Name TEXT,
    EmployeeCode TEXT,
    Salary INT
);

INSERT INTO Employees (EmployeeID, Name, EmployeeCode, Salary)
VALUES 
(001, 'Sham', 'EM001', 30000),
(002, 'Ravi', 'EM002', 32000),
(003, 'Ali', 'EM003', 20000),
(4, 'Ravi', 'EM004', 25000);
INSERT INTO Employees VALUES (5, 'Arun', 'EM001', 25000);
INSERT INTO Employees VALUES (6, 'Kiran', 'EM001', 20000);
WITH RankedSalaries AS (
    SELECT 
        EmployeeID,
        name,
        EmployeeCode,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY EmployeeCode
            ORDER BY salary DESC
        ) AS salary_rank
    FROM Employees
)
SELECT 
    EmployeeID,
    name,
    EmployeeCode,
    salary
FROM RankedSalaries
WHERE salary_rank = 2;

