select A.EmployeeNumber, A.AttendanceMonth, A.NumberAttendance
,sum(A.NumberAttendance) over() as TotalAttendance
--,convert(decimal(18,7),A.NumberAttendance) / sum(A.NumberAttendance) over() * 100.0000 as PercentageAttendance
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

select sum(NumberAttendance) from tblAttendance

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
sum(A.NumberAttendance) 
over(PARTITION BY E.EmployeeNumber, year(A.AttendanceMonth)
     ORDER BY A.AttendanceMonth) as SumAttendance
from tblEmployee as E join (select * from tblAttendance UNION ALL Select * from tblAttendance) as A
on E.EmployeeNumber = A.EmployeeNumber
order by A.EmployeeNumber, A.AttendanceMonth

--range between unbounded preceding and unbounded following - DEFAULT where there is no ORDER BY
--range between unbounded preceding and current row         - DEFAULT where there IS an ORDER BY
