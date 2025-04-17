# Stock Market Trends Based on News Headlines

This project explores the relationship between **news headline sentiment** and the **daily percentage change in the S&P 500 index** using historical data and basic machine learning techniques.

---

## Objective

To determine whether **daily news sentiment** has a predictive or explanatory impact on **stock market performance**, specifically the S&P 500.

---

## Files in This Repo

| File | Description |
|------|-------------|
| `sp500_cleaned_2018_2023.csv` | Cleaned S&P 500 historical data with daily percent changes |


---

##  Tools & Libraries Used

- `yfinance` for downloading stock data
- `pandas` for data cleaning and manipulation
- `matplotlib` for plotting
- `scikit-learn` for linear regression modeling

---

## Analysis Steps

1. **Download S&P 500 data** from 2018–2023 using `yfinance`
2. **Calculate daily % change** in closing prices
3. **Load news headlines** and compute daily average sentiment score
4. **Merge datasets** on the date column
5. **Visualize** the relationship using scatter plots
6. **Run linear regression** to measure how well sentiment predicts stock movement
7. **Evaluate** using regression coefficients and R² score

---

## Results

- A linear regression model was fitted on sentiment vs. market movement.
- The **regression line** was almost flat, and the **R² score was close to 0**, indicating little to no linear relationship.
- **Conclusion:** Headline sentiment **alone** is not a strong predictor of S&P 500 daily returns.

---

## Future Improvements

- Include **lagged sentiment effects** (e.g., yesterday’s news on today’s market)
- Add more **features** such as headline category, source, or volume of news
- Try **non-linear models** or classification approaches
- Expand to individual stocks or sectors instead of just the index

---

## How to Run

1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Run the script or Jupyter notebook

---

## Author

**Pooja Masani**  
Computer Science @ UTK  


**Nayana Patil**  
Computer Science @ UTK  

