const searchBox = document.getElementById('search');
const residuos = document.querySelectorAll('.residuo');
const listaResiduo = document.getElementById('lista-residuo');
const noResults = document.getElementById('no-results');

searchBox.addEventListener('input', function() {
    const searchTerm = searchBox.value.toLowerCase();
    let hasMatches = false;
    
    residuos.forEach(residuo => {
        const title = residuo.querySelector('h2').textContent.toLowerCase();
        if (title.includes(searchTerm)) {
            residuo.style.display = 'block';
            hasMatches = true;
        } else {
            residuo.style.display = 'none';
        }
    });

    listaResiduo.style.display = 'block';
    noResults.style.display = hasMatches ? 'none' : 'block';
});