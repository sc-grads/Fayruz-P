drop table #tblXML
go
create table #tblXML(XmlCol xml)
go
bulk insert #tblXML from 'C:\XML\SampleDataBulkInsert.txt'
select * from #tblXML

drop table #tblXML
go
create table #tblXML(IntCol int, XmlCol xml)
go
insert into #tblXML(XmlCol)
select * from
openrowset(BULK 'C:\XML\SampleDataOpenRowset.txt', SINGLE_BLOB) AS x
select * from #tblXML
