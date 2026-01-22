from flask import Flask,render_template , request,redirect
import requests as req
from my_music import add_entry


app = Flask(__name__)

def get_songs(query):

    result=req.get("https://saavn.sumit.co/api/search/songs",
    params={
      "query": query,
      "page": "0",
      "limit": "10"
    }
    )

    all_json = result.json()

    songs = all_json['data']['results']
    

    # song_names=[]
    # for song in songs:
    #     song_names.append(song['name'])
    
    return songs

@app.route('/',methods=['GET','POST'])

def home():
    return render_template('home.html')


@app.route('/search',methods=['GET','POST'])

def search():

    if request.method =="GET":
        return render_template('search.html',songs=[])
     
    elif request.method == "POST":
        query = request.form['song-search']
        
        return render_template("search.html",
        songs =get_songs(query))
    
# About us page 
@app.route('/about',methods =  ['GET','POST'])
def about ():
    return render_template('about.html')
app.run(debug=True,port=9999)