# Titanic Data Analysis Project

## Objective
Analyze the Titanic passenger dataset and identify survival patterns.

## Dataset
This project uses the standard Titanic training dataset. Kaggle describes the training set as 891 passengers with the `Survived` target and passenger attributes such as class, sex, age, fare, and embarkation port.

Dataset source:
https://www.kaggle.com/c/titanic/data

A direct CSV source is also included in `download_titanic.py`.

## Project questions
1. What proportion of passengers survived?
2. How does survival differ by sex?
3. How does survival differ by passenger class?
4. Does embarkation port show different survival rates?
5. How are age and fare distributed across passengers and survival outcomes?

## Files
- `titanic_analysis.py` — complete Python analysis
- `Titanic_Data_Analysis.ipynb` — notebook version
- `download_titanic.py` — downloads the CSV
- `titanic.csv` — place the downloaded dataset here
- `report.pdf` — 5-minute project report
- `images/` — project visualizations
- `requirements.txt` — Python packages

## Run locally
```bash
pip install -r requirements.txt
python download_titanic.py
python titanic_analysis.py
```

Or open the notebook in Jupyter/Thonny.

## Main findings from the canonical 891-row training set
- 891 passengers are represented.
- 342 survived and 549 did not.
- Overall survival was about 38.4%.
- Female survival was about 74.2%; male survival was about 18.9%.
- Survival by class was about 63.0% in 1st class, 47.3% in 2nd class, and 24.2% in 3rd class.

These are descriptive statistics from the dataset, not causal conclusions.
