# Spreadsheet Data Cleaner

A simple, lightweight **Python-based Excel data cleaning script** designed to automate common spreadsheet cleanup tasks.

This tool takes an Excel file (`.xlsx`) as input and outputs a cleaned version with standardized formatting, fixed columns, normalized dates, and missing values handled automatically.

---

## Features

The script performs multiple automatic cleaning steps:

### 1. Column Standardization

* Converts all column names to lowercase
* Trims spaces
* Replaces internal spaces with underscores
  Example:
  `"Join Date "` → `"join_date"`

### 2. Text Cleanup

Applied to all string columns:

* Removes leading/trailing whitespace
* Converts text to Title Case
  Example:
  `"   alice   smith "` → `"Alice Smith"`

### 3. Date Normalization

Any column containing `date` in its name is parsed and converted to:

```
YYYY-MM-DD
```

### 4. Missing Value Handling

For both text and numeric columns:

* Fills all null values with `"unknown"`

### 5. Duplicate Removal

Removes fully duplicated rows.

### 6. Output

Saves a cleaned version of your file as:

```
cleaned_<original_filename>.xlsx
```

---

## Sample Dataset Included

A sample spreadsheet is included at:

```
sample_dataset/test.xlsx
```

Use it to test how the script cleans messy real-world data.

---

## How to Use

### 1. Make a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate    # .venv\Scripts\activate for Windows
```

### 2. Install dependencies

```bash
pip install pandas openpyxl
```

### 3. Run the script

```bash
python main.py <your_file.xlsx>
```

Example:

```bash
python main.py sample_dataset/test.xlsx
```

---

## Use Case Examples

* Customer Success Teams cleaning client-uploaded spreadsheets
* Data preprocessing before loading into databases
* Automation replacements for Excel manual cleanup
* Learning basic Python/Pandas data manipulation

---
