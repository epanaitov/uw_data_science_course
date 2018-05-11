import sys
import json
import operator

def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))


def main():
	tweet_file = open(sys.argv[1])
	
	tags = {}
	
	for line in tweet_file:
		tweet = json.loads(line)
		
		if 'entities' in tweet:
			entities = tweet['entities']
			if 'hashtags' in entities:
				hashtags = entities['hashtags']
				for tag in hashtags:
					tag_text = tag['text']
					count = 1.0
					if tag_text in tags:
						count = count + tags[tag_text]
					tags[tag_text] = count
					
	sorted_tags = sorted(tags.iteritems(), key=operator.itemgetter(1), reverse=True)
	
	for tag in sorted_tags[:10]:
		print tag[0], " ", tag[1]
			
if __name__ == '__main__':
	main()
