from flask import *
app = Flask(__name__)
app.config['DEBUG'] = True
import data as cfg

@app.route('/')
def hello():

    videos = cfg.videos.values()
    playlists = cfg.playlists.values()
    tags = cfg.tags

    return render_template('index.html',playlists=playlists,videos=videos,tags=tags)

@app.route('/playlists/<list>/')
@app.route('/playlists/<list>/<item>')
def playlists_item(list,item=0):

    item = int(item)

    playlist =  cfg.playlists[list]
    video = playlist["videos"][item]

    return render_template('playlists_item.html', playlist=playlist, video=video)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()