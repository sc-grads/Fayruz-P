--Question 1

select [name] + 'A'
from sys.all_columns

--Question 2

select [name] + N'Ⱥ'
from sys.all_columns

--Question 3

select substring([name],2,len([name])-1) as [name]
from sys.all_columns

--Question 4

select substring([name],1,len([name])-1) as [name]
from sys.all_columns