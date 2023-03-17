begin tran
alter table tblEmployee
add Manager int
go
update tblEmployee
set Manager = ((EmployeeNumber-123)/10)+123
where EmployeeNumber>123
select E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastName,
       M.EmployeeNumber as ManagerNumber, M.EmployeeFirstName as ManagerFirstName, 
	   M.EmployeeLastName as ManagerLastName
from tblEmployee as E
left JOIN tblEmployee as M
on E.Manager = M.EmployeeNumber

rollback tran
