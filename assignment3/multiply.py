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
	
	key = ''
	
	for i in range(0, 5):
		if (matrix == 'a'): 
			key = (col, i)
		else:
			key = (i, row)
		
		mr.emit_intermediate(key, (matrix, col, row, val))
		

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence counts
	
	#filter in two lists:
	
	mul = 0
	
	for row1 in list_of_values:
		(matrix1, col1, row1, val1) = row1
		if (matrix1 == 'a'):
			for row2 in list_of_values:
				(matrix2, col2, row2, val2) = row2
				if (matrix2 == 'b'):
					if (row1 == col2):
						mul = mul + val1*val2
						
	mr.emit((key[0], key[1], mul))
	

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
