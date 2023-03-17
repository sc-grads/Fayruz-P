select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
first_value(NumberAttendance)
over(partition by E.EmployeeNumber order by A.AttendanceMonth) as FirstMonth,
last_value(NumberAttendance)
over(partition by E.EmployeeNumber order by A.AttendanceMonth
rows between unbounded preceding and unbounded following) as LastMonth
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber
