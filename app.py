from flask import Flask, render_template_string
app = Flask(__name__)

MOVIES = [
    {"id": 1, "title": "Big Buck Bunny - FULL MOVIE", "year": "10 min • With Sound", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"},
    {"id": 2, "title": "Elephant Dream - FULL MOVIE", "year": "11 min • With Sound", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"},
    {"id": 3, "title": "For Bigger Blazes", "year": "15 sec • Action", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"},
]

HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>VINIUS - Real Movies</title>
<style>
body{background:#000;color:#fff;font-family:Arial;margin:0;padding:20px}
h1{color:red;text-align:center}
.card{background:#111;border-radius:10px;padding:15px;margin:15px 0}
a{color:#fff;text-decoration:none}
.btn{background:red;color:#fff;padding:10px 20px;border-radius:5px;display:inline-block;margin-top:10px}
video{width:100%;max-width:800px}
</style></head><body>
<h1>VINIUS - Real Movies With Sound</h1>
{% if movie %}
<h2>{{movie.title}}</h2>
<video controls autoplay><source src="{{movie.url}}" type="video/mp4"></video>
<br><a class="btn" href="/">← Back to All Movies</a>
{% else %}
{% for m in movies %}
<div class="card">
<h3>{{m.title}}</h3><p>{{m.year}}</p>
<a class="btn" href="/watch/{{m.id}}">WATCH NOW</a>
</div>
{% endfor %}
{% endif %}
</body></html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, movies=MOVIES, movie=None)

@app.route("/watch/<int:mid>")
def watch(mid):
    m = next((x for x in MOVIES if x["id"]==mid), None)
    return render_template_string(HTML, movies=MOVIES, movie=m)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
