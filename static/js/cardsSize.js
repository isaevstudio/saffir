
  function setEqualHeight() {
    const cards = document.querySelectorAll('.cardnws');
    let maxHeight = 0;

    // Ensure cards are displayed correctly
    cards.forEach(card => {
      card.style.height = 'auto'; // Reset height to measure correctly
      const cardHeight = card.offsetHeight;
      if (cardHeight > maxHeight) {
        maxHeight = cardHeight;
      }
    });

    console.log('Max Height:', maxHeight); // Debugging line to check max height

    // Set all cards to the maximum height
    cards.forEach(card => {
      card.style.height = `${maxHeight}px`;
    });
  }

  // Call the function on page load
  document.addEventListener('DOMContentLoaded', setEqualHeight);

  // Call the function on window resize to handle responsive layouts
  window.addEventListener('resize', setEqualHeight);

