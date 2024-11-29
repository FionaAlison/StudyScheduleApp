document.addEventListener("DOMContentLoaded", function () {
    const apiBaseQuote = "http://studyapp.local/quotes";
    // Fetch and display quotes
    function fetchQuotes() {
        fetch(apiBaseQuote)
            .then(response => response.json())
            .then(data => {
                const quoteList = document.getElementById("quote-list");
                quoteList.innerHTML = '';
                data.forEach(quote => {
                    const li = document.createElement("li");
                    li.innerHTML = `
                        ${quote.text}
                        <button onclick="editQuote(${quote.id})">Edit</button>
                        <button onclick="deleteQuote(${quote.id})">Delete</button>
                    `;
                    quoteList.appendChild(li);
                });
            })
            .catch(error => console.error("Error fetching quotes:", error));
    }

    // Add or update a quote
    document.getElementById("quote-form").addEventListener("submit", function (event) {
        event.preventDefault();
        const id = document.getElementById("quote-id").value;
        const text = document.getElementById("quote-text").value;

        const quote = { text };

        const method = id ? "PUT" : "POST";
        const url = id ? `${apiBaseQuote}/${id}` : apiBaseQuote;

        fetch(url, {
            method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(quote),
        })
            .then(response => {
                if (response.ok) {
                    fetchQuotes();
                    resetForm();
                } else {
                    console.error("Error saving quote:", response.statusText);
                }
            })
            .catch(error => console.error("Network error:", error));
    });

    // Delete a quote
    window.deleteQuote = function (id) {
        fetch(`${apiBaseQuote}/${id}`, { method: "DELETE" })
            .then(response => {
                if (response.ok) fetchQuotes();
            })
            .catch(error => console.error("Error deleting quote:", error));
    };

    // Edit a quote
    window.editQuote = function (id) {
        fetch(`${apiBaseQuote}/${id}`)
            .then(response => response.json())
            .then(quote => {
                document.getElementById("quote-id").value = quote.id;
                document.getElementById("quote-text").value = quote.text;
                document.getElementById("quote-submit-button").textContent = "Update Quote";
            })
            .catch(error => console.error("Error fetching quote:", error));
    };

    // Reset the form
    function resetForm() {
        document.getElementById("quote-id").value = '';
        document.getElementById("quote-text").value = '';
        document.getElementById("quote-submit-button").textContent = "Add Quote";
    }

    // Initial fetch
    fetchQuotes();
});
