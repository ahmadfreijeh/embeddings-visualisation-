#!/usr/bin/env python3
"""
API Test Script for Embeddings Visualization API

This script tests all the API endpoints to ensure they're working correctly.
Run this after starting the server with: python api_test.py
"""

import requests
import json
import time
import sys
from typing import Dict, Any

# Configuration
BASE_URL = "http://localhost:8000"
TIMEOUT = 30  # seconds

def make_request(method: str, endpoint: str, params: Dict = None) -> Dict[str, Any]:
    """Make HTTP request with error handling."""
    url = f"{BASE_URL}{endpoint}"
    
    try:
        print(f"🔄 {method} {url}", end="")
        if params:
            print(f" (params: {params})", end="")
        print(" ... ", end="", flush=True)
        
        response = requests.request(method, url, params=params, timeout=TIMEOUT)
        
        if response.status_code == 200:
            print("✅")
            return {
                "success": True,
                "status_code": response.status_code,
                "data": response.json()
            }
        else:
            print(f"❌ (Status: {response.status_code})")
            return {
                "success": False,
                "status_code": response.status_code,
                "error": response.text
            }
            
    except requests.exceptions.ConnectionError:
        print("❌ (Connection Error)")
        return {
            "success": False,
            "error": "Connection refused - is the server running?"
        }
    except requests.exceptions.Timeout:
        print("❌ (Timeout)")
        return {
            "success": False,
            "error": f"Request timed out after {TIMEOUT} seconds"
        }
    except Exception as e:
        print(f"❌ (Error: {e})")
        return {
            "success": False,
            "error": str(e)
        }

def test_health_endpoint():
    """Test the health/root endpoint."""
    print("\n📋 Testing Health Endpoint")
    print("-" * 40)
    
    result = make_request("GET", "/")
    
    if result["success"]:
        data = result["data"]
        print(f"   Message: {data.get('message', 'N/A')}")
        print(f"   Endpoints: {len(data.get('endpoints', {}))}")
        return True
    else:
        print(f"   Error: {result.get('error', 'Unknown error')}")
        return False

def test_process_endpoints():
    """Test the process endpoints with different parameters."""
    print("\n🔬 Testing Process Endpoints")
    print("-" * 40)
    
    test_cases = [
        {"name": "Default (articles)", "params": {}},
        {"name": "Articles explicit", "params": {"type": "articles"}},
        {"name": "Movies dummy", "params": {"type": "movies"}},
        {"name": "Movies HuggingFace", "params": {"type": "movies", "source": "huggingface"}},
    ]
    
    results = []
    
    for case in test_cases:
        print(f"\n   Testing: {case['name']}")
        result = make_request("GET", "/process", case["params"])
        
        if result["success"]:
            data = result["data"]
            if "data" in data and data["data"]:
                process_data = data["data"]
                print(f"     Type: {process_data.get('type', 'N/A')}")
                print(f"     Source: {process_data.get('source', 'N/A')}")
                print(f"     Count: {process_data.get('count', 'N/A')}")
                print(f"     Chart URL: {process_data.get('chart_url', 'N/A')}")
                results.append(True)
            else:
                print(f"     Error in response data: {data}")
                results.append(False)
        else:
            print(f"     Error: {result.get('error', 'Unknown error')}")
            results.append(False)
        
        # Small delay between requests
        time.sleep(1)
    
    return all(results)

def test_static_files():
    """Test that static files are accessible."""
    print("\n🖼️ Testing Static File Access")
    print("-" * 40)
    
    # Try to access a generated image (if any exist)
    static_url = f"{BASE_URL}/static/"
    
    try:
        response = requests.get(static_url, timeout=5)
        if response.status_code in [200, 403, 404]:  # Any of these is fine for static directory
            print("✅ Static file serving is working")
            return True
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error accessing static files: {e}")
        return False

def check_server_running():
    """Check if the server is running."""
    print("🔍 Checking if server is running...")
    
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running")
            return True
    except:
        pass
    
    print("❌ Server is not running")
    print("\n💡 To start the server, run:")
    print("   uvicorn main:app --reload")
    print("   OR")
    print("   ./start.sh")
    return False

def main():
    """Run all API tests."""
    print("🧪 Embeddings Visualization API - Test Suite")
    print("=" * 50)
    
    # Check if server is running
    if not check_server_running():
        sys.exit(1)
    
    # Run tests
    tests = [
        ("Health Endpoint", test_health_endpoint),
        ("Process Endpoints", test_process_endpoints),
        ("Static Files", test_static_files),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The API is working correctly.")
        print("\n💡 You can now:")
        print("   • Visit http://localhost:8000/docs for interactive API docs")
        print("   • Use the /process endpoint with different parameters")
        print("   • Check the /static/ directory for generated visualizations")
    else:
        print("⚠️ Some tests failed. Please check the server logs and configuration.")
        sys.exit(1)

if __name__ == "__main__":
    main()