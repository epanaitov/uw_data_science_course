import sys
import json
from types import NoneType
import re

def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))

def dictionary(afinnfile):
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")
		scores[term] = int(score)
	
	return scores

def extract_location(tweet):
	
	if 'place' in tweet:
		if type(tweet['place']) != NoneType:
			if 'full_name' in tweet['place']:
				return tweet['place']['full_name']
		
	if 'user' in tweet:
			return tweet['user']['location']
		
	return ''
	
def extract_state(text, states):
	state = ''
	
	for word in states:
		if ' ' in word:
			if text.lower().find(word) > -1:
				state = states[word]
				
	if len(state) == 0:
		for chunk in re.findall(r"[\w'#@]+", text):
			for word in states:
				if ' ' not in word:
					if chunk.lower() == word:
						return states[word]
					
					if chunk.lower() == '#' + word:
						return states[word]
					
					if chunk.lower() == '@' + word:
						return states[word]
					
	return ''
			

def sentiment(text, d):
	
	sum = 0
	
	for chunk in re.findall(r"[\w'#@]+", text):
		if chunk in d:
			sum = sum + d[chunk]
	
	return sum

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	
	d = dictionary(sent_file)
	
	states = {
				'alabama':'AL',
				'alaska':'AK',
				'arizona':'AZ',
				'az':'AZ',
				'arkansas':'AR',
				'ar':'AR',
				'california':'CA', 
				'ca':'CA',
				'sf':'CA',
				'san francisco': 'CA',
				'los angeles': 'CA',
				'san diego': 'CA',
				'colorado':'CO',
				'Connecticut':'CT',
				'ct':'CT',
				'delaware':'DE',
				'florida':'FL',
				'georgia':'GA',
				'hawai':'HI',
				'idaho':'ID',
				'illinois':'IL',
				'il':'IL',
				'indiana':'IN',
				'iowa':'IA',
				'kansas':'KS',
				'ks':'KS',
				'kentucky':'KY',
				'ky':'KY',
				'louisiana':'LA',
				'maine':'ME',
				'maryland':'MD',
				'massachusetts':'MA',
				'ma':'MA',
				'boston':'MA',
				'michigan':'MI',
				'minnesota':'MN',
				'mississippi':'MS',
				'missouri':'MO',
				'montana':'MT',
				'nebraska':'NE',
				'nevada':'NV',
				'new hampshire':'NH',
				'nh': 'NH',
				'new jersey':'NJ',
				'nj':'NJ',
				'new mexico':'NM',
				'new york': 'NY',
				'ny': 'NY',
				'nyc': 'NY',
				'north carolina':'NC',
				'nc':'NC',
				'north dakota':'ND',
				'ohio':'OH',
				'oklahoma': 'OK',
				'oregon': 'OR',
				'pennsylvania':'PA',
				'rhode island':'RI',
				'ri':'RI',
				'south carolina':'SC',
				'sc': 'SC',
				'south dakota': 'SD',
				'tennessee': 'TN',
				'texas': 'TX',
				'tx': 'TX',
				'utah': 'UT',
				'vermont': 'VT',
				'virginia': 'VA',
				'seattle': 'WA',
				'washington': 'WA',
				'west virginia': 'WV',
				'wisconsin': 'WI',
				'wyoming': 'WY'
			}
	
	happiness = {} 
	
	for line in tweet_file:
		tweet = json.loads(line)
		
		if 'text' not in tweet:
			continue
		
		text = tweet['text']
		
		location = extract_location(tweet)
		state = extract_state(location, states)
		
		if len(state) == 0:
			state = extract_state(text, states)
		
		if len(state) == 0:
			continue
		
		sent = sentiment(text, d)
		
		if state in happiness:
			sent = sent + happiness[state]
		
		happiness[state] = sent
			
	max = 0
	happiest_state = ''
	for state in happiness:
		if happiness[state] > max:
			max = happiness[state]
			happiest_state = state
			
	print happiest_state
			
			
if __name__ == '__main__':
	main()
