<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>VINIUS - REAL MOVIES</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;color:#fff;font-family:Arial}
.top{padding:15px 20px;background:#000;position:sticky;top:0;z-index:10}
.logo{color:#e50914;font-weight:900;font-size:28px;letter-spacing:2px}
.hero{padding:50px 20px;background:linear-gradient(to right,#3a0000,#000)}
.hero h1{font-size:32px;margin-bottom:10px}
.hero p{color:#999;margin-bottom:20px}
.btn{background:#e50914;color:#fff;border:none;padding:14px 30px;border-radius:4px;font-weight:bold;font-size:16px;cursor:pointer}
.grid{display:flex;flex-wrap:wrap;gap:16px;padding:20px}
.card{width:165px;background:#181818;border-radius:6px;overflow:hidden;cursor:pointer;transition:.2s}
.card:hover{transform:scale(1.05)}
.card img{width:100%;height:95px;object-fit:cover;background:#222}
.name{padding:8px;font-size:11px;line-height:14px;height:40px;overflow:hidden}
#player{position:fixed;inset:0;background:#000;display:none;z-index:99;flex-direction:column}
#player.show{display:flex}
#player iframe{width:100%;flex:1;border:none}
.close{position:absolute;top:15px;right:15px;background:#e50914;color:#fff;width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:28px;cursor:pointer;z-index:100}
</style>
</head>
<body>
<div class="top"><div class="logo">VINIUS</div></div>
<div class="hero">
<h1>12 Real Full Movies</h1>
<p>Real Hollywood classics. Public domain. 100% legal. No cartoons. Tap any movie to watch full film.</p>
<button class="btn" onclick="playMovie(0)">▶ PLAY NOW</button>
</div>
<div class="grid" id="grid"></div>

<div id="player">
<span class="close" onclick="closePlayer()">✕</span>
<iframe id="frame" allowfullscreen></iframe>
</div>

<script>
const MOVIES = [
 {t:"Night of the Living Dead COLOR (1968)", id:"night-of-the-living-dead-1968-colorized"},
 {t:"House on Haunted Hill (1959)", id:"house_on_haunted_hill"},
 {t:"The Last Man on Earth (1964)", id:"TheLastManOnEarth_201403"},
 {t:"Plan 9 From Outer Space (1959)", id:"Plan9FromOuterSpace"},
 {t:"Carnival of Souls (1962)", id:"CarnivalOfSouls"},
 {t:"Nosferatu (1922)", id:"Nosferatu1922"},
 {t:"Charade (1963) - Audrey Hepburn", id:"Charade_1963"},
 {t:"His Girl Friday (1940)", id:"HisGirlFriday"},
 {t:"White Zombie (1932) - Bela Lugosi", id:"WhiteZombie1932"},
 {t:"The General (1926) - Buster Keaton", id:"TheGeneral1926"},
 {t:"Scarlet Street (1945)", id:"Scarlet_Street_1945"},
 {t:"Little Shop of Horrors (1960)", id:"TheLittleShopOfHorrors"},
];
const grid=document.getElementById('grid');
MOVIES.forEach((m,i)=>{
 grid.innerHTML+=`<div class="card" onclick="playMovie(${i})"><img src="https://archive.org/services/img/${m.id}" onerror="this.src='https://via.placeholder.com/165x95/222/e50914?text=${encodeURIComponent(m.t)}'"><div class="name">${m.t}</div></div>`;
});
function playMovie(i){
 document.getElementById('frame').src="https://archive.org/embed/"+MOVIES[i].id;
 document.getElementById('player').classList.add('show');
}
function closePlayer(){
 document.getElementById('player').classList.remove('show');
 document.getElementById('frame').src='';
}
</script>
</body>
</html>
