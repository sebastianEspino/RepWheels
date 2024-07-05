conf = await fetch(`http://127.0.0.1:8000/api/1.0/Configuracion/`)
data = await conf.json()

const t = document.getElementById('nombre')
t.innerText = data.nombre

