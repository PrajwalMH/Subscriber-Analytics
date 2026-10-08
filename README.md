# Subscriber Analytics Dashboard

An interactive and professional **Streamlit analytics dashboard** for subscriber data cleaning, KPI analysis, churn insights, regional performance, customer spending analysis, and exportable reporting.

This project was developed as part of the **Fifth AI – Day 5 Fundamental Assignment** and demonstrates an end-to-end workflow from raw CSV data to cleaned data, KPI generation, visualization, and an interactive analytics dashboard.

---

## Project Overview

The Subscriber Analytics Dashboard processes subscriber data from a CSV file and transforms it into useful business insights.

The application performs:

- Data quality analysis
- Missing-value completeness reporting
- Duplicate subscriber removal
- Feature engineering
- KPI calculation
- Churn analysis
- Regional performance analysis
- Subscription-plan analysis
- Interactive visualization
- Data filtering
- CSV export
- Automated chart generation

The dashboard is built using **Python, Pandas, Streamlit, Plotly, and Matplotlib**.

---

## Assignment Objective

The original assignment requires an end-to-end workflow from a subscriber CSV dataset to a KPI chart.

The application completes the following tasks:

1. Report completeness for every column.
2. Remove duplicate `subscriber_id` records while keeping the latest record.
3. Create:
   - `tenure_days`
   - `spend_per_month_of_tenure`
4. Build a KPI table by region containing:
   - Number of subscribers
   - Average spend
   - Churn rate
5. Plot churn rate by region with labels.
6. Save:
   - KPI table as CSV
   - Churn-rate visualization as an image

In addition to these requirements, the project includes a complete interactive Streamlit dashboard.

---

## Dashboard Features

### KPI Overview

The dashboard displays important business metrics including:

- Total Subscribers
- Average Subscriber Spend
- Churn Rate
- Average Subscriber Tenure

These values automatically update when dashboard filters are applied.

---

### Interactive Filters

Users can dynamically filter the dashboard using:

- Region
- Subscription Plan
- Subscription Status

Subscription status options include:

- All Subscribers
- Active Subscribers
- Churned Subscribers

All relevant dashboard metrics and visualizations update automatically.

---

## Regional Performance Analysis

The dashboard analyzes subscriber performance across different regions.

The regional KPI table calculates:

| KPI | Description |
|---|---|
| Subscribers | Number of unique subscribers |
| Average Spend | Average subscriber spending |
| Churn Rate | Percentage of subscribers who churned |

The dashboard includes:

- Churn Rate by Region
- Subscriber Distribution by Region
- Regional KPI Summary

---

## Customer and Revenue Insights

The dashboard provides additional customer analytics including:

### Average Spend by Subscription Plan

Compares average subscriber spending across plans such as:

- Basic
- Standard
- Premium

### Subscriber Spend vs Tenure

An interactive scatter plot analyzes the relationship between:

- Subscriber tenure
- Total spending
- Subscriber region

Hover information provides subscriber-level details.

---

## Data Quality Analysis

The application automatically checks dataset quality.

For each column it calculates:

- Non-null values
- Missing values
- Completeness percentage

Example:

```text
Completeness (%) =
Non-null records / Total records × 100
