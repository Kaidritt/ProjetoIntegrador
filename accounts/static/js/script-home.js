document.getElementById('subscriptionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    const formData = new FormData(this); // Coleta os dados do formulário

    fetch('/subscribe/', { // Ajuste aqui para a URL correta do seu servidor Django
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken'), // Inclui o token CSRF
        },
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('confirmationMessage').style.display = 'block';
            this.reset(); // Reseta o formulário
        } else {
            console.error('Erro durante a inscrição:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Erro de rede:', error);
    });
});

// Função para obter o cookie CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se o cookie começa com o nome desejado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}