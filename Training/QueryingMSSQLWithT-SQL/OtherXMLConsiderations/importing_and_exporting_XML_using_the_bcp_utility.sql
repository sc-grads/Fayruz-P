
bcp [70-461S5].dbo.tblDepartment out mydata.out -N -T
create table dbo.tblDepartment2
([Department] varchar(19) null,
[DepartmentHead] varchar(19) null)
bcp [70-461S5].dbo.tblDepartment2 in mydata.out -N –T
