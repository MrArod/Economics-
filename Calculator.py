import streamlit as st
import math

# Title and Description
st.title("Marginal Analysis Tool for Business Owners")
st.write("Optimize production, order quantity, and resource inputs using data-driven marginal analysis.")

# Marginal Cost vs Marginal Revenue Section
st.header("Production Analysis (Marginal Cost vs. Marginal Revenue)")

# Inputs for Production Analysis
total_cost_change = st.number_input("Change in Total Cost (ΔTC)", value=0.0)
quantity_change = st.number_input("Change in Quantity Produced (ΔQ)", value=1.0)
total_revenue_change = st.number_input("Change in Total Revenue (ΔTR)", value=0.0)

# Calculate Marginal Cost and Marginal Revenue
if quantity_change != 0:
    marginal_cost = total_cost_change / quantity_change
    marginal_revenue = total_revenue_change / quantity_change

    # Display results
    st.write(f"Marginal Cost (MC): ${marginal_cost}")
    st.write(f"Marginal Revenue (MR): ${marginal_revenue}")
    
    # Optimal Production Decision
    if marginal_cost == marginal_revenue:
        st.success("Optimal production level found where Marginal Cost equals Marginal Revenue!")
    elif marginal_cost < marginal_revenue:
        st.info("Increase production for higher profits.")
    else:
        st.warning("Decrease production to avoid losses.")
else:
    st.warning("Change in quantity must be greater than 0.")

# Economic Order Quantity (EOQ) Section
st.header("Order Quantity Optimization (EOQ)")

# Inputs for EOQ
demand = st.number_input("Annual Demand (D)", value=1000)
setup_cost = st.number_input("Setup/Ordering Cost per Order (S)", value=100.0)
holding_cost = st.number_input("Holding Cost per Unit (H)", value=10.0)

# Calculate EOQ
if holding_cost != 0:
    eoq = math.sqrt((2 * demand * setup_cost) / holding_cost)
    st.write(f"Optimal Order Quantity (EOQ): {eoq:.2f} units")
else:
    st.warning("Holding cost must be greater than 0.")

# Resource Input Optimization Section
st.header("Resource Input Optimization")

# Inputs for Resource Inputs
labor = st.number_input("Labor Input (L)", value=100)
capital = st.number_input("Capital Input (K)", value=100)
output = st.slider("Desired Output (Y)", min_value=0, max_value=1000, value=500)

# Simple optimization logic (example)
optimal_labor = output / 2
optimal_capital = output / 2

st.write(f"Optimal Labor Input: {optimal_labor}")
st.write(f"Optimal Capital Input: {optimal_capital}")

st.success("Resource optimization complete. Adjust inputs for optimal production.")
