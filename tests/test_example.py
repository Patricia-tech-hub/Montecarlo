import sys
import os
import numpy as np

# Add src/ to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from montecarlo.main import Montecarlo

def test_montecarlo_accuracy():
    np.random.seed(42)
    mc = Montecarlo(0, 1, lambda x: x**2)
    result = mc.integrate(100000)

    expected = 1/3  # The exact integral value
    tolerance = 0.01  # Allow a small numerical error
    
    assert np.isclose(result, expected, atol=tolerance), f"Monte Carlo result {result} is too far from expected {expected}"
    



