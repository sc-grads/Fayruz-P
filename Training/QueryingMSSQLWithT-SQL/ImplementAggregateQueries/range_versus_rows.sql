select A.EmployeeNumber, A.AttendanceMonth, A.NumberAttendance
,sum(A.NumberAttendance) 
over(partition by A.EmployeeNumber, year(A.AttendanceMonth) 
     order by A.AttendanceMonth 
	 rows between current row and unbounded following) as RowsTotal
,sum(A.NumberAttendance) 
over(partition by A.EmployeeNumber, year(A.AttendanceMonth) 
     order by A.AttendanceMonth 
	 range between current row and unbounded following) as RangeTotal
from tblEmployee as E join (select * from tblAttendance UNION ALL select * from tblAttendance) as A
on E.EmployeeNumber = A.EmployeeNumber
--where A.AttendanceMonth < '20150101'
order by A.EmployeeNumber, A.AttendanceMonth

--unbounded preceding and current row
--current row and unbounded following
--unbounded preceding and unbounded following - RANGE and ROWS
