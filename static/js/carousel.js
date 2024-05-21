// Variables
let prev = document.querySelector('.prev');
let next = document.querySelector('.next');
let imgs = document.querySelectorAll('.carousel-img');
let dots = document.querySelectorAll('.dot');
let captions = document.querySelectorAll('.carousel-caption');
let totalImgs = imgs.length;
let imgPosition = 0;
let intervalId;

// Event Listeners
next.addEventListener('click', nextImg);
prev.addEventListener('click', prevImg);

// Update Position
function updatePosition() {
	// Images
	for (let img of imgs) {
		img.classList.remove('visible');
		img.classList.add('hidden');
	}
	imgs[imgPosition].classList.remove('hidden');
	imgs[imgPosition].classList.add('visible');
	// Dots
	for (let dot of dots) {
		dot.className = dot.className.replace(' active', '');
	}
	dots[imgPosition].classList.add('active');
	// Captions
	for (let caption of captions) {
		caption.classList.remove('visible');
		caption.classList.add('hidden');
	}
	captions[imgPosition].classList.remove('hidden');
	captions[imgPosition].classList.add('visible');
}

// Next Img
function nextImg() {
	clearInterval(intervalId); // Reset the timer
	imgPosition++;
	if (imgPosition === totalImgs) {
		imgPosition = 0;
	}
	updatePosition();
	startTimer(); // Start the timer again
}

// Previous Image
function prevImg() {
	clearInterval(intervalId); // Reset the timer
	imgPosition--;
	if (imgPosition < 0) {
		imgPosition = totalImgs - 1;
	}
	updatePosition();
	startTimer(); // Start the timer again
}

// Start Timer
function startTimer() {
	intervalId = setInterval(() => {
		nextImg();
	}, 10000); // Change image every 10 seconds
}

// Dot Position
dots.forEach((dot, dotPosition) => {
	dot.addEventListener('click', () => {
		clearInterval(intervalId); // Reset the timer
		imgPosition = dotPosition;
		updatePosition();
		startTimer(); // Start the timer again
	});
});

// Start the initial timer
startTimer();
