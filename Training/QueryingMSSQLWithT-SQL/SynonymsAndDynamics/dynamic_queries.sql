select * from tblEmployee where EmployeeNumber = 129;
go
declare @command as varchar(255);
set @command = 'select * from tblEmployee where EmployeeNumber = 129;'
set @command = 'Select * from tblTransaction'
execute (@command);
go
declare @command as varchar(255), @param as varchar(50);
set @command = 'select * from tblEmployee where EmployeeNumber = '
set @param ='129'
execute (@command + @param); --sql injection potential
go
declare @command as nvarchar(255), @param as nvarchar(50);
set @command = N'select * from tblEmployee where EmployeeNumber = @ProductID'
set @param =N'129'
execute sys.sp_executesql @statement = @command, @params = N'@ProductID int', @ProductID = @param;
