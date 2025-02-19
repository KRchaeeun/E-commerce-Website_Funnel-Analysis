# E-commerce-Website_Funnel-Analysis
This is a project about Funnel Analysis using E-commerce Website dataset.

## About Dataset
- Dataset: E-commerce website
- Source: [Kaggle](https://www.kaggle.com/datasets/aerodinamicc/ecommerce-website-funnel-analysis)
- Description: Provides information on how users navigate through various pages of the website.

## Project Objectives
- Perform **Funnel Analysis** based on user behavior data within the website.
- Analyze **drop-off rates** and **conversion rates** at each stage.
- Derive insights to improve **user experience**.

## Project Process
1. Understanding the Data – Analyze dataset structure and variables.
2. Data Preprocessing – Handle missing values and clean data using **Python**.
3. **Funnel Analysis** – Calculate stage-wise conversion rates and drop-off rates.
4. Visualization Dashboard – Build an analytical dashboard using **Tableau**.
5. Identify Issues & Suggest Improvements – Derive insights and propose optimizations.

## Understanding the Data

<p align="center">
  <img src="./readme_img/overview.png" alt="overview data">
</p>

### 📌 Dataset Overview and Relationships
| **File Name**                   | **Description**                               | **Details**                          |
|---------------------------------|------------------------------------------------|---------------------------------------|
| `home_page_table.csv` (📄)       | Homepage visit records                         | - `user_id` (User ID) <br> - `page` ("home_page") <br> - Records from **90,400** users |
| `search_page_table.csv` (🔍)     | Search page visit records                      | - `user_id` <br> - `page` ("search_page") <br> - Records from **45,200** users |
| `payment_page_table.csv` (💳)    | Payment page visit records                     | - `user_id` <br> - `page` ("payment_page") <br> - Records from **6,030** users |
| `payment_confirmation_table.csv` (✅) | Payment confirmation page visit records  | - `user_id` <br> - `page` ("payment_confirmation_page") <br> - Only **452** users completed the payment |
| `user_table.csv` (👤)            | User information                              | - `user_id` (User ID) <br> - `date` (Sign-up date) <br> - `device` (Device used: Desktop, etc.) <br> - `sex` (Gender: Male/Female) <br> - Contains information of all **90,400** users |

### 📌 Key Funnel Flow for Analysis
This dataset allows the analysis of the **drop-off rate** and **conversion rate** at each step as users navigate through the website. The funnel steps are as follows:

1. Homepage Visit (`home_page_table`)
2. Search Page Visit (`search_page_table`)
3. Payment Page Visit (`payment_page_table`)
4. Payment Confirmation (`payment_confirmation_table`)

This flow shows how users move from the homepage to the search page, proceed to the payment page, and finally reach the payment confirmation step. The funnel analysis will help identify the drop-off rates at each stage, providing insights into where users are leaving the site.