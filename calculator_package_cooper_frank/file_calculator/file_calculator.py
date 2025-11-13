from pathlib import Path

from tqdm import tqdm

from calculator_package_cooper_frank.calculator import Calculator


class FileCalculator(Calculator):
    def sum_file(self, path=None) -> int:
        if path is None:
            path = Path(__file__).parent / "nums.csv"

        with tqdm(total=100_000_000, desc="Summing file") as pbar:
            total = 0

            with path.open() as f:
                for line in f:
                    total += int(line)
                    pbar.update()

            return total
