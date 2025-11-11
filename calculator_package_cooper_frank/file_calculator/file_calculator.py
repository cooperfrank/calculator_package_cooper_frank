from pathlib import Path

from calculator_package_cooper_frank.calculator import Calculator

class FileCalculator(Calculator):
    def sum_file(self, path=None):
        if path is None:
            path = Path(__file__).parent / "nums.csv"
        raise NotImplementedError


