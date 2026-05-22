const images = [
  "img/asteroid.png",
  "img/hvezda.png",
  "img/nepritel.png",
];

function randomImage() {
  const img = document.getElementById("obrazek");
  const randomIndex = Math.floor(Math.random() * images.length);
  img.src = images[randomIndex];
}
