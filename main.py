"""
Embeddings Visualization API

This FastAPI application generates t-SNE visualizations of text embeddings
for articles and movies using OpenAI's embedding model.
"""

import json
import os
from typing import Dict, List, Any, Tuple

import matplotlib
matplotlib.use('Agg')  # Set backend before importing pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
from sklearn.manifold import TSNE

# Load environment variables
load_dotenv()

# Configuration constants
OPENAI_API_KEY = os.getenv("OPEN_API_KEY")
EMBEDDING_MODEL = "text-embedding-3-small"
TSNE_COMPONENTS = 2
MIN_PERPLEXITY = 5
FIGURE_SIZE = (10, 8)
FONT_SIZE = 8
STATIC_DIR = "static"

# Initialize FastAPI app and OpenAI client
app = FastAPI(
    title="Embeddings Visualization API",
    description="Generate t-SNE visualizations of text embeddings for articles and movies",
    version="1.0.0"
)
client = OpenAI(api_key=OPENAI_API_KEY)

# Mount static files directory
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Data loading functions
def load_json_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load data from JSON file with error handling.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        List of dictionaries containing the data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"✅ Loaded {len(data)} items from {file_path}")
            return data
    except FileNotFoundError:
        print(f"⚠️ File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"⚠️ JSON decode error in {file_path}: {e}")
        return []
    except Exception as e:
        print(f"⚠️ Error loading {file_path}: {e}")
        return []

# Load data from JSON files
DUMMY_ARTICLES = load_json_data("data/articles.json")
DUMMY_MOVIES = load_json_data("data/movies.json")

# Load Hugging Face movies dataset
try:
    hf_movies_df = pd.read_json("hf://datasets/leemthompo/small-movies/small-movies.json")
    HUGGING_FACE_MOVIES = hf_movies_df.to_dict(orient='records')
    print(f"✅ Loaded {len(HUGGING_FACE_MOVIES)} movies from Hugging Face dataset")
except Exception as e:
    print(f"⚠️ Failed to load Hugging Face dataset: {e}")
    HUGGING_FACE_MOVIES = []


def get_data_by_type(data_type: str, source: str = "dummy") -> Tuple[List[Dict[str, Any]], str, str]:
    """
    Get data by type and source with appropriate text and title fields.
    
    Args:
        data_type: Type of data ("articles" or "movies")
        source: Source of data ("dummy" or "huggingface")
    
    Returns:
        Tuple of (data_list, text_field, title_field)
    """
    if data_type == "movies":
        if source == "huggingface" and HUGGING_FACE_MOVIES:
            return HUGGING_FACE_MOVIES, "plot", "title"
        else:
            return DUMMY_MOVIES, "plot", "title"
    else:  # articles
        return DUMMY_ARTICLES, "content", "title"


def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for a list of texts using OpenAI's embedding model.
    
    Args:
        texts: List of text strings to embed
        
    Returns:
        List of embedding vectors
    """
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )
    embeddings_data = response.model_dump()
    return [item['embedding'] for item in embeddings_data['data']]


def create_tsne_visualization(
    embedding_vectors: List[List[float]], 
    titles: List[str], 
    data_type: str
) -> str:
    """
    Create and save a t-SNE visualization plot.
    
    Args:
        embedding_vectors: List of embedding vectors
        titles: List of titles for annotation
        data_type: Type of data for plot title
        
    Returns:
        Path to the saved image file
    """
    # Perform t-SNE dimensionality reduction
    perplexity = min(MIN_PERPLEXITY, len(embedding_vectors) - 1)
    tsne = TSNE(n_components=TSNE_COMPONENTS, perplexity=perplexity, random_state=42)
    tsne_2d = tsne.fit_transform(np.array(embedding_vectors))
    
    # Create the plot
    plt.figure(figsize=FIGURE_SIZE)
    plt.scatter(tsne_2d[:, 0], tsne_2d[:, 1], alpha=0.7, s=50)
    
    # Add title annotations
    for i, title in enumerate(titles):
        plt.annotate(
            title, 
            (tsne_2d[i, 0], tsne_2d[i, 1]), 
            fontsize=FONT_SIZE,
            alpha=0.8
        )
    
    plt.title(f"t-SNE Visualization of {data_type.title()}", fontsize=14, fontweight='bold')
    plt.xlabel("t-SNE Component 1")
    plt.ylabel("t-SNE Component 2")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save the plot
    os.makedirs(STATIC_DIR, exist_ok=True)
    image_path = os.path.join(STATIC_DIR, f"tsne_{data_type}.png")
    plt.savefig(image_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return image_path


def process_data(request: Request) -> Dict[str, Any]:
    """
    Process data and generate t-SNE visualization.
    
    Args:
        request: FastAPI request object containing query parameters
        
    Returns:
        Dictionary containing processing results and chart URL
    """
    # Extract parameters from request
    data_type = request.query_params.get("type", "articles")
    source = request.query_params.get("source", "dummy")
    
    # Get appropriate data based on type and source
    data, text_field, title_field = get_data_by_type(data_type, source)
    
    print(f"Processing {data_type} ({source} source): {len(data)} items")
    print(f"Sample data: {[item[title_field] for item in data[:3]]}")
    
    # Extract text content for embedding
    texts = [item[text_field] for item in data]
    
    # Generate embeddings
    try:
        embedding_vectors = generate_embeddings(texts)
    except Exception as e:
        print(f"❌ Error generating embeddings: {e}")
        raise
    
    # Add embeddings to data items (for potential future use)
    for i, item in enumerate(data):
        item["embedding"] = embedding_vectors[i]
    
    # Create visualization
    titles = [item[title_field] for item in data]
    try:
        image_path = create_tsne_visualization(embedding_vectors, titles, f"{data_type}_{source}")
    except Exception as e:
        print(f"❌ Error creating visualization: {e}")
        raise
    
    # Build public URL
    base_url = str(request.base_url).rstrip("/")
    image_url = f"{base_url}/static/{os.path.basename(image_path)}"
    
    print(f"✅ Saved t-SNE visualization at {image_path}")
    
    return {
        "type": data_type,
        "source": source,
        "count": len(data),
        "texts": texts,
        "chart_url": image_url,
    }


# API Routes

@app.get("/")
def read_root():
    """Root endpoint with API information."""
    return {
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


@app.get("/process")
def get_processed_data(request: Request):
    """
    Process data and generate t-SNE visualization.
    
    Query Parameters:
        type (str): Type of data to process ("articles" or "movies")
        source (str): Data source ("dummy" or "huggingface" for movies only)
        
    Returns:
        Dictionary containing processing results and visualization URL
    """
    try:
        processed_data = process_data(request)
        return {
            "success": True,
            "data": processed_data
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to process data and generate visualization"
        }