# 🤝 Contributing to Embeddings Visualization API

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/embeddings-visualisation-.git
   cd embeddings-visualisation-
   ```
3. **Set up the development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## 🔧 Development Setup

### Environment Configuration

1. Copy the environment template:
   ```bash
   cp .env.example .env
   ```
2. Add your OpenAI API key to `.env`

### Running Tests

```bash
# Quick data tests (no dependencies)
python test_data_only.py

# Full setup validation
python test_setup.py

# API endpoint tests (server must be running)
python api_test.py
```

### Code Style

- Follow **PEP 8** style guidelines
- Use **type hints** for all function parameters and return values
- Add **docstrings** for public functions and classes
- Keep functions focused and modular

## 📋 Types of Contributions

### 🐛 Bug Reports

When reporting bugs, please include:

- **Clear description** of the issue
- **Steps to reproduce** the problem
- **Expected vs actual behavior**
- **Error logs** and stack traces
- **System information** (OS, Python version, package versions)

### ✨ Feature Requests

For new features:

- **Describe the feature** and its use case
- **Explain why** it would be valuable
- **Provide examples** of how it would work
- **Consider backward compatibility**

### 🔧 Code Contributions

1. **Create a feature branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:

   - Write clean, readable code
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**:

   ```bash
   python test_setup.py
   python -m py_compile main.py
   ```

4. **Commit your changes**:

   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

5. **Push to your fork**:

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub

## 📝 Commit Message Guidelines

Use clear, descriptive commit messages:

- **Add**: New features or functionality
- **Fix**: Bug fixes
- **Update**: Changes to existing features
- **Docs**: Documentation changes
- **Test**: Adding or updating tests
- **Refactor**: Code cleanup without functionality changes

Examples:

```
Add: Support for custom embedding models
Fix: Handle empty dataset gracefully
Update: Improve error messages in API responses
Docs: Add deployment examples to README
```

## 🧪 Testing Guidelines

### Adding Tests

When adding new features:

- Add tests to appropriate test files
- Ensure tests cover edge cases
- Test both success and failure scenarios

### Test Categories

1. **Data Tests** (`test_data_only.py`): JSON loading and validation
2. **Setup Tests** (`test_setup.py`): Environment and dependencies
3. **API Tests** (`api_test.py`): Endpoint functionality

## 📊 Data Contributions

### Adding New Sample Data

To add new sample datasets:

1. **Create JSON files** in the `data/` directory
2. **Follow existing schema**:

   ```json
   // articles.json format
   {
     "id": "number",
     "title": "string",
     "content": "string"
   }

   // movies.json format
   {
     "id": "number",
     "title": "string",
     "plot": "string",
     "genre": "string",
     "released": "number"
   }
   ```

3. **Update data loading functions** in `main.py`
4. **Add tests** for new data formats

## 🎯 Areas for Contribution

### High Priority

- **Docker support** for easy deployment
- **Caching layer** for embeddings (Redis/in-memory)
- **Interactive visualizations** with Plotly
- **Batch processing** capabilities
- **Additional embedding models** support

### Medium Priority

- **3D visualizations** option
- **Custom dataset upload** functionality
- **Export features** (PDF, SVG, PNG)
- **Authentication system**
- **Rate limiting**

### Low Priority

- **UI/Frontend** for the API
- **Database integration**
- **Monitoring and logging**
- **Performance optimizations**

## 📖 Documentation

When updating documentation:

- Keep the **README.md** comprehensive but concise
- Update **API documentation** for endpoint changes
- Include **examples** for new features
- Maintain **deployment guides**

## ❓ Questions?

- **GitHub Discussions**: [Project Discussions](https://github.com/ahmadfreijeh/embeddings-visualisation-/discussions)
- **GitHub Issues**: [Report Issues](https://github.com/ahmadfreijeh/embeddings-visualisation-/issues)

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

**Thank you for contributing! 🎉**
