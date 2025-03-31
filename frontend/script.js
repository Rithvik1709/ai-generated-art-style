document.getElementById("transformButton").addEventListener("click", async () => {
    const fileInput = document.getElementById("imageInput");
    const styleSelect = document.getElementById("styleSelect");
    
    if (!fileInput.files.length) {
        alert("Please select an image");
        return;
    }

    const file = fileInput.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = async () => {
        const imageUrl = reader.result;

        const requestData = {
            image_url: imageUrl,
            style: styleSelect.value
        };

        try {
            const response = await fetch("http://127.0.0.1:5000/transform", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(requestData)
            });

            const data = await response.json();
            if (data.output) {
                document.getElementById("outputImage").src = data.output;
            } else {
                alert("Error processing image");
            }
        } catch (error) {
            console.error("Error:", error);
        }
    };
});
