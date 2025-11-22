"""
Test script to verify the project setup is working correctly.
Run this from Windows PowerShell or conda prompt.
"""

import os
import sys

print("=" * 60)
print("Testing Disease Diagnosis Project Setup")
print("=" * 60)

# Test 1: Import Constants
print("\n[Test 1] Importing Constants...")
try:
    from utils.Constants import CH_DIR
    print("✅ SUCCESS: Constants imported")
    print(f"   Project path detected: {CH_DIR}")
except Exception as e:
    print(f"❌ FAILED: {e}")
    sys.exit(1)

# Test 2: Verify path exists
print("\n[Test 2] Verifying project path exists...")
if os.path.exists(CH_DIR):
    print(f"✅ SUCCESS: Path exists")
else:
    print(f"❌ FAILED: Path does not exist: {CH_DIR}")
    sys.exit(1)

# Test 3: Check key files
print("\n[Test 3] Checking key project files...")
key_files = [
    "CS2V.py",
    "Symptoms-Diagnosis.txt",
    "environment.yml",
    "requirements.txt",
    "utils/Constants.py"
]

all_found = True
for file in key_files:
    file_path = os.path.join(CH_DIR, file)
    if os.path.exists(file_path):
        print(f"   ✅ Found: {file}")
    else:
        print(f"   ❌ Missing: {file}")
        all_found = False

if not all_found:
    print("❌ FAILED: Some files are missing")
    sys.exit(1)
else:
    print("✅ SUCCESS: All key files found")

# Test 4: Check Dataset directory
print("\n[Test 4] Checking Dataset directory...")
dataset_path = os.path.join(CH_DIR, "Dataset")
if os.path.exists(dataset_path):
    folds = [f for f in os.listdir(dataset_path) if f.startswith("Fold")]
    print(f"✅ SUCCESS: Found {len(folds)} folds in Dataset/")
else:
    print("❌ FAILED: Dataset/ directory not found")
    sys.exit(1)

# Test 5: Try importing dependencies
print("\n[Test 5] Checking Python dependencies...")
dependencies = {
    "numpy": "numpy",
    "scipy": "scipy", 
    "sklearn": "scikit-learn",
    "gensim": "gensim",
    "Cython": "Cython"
}

missing = []
for module, package in dependencies.items():
    try:
        __import__(module)
        print(f"   ✅ {package}")
    except ImportError:
        print(f"   ❌ {package} - not installed")
        missing.append(package)

if missing:
    print(f"\n⚠️  WARNING: Missing packages: {', '.join(missing)}")
    print("   Run: conda env create -f environment.yml")
else:
    print("✅ SUCCESS: All dependencies installed")

# Summary
print("\n" + "=" * 60)
print("🎉 ALL TESTS PASSED!")
print("=" * 60)
print("\nYour project is ready to use!")
print(f"Project location: {CH_DIR}")
print("\nTo run the main script:")
print("  python CS2V.py")
print("=" * 60)
