# 🚀 Quick Deployment Guide

This guide helps you get the Embeddings Visualization API running quickly.

## ⚡ One-Command Setup

```bash
git clone https://github.com/ahmadfreijeh/embeddings-visualisation-.git
cd embeddings-visualisation-
./start.sh
```

The `start.sh` script will:

- Create a virtual environment
- Install all dependencies
- Guide you through environment setup
- Start the development server

## 🔧 Manual Setup

If you prefer manual setup:

```bash
# 1. Clone and enter directory
git clone https://github.com/ahmadfreijeh/embeddings-visualisation-.git
cd embeddings-visualisation-

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment
cp .env.example .env
# Edit .env file and add your OpenAI API key

# 5. Test setup
python test_data_only.py    # Quick test (no dependencies needed)
python test_setup.py        # Full test (after pip install)

# 6. Run the server
uvicorn main:app --reload
```

## 🌐 Access the API

Once running, visit:

- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Test the Endpoints

```bash
# Test with curl
curl "http://localhost:8000/process?type=articles"
curl "http://localhost:8000/process?type=movies"

# Or run the test suite
python api_test.py
```

## ⚙️ Environment Variables

Create a `.env` file with:

```env
OPEN_API_KEY=your_openai_api_key_here
```

Get your OpenAI API key from: https://platform.openai.com/api-keys

## 🐳 Docker (Coming Soon)

Docker support will be added in future releases for even easier deployment.

## 📞 Need Help?

- 📖 **Full Documentation**: [README.md](README.md)
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/ahmadfreijeh/embeddings-visualisation-/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/ahmadfreijeh/embeddings-visualisation-/discussions)

---

**Happy coding! 🚀✨**
