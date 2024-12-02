document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search');
    const listaResiduo = document.getElementById('lista-residuo');
    const noResults = document.getElementById('no-results');

    // Esconde a mensagem de "Nenhum resultado" ao carregar a página
    noResults.style.display = 'none';

    // Função para filtrar a lista
    function filterList() {
        const searchTerm = searchInput.value.toLowerCase();
        const items = listaResiduo.getElementsByTagName('li');
        let found = false;

        // Percorre os itens da lista
        for (let i = 0; i < items.length; i++) {
            const item = items[i];
            if (item.textContent.toLowerCase().includes(searchTerm)) {
                item.style.display = '';
                found = true;
            } else {
                item.style.display = 'none';
            }
        }

        // Se não encontrar resultados, exibe a mensagem de "nenhum resultado"
        if (!found && searchTerm) {
            noResults.style.display = 'block';
        } else {
            noResults.style.display = 'none';
        }
    }

    // Escuta os eventos de digitação no campo de pesquisa
    searchInput.addEventListener('input', filterList);
});