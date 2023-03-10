/*-----------------------
CREATE EMPTY AdventureWorks2016_RestoreTest
-----------------------*/

USE [master]
GO
CREATE DATABASE [AdventureWorks2016_RestoreTest]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'AdventureWorks2016_RestoreTest_Data', FILENAME = N'C:\SQL_DATA_FILES\AdventureWorks2016_RestoreTest_Data.mdf' , SIZE = 228992KB , MAXSIZE = UNLIMITED, FILEGROWTH = 16384KB )
 LOG ON 
( NAME = N'AdventureWorks2016_RestoreTest_Log', FILENAME = N'C:\SQL_LOG_FILES\AdventureWorks2016_RestoreTest_Log.ldf' , SIZE = 18432KB , MAXSIZE = 2048GB , FILEGROWTH = 16384KB )
GO

ALTER DATABASE [AdventureWorks2016_RestoreTest] SET  READ_WRITE 
GO


/*-----------------------
BACKUP AdventureWorks2016 DATABASE
-----------------------*/

BACKUP DATABASE [AdventureWorks2016] TO  DISK = N'C:\SQL_BACKUPS\adventureworks2016_for_restore.bak' WITH NOFORMAT, NOINIT,  
NAME = N'AdventureWorks2016-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO


/*-----------------------
RESTORE AdventureWorks2016 AS AdventureWorks2016_RestoreTes DATABASE
-----------------------*/

BACKUP DATABASE [AdventureWorks2016_RestoreTest] TO  DISK = N'C:\SQL_BACKUPS\AdventureWorks2016_RestoreTest.bak' WITH NOFORMAT, NOINIT,  
NAME = N'AdventureWorks2016-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO





