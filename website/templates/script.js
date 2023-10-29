var draggedElement = null;
var items;

function handleDragStart(e) {
    console.log('running')
    this.style.opacity = "0.4";
    draggedElement = this;

    e.dataTransfer.effectAllowed = "move";
    e.dataTransfer.setData("item", this.innerHTML);
}

function handleDragOver(e) {
    if (e.preventDefault) 
        e.preventDefault();

    e.dataTransfer.dropEffect = "move";
    return false;
}

function handleDragEnter(e) {
    this.classList.add("dragover");
}

function handleDragLeave(e) {
    this.classList.remove("dragover");
}

function handleDrop(e) {
    console.log('running')
    if (e.stopPropagation)
        e.stopPropagation();

    if (draggedElement != this) {
        let attri = draggedElement.getAttribute('data-item')
        draggedElement.innerHTML = this.innerHTML;
        draggedElement.setAttribute("data-item", this.getAttribute('data-item'));

        let replacedItem = e.dataTransfer.getData("item");
        this.innerHTML = replacedItem;
        this.setAttribute("data-item", attri);
    }

    return false;
}

function handleDragEnd(e) {
    this.style.opacity = "1";

    items.forEach(function(item) {
        item.classList.remove("dragover");
    });
}

document.addEventListener("DOMContentLoaded", event => {
    items = document.querySelectorAll(".container .box");

    items.forEach(function(item) {
      item.addEventListener("dragstart", handleDragStart);
      item.addEventListener("dragenter", handleDragEnter);
      item.addEventListener("dragover", handleDragOver);
      item.addEventListener("dragleave", handleDragLeave);
      item.addEventListener("drop", handleDrop);
      item.addEventListener("dragend", handleDragEnd);
    });
});
