import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("PN Junction Diode Simulator")

st.write("This simulator shows the I-V characteristics of a PN junction diode.")

# User Inputs
st.sidebar.header("Input Parameters")

temperature = st.sidebar.slider("Temperature (K)", 250, 400, 300)
ideality = st.sidebar.slider("Ideality Factor (n)", 1.0, 2.0, 1.5)
Is = st.sidebar.number_input("Saturation Current (Is)", value=1e-12, format="%.2e")

# Constants
k = 1.38e-23
q = 1.6e-19

# Thermal Voltage
Vt = (k * temperature) / q

# Voltage Range
V = np.linspace(-1, 1, 200)

# Shockley Diode Equation
I = Is * (np.exp(V / (ideality * Vt)) - 1)

# Plot Graph
fig, ax = plt.subplots()
ax.plot(V, I)
ax.set_xlabel("Voltage (V)")
ax.set_ylabel("Current (A)")
ax.set_title("PN Junction I-V Characteristics")
ax.grid(True)

st.pyplot(fig)

# Forward / Reverse Bias Explanation
st.subheader("Diode Behavior")

if st.checkbox("Show Explanation"):
    st.write("""
    **Forward Bias**
    - Positive voltage applied to P-side.
    - Depletion region decreases.
    - Current increases rapidly.

    **Reverse Bias**
    - Negative voltage applied to P-side.
    - Depletion region increases.
    - Only small leakage current flows.
    """)

# Depletion Width Estimation
st.subheader("Depletion Region Estimation")

Na = st.number_input("Acceptor Concentration Na (cm^-3)", value=1e16, format="%.2e")
Nd = st.number_input("Donor Concentration Nd (cm^-3)", value=1e16, format="%.2e")

epsilon = 11.7 * 8.85e-14
Vbi = 0.7

W = np.sqrt((2 * epsilon * Vbi / q) * ((1 / Na) + (1 / Nd)))

st.write("Estimated Depletion Width (cm):", W)
