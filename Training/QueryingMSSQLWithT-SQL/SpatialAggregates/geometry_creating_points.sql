BEGIN TRAN
CREATE TABLE tblGeom
(GXY geometry,
Description varchar(30),
IDtblGeom int CONSTRAINT PK_tblGeom PRIMARY KEY IDENTITY(1,1))
INSERT INTO tblGeom
VALUES (geometry::STGeomFromText('POINT (3 4)', 0),'First point'),
       (geometry::STGeomFromText('POINT (3 5)', 0),'Second point'),
	   (geometry::Point(4, 6, 0),'Third Point'),
	   (geometry::STGeomFromText('MULTIPOINT ((1 2), (2 3), (3 4))', 0), 'Three Points')

Select * from tblGeom

ROLLBACK TRAN
