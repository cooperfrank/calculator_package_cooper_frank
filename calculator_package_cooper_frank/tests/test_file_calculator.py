from calculator_package_cooper_frank.file_calculator import FileCalculator


def test_file_calculator():
    assert FileCalculator().sum_file() == 6
