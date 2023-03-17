select E.EmployeeNumber, T.Amount
from [dbo].[tblEmployee] as E
left join [dbo].[tblTransaction] as T
on E.EmployeeNumber = T.EmployeeNumber
where E.EmployeeNumber = 134

select E.EmployeeNumber, T.Amount
from [dbo].[tblEmployeeNoIndex] as E
left join [dbo].[tblTransactionNoIndex] as T
on E.EmployeeNumber = T.EmployeeNumber
where E.EmployeeNumber = 134
select E.EmployeeNumber, T.Amount
from [dbo].[tblEmployee] as E
left join [dbo].[tblTransaction] as T
on E.EmployeeNumber = T.EmployeeNumber
where E.EmployeeNumber / 10 = 34 --Not SARG

select E.EmployeeNumber, T.Amount
from [dbo].[tblEmployee] as E
left join [dbo].[tblTransaction] as T
on E.EmployeeNumber = T.EmployeeNumber
where E.EmployeeNumber between 340 and 349 --SARG
plan guides
select *
into dbo.tblTransactionBig
from [dbo].[tblTransaction]

insert into dbo.tblTransactionBig ([Amount], [DateOfTransaction], [EmployeeNumber])
select T1.Amount, T2.DateOfTransaction, 1 as EmployeeNumber
from [dbo].[tblTransaction] as T1
cross join (select * from [dbo].[tblTransaction] where EmployeeNumber<200) as T2

create nonclustered index idx_tbltblTransactionBig on dbo.tblTransactionBig(EmployeeNumber)

create proc procTransactionBig(@EmployeeNumber as int) WITH RECOMPILE
as
select *
from tblTransactionBig as T
left join tblEmployee as E
on T.EmployeeNumber = E.EmployeeNumber
where T.EmployeeNumber = @EmployeeNumber

exec procTransactionBig 1
exec procTransactionBig 132

Hints
select D.Department, D.DepartmentHead, E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastName 
from [dbo].[tblDepartment] as D  WITH (NOLOCK)
left join [dbo].[tblEmployee] as E
on D.Department = E.Department
where D.Department = 'HR'
select D.Department, D.DepartmentHead, E.EmployeeNumber, E.EmployeeFirstName, E.EmployeeLastName 
from [dbo].[tblDepartment] as D  WITH (REPEATABLEREAD)
left join [dbo].[tblEmployee] as E
on D.Department = E.Department
where D.Department = 'HR'
•	dynamic vs. parameterised queries
DECLARE @param varchar(1000) = '127';

DECLARE @sql nvarchar(max) =
    N'
    SELECT *
    FROM [dbo].[tblTransaction] AS T
    WHERE T.EmployeeNumber = ' + @param;

EXECUTE (@sql);


DECLARE @parameter varchar(1000) = '127' + char(10) + 'SELECT * from dbo.tblTransaction';

DECLARE @sql nvarchar(max) =
    N'
    SELECT *
    FROM [dbo].[tblTransaction] AS T
    WHERE T.EmployeeNumber = ' + @parameter;

EXECUTE (@sql);

DECLARE @param varchar(1000) = '127';

EXECUTE sys.sp_executesql
    @statement = 
        N'
        SELECT *
        FROM [dbo].[tblTransaction] AS T
    WHERE T.EmployeeNumber = @EmployeeNumber;',
    @params = N'@EmployeeNumber varchar(1000)',
    @EmployeeNumber = @param;

