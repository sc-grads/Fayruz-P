select E.EmployeeNumber as ENumber, E.EmployeeFirstName,
       E.EmployeeLastName, T.EmployeeNumber as TNumber, 
       sum(T.Amount) as TotalAmount
from tblEmployee as E
left join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
where T.EmployeeNumber IS NULL
group by E.EmployeeNumber, T.EmployeeNumber, E.EmployeeFirstName,
       E.EmployeeLastName
order by E.EmployeeNumber, T.EmployeeNumber, E.EmployeeFirstName,
       E.EmployeeLastName
-- derived table

select ENumber, EmployeeFirstName, EmployeeLastName
from (
select E.EmployeeNumber as ENumber, E.EmployeeFirstName,
       E.EmployeeLastName, T.EmployeeNumber as TNumber, 
       sum(T.Amount) as TotalAmount
from tblEmployee as E
left join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
group by E.EmployeeNumber, T.EmployeeNumber, E.EmployeeFirstName,
       E.EmployeeLastName) as newTable
where TNumber is null
order by ENumber, TNumber, EmployeeFirstName,
       EmployeeLastName
-- RIGHT JOIN

select *
from (
select E.EmployeeNumber as ENumber, E.EmployeeFirstName,
       E.EmployeeLastName, T.EmployeeNumber as TNumber, 
       sum(T.Amount) as TotalAmount
from tblEmployee as E
right join tblTransaction as T
on E.EmployeeNumber = T.EmployeeNumber
group by E.EmployeeNumber, T.EmployeeNumber, E.EmployeeFirstName,
       E.EmployeeLastName) as newTable
where ENumber is null
order by ENumber, TNumber, EmployeeFirstName,
       EmployeeLastName
