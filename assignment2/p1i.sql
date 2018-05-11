drop table if exists search_freq;
create table search_freq as 
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
;

drop table if exists similarity;
create table similarity as select f1.docid as row, f2.docid as col, sum(f1.count * f2.count) as val
    from search_freq f1, search_freq f2 where (f1.term = f2.term) and (f1.docid < f2.docid)
    group by f1.docid, f2.docid;

select * from similarity where row = 'q' or col = 'q' order by val desc limit 10;
