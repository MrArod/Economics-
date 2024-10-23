# Economics Calculator 
# Marginal Analysis Tool for Business Owners

This Streamlit app helps business owners optimize production, order quantities, and resource inputs through data-driven marginal analysis. The tool is user-friendly and offers real-time feedback to make informed business decisions.

## Features

- **Production Analysis (Marginal Cost vs. Marginal Revenue)**: Determine the optimal production level by comparing Marginal Cost (MC) and Marginal Revenue (MR) to maximize profits or minimize losses.
- **Economic Order Quantity (EOQ)**: Calculate the optimal order quantity to minimize inventory costs, balancing ordering and holding costs.
- **Resource Input Optimization**: Optimize labor and capital inputs to achieve desired output, with a simple example of input balancing.

## How to Run

### 1. Clone the Repository

```git
git clone https://github.com/YourUsername/Marginal_Analysis_Tool.git
cd Marginal_Analysis_Tool
2. Install the Required Libraries
You can install the required dependencies using pip. Make sure you have Python installed, then run:

python
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt file yet, create one with this command:

python
Copy code
pip freeze > requirements.txt
This will include the necessary libraries such as Streamlit and any other dependencies.

3. Run the Streamlit App
Once everything is set up, start the Streamlit app with the following command:

python
Copy code
streamlit run app.py
This will launch the app in your default browser. You can now input your business data and receive recommendations for optimal production, order quantities, and resource allocation.

How It Works
1. Production Analysis:
Input the Change in Total Cost (ΔTC), Change in Quantity Produced (ΔQ), and Change in Total Revenue (ΔTR).
The app calculates Marginal Cost (MC) and Marginal Revenue (MR) and provides recommendations based on these values.
If MC equals MR, you've found the optimal production level. If MC is less than MR, it’s suggested to increase production, and vice versa.
2. Economic Order Quantity (EOQ):
Input the Annual Demand (D), Setup/Ordering Cost per Order (S), and Holding Cost per Unit (H).
The app calculates the EOQ, which is the ideal order quantity to minimize total inventory costs.
3. Resource Input Optimization:
Input Labor Input (L), Capital Input (K), and the Desired Output (Y).
The app provides simple calculations for balancing labor and capital to meet your output goals.
Example Inputs
Marginal Cost vs Marginal Revenue:

ΔTC = 500
ΔQ = 10
ΔTR = 700
EOQ:

Annual Demand (D) = 1000
Setup/Ordering Cost (S) = 100
Holding Cost (H) = 10
Resource Input:

Labor (L) = 100
Capital (K) = 100
Desired Output (Y) = 500
Requirements
Python 3.x
Streamlit
Math library (default with Python)
License
This project is licensed under the MIT License.
