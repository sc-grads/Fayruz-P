select * from tblEmployee
where [EmployeeLastName] <> 'Word'

select * from tblEmployee
where [EmployeeLastName] like '_W%'

Select * from tblEmployee
where [EmployeeLastName] like '[r-t]%'

Select * from tblEmployee
where [EmployeeLastName] like '[^rst]%'

-- % = 0-infinity characters
-- _ = 1 character
-- [A-G] = In the range A-G.
-- [AGQ] = A, G or Q.
-- [^AGQ] = NOT A, G or Q.

select * from tblEmployee
where EmployeeLastName like '[%]%'

select * from tblEmployee
where EmployeeLastName like '`%%' ESCAPE '`'
