from flask import *
import data as cfg

app = Flask(__name__)
app.config['DEBUG'] = True

''' Функция поиска '''

def filter_by_tag(tag,videos):

    found = []
    for video in videos:
        if tag in video["tags"]:
            found.append(video)
    return found

''' Главная страничка '''

@app.route('/')
def hello():

    videos = cfg.videos.values()
    playlists = cfg.playlists.values()
    tags = cfg.tags

    return render_template('index.html',playlists=playlists,videos=videos,tags=tags)

''' Страничка плейлиста '''

@app.route('/playlists/<list>/')
@app.route('/playlists/<list>/<item>')
def playlists_item(list,item=0):

    item = int(item)

    playlist =  cfg.playlists[list]
    video = playlist["videos"][item]

    return render_template('playlists_item.html', playlist=playlist, video=video)


''' Страничка тега '''

@app.route('/tags/<tag>')
def tags_item(tag):

    videos =  cfg.videos.values()
    filtered = filter_by_tag(tag,videos)
    return render_template('tags_item.html',tag=tag,videos=filtered)


''' Одно видео '''

@app.route('/videos/<id>')
def videos_item(id):

 video = cfg.videos.get(id)
 return render_template('videos_item.html', video=video)


''' Описание проекта '''

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()