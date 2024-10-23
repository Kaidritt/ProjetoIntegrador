let currentIndex = 0;
const cards = document.querySelectorAll('.recicle-card');
const totalCards = cards.length;
const carouselContainer = document.getElementById('carousel-container');

document.getElementById('nextBtn').addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % totalCards;
    updateCarousel();
});

document.getElementById('prevBtn').addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + totalCards) % totalCards;
    updateCarousel();
});

function updateCarousel() {
    const offset = -currentIndex * 100;
    carouselContainer.style.transform = `translateX(${offset}%)`;
}

document.addEventListener('DOMContentLoaded', () => {
    // Cria o mapa
    const map = L.map('map').setView([-24.9555, -53.4552], 13); // Coordenadas de Cascavel
    
    // Adiciona uma camada de tile
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
	    maxZoom: 19,
	    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
	}).addTo(map);
		
	navigator.geolocation.getCurrentPosition(success, error);
		
	let marker;
	let circle;
		
	function success(position) {
	    const lat = position.coords.latitude;
	    const lon = position.coords.longitude;
			
	    const accuracy = position.coords.accuracy;
			
		if (marker) {
			map.removeLayer(marker);
			map.removeLayer(circle);
		}
			
		marker = L.marker([lat, lon]).addTo(map);
		circle = L.circle([lat, lon], { radius: accuracy }).addTo(map);
			
		map.fitBounds(circle.getBounds());
	}
		
	function error(error) {
		if (error.code === 1) {
			alert("É necessário autorizar o acesso à localização");
		} else {
			alert("Não foi possível acessar a localização atual");
		}
	}
		
    // Adiciona um marcador
    //const marker = L.marker([-24.95555, -53.4552]).addTo(map);
    //marker.bindPopup('Cascavel').openPopup();
    
    function createCircleIcon(color) {
        return L.divIcon({
            className: 'custom-circle-icon',
            html: `<div style="background-color: ${color}; width: 10px; height: 10px; border-radius: 50%;"></div>`,
            iconSize: [10, 10],
            iconAnchor: [5, 5],
            popupAnchor: [0, -5],
        });
    }

        // Definir as coordenadas dos 10 pontos fictícios
    var pontosDeColeta = [
        { coords: [-24.9530, -53.4550], color: '008000', descricao: 'Vidro' },
        { coords: [-24.9600, -53.4500], color: 'FF0000', descricao: 'Plástico' },
        { coords: [-24.9500, -53.4600], color: '008000', descricao: 'Vidro' },
        { coords: [-24.9555, -53.4600], color: 'FFFF00', descricao: 'Metal' },
        { coords: [-24.9575, -53.4500], color: 'FF0000', descricao: 'Plástico' },
        { coords: [-24.9515, -53.4570], color: '50301E', descricao: 'Orgânico' },
        { coords: [-24.9540, -53.4530], color: 'FF0000', descricao: 'Plástico' },
        { coords: [-24.9560, -53.4545], color: 'FFFF00', descricao: 'Metal' },
        { coords: [-24.9520, -53.4580], color: 'FF0000', descricao: 'Plástico' },
        { coords: [-24.9580, -53.4520], color: '2B58DE', descricao: 'Papel' },
        { coords: [-24.9590, -53.4550], color: '50301E', descricao: 'Orgânico' },
        { coords: [-24.9545, -53.4590], color: '008000', descricao: 'Vidro' },
        { coords: [-24.9510, -53.4550], color: '2B58DE', descricao: 'Papel' },
        { coords: [-24.9550, -53.4520], color: '50301E', descricao: 'Orgânico' },
        { coords: [-24.9570, -53.4580], color: '008000', descricao: 'Vidro' }
    ];

     // Adicionar cada ponto de coleta no mapa
    pontosDeColeta.forEach(function(ponto) {
        L.marker(ponto.coords, { icon: createIcon(ponto.color) })
        .bindPopup(
            ponto.descricao)
        .addTo(map);
        });
});