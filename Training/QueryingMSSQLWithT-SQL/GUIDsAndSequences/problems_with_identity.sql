begin tran
insert into tblEmployee2
values ('New Name')
select * from tblEmployee2
rollback tran

truncate table tblEmployee2
