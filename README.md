# 📊 Random Process Simulation: Mean and Autocorrelation Analysis

Welcome to this repository! 👋  
This project presents a **Python-based simulation** to analyze the statistical
behavior of a random process defined as:

\[
X(t) = \cos(\omega t + \theta)
\]

where:
- 🔹 **ω (omega)** is a constant angular frequency  
- 🔹 **θ (theta)** is a random variable uniformly distributed in the interval *(0, 2π)*

The main purpose of this project is to investigate whether the given random
process is **time-dependent** by studying its **mean** and **autocorrelation**
using numerical simulation and visualization techniques.

---

## 🎯 Project Objectives

The key goals of this simulation are:

1. 🔁 Simulate multiple realizations of the random process **X(t)**.
2. 📈 Compute and visualize the **mean value** \( E[X(t)] \) over time.
3. 🔄 Compute and visualize the **autocorrelation function**  
   \( R_X(t, t+\tau) \) for a fixed time shift \( \tau \).
4. 🧐 Analyze whether the statistical properties of the process vary with time.

---

## 🧠 Theoretical Background

A random process is considered **time-invariant (stationary)** if its statistical
properties remain unchanged over time.

- 📌 If the **mean** changes with time → the process is **time-dependent**.
- 📌 If the **autocorrelation** depends on time *t* instead of only the time
  difference \( \tau \) → the process is **time-dependent**.

In this project, the autocorrelation is evaluated using:

\[
R_X(t, t+\tau) = E[X(t)X(t+\tau)]
\]

This helps determine whether the process depends explicitly on time or only on
the time difference.

---

## 🛠️ Tools & Libraries Used

The simulation is implemented using the following Python libraries:

- 🧮 **NumPy** — numerical computation and random variable generation
- 📊 **Matplotlib** — data visualization and plotting

---

## ▶️ How to Run the Code

Follow these steps to run the simulation on your machine:

1. ✅ Ensure **Python 3** is installed.
2. 📦 Install the required libraries:
   ```bash
   python -m pip install numpy matplotlib
