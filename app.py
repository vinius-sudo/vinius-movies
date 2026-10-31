from flask import Flask, render_template_string
app = Flask(__name__)

# 12 REAL FULL MOVIES - PUBLIC DOMAIN - WORKING TODAY - NOT CARTOON
MOVIES = [
 {"title":"Night of the Living Dead (1968) Color - FULL","year":"1968","id":"night-of-the-living-dead-1968-colorized"},
 {"title":"The Last Man on Earth (1964) Vincent Price","year":"1964","id":"TheLastManOnEarth_201403"},
 {"title":"House on Haunted Hill (1959) Vincent Price","year":"1959","id":"house_on_haunted_hill"},
 {"title":"Plan 9 From Outer Space (1959)","year":"1959","id":"Plan9FromOuterSpace"},
 {"title":"Carnival of Souls (1962) Horror","year":"1962","id":"CarnivalOfSouls"},
 {"title":"Nosferatu (1922) Dracula Original","year":"1922","id":"Nosferatu1922"},
 {"title":"Charade (1963) Audrey Hepburn","year":"1963","id":"Charade_1963"},
 {"title":"The General (1926) Buster Keaton","year":"1926","id":"TheGeneral1926"},
 {"title":"Scarlet Street (1945) Film Noir","year":"1945","id":"Scarlet_Street_1945"},
 {"title":"Little Shop of Horrors (1960)","year":"1960","id":"TheLittleShopOfHorrors"},
 {"title":"White Zombie (1932) Bela Lugosi","year":"1932","id":"WhiteZombie1932"},
 {"title":"His Girl Friday (1940) Comedy","year":"1940","id":"HisGirlFriday"},
]

HTML = """
<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>VINIUS REAL MOVIES</title>
<style>
body{margin:0;background:#000;color:#fff;font-family:Arial}
.top{padding:12px;background:#000;position:sticky;top:0;z-index:10}
.logo{color:#e50914;font-weight:900;font-size:26px}
.hero{padding:40px 20px;background:linear-gradient(#222,#000)}
.btn{background:#e50914;color:#fff;border:none;padding:12px 24px;border-radius:4px;font-weight:bold;font-size:16px}
.grid{display:flex;flex-wrap:wrap;gap:12px;padding:15px}
.card{width:160px;background:#181818;border-radius:6px;overflow:hidden;cursor:pointer}
.card img{width:100%;height:90px;object-fit:cover;background:#222}
.name{padding:6px;font-size:11px;height:36px;overflow:hidden}
#wrap{position:fixed;inset:0;background:#000;display:none;z-index:99;flex-direction:column}
#wrap.show{display:flex}
iframe,video{width:100%;flex:1;border:none;background:#000}
.info{padding:12px;background:#111}
.x{position:absolute;top:10px;right:15px;font-size:28px;cursor:pointer;background:rgba(0,0,0,0.8);border-radius:50%;width:38px;height:38px;display:flex;align-items:center;justify-content:center;z-index:100}
</style></head><body>
<div class="top"><div class="logo">VINIUS - REAL MOVIES</div></div>
<div class="hero"><h1>12 REAL FULL MOVIES</h1><p>Not cartoons! Hollywood horror, comedy, noir - 100% FREE & LEGAL public domain. Tap to play FULL movie.</p><button class="btn" onclick="play(0)">▶ PLAY NOW</button></div>
<div class="grid">
{% for m in movies %}<div class="card" onclick="play({{loop.index0}})"><img src="https://archive.org/services/img/{{m.id}}"><div class="name">{{m.title}}</div></div>{% endfor %}
</div>
<div id="wrap"><span class="x" onclick="closeP()">✕</span><iframe id="frame" allowfullscreen></iframe><div class="info"><h3 id="vt"></h3><p style="color:#aaa">Full movie from Internet Archive - if slow, wait 15 sec</p></div></div>
<script>
const MOVIES = {{movies|tojson}};
function play(i){
  const m = MOVIES[i];
  document.getElementById('frame').src = "https://archive.org/embed/" + m.id;
  document.getElementById('vt').innerText = m.title;
  document.getElementById('wrap').classList.add('show');
}
function closeP(){document.getElementById('wrap').classList.remove('show');document.getElementById('frame').src='';}
</script>
</body></html>
"""
@app.route('/')
def home(): return render_template_string(HTML, movies=MOVIES)
