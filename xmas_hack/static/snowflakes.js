// snowflakes.js
const numSnowflakes = 50; // Adjust the number of snowflakes
const body = document.querySelector('body');

function createSnowflake() {
    const snowflake = document.createElement('div');
    snowflake.innerHTML = "&#10052;"; // Unicode for snowflake
    snowflake.classList.add('snowflake');
    snowflake.style.left = `${Math.random() * 100}vw`;
    snowflake.style.animationDuration = `${Math.random() * 5 + 3}s`; // Adjust animation duration
    snowflake.style.animationDelay = `${Math.random()}s`; // Add delay to each snowflake
    body.appendChild(snowflake);

    snowflake.addEventListener('animationiteration', () => {
        snowflake.remove();
        createSnowflake();
    });
}

for (let i = 0; i < numSnowflakes; i++) {
    createSnowflake();
}
