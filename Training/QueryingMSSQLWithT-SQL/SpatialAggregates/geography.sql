begin tran
create table tblGeog
(GXY geography,
Description varchar(30),
IDtblGeog int CONSTRAINT PK_tblGeog PRIMARY KEY IDENTITY(1,1))
insert into tblGeog
VALUES (geography::STGeomFromText('POINT (-73.993492 40.750525)', 4326),'Madison Square Gardens, NY'),
       (geography::STGeomFromText('POINT (-0.177452 51.500905)', 4326),'Royal Albert Hall, London'),
	   (geography::STGeomFromText('LINESTRING (-73.993492 40.750525, -0.177452 51.500905)', 4326),'Connection')

select * from tblGeog

DECLARE @g as geography
select @g = GXY from tblGeog where IDtblGeog = 1

select IDtblGeog, GXY.STGeometryType() as MyType
, GXY.STStartPoint().ToString() as StartingPoint
, GXY.STEndPoint().ToString() as EndingPoint
, GXY.STPointN(1).ToString() as FirstPoint
, GXY.STPointN(2).ToString() as SecondPoint
, GXY.STLength() as MyLength
, GXY.STIntersection(@g).ToString() as Intersection
, GXY.STNumPoints() as NumberPoints
, GXY.STDistance(@g) as DistanceFromFirstLine
from tblGeog

DECLARE @h as geography

select @g = GXY from tblGeog where IDtblGeog = 1
select @h = GXY from tblGeog where IDtblGeog = 2
select @g.STDistance(@h) as MyDistance

select GXY.STUnion(@g)
from tblGeog
where IDtblGeog = 2 

ROLLBACK TRAN

select * from sys.spatial_reference_systems
