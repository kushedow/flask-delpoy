from flask import *

app = Flask(__name__)

import data as cfg

def filter_by_tag(tag,videos):

    result = []
    for video in videos:
        if tag in video["tags"]:
            result.append(video)
    return result


@app.route('/products')
def products():
    return "Здесь будут продукты"

@app.route('/')
def hello_world():

    videos =  [ v for v in cfg.videos.values() ]

    playlists = [ v for v in cfg.playlists.values() ]

    return render_template('index.html',playlists=playlists,videos=videos,tags=cfg.tags)


@app.route('/videos/<id>')
def videos_item(id):

 video = cfg.videos.get(id)

 return render_template('videos_item.html', video=video)

@app.route('/playlists/<list>/')
@app.route('/playlists/<list>/<item>')
def playlists_item(list,item=0):


    item = int(item)

    playlist =  cfg.playlists[list]
    video = playlist["videos"][item]

    return render_template('playlists_item.html',video=video,playlist=playlist)


@app.route('/tags/<tag>')
def tags_item(tag):

    videos =  [ v for v in cfg.videos.values() ]
    filtered = filter_by_tag(tag,videos)
    return render_template('tags_item.html',tag=tag,videos=filtered)

@app.route('/about')
def about():
    return render_template('about.html')

app.run()