
-- To insert data into the 'Students' table
-- Student ID, Student Name, Class, Age, Height

/*
INSERT INTO STUDENTS values (
'10002', 'Michael', 'Arts', '15', '5.7'
);
*/

-- To View all content of the table using the wildcard '*'
SELECT * From [DBA].[dbo].[Students]

-- To view specific content of the table using the headings
-- Views the column header with an alias
-- SELECT [Student ID] as [ID] From [DBA].[dbo].[Students]

-- To update given data into the table
-- UPDATE 'table name' set 'Column heading' where 'preferrably the student ID because it's a unique value for all members of the table' 

-- UPDATE [DBA].[dbo].[Students] set [Student Name] = 'David', [Age] = 18, [Class] = 'Commercial' where [Student ID] = '10000'


-- To delete from the table
-- DELETE from 'table name' where 'student ID = the person's data to be deleted'

--DELETE From [DBA].[dbo].[Students] where [Student ID] = '10002'

SELECT @@servername
