select * 
from tblTransaction as T
Where EmployeeNumber in
    (Select EmployeeNumber from tblEmployee where EmployeeLastName not like 'y%')
order by EmployeeNumber -- must be in tblEmployee AND tblTransaction, and not 126-129
                        -- INNER JOIN

select * 
from tblTransaction as T
Where EmployeeNumber not in
    (Select EmployeeNumber from tblEmployee where EmployeeLastName like 'y%')
order by EmployeeNumber -- must be in tblTransaction, and not 126-129
                        -- LEFT JOIN
