#!/usr/bin/env python3
"""
Test the enhanced field validation and error handling
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_field_validation():
    """Test field validation with invalid field names"""
    print("🧪 Testing field validation and error handling...")
    
    # Test with invalid text field
    print("\n1. Testing invalid text_field:")
    response = requests.get(f"{BASE_URL}/process?type=movies&text_field=invalid_field")
    result = response.json()
    print(f"   Status: {response.status_code}")
    print(f"   Success: {result.get('success', 'N/A')}")
    print(f"   Error Type: {result.get('error_type', 'N/A')}")
    print(f"   Error: {result.get('error', 'No error message')[:100]}...")
    
    # Test with invalid title field
    print("\n2. Testing invalid title_field:")
    response = requests.get(f"{BASE_URL}/process?type=movies&title_field=invalid_field")
    result = response.json()
    print(f"   Status: {response.status_code}")
    print(f"   Success: {result.get('success', 'N/A')}")
    print(f"   Error Type: {result.get('error_type', 'N/A')}")
    print(f"   Error: {result.get('error', 'No error message')[:100]}...")
    
    # Test with both invalid fields
    print("\n3. Testing both invalid fields:")
    response = requests.get(f"{BASE_URL}/process?type=movies&text_field=bad_field&title_field=bad_title")
    result = response.json()
    print(f"   Status: {response.status_code}")
    print(f"   Success: {result.get('success', 'N/A')}")
    print(f"   Error Type: {result.get('error_type', 'N/A')}")
    print(f"   Error: {result.get('error', 'No error message')[:100]}...")
    
    # Test valid fields (should work)
    print("\n4. Testing valid fields:")
    response = requests.get(f"{BASE_URL}/process?type=movies&text_field=plot&title_field=title")
    result = response.json()
    print(f"   Status: {response.status_code}")
    print(f"   Success: {result.get('success', 'N/A')}")
    if result.get('success'):
        print(f"   Data Type: {result['data'].get('type', 'N/A')}")
        print(f"   Count: {result['data'].get('count', 'N/A')}")
        print(f"   Fields Used: {result['data'].get('fields_used', 'N/A')}")
    
    print("\n✅ Field validation tests completed!")

def test_data_info():
    """Test the data-info endpoint"""
    print("\n🔍 Testing /data-info endpoint:")
    response = requests.get(f"{BASE_URL}/data-info")
    result = response.json()
    print(f"   Status: {response.status_code}")
    print("   Available data sources:")
    for source_name, source_info in result.get('available_data_sources', {}).items():
        print(f"     - {source_name}: {source_info.get('count', 0)} items")
        print(f"       Fields: {source_info.get('fields', [])}")

if __name__ == "__main__":
    try:
        print("🚀 Starting API validation tests...")
        
        # Test data info first
        test_data_info()
        
        # Test field validation
        test_field_validation()
        
        print("\n🎉 All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the API server.")
        print("   Please make sure the server is running with: uvicorn main:app --reload")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")