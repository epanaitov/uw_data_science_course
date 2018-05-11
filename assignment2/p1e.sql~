select count(*) from (
	select sum(count) as totals from frequency group by docid having totals > 300
);
