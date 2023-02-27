USE [OurFirstDatabase]
GO

INSERT INTO [dbo].[personalInfo]
           ([firstName]
           ,[lastName]
           ,[dob]
           ,[id])
     VALUES
           ('Abbas'
           ,'Mehmood'
           ,'01/01/2020'
           ,777)
GO


select * from personalInfo