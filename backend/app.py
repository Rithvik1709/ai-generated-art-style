from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# ✅ Replace with your Replicate API Key
REPLICATE_API_KEY = "r8_6j8DP3V3PPiEFsz3UvWKtRmq0NAXUca2eIXIj"

# ✅ Model Versions for Different Styles
MODEL_VERSIONS = {
    "ghibli": "timothybrooks/instruct-pix2pix",
    "minecraft": "stability-ai/stable-diffusion-xl",
    "cartoon": "timothybrooks/instruct-pix2pix",
    "spiderverse": "stability-ai/stable-diffusion-xl",
    "pencil_sketch": "stability-ai/stable-diffusion-xl",
    "watercolor": "stability-ai/stable-diffusion-xl",
    "oil_painting": "stability-ai/stable-diffusion-xl",
    "van_gogh": "timothybrooks/instruct-pix2pix"
}

@app.route("/transform", methods=["POST"])
def transform_image():
    try:
        # ✅ Ensure JSON request
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 415

        data = request.get_json()
        image_url = data.get("image_url")
        style = data.get("style")

        if not image_url or not style:
            return jsonify({"error": "Image URL and style are required"}), 400

        if style not in MODEL_VERSIONS:
            return jsonify({"error": "Invalid style"}), 400

        headers = {
            "Authorization": f"Token {REPLICATE_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "version": MODEL_VERSIONS[style],
            "input": {"image": image_url}
        }

        # ✅ Send request to Replicate API
        response = requests.post("https://api.replicate.com/v1/predictions", json=payload, headers=headers, verify=False)

        if response.status_code != 200:
            return jsonify({"error": response.json()}), response.status_code

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
