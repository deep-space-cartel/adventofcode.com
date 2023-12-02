import logging
from dataclasses import dataclass, field
from typing import List

@dataclass
class CalibrationValue:
    # TODO: Add type validation
    value: str

    # TODO: Use tuples
    MAP = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    def get_first_letter_position(self, string: str) -> int:
        for i, symbol in enumerate(string):
            if not symbol.isnumeric():
                return i

    def apply_map(self, value: str):
        numbers = []
        start = 0
        while start < len(value):
            # logging.error("start: %s", start)
            for length in range(1, 6):
                substring = value[start:start+length]
                # logging.error("Checking '%s'", substring)
                if substring.isnumeric():
                    # logging.critical("Found: %s", substring)
                    numbers.append(substring)
                    break
                if substring in self.MAP.keys():
                    # logging.critical("Found: %s", substring)
                    numbers.append(self.MAP[substring])
                    break
            start += 1
        # logging.error("numbers: %s", numbers)
        return "".join(numbers)

    # def apply_map(self, value: str, start: int = 0) -> str:
    #     while start < len(value):
    #         # TODO: start should be "first not numeric symbol"
    #         size_min = 1 + start
    #         # TODO: Use self.MAP to get size_max
    #         size_max = 5 + start
    #         for size in range(size_min, size_max + 1):
    #             logging.error("Size: %s", size)
    #             substring = value[start:size]
    #             logging.error("Processing value[%s:%s] '%s'", start, size, substring)
    #             if substring in self.MAP.keys():
    #                 logging.error("Found: %s", substring)
    #                 value = value.replace(substring, self.MAP[substring], 1)
    #                 logging.error("Replaced: %s", value)
    #                 start = self.get_first_letter_position(value)
    #                 if start is None:
    #                     return value
    #                 logging.error("New start: %s", start)
    #                 value = self.apply_map(value, start)
    #                 break
    #         start += 1

    #     return value
    #     # for k, v in self.MAP.items():
    #     #     if value.startswith(k):
    #     #         value = value.replace(k, v)
    #     # return value


    # TODO: Make sure that there are at least 2 digits
    # TODO: Add cache
    def get_first_digit(self) -> str:
        logging.error("Processing: %s", self.value)
        for symbol in self.apply_map(self.value):
            if symbol.isnumeric():
                return symbol
        raise Exception("First digit not found")

    # TODO: Make sure that there are at least 2 digits
    # TODO: Add cache
    def get_last_digit(self) -> str:
        for symbol in self.apply_map(self.value)[::-1]:
            if symbol.isnumeric():
                return symbol
        raise Exception("Last digit not found")

    def get_value(self) -> int:
        return int(self.get_first_digit() + self.get_last_digit())


@dataclass
class CalibrationValues:
    values: List[CalibrationValue] = field(default_factory=list)

    # TODO: Do not return 0 for empty list
    def get_sum(self) -> int:
        total = 0
        for value in self.values:
            total += value.get_value()
        return total
