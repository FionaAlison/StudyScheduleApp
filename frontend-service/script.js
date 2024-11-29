document.addEventListener("DOMContentLoaded", function () {
    const apiBaseSchedule = "http://studyapp.local/schedules";
    const apiBaseQuote = "http://studyapp.local/quotes";
    // Fetch and display schedules
    function fetchSchedules() {
        fetch(apiBaseSchedule)
            .then(response => response.json())
            .then(data => {
                const scheduleList = document.getElementById("schedule-list");
                scheduleList.innerHTML = '';
                data.forEach(schedule => {
                    const li = document.createElement("li");
                    li.innerHTML = `
                        ${schedule.title} - ${schedule.date} at ${schedule.time}
                        <button onclick="editSchedule(${schedule.id})">Edit</button>
                        <button onclick="deleteSchedule(${schedule.id})">Delete</button>
                    `;
                    scheduleList.appendChild(li);
                });
            })
            .catch(error => console.error("Error fetching schedules:", error));
    }

    // Add or update a schedule
    document.getElementById("schedule-form").addEventListener("submit", function (event) {
        event.preventDefault();
        const id = document.getElementById("schedule-id").value;
        const title = document.getElementById("title").value;
        const date = document.getElementById("date").value;
        const time = document.getElementById("time").value;

        const schedule = { title, date, time };

        const method = id ? "PUT" : "POST";
        const url = id ? `${apiBaseSchedule}/${id}` : apiBaseSchedule;

        fetch(url, {
            method,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(schedule),
        })
            .then(response => {
                if (response.ok) {
                    fetchSchedules();
                    resetForm();
                } else {
                    console.error("Error saving schedule:", response.statusText);
                }
            })
            .catch(error => console.error("Network error:", error));
    });

    // Delete a schedule
    window.deleteSchedule = function (id) {
        fetch(`${apiBaseSchedule}/${id}`, { method: "DELETE" })
            .then(response => {
                if (response.ok) fetchSchedules();
            })
            .catch(error => console.error("Error deleting schedule:", error));
    };

    // Edit a schedule
    window.editSchedule = function (id) {
        fetch(`${apiBaseSchedule}/${id}`)
            .then(response => response.json())
            .then(schedule => {
                document.getElementById("schedule-id").value = schedule.id;
                document.getElementById("title").value = schedule.title;
                document.getElementById("date").value = schedule.date;
                document.getElementById("time").value = schedule.time;
                document.getElementById("submit-button").textContent = "Update Schedule";
            })
            .catch(error => console.error("Error fetching schedule:", error));
    };

    // Fetch daily motivational quote
    function fetchQuote() {
        fetch(`${apiBaseQuote}/random`) // Fetching a random quote
            .then(response => response.json())
            .then(data => {
                document.getElementById("quote").textContent = data.quote;
            })
            .catch(error => console.error("Error fetching quote:", error));
    }

    // Refresh quote button
    document.getElementById("refresh-quote").addEventListener("click", fetchQuote);

    // Reset the schedule form
    function resetForm() {
        document.getElementById("schedule-id").value = '';
        document.getElementById("title").value = '';
        document.getElementById("date").value = '';
        document.getElementById("time").value = '';
        document.getElementById("submit-button").textContent = "Add Schedule";
    }

    // Initial fetch for schedules and quote
    fetchSchedules();
    fetchQuote();
});
