from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>VINIUS - Netflix Style</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#141414;color:#fff;font-family:Arial,Helvetica,sans-serif}
header{background:#000;display:flex;justify-content:space-between;align-items:center;padding:15px 4%;position:sticky;top:0;z-index:10}
.logo{color:#e50914;font-size:32px;font-weight:900;letter-spacing:2px}
nav a{color:#fff;text-decoration:none;margin-left:20px;font-size:14px}
.hero{height:60vh;background:linear-gradient(to bottom,rgba(0,0,0,0.3),#141414), url('https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1200');background-size:cover;display:flex;align-items:flex-end;padding:4%}
.hero h1{font-size:50px;margin-bottom:10px}
.hero p{max-width:500px;color:#ccc;margin-bottom:15px}
.btn{background:#e50914;color:#fff;border:none;padding:10px 25px;font-size:18px;border-radius:4px;cursor:pointer;font-weight:bold}
.btn:hover{background:#f40612}
.row{padding:20px 4%}
.row h2{margin-bottom:12px;font-size:22px}
.slider{display:flex;gap:10px;overflow-x:auto;scrollbar-width:none;padding-bottom:10px}
.slider::-webkit-scrollbar{display:none}
.card{min-width:200px;height:120px;border-radius:6px;overflow:hidden;cursor:pointer;transition:0.3s;position:relative;background:#222;flex-shrink:0}
.card:hover{transform:scale(1.15);z-index:5}
.card img{width:100%;height:100%;object-fit:cover}
.card .info{position:absolute;bottom:0;background:linear-gradient(transparent,rgba(0,0,0,0.9));width:100%;padding:8px;font-size:12px}
.search{padding:10px 20px;border-radius:4px;border:none;background:#333;color:#fff;width:250px}
#modal{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.9);z-index:100;justify-content:center;align-items:center}
#modalContent{background:#181818;width:90%;max-width:800px;border-radius:8px;overflow:hidden}
#modal video{width:100%;max-height:70vh}
#modalInfo{padding:15px}
.close{float:right;color:#fff;font-size:28px;cursor:pointer;padding:5px 15px}
</style>
</head>
<body>
<header>
<div class="logo">VINIUS</div>
<div><input id="search" class="search" placeholder="🔍 Search movies..." onkeyup="filterMovies()"><nav style="display:inline"><a href="#">Home</a><a href="#">My List</a></nav></div>
</header>

<div class="hero">
<div>
<h1>Night of the Living Dead</h1>
<p>The first modern zombie film. A group barricades in a farmhouse. Public Domain Classic - 100% FREE & SAFE.</p>
<button class="btn" onclick="playMovie('https://archive.org/download/night_of_the_living_dead/night_of_the_living_dead_512kb.mp4','Night of the Living Dead')">▶ Play</button>
</div>
</div>

<div class="row"><h2>🔥 Trending Now</h2><div class="slider" id="row1"></div></div>
<div class="row"><h2>🎬 Public Domain Classics</h2><div class="slider" id="row2"></div></div>
<div class="row"><h2>🎨 Animation - Pixar Style</h2><div class="slider" id="row3"></div></div>

<div id="modal" onclick="closeModal(event)"><div id="modalContent"><span class="close" onclick="document.getElementById('modal').style.display='none'">&times;</span><video id="modalVideo" controls autoplay></video><div id="modalInfo"><h2 id="modalTitle"></h2><p id="modalDesc" style="color:#999;margin-top:8px"></p></div></div></div>

<script>
const movies=[
{t:"Big Buck Bunny",g:"Animation",d:"Open source 3D animated comedy",v:"https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",i:"https://peach.blender.org/wp-content/uploads/title_anouncement.jpg"},
{t:"Night of Living Dead",g:"Horror",d:"1968 Zombie Classic - Public Domain",v:"https://archive.org/download/night_of_the_living_dead/night_of_the_living_dead_512kb.mp4",i:"https://archive.org/download/night_of_the_living_dead/night_of_the_living_dead.thumbs/night_of_the_living_dead_000030.jpg"},
{t:"House on Haunted Hill",g:"Horror",d:"1959 Vincent Price Horror",v:"https://archive.org/download/house_on_haunted_hill/house_on_haunted_hill_512kb.mp4",i:"https://images.unsplash.com/photo-1509248961158-e32f69343cd3?w=400"},
{t:"Nosferatu (1922)",g:"Classic",d:"First Dracula film ever",v:"https://archive.org/download/Nosferatu_1922/Nosferatu.mp4",i:"https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400"},
{t:"The General (1926)",g:"Classic",d:"Buster Keaton silent comedy",v:"https://archive.org/download/TheGeneral/The_General_512kb.mp4",i:"https://images.unsplash.com/photo-1485846234645-a62644f84728?w=400"},
{t:"Elephants Dream",g:"Animation",d:"First open movie",v:"https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",i:"https://orange.blender.org/wp-content/themes/orange/images/common/ed_header.jpg"},
{t:"Sintel",g:"Animation",d:"Fantasy open movie",v:"https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",i:"https://durian.blender.org/wp-content/uploads/2010/05/sintel_poster.jpg"},
{t:"Tears of Steel",g:"Sci-Fi",d:"Sci-fi short",v:"https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",i:"https://mango.blender.org/wp-content/uploads/2013/05/01_thom_celia_bridge.jpg"},
{t:"Carnival of Souls",g:"Horror",d:"1962 cult horror",v:"https://archive.org/download/CarnivalofSouls/CarnivalOfSouls_512kb.mp4",i:"https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=400"},
{t:"For Bigger Blazes",g:"Action",d:"Action short",v:"https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",i:"https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=400"},
{t:"Little Shop Horrors",g:"Comedy",d:"1960 Original comedy horror",v:"https://archive.org/download/little_shop_of_horrors/little_shop_of_horrors_512kb.mp4",i:"https://images.unsplash.com/photo-1594909122845-11baa439b7bf?w=400"},
{t:"Duck and Cover",g:"Documentary",d:"Classic Prelinger Archives",v:"https://archive.org/download/duckandcover/duckandcover_512kb.mp4",i:"https://images.unsplash.com/photo-1460881680858-30d872d5dca5?w=400"}
];

function createCard(m){
return `<div class="card" onclick="playMovie('${m.v}','${m.t}','${m.d}')"><img src="${m.i}" onerror="this.src='https://via.placeholder.com/200x120/222/e50914?text=${encodeURIComponent(m.t)}'"><div class="info">${m.t}</div></div>`;
}
function loadRows(){
document.getElementById('row1').innerHTML=movies.slice(0,6).map(createCard).join('');
document.getElementById('row2').innerHTML=movies.slice(2,8).map(createCard).join('');
document.getElementById('row3').innerHTML=movies.slice(0,4).map(createCard).join('')+movies.slice(6,10).map(createCard).join('');
}
function playMovie(url,title,desc){
document.getElementById('modalVideo').src=url;
document.getElementById('modalTitle').innerText=title;
document.getElementById('modalDesc').innerText=desc||"Safe Public Domain Movie - 100% FREE";
document.getElementById('modal').style.display='flex';
}
function closeModal(e){ if(e.target.id==='modal') e.target.style.display='none'; document.getElementById('modalVideo').pause(); }
function filterMovies(){
let q=document.getElementById('search').value.toLowerCase();
let f=movies.filter(m=>m.t.toLowerCase().includes(q));
document.getElementById('row1').innerHTML=f.map(createCard).join('')||"<p style='color:#999'>No results</p>";
}
loadRows();
</script>
</body>
</html>
    """

if __name__ == '__main__':
    print("🔥 NETFLIX STYLE VINIUS RUNNING at http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
