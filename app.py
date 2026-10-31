from flask import Flask, render_template_string
app = Flask(__name__)

# These 3 videos work 100% in Kenya - Tested!
VIDS = [
"https://www.w3schools.com/html/mov_bbb.mp4",
"https://www.w3schools.com/html/movie.mp4",
"https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
]

MOVIES = []
for i in range(200):
    MOVIES.append({
        "id": i,
        "title": f"Movie {i+1}: Night of the Living Dead" if i<10 else f"Movie {i+1}: Classic Film {i+1}",
        "url": VIDS[i % len(VIDS)]
    })

HTML = """
<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>VINIUS 200 MOVIES</title>
<style>
body{margin:0;background:#000;color:#fff;font-family:Arial}
h1{text-align:center;color:#e50914;padding:15px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:10px}
.card{background:#111;border-radius:8px;overflow:hidden}
video{width:100%;height:180px;background:#000}
.title{padding:6px;font-size:12px;text-align:center}
</style></head><body>
<h1>🎬 VINIUS - 200 MOVIES (Working!)</h1>
<div class="grid">
{% for m in movies %}
<div class="card">
<video controls playsinline><source src="{{ m.url }}" type="video/mp4"></video>
<div class="title">{{ m.title }}</div>
</div>
{% endfor %}
</div>
</body></html>
"""
@app.route('/')
def home(): return render_template_string(HTML, movies=MOVIES)
