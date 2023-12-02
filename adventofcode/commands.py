import click
from adventofcode.models import CalibrationValue, CalibrationValues

@click.group()
def cli():
    pass

@click.command()
@click.option('--input', default='puzzles/day1/example.txt')
def day1(input: str):
    click.echo('Input: %s' % input)
    with open(input) as fh:
        lines = fh.read().splitlines()

    values = CalibrationValues()

    for line in lines:
        click.echo("Processing '%s'" % line)
        value = CalibrationValue(line)
        values.values.append(value)

    for value in values.values:
        click.echo(value.get_value())

    click.echo("Sum: %s" % values.get_sum())


@click.command()
def day2():
    raise NotImplemented()

cli.add_command(day1)
cli.add_command(day2)

if __name__ == '__main__':
    cli()
