alter table tblTransaction
add constraint chkAmount check (Amount>-1000 and Amount < 1000)

insert into tblTransaction
values (1010, '2014-01-01', 1)

alter table tblEmployee with nocheck
add constraint chkMiddleName check
(REPLACE(EmployeeMiddleName,'.','') = EmployeeMiddleName or EmployeeMiddleName is null)

alter table tblEmployee
drop constraint chkMiddleName

begin tran
  insert into tblEmployee
  values (2003, 'A', 'B.', 'C', 'D', '2014-01-01', 'Accounts')
  select * from tblEmployee where EmployeeNumber = 2003
rollback tran

alter table tblEmployee with nocheck
add constraint chkDateOfBirth check (DateOfBirth between '1900-01-01' and getdate())

begin tran
  insert into tblEmployee
  values (2003, 'A', 'B', 'C', 'D', '2115-01-01', 'Accounts')
  select * from tblEmployee where EmployeeNumber = 2003
rollback tran

create table tblEmployee2
(EmployeeMiddleName varchar(50) null, constraint CK_EmployeeMiddleName check
(REPLACE(EmployeeMiddleName,'.','') = EmployeeMiddleName or EmployeeMiddleName is null))

drop table tblEmployee2

alter table tblEmployee
drop chkDateOfBirth
alter table tblEmployee
drop chkMiddleName
alter table tblTransaction
drop chkAmount
