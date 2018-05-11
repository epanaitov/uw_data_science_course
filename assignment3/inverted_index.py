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
	key = record[0]
	value = record[1]
	words = value.split()
	for w in words:
		mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence counts
	ids_list = Set([])
	for v in list_of_values:
		ids_list.add(v)
	mr.emit((key, list(ids_list)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
