dm_db_index_usage_stats
select db_name(database_id) as [Database Name]
, object_name(ddius.object_id) as [Table Name]
, i.name as [Index Name]
, ddius.*
from sys.dm_db_index_usage_stats as ddius
join sys.indexes as i on ddius.object_id = i.object_id and ddius.index_id = i.index_id
where database_id = db_id()
sys.dm_db_missing_index_details
select T.*
into dbo.tblTransactionBigger
from [dbo].[tblTransaction] as T
cross join [dbo].[tblTransaction] as T2

select * from dbo.tblTransactionBigger
where [EmployeeNumber] = 127

select * from sys.dm_db_missing_index_details

select mig.*, statement as table_name, column_id, column_name, column_usage
from sys.dm_db_missing_index_details as mid
cross apply sys.dm_db_missing_index_columns(mid.index_handle)
inner join sys.dm_db_missing_index_groups as mig on mig.index_handle = mid.index_handle
where database_id = db_id()
order by column_id

drop table dbo.tblTransactionBigger
sys.dm_db_index_physical_stats
SELECT * FROM sys.dm_db_index_physical_stats  
    (DB_ID(N'70-461'), OBJECT_ID(N'dbo.tblEmployee'), NULL, NULL , 'DETAILED');  
     database_id       object_id                     index_id/partition_number/mode

