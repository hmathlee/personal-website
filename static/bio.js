var originalImg = document.getElementById("original-img");
var segmentedImg = document.getElementById("segmented-img");
var blackBackgroundImg = document.getElementById("black-background-img");

document.addEventListener("mousemove", function(e) {
    const rect = blackBackgroundImg.getBoundingClientRect();
    const x = event.clientX;
    const y = event.clientY;
    if (x >= rect.left && x <= rect.right && y >= rect.top && y <= rect.bottom) {
        var canvas = document.createElement("canvas");
        var canvasContext = canvas.getContext("2d");

        const w = blackBackgroundImg.width;
        const h = blackBackgroundImg.height;

        canvas.width = w;
        canvas.height = h;

        canvasContext.drawImage(blackBackgroundImg, 0, 0, w, h);

        const pixel = canvasContext.getImageData(x - rect.left, y - rect.top, 1, 1).data;
        if (pixel[0] > 0 || pixel[1] > 0 || pixel[2] > 0) {
            segmentedImg.addEventListener("click", popupBio);
            segmentedImg.style.cursor = "pointer";
            segmentedImg.style.zIndex = "1";
            originalImg.style.zIndex = "-1";
        }
        else {
            segmentedImg.removeEventListener("click", popupBio);
            segmentedImg.style.cursor = "auto";
            segmentedImg.style.zIndex = "-1";
            originalImg.style.zIndex = "1";
        }
    }
})

const bioContainer = document.getElementById("bio-container");
const bioText = document.getElementById("bio-text");

function popupBio() {
    bioContainer.innerHTML = bioText.innerHTML;
}