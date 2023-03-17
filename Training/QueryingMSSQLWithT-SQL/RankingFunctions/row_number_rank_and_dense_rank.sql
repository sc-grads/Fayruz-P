
select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
ROW_NUMBER() OVER(ORDER BY E.EmployeeNumber, A.AttendanceMonth) as TheRowNumber,
RANK() OVER(ORDER BY E.EmployeeNumber, A.AttendanceMonth) as TheRank,
DENSE_RANK() OVER(ORDER BY E.EmployeeNumber, A.AttendanceMonth) as TheDenseRank
from tblEmployee as E join 
(Select * from tblAttendance union all select * from tblAttendance) as A
on E.EmployeeNumber = A.EmployeeNumber

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
ROW_NUMBER() OVER(PARTITION BY E.EmployeeNumber
                  ORDER BY A.AttendanceMonth) as TheRowNumber,
RANK()       OVER(PARTITION BY E.EmployeeNumber
                  ORDER BY A.AttendanceMonth) as TheRank,
DENSE_RANK() OVER(PARTITION BY E.EmployeeNumber
                  ORDER BY A.AttendanceMonth) as TheDenseRank
from tblEmployee as E join 
(Select * from tblAttendance union all select * from tblAttendance) as A
on E.EmployeeNumber = A.EmployeeNumber

select *, row_number() over(order by (select null)) from tblAttendance
