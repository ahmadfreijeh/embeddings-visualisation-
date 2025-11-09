# 🎬📊 Embeddings Visualization API

A FastAPI application that generates beautiful t-SNE visualizations of text embeddings for articles and movies using OpenAI's embedding model.

[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub repo](https://img.shields.io/badge/GitHub-embeddings--visualisation-black.svg)](https://github.com/ahmadfreijeh/embeddings-visualisation-)
[![OpenAI](https://img.shields.io/badge/OpenAI-text--embedding--3--small-orange.svg)](https://openai.com)

## 🚀 Features

- **Text Embeddings**: Generate high-quality embeddings using OpenAI's `text-embedding-3-small` model
- **t-SNE Visualization**: Create interactive 2D visualizations of embedding clusters
- **Multiple Data Sources**:
  - Local dummy data for testing
  - Hugging Face datasets integration
- **RESTful API**: Clean, documented endpoints with FastAPI
- **Static File Serving**: Automatically generated and served visualization images
- **Error Handling**: Comprehensive error handling with informative responses

## 📁 Project Structure

```
embeddings/
├── main.py              # Main FastAPI application
├── data/                # JSON data files
│   ├── articles.json    # Sample articles for testing
│   └── movies.json      # Sample movies for testing
├── static/              # Generated visualization images
├── test_setup.py        # Complete setup validation
├── test_data_only.py    # Quick data loading test
├── api_test.py          # API endpoint testing
├── start.sh             # Quick start script
├── .env                 # Environment variables (create this)
├── .env.example         # Environment template
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- OpenAI API key
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/ahmadfreijeh/embeddings-visualisation-.git
cd embeddings-visualisation-
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

Create a `.env` file in the root directory:

```env
OPEN_API_KEY=your_openai_api_key_here
```

**⚠️ Important**: Never commit your `.env` file to version control!

### 5. Create Requirements File

```bash
# Generate requirements.txt if it doesn't exist
pip freeze > requirements.txt
```

Expected dependencies:

```
fastapi>=0.100.0
uvicorn>=0.23.0
openai>=1.0.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
numpy>=1.24.0
pandas>=2.0.0
python-dotenv>=1.0.0
python-multipart>=0.0.6
```

## 🚀 Running the Application

### Development Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at:

- **Application**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## ⚡ Quick Start Examples

### 1. Test the API Health

```bash
curl http://localhost:8000/
```

### 2. Process Sample Articles

```bash
curl "http://localhost:8000/process?type=articles"
```

**Expected output:**

- ✅ Generates embeddings for 8 sample articles
- 🎨 Creates `tsne_articles_dummy.png` visualization
- 📊 Shows clustering of ML, cooking, and science topics

### 3. Process Sample Movies

```bash
curl "http://localhost:8000/process?type=movies"
```

**Expected output:**

- ✅ Processes 6 classic movies (Pulp Fiction, The Matrix, etc.)
- 🎨 Creates `tsne_movies_dummy.png` visualization
- 📊 Shows genre-based clustering

### 4. Try Real Movie Dataset

```bash
curl "http://localhost:8000/process?type=movies&source=huggingface"
```

**Expected output:**

- ✅ Processes 100+ real movies from Hugging Face
- 🎨 Creates `tsne_movies_huggingface.png` visualization
- 📊 Shows professional movie data clustering

### 5. Explore Available Data

```bash
curl "http://localhost:8000/data-info"
```

**What you'll get:**

- 📋 Complete list of available fields for each dataset
- 🔍 Sample data structure for each source
- 💡 Field auto-detection priorities

## 📚 API Documentation

### Base URL

```
http://localhost:8000
```

### Endpoints

#### `GET /`

**Description**: API information and documentation

**Response**:

```json
{
  "message": "Welcome to the Embeddings Visualization API!",
  "description": "Generate t-SNE visualizations of text embeddings for articles and movies",
  "endpoints": {
    "/process": "Generate embeddings and visualizations",
    "/process?type=articles": "Process articles (dummy data)",
    "/process?type=movies": "Process movies (dummy data)",
    "/process?type=movies&source=huggingface": "Process movies from Hugging Face dataset"
  },
  "parameters": {
    "type": "Data type: 'articles' or 'movies' (default: 'articles')",
    "source": "Data source: 'dummy' or 'huggingface' (default: 'dummy', only for movies)"
  }
}
```

#### `GET /process`

**Description**: Process data and generate t-SNE visualization

**Query Parameters**:

- `type` (string, optional): Data type to process
  - `articles` (default): Process article data
  - `movies`: Process movie data
- `source` (string, optional): Data source (only for movies)
  - `dummy` (default): Use local JSON data
  - `huggingface`: Use Hugging Face dataset

**Examples**:

```bash
# Process articles (default)
curl "http://localhost:8000/process"

# Process dummy movies
curl "http://localhost:8000/process?type=movies"

# Process Hugging Face movies
curl "http://localhost:8000/process?type=movies&source=huggingface"
```

**Success Response**:

```json
{
  "success": true,
  "data": {
    "type": "articles",
    "source": "dummy",
    "count": 8,
    "texts": ["Machine learning is...", "..."],
    "chart_url": "http://localhost:8000/static/tsne_articles_dummy.png"
  }
}
```

**Error Response**:

```json
{
  "success": false,
  "error": "Error message details",
  "message": "Failed to process data and generate visualization"
}
```

## 🎯 Visual Examples

### Articles Processing

#### Basic Articles Request

```bash
curl "http://localhost:8000/process?type=articles"
```

**Response:**

```json
{
  "success": true,
  "data": {
    "type": "articles",
    "source": "dummy",
    "count": 8,
    "fields_used": {
      "text_field": "content",
      "title_field": "title"
    },
    "available_fields": ["id", "title", "content"],
    "texts": [
      "Machine learning is a subset of artificial intelligence...",
      "Italian cuisine is known for its regional diversity...",
      "The universe is estimated to be 13.8 billion years old..."
    ],
    "chart_url": "http://localhost:8000/static/tsne_articles_dummy.png"
  }
}
```

#### Custom Field Mapping for Articles

```bash
curl "http://localhost:8000/process?type=articles&text_field=content&title_field=title"
```

### Movies Processing

#### Basic Movies Request (Dummy Data)

```bash
curl "http://localhost:8000/process?type=movies"
```

**Response:**

```json
{
  "success": true,
  "data": {
    "type": "movies",
    "source": "dummy",
    "count": 6,
    "fields_used": {
      "text_field": "plot",
      "title_field": "title"
    },
    "available_fields": ["id", "title", "plot", "runtime", "genre", "released"],
    "texts": [
      "The lives of two mob hitmen, a boxer, a gangster and his wife...",
      "A computer programmer is rescued from the Matrix...",
      "A thief who enters people's dreams and steals their secrets..."
    ],
    "chart_url": "http://localhost:8000/static/tsne_movies_dummy.png"
  }
}
```

#### Hugging Face Movies Dataset

```bash
curl "http://localhost:8000/process?type=movies&source=huggingface"
```

**Response:**

```json
{
  "success": true,
  "data": {
    "type": "movies",
    "source": "huggingface",
    "count": 100,
    "fields_used": {
      "text_field": "plot",
      "title_field": "title"
    },
    "available_fields": ["id", "title", "plot", "genre", "year", "director"],
    "texts": [
      "Real movie plot summaries from the Hugging Face dataset...",
      "Professional movie descriptions with rich metadata...",
      "Diverse collection spanning multiple decades and genres..."
    ],
    "chart_url": "http://localhost:8000/static/tsne_movies_huggingface.png"
  }
}
```

#### Custom Field Mapping for Movies

```bash
curl "http://localhost:8000/process?type=movies&text_field=plot&title_field=title&source=huggingface"
```

### Error Handling Examples

#### Invalid Field Names

```bash
curl "http://localhost:8000/process?type=movies&text_field=invalid_field"
```

**Error Response:**

```json
{
  "success": false,
  "error": "Text field 'invalid_field' not found in data and no suitable alternative detected. Available fields: ['id', 'title', 'plot', 'runtime', 'genre', 'released']. Please specify a valid text_field parameter from the available fields.",
  "error_type": "field_validation_error",
  "message": "Field validation failed. Please check available fields using /data-info endpoint.",
  "suggestion": "Use /data-info to see available fields, then specify text_field and/or title_field parameters."
}
```

### Data Information Endpoint

```bash
curl "http://localhost:8000/data-info"
```

**Response:**

```json
{
  "available_data_sources": {
    "articles": {
      "source": "static/dummy",
      "count": 8,
      "fields": ["id", "title", "content"],
      "sample": {
        "id": 1,
        "title": "Machine Learning Basics",
        "content": "Machine learning is a subset of artificial intelligence..."
      }
    },
    "movies_static": {
      "source": "static/dummy",
      "count": 6,
      "fields": ["id", "title", "plot", "runtime", "genre", "released"],
      "sample": {
        "id": 1,
        "title": "Pulp Fiction",
        "plot": "The lives of two mob hitmen, a boxer, a gangster and his wife...",
        "runtime": 154,
        "genre": "Crime",
        "released": 1994
      }
    },
    "movies_huggingface": {
      "source": "huggingface",
      "count": 100,
      "fields": ["id", "title", "plot", "genre", "year", "director"],
      "sample": {
        "id": 1,
        "title": "Sample Movie",
        "plot": "Professional movie description from dataset...",
        "genre": "Drama",
        "year": 2020,
        "director": "Sample Director"
      }
    }
  },
  "field_auto_detection": {
    "text_field_priority": ["content", "plot", "description", "text", "body"],
    "title_field_priority": ["title", "name", "heading", "subject"]
  },
  "usage_examples": {
    "default_articles": "/process?type=articles",
    "default_movies": "/process?type=movies",
    "custom_fields": "/process?type=movies&text_field=plot&title_field=title",
    "huggingface_movies": "/process?type=movies&source=huggingface"
  }
}
```

## 📊 Data Sources

### 1. Local JSON Files

#### Articles (`data/articles.json`)

Sample data covering various topics:

- Machine Learning & AI
- Cooking & Cuisine
- Space & Astronomy

**Schema**:

```json
{
  "id": "number",
  "title": "string",
  "content": "string"
}
```

#### Movies (`data/movies.json`)

Classic movie data including:

- Plot summaries
- Key scenes
- Runtime and genre information

**Schema**:

```json
{
  "id": "number",
  "title": "string",
  "plot": "string",
  "runtime": "number",
  "keyScene": "string",
  "genre": "string",
  "released": "number"
}
```

### 2. Hugging Face Integration

The API integrates with the Hugging Face `leemthompo/small-movies` dataset for additional movie data.

## 🔧 Configuration

### Environment Variables

| Variable       | Description    | Required | Default |
| -------------- | -------------- | -------- | ------- |
| `OPEN_API_KEY` | OpenAI API key | ✅ Yes   | None    |

### Application Constants

Located in `main.py`:

```python
EMBEDDING_MODEL = "text-embedding-3-small"  # OpenAI model
TSNE_COMPONENTS = 2                         # t-SNE dimensions
MIN_PERPLEXITY = 5                          # Minimum perplexity for t-SNE
FIGURE_SIZE = (10, 8)                       # Plot dimensions
FONT_SIZE = 8                               # Annotation font size
STATIC_DIR = "static"                       # Static files directory
```

## 🧪 Testing### Quick Data Test (No Dependencies)

Test just the data loading without installing packages:

```bash
python test_data_only.py
```

This validates:

- JSON file syntax and structure
- Data loading functionality
- Required fields in data

### Setup Validation

Test environment, data, and dependencies:

```bash
python test_setup.py
```

This checks:

- Data files and structure
- Environment configuration
- Package availability
- Code syntax

### API Testing

Test all API endpoints (requires running server):

```bash
python api_test.py
```

This validates:

- Server connectivity
- All endpoint functionality
- Response formats
- Static file serving

### Manual Testing

1. **Health Check**:

```bash
curl http://localhost:8000/
```

2. **Process Articles**:

```bash
curl "http://localhost:8000/process?type=articles"
```

3. **Process Movies**:

```bash
curl "http://localhost:8000/process?type=movies"
```

### Custom Test Scripts

Create a test script (`test_api.py`):

```python
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

def test_process_articles():
    response = requests.get(f"{BASE_URL}/process?type=articles")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] == True
    assert "chart_url" in data["data"]

if __name__ == "__main__":
    test_health()
    test_process_articles()
    print("All tests passed! ✅")
```

## 🐛 Troubleshooting

### Common Issues

1. **OpenAI API Key Error**:

   ```
   Error: Invalid API key
   ```

   **Solution**: Check your `.env` file and ensure `OPEN_API_KEY` is correct.

2. **Module Import Error**:

   ```
   ModuleNotFoundError: No module named 'fastapi'
   ```

   **Solution**: Activate virtual environment and install dependencies.

3. **Hugging Face Dataset Error**:

   ```
   Failed to load Hugging Face dataset
   ```

   **Solution**: Check internet connection. API will fallback to dummy data.

4. **Port Already in Use**:
   ```
   OSError: [Errno 48] Address already in use
   ```
   **Solution**: Use a different port or kill the existing process.

### Debug Mode

Run with debug logging:

```bash
uvicorn main:app --reload --log-level debug
```

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add type hints to all functions
- Include docstrings for public functions
- Add error handling for external API calls
- Update tests when adding new features

## 📈 Performance Considerations

- **Embedding Generation**: ~1-2 seconds per request (depends on text length)
- **t-SNE Computation**: ~2-5 seconds (depends on data size)
- **Memory Usage**: ~50-100MB (depends on dataset size)
- **Rate Limits**: Subject to OpenAI API rate limits

## 🔮 Future Enhancements

- [ ] **Caching**: Redis integration for embedding caching
- [ ] **Authentication**: API key-based access control
- [ ] **Batch Processing**: Process multiple datasets simultaneously
- [ ] **3D Visualizations**: Optional 3D t-SNE plots
- [ ] **Custom Datasets**: Upload and process custom JSON files
- [ ] **Export Options**: PDF, SVG export formats
- [ ] **Interactive Plots**: Plotly integration for interactive visualizations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing excellent embedding models
- **FastAPI** for the robust web framework
- **Scikit-learn** for t-SNE implementation
- **Hugging Face** for dataset integration
- **Matplotlib** for visualization capabilities

---

**Happy coding! 🚀✨**
