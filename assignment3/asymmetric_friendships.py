import MapReduce
import sys

from sets import Set

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# key: document identifier
	# value: document contents
	f1 = record[0]
	f2 = record[1]
	
	mr.emit_intermediate((f1, f2), (f1, f2))
	mr.emit_intermediate((f2, f1), (f1, f2))

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence counts
	if (len(list_of_values) == 1):
		mr.emit(key)
		
	

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
