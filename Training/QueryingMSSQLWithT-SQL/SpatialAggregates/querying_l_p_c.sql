begin tran
create table tblGeom
(GXY geometry,
Description varchar(20),
IDtblGeom int CONSTRAINT PK_tblGeom PRIMARY KEY IDENTITY(5,1))
insert into tblGeom
VALUES (geometry::STGeomFromText('LINESTRING (1 1, 5 5)', 0),'First line'),
       (geometry::STGeomFromText('LINESTRING (5 1, 1 4, 2 5, 5 1)', 0),'Second line'),
	   (geometry::STGeomFromText('MULTILINESTRING ((1 5, 2 6), (1 4, 2 5))', 0),'Third line'),
	   (geometry::STGeomFromText('POLYGON ((4 1, 6 3, 8 3, 6 1, 4 1))', 0), 'Polygon'),
	   (geometry::STGeomFromText('CIRCULARSTRING (1 0, 0 1, -1 0, 0 -1, 1 0)', 0), 'Circle')
SELECT * FROM tblGeom



select IDtblGeom, GXY.STGeometryType() as MyType
, GXY.STStartPoint().ToString() as StartingPoint
, GXY.STEndPoint().ToString() as EndingPoint
, GXY.STPointN(1).ToString() as FirstPoint
, GXY.STPointN(2).ToString() as SecondPoint
, GXY.STPointN(1).STX as FirstPointX
, GXY.STPointN(1).STY as FirstPointY
, GXY.STBoundary().ToString() as Boundary
, GXY.STLength() as MyLength
, GXY.STNumPoints() as NumberPoints
from tblGeom

DECLARE @g as geometry
select @g = GXY from tblGeom where IDtblGeom = 5

select IDtblGeom, GXY.STIntersection(@g).ToString() as Intersection
, GXY.STDistance(@g) as DistanceFromFirstLine
from tblGeom

select GXY.STUnion(@g), Description
from tblGeom
where IDtblGeom = 8 

rollback tran

