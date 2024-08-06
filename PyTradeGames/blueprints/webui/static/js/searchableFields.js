// ------------------------------------------------------------
// Searchable fields on table
// ------------------------------------------------------------
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".search-input").forEach(inputField=> {
        const tableRows = inputField.closest("table").querySelectorAll("tbody tr");
        const headerCell = inputField.closest("th");
        const otherHeaderCells = inputField.closest("tr").querySelectorAll("th");
        const columnIndex = Array.from(otherHeaderCells).indexOf(headerCell);
        const searchableCells = Array.from(tableRows)
            .map(row => row.querySelectorAll("td")[columnIndex-1]);
        
        inputField.addEventListener("input", () => {
            const searchQuery = inputField.value.toLowerCase();

            for (const tableCell of searchableCells) {
                const row = tableCell.closest("tr");
                const value = tableCell.textContent
                    .toLowerCase();
                
                row.style.visibility = null;

                if (value.search(searchQuery) === -1) {
                    row.style.visibility = "collapse";
                }
            }
        })
    })
})