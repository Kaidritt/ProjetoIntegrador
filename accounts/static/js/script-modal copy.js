document.addEventListener("DOMContentLoaded", function() {
    const errorModal = document.getElementById("errorModal");
    const closeModal = document.querySelector(".close");
    const errorMessagesList = document.getElementById("errorMessagesList");

    // Função para exibir as mensagens na modal
    function displayErrors(errors) {
        errorMessagesList.innerHTML = ''; // Limpa as mensagens anteriores
        errors.forEach(error => {
            const listItem = document.createElement("li");
            listItem.textContent = error;
            errorMessagesList.appendChild(listItem);
        });

        errorModal.style.display = "block"; // Exibe a modal
    }

    // Fecha a modal ao clicar no "X"
    closeModal.addEventListener("click", function() {
        errorModal.style.display = "none";
    });

    // Verifica se há mensagens de erro e exibe a modal
    {% if messages %}
        const errors = [];
        {% for message in messages %}
            errors.push("{{ message }}");
        {% endfor %}
        displayErrors(errors);
    {% endif %}
});