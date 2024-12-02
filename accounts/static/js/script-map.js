const map = L.map('map').setView([-23.5505, -46.6333], 13);

// Adiciona a camada de tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Funções de localização
function onLocationFound(e) {
    const radius = e.accuracy / 2;
    L.marker(e.latlng).addTo(map)
        .bindPopup(`Você está em um raio de ${radius} metros deste ponto`).openPopup();
    L.circle(e.latlng, radius).addTo(map);
}

function onLocationError(e) {
    alert(e.message);
}

// Ativa a localização do usuário
map.on('locationfound', onLocationFound);
map.on('locationerror', onLocationError);
map.locate({setView: true, maxZoom: 16}); // Tenta localizar o usuário ao inicializar o mapa

// Controle de localização
const locationControl = L.control({position: 'topleft'});
locationControl.onAdd = function(map) {
    const div = L.DomUtil.create('div', 'leaflet-bar leaflet-control');