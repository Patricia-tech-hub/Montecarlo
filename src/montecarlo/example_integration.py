import sys
import os

# Add src/ to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from montecarlo.main import Montecarlo

integral = Montecarlo(0, 1, lambda x: x**2)
print(integral.integrate(100000))
integral.plot(1000)
