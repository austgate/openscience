import json, glob

from collections import Counter

class DataLayer():
    
    def network(self):
        
        nodes = []
        links = []
        listing = Counter()
        files = glob.glob('data/*.txt')
        if files is None:
            print "failed to find any files"

        for filez in files:
            data = json.loads(open(filez, 'r').read())
            for result in data['results']:
                listing[result['from_user']] += 1   
        
        num_tweets=0
        nodes.append({ 'name': 'Weird Council', 'group':0})
        for k,v in listing.iteritems():
            num_tweets += 1
            nodes.append({ 'name':k, 'group':0})
            links.append({ "source": 0,"target": num_tweets,"value": v})
            
        return json.dumps({'nodes':nodes, 'links':links})