--Clustered Index
create clustered index idx_tblEmployee on [dbo].[tblEmployee]([EmployeeNumber])

drop index idx_tblEmployee on [dbo].[tblEmployee]

select * from [dbo].[tblEmployee2] where [EmployeeNumber] = 127
select * from [dbo].[tblEmployee2]

select *
into [dbo].[tblEmployee2]
from [dbo].[tblEmployee]
where EmployeeNumber <> 131

--seek = few number of rows based on the index
--scan = going through the entire table

alter table [dbo].[tblEmployee2]
add constraint pk_tblEmployee2 PRIMARY KEY(EmployeeNumber)

create table myTable (Field1 int primary key)
--Non-clustered Index
create nonclustered index idx_tblEmployee_DateOfBirth on [dbo].[tblEmployee]([DateOfBirth])
create nonclustered index idx_tblEmployee_DateOfBirth_Department on [dbo].[tblEmployee]([DateOfBirth],Department)

drop index idx_tblEmployee on [dbo].[tblEmployee]

select * from [dbo].[tblEmployee2] where [EmployeeNumber] = 127
select * from [dbo].[tblEmployee2]

select DateOfBirth, Department
from [dbo].[tblEmployee]
where DateOfBirth>='1992-01-01' and DateOfBirth<'1993-01-01'

--seek = few number of rows based on the index
--scan = going through the entire table

alter table [dbo].[tblDepartment]
add constraint unq_tblDepartment UNIQUE(Department)
Filtered indices


CREATE NONCLUSTERED INDEX idx_tblEmployee_Employee  
    ON dbo.tblEmployee(EmployeeNumber) where EmployeeNumber<139;
INCLUDE
CREATE NONCLUSTERED INDEX idx_tblEmployee_Employee  
    ON dbo.tblEmployee(EmployeeNumber) include (EmployeeFirstName);

DROP INDEX idx_tblEmployee_Employee ON dbo.tblEmployee
