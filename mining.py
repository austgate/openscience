from flask import Flask,app,render_template
from parsing import Parsing
from data import DataLayer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweet/', methods=['GET'])
@app.route('/tweet/<name>', methods=['GET'])
def tweeter(name=None):
    parz = Parsing()
    if name is None:
        data = parz.index_data()
        return render_template('tweetindex.html', data=data)
    else:
        data = parz.tweeter_data(name)

        return render_template('tweet.html', data=data)
 
@app.route('/message/<messageid>', methods=['GET'])   
def tweet(messageid=None):
    
    if id is None:
        return render_template(404)
    
    parz = Parsing()
    datum = parz.get_tweet(messageid)
    return render_template("message.html", datum=datum)

@app.route('/data/<api>', methods=['GET'])
def show_data(api=None): 
    
    if api == "network":
        data_api = api
        return render_template('book.html', data_api=data_api)
    if api == "book":
        data_api = api
        return render_template('book.html',data_api=data_api)
    if api == "words":
        raw = DataLayer()
        words = raw.count_words()
        return render_template("word.html", words=words)         
       
@app.route('/data/json/<api>', methods=['GET']) 
def data_api(api=None):
    if api is None:
        print "Please define an API type"
        
    raw = DataLayer()
    if api == "network":
        return raw.network()
    if api == "book":
        return raw.books() 
    if api == "words":
        words = raw.count_words()
        return render_template("word.html", words=words)  

if __name__ == '__main__':
    app.run(debug=True)