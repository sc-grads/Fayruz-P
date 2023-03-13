--Initialise a variable, give it a data type and an initial value

DECLARE @myvar as numeric(7,2) = 3

SELECT POWER(@myvar,3) -- 27
SELECT SQUARE(@myvar) -- 9
SELECT POWER(@myvar,0.5) -- square root of 3
SELECT SQRT(@myvar) -- square root of 3

GO

DECLARE @myvar as numeric(7,2) = 12.345

SELECT FLOOR(@myvar) -- this equals 12
SELECT CEILING(@myvar) -- this equals 13
SELECT ROUND(@myvar,-1) as myRound -- this equals 10

GO

SELECT PI() as myPI
SELECT EXP(1) as e

DECLARE @myvar AS NUMERIC(7,2) = -456

SELECT ABS(@myvar) as myABS, SIGN(@myvar) as mySign -- This equals 456 and -1.

GO

SELECT RAND(345) -- A random number, based on the initial seed

