import csv
from typing import Any


class ProcessFile:

    @staticmethod
    def read_csv_file(path_file: str, mode: str = 'r', encoding: str = 'utf-8') -> list[dict[str, str]]:
        with open(path_file, mode, encoding=encoding) as rfile:
            reader = csv.DictReader(rfile, delimiter=';')
            data = [row for row in reader]

        return data

    @staticmethod
    def write_csv_file(
            path_file: str, data: list[dict[str, str]], fieldnames: list[str], mode: str = 'w', encoding: str = 'utf-8'
    ) -> None:
        with open(path_file, mode, encoding=encoding, newline='') as wfile:
            writer = csv.DictWriter(wfile, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            writer.writerows(data)
