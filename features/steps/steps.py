# TODO: Configure debug as default logging level.
import logging
from numbers import Number
from behave.runner import Context
from adventofcode.models import CalibrationValue, CalibrationValues

@given(u'newly-improved calibration document')
def step_impl(context: Context):
    values = CalibrationValues()
    for row in context.table:
        first_cell = row[0]
        values.values.append(CalibrationValue(first_cell))
    context.values = values

@when(u'combining the first digit and the last digit on each line')
def step_impl(context: Context):
    pass


@then(u'calibration values are')
def step_impl(context: Context):
    for i, row in enumerate(context.table):
        # TODO: Make suggestions work here
        logging.error(context.values.values[i])
        assert context.values.values[i].get_value() == int(row[0])
        # logging.error("%s: %s", i, line)


@then(u'the sum of all of the calibration values is "{number}"')
def step_impl(context: Context, number: Number):
    logging.error("sum: %s, number: %s", context.values.get_sum(), number)
    assert context.values.get_sum() == int(number)
