// Get references to the Grinch and Santa images
const grinch = document.getElementById('grinch');
const santa = document.getElementById('santa');

// Initial positions
let grinchPosition = 0;
let santaPosition = 0;

// Function to move the Grinch and Santa Claus
function chase() {
    // Update positions
    grinchPosition += 5; // Adjust the speed of the chase
    santaPosition += 7; // Adjust the speed of the chase

    // Set new positions
    grinch.style.left = grinchPosition + 'px';
    santa.style.left = santaPosition + 'px';

    // Repeat the chase animation using requestAnimationFrame
    if (santaPosition < window.innerWidth) {
        requestAnimationFrame(chase);
    } else {
        alert('The Grinch caught Santa!');
    }
}

// Start the chase when the page loads
window.onload = chase;
