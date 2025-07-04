
# 📊 Lending Platform Product Dashboard (Tableau)

This project analyzes real-world lending behavior using cleaned LendingClub data from 2015–2018. It was built as a part of product-data portfolio preparation for placements and showcases how to extract actionable insights from borrower behavior, risk patterns, and disbursement trends using visual analytics.

---

## 📂 Dataset

**Source:** Kaggle / LendingClub (cleaned version)  
**Files Used:**  
- `X.csv` – loan application features  
- `target.csv` – loan_status (0 = Fully Paid, 1 = Defaulted)  
- Merged into `lending_dashboard_data.csv`

---

## 🎯 Objectives

- Visualize loan disbursement funnel (Paid vs Defaulted)
- Analyze loan volumes over time
- Compare default risk across credit grades
- Understand borrower purpose and associated risk
- Build a dashboard-ready product visual using Tableau

---

## 📊 Dashboard Highlights

1. **Loan Status Funnel**
   - 78% of loans were fully paid
   - 22% of loans defaulted

2. **Monthly Loan Volume Trend**
   - Peak loan disbursal in mid-2017
   - Growth slowdown seen post-2018

3. **Default Rate by Loan Grade**
   - Grade G has highest default rate (~30%)
   - Grade A & B loans are lowest risk (<5%)

4. **Purpose-Wise Loan Breakdown**
   - Most loans were for debt consolidation and credit cards
   - Small business loans show highest default risk

---

## 💡 Key Business/Product Insights

- **Risk-Segmented Lending**: Clear correlation between loan grade and default rate  
- **Low-Income Risk Group**: Default rate increases for borrowers earning < ₹50K annually  
- **Purpose Drives Risk**: 'Small Business' loans are high-risk, while 'Medical' and 'Home Improvement' are safer  
- **Loan Cycle Timing**: Lending peaks seasonally, insights useful for product timing and approvals

---

## 🧠 Tools Used

- **Tableau Public** for dashboarding
- **Python (pandas)** for CSV merging & data prep
- **Jupyter Notebook** (optional) for EDA

---

## 🖼️ Screenshots

> Include exported dashboard screenshots here  
> Or link to live dashboard (if saved to Tableau Public)

---

## 🧾 Files in Repo


---

## 📎 Made with real data by **Yash Sharma**, 2025  
=======

8d4abeb9ad0e742f182fe4f8f36b5284bbd48ec9
