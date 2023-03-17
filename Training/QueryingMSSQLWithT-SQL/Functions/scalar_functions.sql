CREATE FUNCTION AmountPlusOne(@Amount smallmoney)
RETURNS smallmoney
AS
BEGIN

    RETURN @Amount + 1

END
GO


select DateOfTransaction, EmployeeNumber, Amount, dbo.AmountPlusOne(Amount) as AmountAndOne
from tblTransaction

DECLARE @myValue smallmoney
EXEC @myValue = dbo.AmountPlusOne @Amount = 345.67
select @myValue
