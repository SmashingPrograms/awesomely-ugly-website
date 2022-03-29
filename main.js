function toHex(unit) {
  return Number(unit).toString(16)
}

let max = 16777215

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
};

let rand = toHex(getRandomInt(max))

// Uncomment if you think there won't be seizures

// setInterval(function(){
//   rand = toHex(getRandomInt(max))
//   document.body.style.backgroundColor=`#${rand}`
// }, 10);

function openInNewTab(url) {
  setInterval(function(){
    let win = window.open(url, '_blank');
    win.focus();
  }, 1000);
  !false;
}

function swapImage() {
  const allImages = document.getElementsByTagName("img");
  const lastImage = allImages[allImages.length-1];
  lastImage.src = `https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file&wpvalue=The_Fighting_Coward_(SAYRE_14435).jpg`
}