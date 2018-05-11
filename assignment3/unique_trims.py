import MapReduce
import sys

from sets import Set

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# create table C as select A.row_num as row, B.col_num as col, sum(A.value * B.value) as val
#     from A, B where A.col_num = B.row_num
#     group by A.row_num, B.col_num;


def mapper(record):
	# key: document identifier
	# value: document contents
	
	(matrix, col, row, val) = record
	mr.emit_intermediate((row, col), (matrix, val))

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence counts
	mr.emit(key)
		
	

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
