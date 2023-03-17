declare @x1 xml, @x2 xml 
set @x1='<Shopping ShopperName="Phillip Burton" >  
<ShoppingTrip ShoppingTripID="L1" >  
  <Item Cost="5">Bananas</Item>  
  <Item Cost="4">Apples</Item>  
  <Item Cost="3">Cherries</Item>
</ShoppingTrip></Shopping>'
set @x2='<Shopping ShopperName="Phillip Burton" >
<ShoppingTrip ShoppingTripID="L2" >  
  <Item>Emeralds</Item>  
  <Item>Diamonds</Item>  
  <Item>Furniture
        <Color></Color></Item>  
</ShoppingTrip>  
</Shopping>'  

drop table #tblXML;
create table #tblXML(pkXML INT PRIMARY KEY, xmlCol XML)

insert into #tblXML(pkXML, xmlCol) VALUES (1, @x1)
insert into #tblXML(pkXML, xmlCol) VALUES (2, @x2)

create primary xml index pk_tblXML on #tblXML(xmlCol)
create xml index secpk_tblXML_Path on #tblXML(xmlCol)
       using xml index pk_tblXML FOR PATH
create xml index secpk_tblXML_Value on #tblXML(xmlCol)
       using xml index pk_tblXML FOR VALUE
create xml index secpk_tblXML_Property on #tblXML(xmlCol)
       using xml index pk_tblXML FOR PROPERTY
