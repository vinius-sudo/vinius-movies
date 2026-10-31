from flask import Flask, render_template_string
app = Flask(__name__)

MOVIES = [
    {"title": "Big Buck Bunny - FULL MOVIE", "year": "10 min - With Sound", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"},
    {"title": "Elephant Dream - FULL MOVIE", "year": "11 min - With Sound", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"},
    {"title": "Night of the Living Dead", "year": "1968 - 96 min - Public Domain SAFE", "url": "https://archive.org/download/night_of_the_living_dead/night_of_the_living_dead_512kb.mp4"},
    {"title": "House on Haunted Hill", "year": "1959 - 75 min - Public Domain SAFE", "url": "https://archive.org/download/house_on_haunted_hill/house_on_haunted_hill_512kb.mp4"},
    {"title": "Nosferatu", "year": "1922 - Dracula - Public Domain SAFE", "url": "https://archive.org/download/Nosferatu_1922/Nosferatu.mp4"},
    {"title": "The General", "year": "1926 - Buster Keaton SAFE", "url": "https://archive.org/download/TheGeneral/The_General_512kb.mp4"},
    {"title": "Carnival of Souls", "year": "1962 - Horror SAFE", "url": "https://archive.org/download/CarnivalofSouls/CarnivalOfSouls_512kb.mp4"},
    {"title": "Sintel", "year": "15 min - Fantasy - CC SAFE", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4"},
    {"title": "Tears of Steel", "year": "12 min - Sci-Fi - CC SAFE", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4"},
    {"title": "Duck and Cover", "year": "1951 - Prelinger SAFE", "url": "https://archive.org/download/duckandcover/duckandcover_512kb.mp4"},
    {"title": "Little Shop of Horrors", "year": "1960 - Public Domain SAFE", "url": "https://archive.org/download/little_shop_of_horrors/little_shop_of_horrors_512kb.mp4"},
    {"title": "For Bigger Blazes", "year": "15 sec - Action", "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"},
]

HTML = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>VINIUS MOVIES</title><style>
body{background:#000;color:#fff;font-family:Arial;padding:20px;margin:0}
h1{color:red;text-align:center}.card{background:#111;border-radius:12px;padding:15px;margin:15px auto;max-width:600px}
video{width:100%;border-radius:8px}.btn{background:red;color:#fff;padding:12px 20px;border-radius:6px;display:inline-block;margin-top:10px;text-decoration:none;font-weight:bold}
</style></head><body>
<h1>🔥 VINIUS - 12 Real Movies With Sound 🔥</h1>
<p style="text-align:center;color:#aaa">All SAFE - Public Domain / Creative Commons - Cloud Hosted</p>
{% for m in movies %}<div class="card"><h2>{{m.title}}</h2><p>{{m.year}}</p>
<video controls><source src="{{m.url}}" type="video/mp4"></video><br>
<a class="btn" href="{{m.url}}" target="_blank">▶ WATCH</a></div>{% endfor %}
</body></html>
"""

@app.route('/')
def index():
    return render_template_string(HTML, movies=MOVIES)
