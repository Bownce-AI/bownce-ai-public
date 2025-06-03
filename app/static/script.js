const convHist = [];

/**
 * @description This script handles the interaction with the OpenAI API and
 * updates the UI accordingly.
 * @returns {Promise<void>}
 */
async function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    const messagesDiv = document.getElementById("messages");

    const userMessage = document.createElement("p");
    userMessage.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    messagesDiv.appendChild(userMessage);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    const aiMessage = document.createElement("p");
    //aiMessage.innerHTML += `<p><strong>AI:</strong></p>`;
    messagesDiv.appendChild(aiMessage);

    convHist.push({ role: "user", content: userInput });

    // Clear the input field
    document.getElementById("userInput").value = "";


    const response = await fetch("http://192.168.178.150:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: convHist })
    });

    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");
    let done = false;
    let fullResponse = "";
    let accumulatedChunks = "";

    while (!done) {
        const { value, done: readingDone } = await reader.read();
        done = readingDone;

        if (value) {
            const chunk = decoder.decode(value, { stream: true });
            accumulatedChunks += chunk;

            aiMessage.innerHTML = `<p><strong>AI:</strong></p>` + marked.parse(accumulatedChunks); // Append formatted chunk to the message
            messagesDiv.scrollTop = messagesDiv.scrollHeight; // Scroll to the bottom
        }
    }
    fullResponse = accumulatedChunks; // Store the full response
    //formattedResponse = formattedResponse.replace(/<\/li>/g, '</li><br>\n');
    convHist.push({ role: "assistant", content: fullResponse });
    console.log(convHist);
}

document.getElementById("userInput").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("sendButton").click();
    }
});

const userInput = document.getElementById("userInput");
userInput.addEventListener("input", () => {
    userInput.style.height = "auto";
    userInput.style.height = "${userInput.scrollHeight}px";
});
