document.addEventListener('DOMContentLoaded', () => {
    // Initialize the map once Leaflet is loaded
    initializeMap();
});

function initializeMap() {
    // Create the map centered on Cascavel
    const map = L.map('map').setView([-24.9555, -53.4552], 13); 

    L.Icon.Default.imagePath = '/static/images/';

    // Add a tile layer
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    
    // Request user's current location
    navigator.geolocation.getCurrentPosition(success, error);
    
    let marker;
    let circle;

    function success(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        const accuracy = position.coords.accuracy;

        // Remove previous markers and circles
        if (marker) {
            map.removeLayer(marker);
            map.removeLayer(circle);
        }

        // Create a new marker for the user's location
        marker = L.marker([lat, lon]).addTo(map);
        circle = L.circle([lat, lon], { radius: accuracy }).addTo(map);
        
        // Adjust map view to fit the circle
        map.fitBounds(circle.getBounds());
    }

    function error(err) {
        switch(err.code) {
            case err.PERMISSION_DENIED:
                alert("É necessário autorizar o acesso à localização");
                break;
            case err.POSITION_UNAVAILABLE:
            case err.TIMEOUT:
            case err.UNKNOWN_ERROR:
                alert("Não foi possível acessar a localização atual");
                break;
        }
    }

    // Default Leaflet
    const pontosDeColeta = [
        { coords: [-24.98772, -53.45399], color: '008000', descricao: 'VIDRO' },
        { coords: [-24.97474, -53.42482], color: 'FF0000', descricao: 'PLÁSTICO' },
        { coords: [-24.95714, -53.42066], color: 'FFFF00', descricao: 'METAL' },
        { coords: [-24.93395, -53.40504], color: '008000', descricao: 'VIDRO' },
        { coords: [-24.97255, -53.49671], color: 'FF0000', descricao: 'PLÁSTICO' },
        { coords: [-24.94827, -53.49808], color: '50301E', descricao: 'ORGÂNICO' },
        { coords: [-53.49808, -53.46821], color: 'FF0000', descricao: 'PLÁSTICO' },
        { coords: [-24.92586, -53.44521], color: 'FFFF00', descricao: 'METAL' },
        { coords: [-24.91091, -53.43491], color: '2B58DE', descricao: 'PAPEL' },
        { coords: [-24.91172, -53.41512], color: '50301E', descricao: 'ORGÂNICO' },
        { coords: [-24.92418, -53.41924], color: '008000', descricao: 'VIDRO' },
        { coords: [-24.91920, -53.43228], color: '2B58DE', descricao: 'PAPEL' },
        { coords: [-24.92763, -53.42236], color: '50301E', descricao: 'ORGÂNICO' },
        { coords: [-24.91586, -53.42119], color: 'FF0000', descricao: 'PLÁSTICO' },
        { coords: [-24.91653, -53.41763], color: 'FFFF00', descricao: 'Eletrônicos' }
    ];        

    // Add default Leaflet markers
    pontosDeColeta.forEach(function(ponto) {
        L.marker(ponto.coords)
            .bindPopup(ponto.descricao)
            .addTo(map);
    });
}