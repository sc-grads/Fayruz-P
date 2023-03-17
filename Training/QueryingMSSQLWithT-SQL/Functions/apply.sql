SELECT * 
from dbo.TransList(123)
GO

select *, (select count(*) from dbo.TransList(E.EmployeeNumber)) as NumTransactions
from tblEmployee as E

select *
from tblEmployee as E
outer apply TransList(E.EmployeeNumber) as T

select *
from tblEmployee as E
cross apply TransList(E.EmployeeNumber) as T

--123 left join TransList(123)
--124 left join TransList(124)

--outer apply all of tblEmployee, UDF 0+ rows
--cross apply UDF 1+ rows

--outer apply = LEFT JOIN
--cross apply = INNER JOIN

select *
from tblEmployee as E
where  (select count(*) from dbo.TransList(E.EmployeeNumber)) >3
