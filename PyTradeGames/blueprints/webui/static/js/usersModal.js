
// ------------------------------------------------------------
// Dynamic modal content
// ------------------------------------------------------------
const modal = document.getElementById('confirmationModal')

if (modal) {
    modal.addEventListener('show.bs.modal', event => {
        // Button that triggered the modal
        const button = event.relatedTarget;
        // Extract information from button
        const id = button.getAttribute('data-bs-id');
        const name = button.getAttribute('data-bs-name');
        const options = button.getAttribute('data-bs-games').split(';').map(games => games.split(','))

        for (const option of options) {
            console.log(option)
        }

        // Update the modal's content
        const idField = document.getElementById('modal-field-id');
        const gameField = document.getElementById('modal-field-game');

        idField.value = id;
        gameField.value = name;
    })
}