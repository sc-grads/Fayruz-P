When to use cursors
declare @EmployeeID int
declare csr CURSOR FOR 
select EmployeeNumber
from [dbo].[tblEmployee]
where EmployeeNumber between 120 and 299

open csr
fetch next from csr into @EmployeeID
while @@FETCH_STATUS = 0
begin
	select * from [dbo].[tblTransaction] where EmployeeNumber = @EmployeeID
	fetch next from csr into @EmployeeID
end
close csr
deallocate csr
Alternatives
select T.*
from tblTransaction as T
right join tblEmployee as E
on T.EmployeeNumber = E.EmployeeNumber
where E.EmployeeNumber between 120 and 299 
and T.EmployeeNumber is not null
impact of scalar UDFs
--set statistics time on


CREATE FUNCTION fnc_TransactionTotal (@intEmployee as int)
returns money
as
begin
declare @TotalAmount as money
select @TotalAmount = sum(Amount) 
from [dbo].[tblTransaction]
where EmployeeNumber = @intEmployee
return @TotalAmount
end

set showplan_all on
go
set showplan_text on
go
select [EmployeeNumber], dbo.fnc_TransactionTotal([EmployeeNumber]) 
from [dbo].[tblEmployee]

select E.[EmployeeNumber], sum(Amount) as TotalAmount
from [dbo].[tblEmployee] as E
left join [dbo].[tblTransaction] as T
on E.EmployeeNumber = T.EmployeeNumber
group by E.[EmployeeNumber]
set statistics time off
set showplan_all off

select EmployeeNumber, dbo.fnc_TransactionTotal(EmployeeNumber)
from dbo.tblEmployee

select E.EmployeeNumber, sum(T.Amount) as TotalAmount
from dbo.tblEmployee as E
left join dbo.tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
group by E.EmployeeNumber

select E.EmployeeNumber, (select sum(Amount) from tblTransaction as T 
                          where T.EmployeeNumber = E.EmployeeNumber) as TotalAmount
from dbo.tblEmployee as E


create function fnc_TransactionAll (@intEmployee as int)
returns @returntable table
(Amount smallmoney)
as
begin
	insert @returntable
	select amount
	from dbo.tblTransaction
	where EmployeeNumber = @intEmployee
	return
end

select * from dbo.fnc_TransactionAll (128)

select EmployeeNumber, sum(T.Amount) as TotalAmount
from dbo.tblEmployee as E
outer apply fnc_TransactionAll(EmployeeNumber) as T
group by EmployeeNumber

select E.EmployeeNumber, sum(T.Amount) as TotalAmount
from dbo.tblEmployee as E
left join dbo.tblTransaction as T on E.EmployeeNumber = T.EmployeeNumber
group by E.EmployeeNumber
