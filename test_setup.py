#!/usr/bin/env python3
"""
Simple test script to verify the API setup and data loading.
"""

import json
import os
import sys
from pathlib import Path

def test_data_files():
    """Test that data files exist and are valid JSON."""
    print("🧪 Testing data files...")
    
    data_dir = Path("data")
    if not data_dir.exists():
        print("❌ Data directory doesn't exist!")
        return False
    
    files_to_test = ["articles.json", "movies.json"]
    
    for filename in files_to_test:
        filepath = data_dir / filename
        
        if not filepath.exists():
            print(f"❌ {filename} doesn't exist!")
            return False
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"✅ {filename}: {len(data)} items loaded")
        except json.JSONDecodeError as e:
            print(f"❌ {filename}: Invalid JSON - {e}")
            return False
        except Exception as e:
            print(f"❌ {filename}: Error - {e}")
            return False
    
    return True

def test_env_setup():
    """Test environment setup."""
    print("\n🔧 Testing environment setup...")
    
    # Check if .env.example exists
    if Path(".env.example").exists():
        print("✅ .env.example template found")
    else:
        print("⚠️ .env.example template not found")
    
    # Check if .env exists
    if Path(".env").exists():
        print("✅ .env file found")
        # Try to load it
        try:
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv("OPEN_API_KEY")
            if api_key and api_key != "your_openai_api_key_here":
                print("✅ OpenAI API key is configured")
            else:
                print("⚠️ OpenAI API key not properly configured")
        except ImportError:
            print("⚠️ python-dotenv not installed")
    else:
        print("⚠️ .env file not found - create one from .env.example")
    
    return True

def test_imports():
    """Test that all required packages can be imported."""
    print("\n📦 Testing package imports...")
    
    required_packages = [
        ("fastapi", "FastAPI"),
        ("uvicorn", "Uvicorn"),
        ("openai", "OpenAI"),
        ("sklearn", "scikit-learn"),
        ("matplotlib", "Matplotlib"),
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("dotenv", "python-dotenv")
    ]
    
    all_imports_ok = True
    
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"✅ {name}")
        except ImportError:
            print(f"❌ {name} - install with: pip install {package}")
            all_imports_ok = False
        except Exception as e:
            print(f"❌ {name} - error: {e}")
            all_imports_ok = False
    
    return all_imports_ok

def test_main_syntax():
    """Test that main.py has valid Python syntax."""
    print("\n🐍 Testing main.py syntax...")
    
    try:
        import py_compile
        py_compile.compile('main.py', doraise=True)
        print("✅ main.py syntax is valid")
        return True
    except py_compile.PyCompileError as e:
        print(f"❌ Syntax error in main.py: {e}")
        return False
    except Exception as e:
        print(f"❌ Error checking main.py: {e}")
        return False

def test_data_loading_only():
    """Test just the data loading functionality without importing main.py."""
    print("\n📊 Testing data loading functionality...")
    
    try:
        # Test the data loading function in isolation
        import json
        
        def load_json_data(file_path: str):
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        
        articles = load_json_data("data/articles.json")
        movies = load_json_data("data/movies.json")
        
        print(f"✅ Articles: {len(articles)} items loaded")
        print(f"✅ Movies: {len(movies)} items loaded")
        
        # Validate structure
        if articles and 'title' in articles[0] and 'content' in articles[0]:
            print("✅ Articles structure is valid")
        else:
            print("❌ Articles structure is invalid")
            return False
            
        if movies and 'title' in movies[0] and 'plot' in movies[0]:
            print("✅ Movies structure is valid")
        else:
            print("❌ Movies structure is invalid")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Data loading failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Running API setup tests...\n")
    
    # Run tests
    tests = [
        ("Data Files", test_data_files),
        ("Environment Setup", test_env_setup),
        ("Data Loading Logic", test_data_loading_only),
        ("Package Imports", test_imports),
        ("Main.py Syntax", test_main_syntax),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*50)
    print("📋 TEST SUMMARY")
    print("="*50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Ready to run the API.")
        print("\n💡 Next steps:")
        print("   1. Ensure .env file has your OpenAI API key")
        print("   2. Run: uvicorn main:app --reload")
        print("   3. Visit: http://localhost:8000")
    else:
        print("⚠️ Some tests failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()