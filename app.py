from flask import Flask, render_template_string
app = Flask(__name__)
MOVIES = [
 {"title": "Night of the Living Dead (1968)", "url": "https://archive.org/download/night_of_the_living_dead/night_of_the_living_dead_512kb.mp4"},
 {"title": "House on Haunted Hill (1959)", "url": "https://archive.org/download/house_on_haunted_hill/house_on_haunted_hill_512kb.mp4"},
 {"title": "Plan 9 from Outer Space", "url": "https://archive.org/download/plan_9_from_outer_space/plan_9_from_outer_space_512kb.mp4"},
 {"title": "Little Shop of Horrors (1960)", "url": "https://archive.org/download/TheLittleShopOfHorrors/The_Little_Shop_of_Horrors_512kb.mp4"},
 {"title": "Carnival of Souls (1962)", "url": "https://archive.org/download/CarnivalOfSouls/CarnivalOfSouls_512kb.mp4"},
 {"title": "Nosferatu (1922)", "url": "https://archive.org/download/Nosferatu1922/Nosferatu_512kb.mp4"},
]
HTML = """<!DOCTYPE html><html><head><title>Vinius Movies</title>
<style>body{background:#000;color:#fff;font-family:Arial;padding:15px}
h1{color:#e50914;text-align:center}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}
.card{background:#111;border-radius:10px;padding:10px}video{width:100%;border-radius:8px}</style>
</head><body><h1>🎬 VINIUS MOVIES</h1><div class="grid">
{% for m in movies %}<div class="card"><h3>{{ m.title }}</h3>
<video controls><source src="{{ m.url }}" type="video/mp4"></video></div>{% endfor %}
</div></body></html>"""
@app.route('/')
def home(): return render_template_string(HTML, movies=MOVIES)
