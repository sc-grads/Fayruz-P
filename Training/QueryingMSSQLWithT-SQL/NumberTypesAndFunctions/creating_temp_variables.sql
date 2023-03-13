-- Creating temporary variables
-- Initialise a variable, give it a data type and an initial value
DECLARE @myvar as int = 2
-- Increase that value by 1
SET @myvar = @myvar + 1
-- Retrieve that value
SELECT @myvar AS myVariable
