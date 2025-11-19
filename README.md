# AI-Generated Art Style Transformer

Transform your images into stunning artwork with various artistic styles using AI! This web application uses the Replicate API to apply different art styles to your images, including Studio Ghibli, Minecraft, Spider-Verse, and classic painting styles.

## 🎨 Features

- **Multiple Art Styles**: Choose from 8 different artistic transformations:
  - 🎬 **Studio Ghibli** - Anime-inspired artistic style
  - 🧱 **Minecraft** - Blocky, pixelated game aesthetic
  - 🎭 **Cartoon** - Playful cartoon-style rendering
  - 🕷️ **Spider-Verse** - Comic book and animated movie style
  - ✏️ **Pencil Sketch** - Hand-drawn pencil art
  - 🎨 **Watercolor** - Soft, flowing watercolor painting
  - 🖼️ **Oil Painting** - Classical oil painting texture
  - 🌟 **Van Gogh** - Impressionist style inspired by Vincent van Gogh

- **Easy to Use**: Simple web interface with drag-and-drop functionality
- **Fast Processing**: Powered by Replicate's AI models
- **RESTful API**: Backend API for programmatic access

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)
- A modern web browser (Chrome, Firefox, Safari, or Edge)
- A Replicate API key ([Get one here](https://replicate.com/))

## 🚀 Installation

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install the required Python dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your Replicate API key:
   - Open `backend/app.py`
   - Replace the placeholder API key on line 9 with your own:
   ```python
   REPLICATE_API_KEY = "your_api_key_here"
   ```

### Frontend Setup

No additional installation is required for the frontend. It's a static HTML/CSS/JS application.

## 🎮 Usage

### Starting the Application

1. **Start the Backend Server**:
```bash
cd backend
python app.py
```
The Flask server will start on `http://127.0.0.1:5000`

2. **Open the Frontend**:
   - Open `frontend/index.html` in your web browser
   - Or serve it using a local server:
   ```bash
   cd frontend
   python -m http.server 8000
   ```
   Then navigate to `http://localhost:8000` in your browser

### Transforming an Image

1. Click on the file input to select an image from your device
2. Choose your desired art style from the dropdown menu
3. Click the "Transform" button
4. Wait for the AI to process your image
5. View your transformed artwork!

## 🔌 API Documentation

### Transform Endpoint

**POST** `/transform`

Transforms an image URL into a specified art style.

#### Request Body
```json
{
  "image_url": "base64_encoded_image_or_url",
  "style": "ghibli"
}
```

#### Available Styles
- `ghibli`
- `minecraft`
- `cartoon`
- `spiderverse`
- `pencil_sketch`
- `watercolor`
- `oil_painting`
- `van_gogh`

#### Response
```json
{
  "output": "url_to_transformed_image",
  "status": "processing/completed"
}
```

#### Error Response
```json
{
  "error": "Error message"
}
```

## 📁 Project Structure

```
ai-generated-art-style/
├── backend/
│   ├── app.py              # Flask API server
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html         # Main HTML page
│   ├── script.js          # JavaScript for image handling
│   └── styles.css         # Styling for the UI
└── README.md              # Project documentation
```

## 🛠️ Technologies Used

- **Backend**: 
  - Flask (Python web framework)
  - Flask-CORS (Cross-Origin Resource Sharing)
  - Requests (HTTP library)
  - Replicate API (AI model hosting)

- **Frontend**: 
  - HTML5
  - CSS3
  - Vanilla JavaScript

## ⚙️ Configuration

### Replicate API Key

To use this application, you need a Replicate API key:

1. Sign up at [Replicate](https://replicate.com/)
2. Navigate to your account settings
3. Generate an API token
4. Add the token to `backend/app.py`:
```python
REPLICATE_API_KEY = "your_api_key_here"
```

### CORS Configuration

The backend is configured to accept requests from any origin. To restrict this in production:

```python
CORS(app, origins=["http://your-frontend-domain.com"])
```

## 🐛 Troubleshooting

### Common Issues

**"Request must be JSON" error**
- Ensure the Content-Type header is set to `application/json`

**"Invalid style" error**
- Verify you're using one of the supported style names

**Image not loading**
- Check that the backend server is running on port 5000
- Verify your Replicate API key is valid
- Ensure your image is in a supported format (JPG, PNG)

**CORS errors**
- Make sure Flask-CORS is installed
- Verify the backend is running before accessing the frontend

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
