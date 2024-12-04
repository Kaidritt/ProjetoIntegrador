document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search');
    const residuos = document.querySelectorAll('.residuo'); // Query all 'residuo' divs
    const noResults = document.createElement('p');
    noResults.textContent = 'A pesquisa não encontrou nenhum resultado.';
    noResults.style.display = 'none'; // Initially hide it

    // Add the 'noResults' message below the search input
    const searchSection = document.querySelector('.search-section');
    searchSection.appendChild(noResults);

    // Função para filtrar a lista
    function filterResiduos() {
        const searchTerm = searchInput.value.toLowerCase();
        let found = false;

        // Percorre os itens da lista de resíduos
        residuos.forEach(function(residuo) {
            const name = residuo.dataset.name.toLowerCase();
            if (name.includes(searchTerm)) {
                residuo.style.display = '';
                found = true;
            } else {
                residuo.style.display = 'none';
            }
        });

        // Exibe a mensagem de "Nenhum resultado" se não encontrar nada
        if (!found && searchTerm) {
            noResults.style.display = 'block';
        } else {
            noResults.style.display = 'none';
        }
    }

    // Escuta os eventos de digitação no campo de pesquisa
    searchInput.addEventListener('input', filterResiduos);
});