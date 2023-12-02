import pytest
from adventofcode.models import CalibrationValue, CalibrationValues

class TestCalibrationValue:

    @pytest.mark.parametrize("string,result", [
        ("two1nine", "219"),
        ("eightwothree", "823")
    ])
    def test_apply_map(self, string: str, result: str):
        cv = CalibrationValue(string)
        assert cv.apply_map(cv.value) == result

    @pytest.mark.parametrize("string,first,last,value", [
        # Part 1
        ("1abc2", "1", "2", 12),
        ("pqr3stu8vwx", "3", "8", 38),
        ("a1b2c3d4e5f", "1", "5", 15),
        ("treb7uchet", "7", "7", 77),
        # Part 2
        ("two1nine", "2", "9", 29),
        ("eightwothree", "8", "3", 83),
        ("abcone2threexyz", "1", "3", 13),
        ("xtwone3four", "2", "4", 24),
        ("4nineeightseven2", "4", "2", 42),
        ("zoneight234", "1", "4", 14),
        ("7pqrstsixteen", "7", "6", 76),
        # Input
        ("hcpjssql4kjhbcqzkvr2fivebpllzqbkhg", "4", "5", 45),
        ("4threethreegctxg3dmbm1", "4", "1", 41),
        ("1lxk2hfmcgxtmps89mdvkl", "1", "9", 19),
        ("sixbfjblhsjr3", "6", "3", 63),
        ("soneighttwo39ktl132", "1", "2", 12),
        ("sqd1fivenfsmpsmjtscfivedzxfhnbbj8six", "1", "6", 16),
        ("9oneonetwofiveseven42", "9", "2", 92),
        ("7mhpslddjtwo9sixkzdvqzvggvfoursdvd", "7", "4", 74),
        ("onetwothreextbtpkrcphhp4kfplhqdvp9", "1", "9", 19),
        ("89l991eightttxtj3", "8", "3", 83),
        ("znbkscjpxnjzninesevenjnkdvckhgtwo5five", "9", "5", 95),
        ("ffnrprtnine1tjznmckv5sixczv", "9", "6", 96),
        # ...
        # Custom
        ("2oneight", "2", "8", 28),
        ("oneight", "1", "8", 18),
    ])
    def test_get_first_digit(self, string: str, first: str, last: str, value: int):
        cv = CalibrationValue(string)
        assert cv.get_first_digit() == first
        assert cv.get_last_digit() == last
        assert cv.get_value() == value

class TestCalibrationValues:

    def test_get_sum(self):
        # Part 1
        cvs = CalibrationValues(
            [
                CalibrationValue("1abc2"),
                CalibrationValue("pqr3stu8vwx"),
                CalibrationValue("a1b2c3d4e5f"),
                CalibrationValue("treb7uchet")
            ],
        )
        assert cvs.get_sum() == 142

        # Part 2
        cvs = CalibrationValues(
            [
                CalibrationValue("two1nine"),
                CalibrationValue("eightwothree"),
                CalibrationValue("abcone2threexyz"),
                CalibrationValue("xtwone3four"),
                CalibrationValue("4nineeightseven2"),
                CalibrationValue("zoneight234"),
                CalibrationValue("7pqrstsixteen"),
            ],
        )
        assert cvs.get_sum() == 281


