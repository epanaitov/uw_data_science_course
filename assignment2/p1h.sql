drop table similarity;
create table similarity as select f1.docid as row, f2.docid as col, sum(f1.count * f2.count) as val
    from frequency f1, frequency f2 where (f1.term = f2.term) and (f1.docid = '10080_txt_crude')
    group by f1.docid, f2.docid;

select val from similarity where row = '10080_txt_crude' and col = '17035_txt_earn';
