// Drag and Drop Elements
const dropZone = document.getElementById("dropZone");
const fileInput = document.getElementById("fileInput");
const previewContainer = document.getElementById("previewContainer");
const imagePreview = document.getElementById("imagePreview");

// Highlight Drop Zone on Drag
dropZone.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropZone.classList.add("drag-hover");
});

// Remove Highlight on Drag Leave
dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("drag-hover");
});

// Handle File Drop
dropZone.addEventListener("drop", (event) => {
    event.preventDefault();
    dropZone.classList.remove("drag-hover");
    const file = event.dataTransfer.files[0];
    if (file) {
        handleFile(file);
    }
});

// Handle File Browse
fileInput.addEventListener("change", (event) => {
    const file = event.target.files[0];
    if (file) {
        handleFile(file);
    }
});

// Handle File Upload
function handleFile(file) {
    if (file.type.startsWith("image/")) {
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            previewContainer.style.display = "block";
        };
        reader.readAsDataURL(file);
    } else {
        alert("Please upload a valid image file.");
    }
}

