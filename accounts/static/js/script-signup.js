document.addEventListener("DOMContentLoaded", function() {
    const signupForm = document.getElementById("signup-form");
    
    if (signupForm) {
        // Limpa os campos do formulário individualmente
        const inputs = signupForm.querySelectorAll("input");
        inputs.forEach(input => {
            input.value = '';
        });

        // Limpa as mensagens de erro
        const errorMessages = signupForm.querySelectorAll('.error');
        errorMessages.forEach(error => {
            error.textContent = ''; // Remove o conteúdo do erro
            error.style.display = 'none'; // Opcional: esconde a mensagem
        });
    }
});