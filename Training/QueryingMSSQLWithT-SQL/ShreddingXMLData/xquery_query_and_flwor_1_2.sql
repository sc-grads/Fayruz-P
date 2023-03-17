--XQuery Query and FLWOR 1
select @x.query('for $ValueRetrieved in /Shopping/ShoppingTrip/Item
                 return $ValueRetrieved')
select @x.query('for $ValueRetrieved in /Shopping/ShoppingTrip/Item
                 return string($ValueRetrieved)')
select @x.query('for $ValueRetrieved in /Shopping/ShoppingTrip[1]/Item
                 return concat(string($ValueRetrieved),";")')
--XQuery Query and FLWOR 2
select @x.query('for $ValueRetrieved in /Shopping/ShoppingTrip[1]/Item
                 let $CostVariable := $ValueRetrieved/@Cost
                 where $CostVariable >= 4
                 order by $CostVariable
                 return concat(string($ValueRetrieved),";")')
