
begin transaction

select count(*) from tblTransaction

delete tblTransaction
from tblEmployee as E
right join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
where E.EmployeeNumber is null

select count(*) from tblTransaction

rollback transaction

select count(*) from tblTransaction
-- Version 2

begin transaction
select count(*) from tblTransaction

delete tblTransaction
from tblTransaction
where EmployeeNumber IN
(select TNumber
from (
select E.EmployeeNumber as ENumber, E.EmployeeFirstName,
       E.EmployeeLastName, T.EmployeeNumber as TNumber, 
       sum(T.Amount) as TotalAmount
from tblEmployee as E
right join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
group by E.EmployeeNumber, T.EmployeeNumber, E.EmployeeFirstName,
       E.EmployeeLastName) as newTable
where ENumber is null)
select count(*) from tblTransaction
rollback tran
select count(*) from tblTransaction
