#!/bin/bash

# Quick Start Script for Embeddings Visualization API
# This script helps developers get the API running quickly

set -e  # Exit on any error

echo "🚀 Embeddings Visualization API - Quick Start"
echo "=============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️ $1${NC}"
}

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

print_status "Python 3 found: $(python3 --version)"

# Check if we're in a virtual environment
if [[ "$VIRTUAL_ENV" != "" ]]; then
    print_status "Virtual environment is active: $VIRTUAL_ENV"
else
    print_warning "No virtual environment detected."
    echo "Creating virtual environment..."
    
    # Create virtual environment
    python3 -m venv venv
    
    # Activate it
    source venv/bin/activate
    
    print_status "Virtual environment created and activated"
fi

# Install dependencies
echo ""
print_info "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

print_status "Dependencies installed successfully"

# Check .env file
echo ""
if [ ! -f ".env" ]; then
    print_warning ".env file not found. Creating from template..."
    cp .env.example .env
    print_warning "Please edit .env file and add your OpenAI API key!"
    echo ""
    echo "Edit the .env file:"
    echo "OPEN_API_KEY=your_actual_openai_api_key_here"
    echo ""
    read -p "Press Enter after you've updated the .env file..."
else
    print_status ".env file exists"
fi

# Run setup tests
echo ""
print_info "Running setup tests..."
python test_setup.py

# Start the server
echo ""
print_info "Starting the API server..."
echo "The API will be available at:"
echo "  • Main API: http://localhost:8000"
echo "  • Interactive Docs: http://localhost:8000/docs"
echo "  • Alternative Docs: http://localhost:8000/redoc"
echo ""
print_info "Press Ctrl+C to stop the server"
echo ""

# Start the server with uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000