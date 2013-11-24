import json, glob, re

from collections import Counter


class Parsing():
    
    def index_data(self):
        listing = Counter()
        
        files = glob.glob('data/*.txt')
        if files is None:
            print "failed to find any files"

        for filez in files:
            data = json.loads(open(filez, 'r').read())
            for result in data['results']:
                listing[result['from_user']] += 1

        return listing    
    
    def tweeter_data(self, author):

        novels = {}
        books = []
        recipients = set()
        user = ""
        user_name = ""
        files = glob.glob('data/*.txt')
        if files is None:
            print "failed to find any files"

        for filez in files:
            data = json.loads(open(filez, 'r').read()) 
            for result in data['results']:
                if result['from_user'] == author:
                    user = result['from_user']
                    user_name = result['from_user_name']
                    book = self._getnovels(result['text'])
                    if book:
                        recipient = self._getrecipient(result['text'])
                        if recipient:
                            b =  self._converttitle(book.group().strip())
                            novels = {'id' : result['id'], 'book' : b, 'recipient' : recipient.group()[1:]}
                            
                        else:
                            b =  self._converttitle(book.group().strip())
                            novels = {'id' : result['id'], 'book' : b}
                        books.append(novels)
                        
                    recipient = self._getrecipient(result['text'])
                    if recipient:
                        recipients.add(recipient.group()[1:])
                    

        listing = {
            'user_name' : user,
             'name' : user_name,
             'novels' : books, 
             'recipients' : recipients    
        }

        return listing
    
    def get_tweet(self, mid):
        files = glob.glob('data/*.txt')
        if files is None:
            print "failed to find any files"
        print "mesage id", mid
        for filez in files:
            data = json.loads(open(filez, 'r').read()) 
            for result in data['results']:
                if int(mid) == int(result['id']):
                    return result
          
    
    def _getnovels(self, tweet):
        match = re.search("(PSS | Perdido | Perdido Street Station | Iron | Iron Council | Scar | Jake | King | King Rat | City)", tweet, re.M|re.I)
        if match:
            return match

    def _getrecipient(self, tweet):
        match = re.search("(@\w+)", tweet, re.M|re.I)
        if match:
            return match
        
    def _converttitle(self, title):
        print title
        if title == "Perdido" or title == "PSS":
            return "Perido Street Station"
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