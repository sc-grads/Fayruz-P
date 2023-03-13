declare @myvar as int

select 1+1+1+1+1+@myvar+1+1 as myCol

declare @mystring as nvarchar(20)
select datalength(@mystring) as mystring

declare @mydecimal decimal(5,2)
select try_convert(decimal(5,2),1000)
select try_cast(1000 as decimal(5,2))
