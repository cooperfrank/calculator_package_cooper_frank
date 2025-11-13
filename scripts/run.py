from pathlib import Path

from calculator_package_cooper_frank import Calculator
from calculator_package_cooper_frank.file_calculator import FileCalculator

print(Calculator().add(1, 2))
print(FileCalculator().sum_file(Path("~/nums.csv").expanduser()))
