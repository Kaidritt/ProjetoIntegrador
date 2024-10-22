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
    const offset = -currentIndex * 100; // Assuming each card takes up 100% width
    carouselContainer.style.transform = `translateX(${offset}%)`;
}