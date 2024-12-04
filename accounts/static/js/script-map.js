document.addEventListener('DOMContentLoaded', function () {
    // Get the JSON data from the data-pontos attribute (stored in a hidden div)
    const pontosData = JSON.parse(document.getElementById('pontos-data').getAttribute('data-pontos'));

    // Initialize the map, centered at Cascavel with a default zoom level of 8
    const map = L.map('map').setView([-24.9558300, -53.4552800], 15);  // Consider changing coordinates to a more central location for your users

    // Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Optional: Add a control for zooming
    L.control.zoom().addTo(map);

    // Iterate through the pontosData to place markers on the map
    pontosData.forEach(ponto => {
        // Check if latitude and longitude are valid
        if (ponto.latitude && ponto.longitude) {
            // Create a marker at the specified latitude and longitude
            const marker = L.marker([ponto.latitude, ponto.longitude]).addTo(map);

            // Create the popup content with address and waste types
            const popupContent = `
                <b>${ponto.endereco}</b><br>
                Tipos de resíduo: ${ponto.tipos_residuo ? ponto.tipos_residuo : 'Não especificado'}
            `;

            // Bind the popup to the marker
            marker.bindPopup(popupContent);

            // Optional: Change the marker icon based on waste types (for example, use different icons for different types of waste)
            // If you want to use custom icons, you could do something like:
            /*
            const icon = L.icon({
                iconUrl: 'path/to/your-icon.png',  // Update with the correct path
                iconSize: [25, 25],  // Define the size of the icon
                iconAnchor: [12, 12]  // Anchor the icon to the center
            });
            marker.setIcon(icon);
            */
        }
    });
    
    // Optional: Fit the map bounds to the markers
    const bounds = pontosData.map(ponto => [ponto.latitude, ponto.longitude]);
    map.fitBounds(bounds);

});