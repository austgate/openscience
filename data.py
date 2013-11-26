import json, glob, re
from sets import Set

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
            nodes.append({ 'name':k, 'group':num_tweets, "value": v})
            links.append({ "source": 0,"target": num_tweets,"value": v})
            
        return json.dumps({'nodes':nodes, 'links':links})
    
    def count_words(self):
        
        stopwords = Set(['a', 'an', 'the', 'they', 'he', 'she', 'it'])
        
        listing = Counter()
        files = glob.glob('data/*.txt')
        if files is None:
            print "failed to find any files"

        for filez in files:
            data = json.loads(open(filez, 'r').read())
            for result in data['results']:
                for d in result['text'].split():
                    if d not in stopwords and d[:1] is not "@":
                        listing[self.clean_punc(d)] += 1  
        wordfreq = sorted(listing.items())
        return wordfreq
    
    def books(self):
        
        nodes = []
        links = []
        novels = Counter()
        files = glob.glob('data/*.txt')
        if files is None:
            print "failed to find any files"

        for filez in files:
            data = json.loads(open(filez, 'r').read())
            for result in data['results']:
                book = self._getnovels(result['text'])
                if book:
                    novels[self._converttitle(book.group().strip())] += 1  

        num_tweets=0
        nodes.append({ 'name': 'Weird Council', 'group':0})
        for k,v in novels.iteritems():
            num_tweets += 1
            nodes.append({ 'name':k, 'group':num_tweets, "value": (v * 5)})
            links.append({ "source": 0,"target": 0,"value": v})
            
        return json.dumps({'nodes':nodes, 'links':links})
    
    def _getnovels(self, tweet):
        match = re.search("(pss | perdido | perdido street station | iron | iron council | scar | jake | king | king rat | the city | railsea | embassytown)", tweet, re.M|re.I)
        if match:
            return match
        
    def _converttitle(self, title):
        
        if title == "Perdido" or title == "PSS":
            return "Perdido Street Station"
        elif title == "Iron":
            return "The Iron Council"
        elif title == "Scar":
            return "The Scar"     
        elif title == "Jake":
            return "Looking for Jake" 
        elif title == "King":
            return "King Rat"
        elif title == "City":
            return "The City and the City"
        elif title == "the City":
            return "The City and the City"
        elif title == "EMBASSYTOWN":
            return "Embassytown"
        elif title == "RAILSEA":
            return "Railsea"
        else:
            return title

    def clean_punc(self, word):
        
        return word.strip("!").strip(",").strip(":").strip(".").strip('"').strip("@").strip('#').strip('(').strip(")").strip("+").strip("*")