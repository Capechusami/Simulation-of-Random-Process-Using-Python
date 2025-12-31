import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega = 2 * np.pi  # Frequency (constant)
num_samples = 10000  # Number of realizations
t_values = np.linspace(0, 2, 100)  # Time values to evaluate
theta = np.random.uniform(0, 2 * np.pi, size=num_samples)  # θ ~ U(0, 2π) to make the process WSS

# Simulate the random process X(t) = cos(ωt + θ)
def simulate_X(t, omega, theta):
    return np.cos(omega * t + theta)

# Compute mean and autocorrelation
mean_X = np.array([np.mean(simulate_X(t, omega, theta)) for t in t_values])
autocorrelation_X = np.zeros(len(t_values))

# Evaluate autocorrelation for τ = 1
tau = 1
for i, t in enumerate(t_values):
    t_shifted = t + tau
    X_t = simulate_X(t, omega, theta)
    X_t_shifted = simulate_X(t_shifted, omega, theta)
    autocorrelation_X[i] = np.mean(X_t * X_t_shifted)

# Plot results
plt.figure(figsize=(12, 6))

# Plot mean
plt.subplot(1, 2, 1)
plt.plot(t_values, mean_X, label="Mean of X(t)", color="blue")
plt.axhline(0, color="red", linestyle="--", label="Expected Mean Line")
plt.xlabel("Time (t)")
plt.ylabel("Mean of X(t)")
plt.title("Mean of X(t) Over Time")
plt.legend()
plt.grid()

# Plot autocorrelation
plt.subplot(1, 2, 2)
plt.plot(t_values, autocorrelation_X, label=f"Autocorrelation (τ={tau})", color="green")
plt.xlabel("Time (t)")
plt.ylabel("Autocorrelation")
plt.title("Autocorrelation of X(t) with Shift τ")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
