select * from
(select D.Department, EmployeeNumber, EmployeeFirstName, EmployeeLastName,
       rank() over(partition by D.Department order by E.EmployeeNumber) as TheRank
 from tblDepartment as D 
 join tblEmployee as E on D.Department = E.Department) as MyTable
where TheRank <= 5
order by Department, EmployeeNumber
