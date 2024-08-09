
// ------------------------------------------------------------
// Dynamic modal content
// ------------------------------------------------------------
const modal = document.getElementById('confirmationModal')

if (modal) {
    modal.addEventListener('show.bs.modal', event => {
        // Button that triggered the modal
        const button = event.relatedTarget;
        // Extract information from button
        const id = button.getAttribute('data-bs-id')
        const name = button.getAttribute('data-bs-name')
        const action = button.getAttribute('data-bs-action')

        // Update the modal's content
        const idField = document.getElementById('modal-field-id')
        const gameField = document.getElementById('modal-field-game')
        const actionField = document.getElementById('modal-field-action')

        idField.value = id
        gameField.value = name
        actionField.value = action
    })
}