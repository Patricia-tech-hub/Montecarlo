# Montecarlo Integration

This project implements Monte Carlo integration, a method for numerically approximating the integral of a function using random sampling.

## Project Structure

- `src/montecarlo/main.py`: Contains the implementation of the `Montecarlo` class.
- `tests/test_example.py`: Contains unit tests for the `Montecarlo` class.
- `README.md`: Project documentation.

## Montecarlo Class

The `Montecarlo` class provides methods to approximate the integral of a function over a given interval using Monte Carlo integration.

### Methods

- `__init__(self, a, b, f)`: Initializes the Montecarlo instance with the interval `[a, b]` and the function `f`.
- `integrate(self, n)`: Approximates the integral of `f` in the interval `[a, b]` using `n` random points.
- `plot(self, n)`: Plots the result of the integration using 1 to `n` points, showing how the approximation converges to the true value as `n` increases.

## Installation

1. Clone the repository:
    ```sh
    git clone 
    cd montecarlo_integration
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt

## Usage

```python
from montecarlo.main import Montecarlo

# Define the function to integrate
def f(x):
    return x ** 2

# Create a Montecarlo instance
mc = Montecarlo(0, 1, f)

# Approximate the integral using 1000 random points
result = mc.integrate(1000)
print(f"Approximate integral: {result}")

# Plot the convergence of the approximation
mc.plot(1000)