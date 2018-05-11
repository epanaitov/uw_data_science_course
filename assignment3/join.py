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
	key = record[1]
	for field in record:
		mr.emit_intermediate(key, field)

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence counts
	vals_list = []
	order_list = []
	for v in list_of_values:
		if v == 'order':
			order_list = []
		if v == 'line_item':
			if len(order_list) == 0:
				order_list = vals_list
			else:
				mr.emit(order_list + vals_list)
			vals_list = []	 
			
		vals_list.append(v)
		
	mr.emit(order_list + vals_list)
		
	

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
