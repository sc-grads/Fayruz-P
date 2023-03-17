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
	   (geometry::STGeomFromText('POLYGON ((5 2, 7 2, 7 4, 5 4, 5 2))', 0), 'Second Polygon'),
	   (geometry::STGeomFromText('CIRCULARSTRING (1 0, 0 1, -1 0, 0 -1, 1 0)', 0), 'Circle')
select * from tblGeom

SELECT *  FROM tblGeom
where GXY.Filter(geometry::Parse('POLYGON((2 1, 1 4, 4 4, 4 1, 2 1))')) = 1
UNION ALL
SELECT geometry::STGeomFromText('POLYGON((2 1, 1 4, 4 4, 4 1, 2 1))', 0), 'Filter', 0

declare @i as geometry
select @i = geometry::UnionAggregate(GXY) 
from tblGeom

Select @i as CombinedShapes

declare @j as geometry
select @j = geometry::CollectionAggregate(GXY) 
from tblGeom

select @j

Select @i as CombinedShapes
--union all
select geometry::EnvelopeAggregate(GXY) as Envelope from tblGeom
--union all
select geometry::ConvexHullAggregate(GXY) as Envelope from tblGeom

ROLLBACK TRAN





