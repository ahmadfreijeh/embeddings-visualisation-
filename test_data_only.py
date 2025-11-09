#!/usr/bin/env python3
"""
Simple data loading test - tests only the JSON data loading without dependencies.
This can be run even without installing the full requirements.
"""

import json
import os
from pathlib import Path

def test_data_loading():
    """Test that data files can be loaded correctly."""
    print("🧪 Testing data loading...")
    
    # Check if data directory exists
    data_dir = Path("data")
    if not data_dir.exists():
        print("❌ Data directory not found!")
        return False
    
    # Test articles
    try:
        with open("data/articles.json", 'r', encoding='utf-8') as f:
            articles = json.load(f)
        
        print(f"✅ Loaded {len(articles)} articles")
        
        # Validate structure
        if articles and isinstance(articles, list):
            first_article = articles[0]
            required_fields = ['id', 'title', 'content']
            missing_fields = [field for field in required_fields if field not in first_article]
            
            if missing_fields:
                print(f"❌ Articles missing required fields: {missing_fields}")
                return False
            else:
                print("✅ Articles structure is valid")
        else:
            print("❌ Articles data is not a list")
            return False
            
    except Exception as e:
        print(f"❌ Failed to load articles: {e}")
        return False
    
    # Test movies
    try:
        with open("data/movies.json", 'r', encoding='utf-8') as f:
            movies = json.load(f)
        
        print(f"✅ Loaded {len(movies)} movies")
        
        # Validate structure
        if movies and isinstance(movies, list):
            first_movie = movies[0]
            required_fields = ['id', 'title', 'plot']
            missing_fields = [field for field in required_fields if field not in first_movie]
            
            if missing_fields:
                print(f"❌ Movies missing required fields: {missing_fields}")
                return False
            else:
                print("✅ Movies structure is valid")
        else:
            print("❌ Movies data is not a list")
            return False
            
    except Exception as e:
        print(f"❌ Failed to load movies: {e}")
        return False
    
    return True

def test_json_syntax():
    """Test that JSON files have valid syntax."""
    print("\n📝 Testing JSON syntax...")
    
    json_files = ["data/articles.json", "data/movies.json"]
    
    for filepath in json_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                json.load(f)
            print(f"✅ {filepath} has valid JSON syntax")
        except json.JSONDecodeError as e:
            print(f"❌ {filepath} has invalid JSON: {e}")
            return False
        except FileNotFoundError:
            print(f"❌ {filepath} not found")
            return False
        except Exception as e:
            print(f"❌ Error reading {filepath}: {e}")
            return False
    
    return True

def main():
    """Run data-only tests."""
    print("📊 Data Loading Tests")
    print("=" * 30)
    
    tests = [
        test_json_syntax,
        test_data_loading,
    ]
    
    all_passed = True
    
    for test in tests:
        try:
            result = test()
            if not result:
                all_passed = False
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            all_passed = False
    
    print("\n" + "=" * 30)
    if all_passed:
        print("🎉 All data tests passed!")
        print("💡 Data files are ready for the API")
    else:
        print("❌ Some tests failed")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())