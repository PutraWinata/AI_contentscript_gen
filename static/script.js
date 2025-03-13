function generateContent() {
    const targetAudience = document.getElementById("target").value;
    const goal = document.getElementById("goal").value;
    const platform = document.getElementById("platform").value;
    const videoLength = document.getElementById("video_length").value;
    const style = document.getElementById("style").value;
    const cta = document.getElementById("cta").value;

    const loadingModal = document.getElementById("loading-modal");
    loadingModal.style.display = "flex"; // Show loading modal

    fetch("/generate", {
        method: "POST",
        body: JSON.stringify({
            target: targetAudience, 
            goal, 
            platform, 
            video_lenght: videoLength, 
            style, 
            cta
        }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        loadingModal.style.display = "none"; // Hide loading modal
        
        const responseContainer = document.getElementById("ai-response");
        responseContainer.innerHTML = ""; // Clear previous results
        document.getElementById("result").style.display = "block";

        const contentIdeas = data.content_ideas.split("\n\n");

        contentIdeas.forEach((idea) => {
            if (idea.trim() !== "") {
                const listItem = document.createElement("li");
                listItem.innerHTML = idea
                    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
                    .replace(/\n/g, "<br>");
                responseContainer.appendChild(listItem);
            }
        });
    })
    .catch(error => {
        console.error("Error:", error);
        loadingModal.style.display = "none"; // Hide modal on error
    });
}
    