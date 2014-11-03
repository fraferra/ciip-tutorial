from flask import *
import requests

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    q=request.args.get('q')
    if q is None:
    	q=''
    r=requests.get("http://api.giphy.com/v1/gifs/search?q="+ q +"&api_key=dc6zaTOxFJmzC")
    gifs=r.json()['data']
    return render_template('index.html', gifs=gifs)




if __name__ == "__main__":
    app.run(debug=True )

