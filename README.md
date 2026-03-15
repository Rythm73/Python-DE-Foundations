# 🐍 Python-DE-Foundations

A structured 30-day Python practice plan focused on building
strong foundations for Data Engineering.

## 🎯 Goal
Build Python skills specifically for Data Engineering —
covering functions, data structures, file handling,
SQL, Pandas, and pipeline logic.

---

## 📅 Progress Tracker

| Day | Topic | Status |
|-----|-------|--------|
| Day 01 | Functions, Parameters & Arguments | ✅ |
| Day 02 | Lists, Dictionaries, Loops & Error Handling | ✅ |
| Day 03 | Coming soon... | ⏳ |

---

## 📂 Day 01 — Functions, Parameters & Arguments

### 🔧 Function Basics
- No-parameter functions
- Single & multiple parameters
- Default parameters
- User input inside functions
- Returning multiple values (tuple)

### 📝 String Formatting
- String concatenation (`+`)
- `.format()` method
- f-strings (modern, preferred in Python 3.6+)

### ➕ Math & Logic
- Basic math functions (add, sub, div, pow, mul)
- Dispatcher / Router pattern (`math_router`)

### 📦 Data Structures
- Dictionary creation and return
- List operations (filter, slice, append)
- Nested dictionaries
- `zip()` for parallel iteration

### 📊 Data Processing (DE Focused)
- `generate_schema` → metadata management
- `calculate_stats` → min, max, average in one call
- `count_frequencies` → log analysis and profiling
- `merge_configs` → pipeline config merging
- `invert_mapping` → label encoding and lookups
- `batch_data` → ETL pipeline batching
- `sliding_window` → time-series processing

### 🧹 Data Cleaning
- `clean_text` → regex-based text cleaning
- `clean_currency` → financial data formatting
- `fill_missing_values` → handling NULL values
- `standardize_dates` → date format normalization

---

## 📂 Day 02 — Lists, Dictionaries, Loops & Error Handling

### 🔁 Loops & Iteration
- `for` loops over lists and dictionaries
- `while` loops
- `break`, `continue`, `pass`
- Nested loops
- List comprehensions

### 📦 Lists & Dictionaries (Deep Dive)
- List slicing and indexing
- Dictionary methods (`.keys()`, `.values()`, `.items()`)
- Nested dictionaries and lists
- Sorting and filtering

### ⚠️ Error Handling (DE Critical)
- `try` / `except` — catching errors gracefully
- Catching multiple errors
- `finally` block — closing DB connections
- `raise` — custom validation errors
- `safe_convert` → pipeline-safe type conversion

### 🔧 Real DE Use Cases
- Skipping bad rows instead of crashing pipelines
- Graceful NULL and type handling
- Validating data before loading into database

---

## 🛠️ Tools & Environment
- Language: Python 3
- Editor: VS Code
- OS: macOS

## 📌 How to Use
Each day has its own folder (day_01, day_02...) with
practice files and detailed reference comments.