CREATE FUNCTION TransactionList(@EmployeeNumber int)
RETURNS TABLE AS RETURN
(
    SELECT * FROM tblTransaction
	WHERE EmployeeNumber = @EmployeeNumber
)

SELECT * 
from dbo.TransactionList(123)

select *
from tblEmployee
where exists(select * from dbo.TransactionList(EmployeeNumber))

select distinct E.*
from tblEmployee as E
join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber

select *
from tblEmployee as E
where exists(Select EmployeeNumber from tblTransaction as T where E.EmployeeNumber = T.EmployeeNumber)
