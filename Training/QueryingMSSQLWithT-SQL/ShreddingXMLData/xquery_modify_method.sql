set @x.modify('replace value of (/Shopping/ShoppingTrip[1]/Item[3]/@Cost)[1]
                  with "6.0"')
select @x
set @x.modify('insert <Item Cost="5">New Food</Item>
			   into (/Shopping/ShoppingTrip)[2]')
select @x
