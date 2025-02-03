document.addEventListener("DOMContentLoaded", function () {
    // Helper function to update an image based on the select element change.
    function updateImage(selectId, imageId) {
        const selectElem = document.getElementById(selectId);
        selectElem.addEventListener("change", function () {
            // Get the currently selected option.
            const selectedOption = selectElem.options[selectElem.selectedIndex];
            // Retrieve the image URL from the data attribute.
            const newImageUrl = selectedOption.getAttribute("data-img");
            // Update the corresponding image element's src attribute.
            document.getElementById(imageId).setAttribute("src", newImageUrl);
        });
    }

    // Set up the event listeners for each card.
    updateImage("suspectSelect", "suspectImage");
    updateImage("weaponSelect", "weaponImage");
    updateImage("roomSelect", "roomImage");
})