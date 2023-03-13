declare @firstname as nvarchar(20)
declare @middlename as nvarchar(20)
declare @lastname as nvarchar(20)

set @firstname = 'Sarah'
--set @middlename = 'Jane'
set @lastname = 'Milligan'

-- select @firstname + ' ' + @middlename + ' ' + @lastname as FullName
select @firstname + iif(@middlename is null, '', ' ' + @middlename) + ' ' + @lastname as FullName
select @firstname + CASE WHEN @middlename IS NULL THEN '' ELSE ' ' + @middlename END + ' ' + @lastname as FullName
select @firstname + coalesce(' ' + @middlename,'') + ' ' + @lastname as FullName
SELECT CONCAT(@firstname,' ' + @middlename, ' ' , @lastname) as FullName
