
// ------------------------------------------------------------
// Dynamic modal content
// ------------------------------------------------------------
const modal = document.getElementById('confirmationModal')

if (modal) {
    modal.addEventListener('show.bs.modal', event => {
        // Button that triggered the modal
        const button = event.relatedTarget;
    })
}