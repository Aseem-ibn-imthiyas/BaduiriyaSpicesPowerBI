import pandas as pd

print("=" * 60)
print("BADUIRIYA SPICES - PYTHON DATA ANALYSIS")
print("=" * 60)

print("\nAnalysis Areas")
print("-" * 60)

areas = [
    "Revenue analysis",
    "Cost analysis",
    "Profit analysis",
    "Profit margin",
    "Product performance",
    "Monthly sales",
    "Units sold",
    "Operational costs",
    "Revenue forecasting",
]

for number, area in enumerate(areas, start=1):
    print(f"{number}. {area}")

print("\nPython analysis module is ready.")