create synonym EmployeeTable
for tblEmployee
go

select * from EmployeeTable

create synonym DateTable
for tblDate
go

select * from DateTable

create synonym RemoteTable
for OVERTHERE.70-461remote.dbo.tblRemote
go

select * from RemoteTable
