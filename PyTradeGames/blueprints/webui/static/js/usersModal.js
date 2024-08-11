
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
        const user_id = button.getAttribute('data-bs-myuser')
        const end_user_name = button.getAttribute('data-bs-name');
        const options = button.getAttribute('data-bs-games').split(';').map(games => games.split(','))

        // Update the modal's content
        const start_user_id = modal.querySelector('input#start_user');
        const start_game = modal.querySelector('select#start_game_input');
        const start_game_id = modal.querySelector('input#start_game');
        const end_user = modal.querySelector('input#end_user_input');
        const end_user_id = modal.querySelector('input#end_user');
        const end_game = modal.querySelector('select#end_game_input');
        const end_game_id = modal.querySelector('input#end_game');

        start_user_id.value = user_id;
        end_user.value = end_user_name;
        end_user_id.value = id;

        end_game.innerHTML = '<option value=""></option>';
        for (const opt of options) {
            end_game.innerHTML += '<option value="' + opt[0] + '">' + opt[1] + '</option>';
        }

        start_game.addEventListener('change', selection => {
            start_game_id.value = selection.target.value;
        })

        end_game.addEventListener('change', selection => {
            end_game_id.value = selection.target.value;
        })
    })
}