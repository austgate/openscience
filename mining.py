from flask import Flask,app,render_template
from parsing import Parsing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)