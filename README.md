# Task 1: Data Cleaning and Preprocessing

## Internship Task
This repository contains my submission for **Task 1: Data Cleaning and Preprocessing** completed as part of my **Data Analyst Internship**.

## Objective
The objective of this task is to clean and prepare a raw dataset by handling missing values, checking duplicates, standardizing column names, converting date formats, and verifying data types.

## Dataset Used
- **Dataset Name:** Netflix Movies and TV Shows
- **Source:** Kaggle
- **File:** `netflix_titles.csv`

## Repository Structure
```
Task-1-Data-Cleaning-and-Preprocessing/
│
├── dataset/
│   ├── netflix_titles.csv
│   └── cleaned_netflix_titles.csv
│
├── code/
│   └── data_cleaning.py
│
├── notebook/
│   └── data_cleaning.ipynb
│
├── report/
│   └── data_cleaning_summary.txt
│
└── README.md
```

## Steps Performed

1. **Handled missing values:**
   - `director` → `Unknown`
   - `cast` → `Unknown`
   - `country` → `Unknown`
   - `rating` → `Not Rated`
   - `duration` → `Unknown`

2. **Checked for duplicate records:**
   - Found **0 duplicate rows**

3. **Standardized column names:**
   - Converted all column headers to lowercase
   - Replaced spaces with underscores

4. **Converted `date_added` column:**
   - Changed to datetime format using Pandas

5. **Verified data types:**
   - Ensured all columns had appropriate data types after cleaning

## Cleaning Summary
| Metric | Value |
|---|---|
| Original rows | 8807 |
| Final rows | 8807 |
| Duplicate rows removed | 0 |

## Tools and Libraries Used
- Python 3
- Pandas
- Jupyter Notebook

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Kushankumarag/Task-1-Data-Cleaning-and-Preprocessing.git
   ```
2. Install dependencies:
   ```bash
   pip install pandas
   ```
3. Run the script:
   ```bash
   python code/data_cleaning.py
   ```

## Key Learning Outcomes
- Identified and treated missing values across multiple columns
- Detected and handled duplicate records
- Standardized column names for consistency
- Converted date columns to proper datetime format
- Improved overall dataset quality for downstream analysis

## Author
**Kushan Kumar**  
Data Analyst Internship | Task 1 Submission
