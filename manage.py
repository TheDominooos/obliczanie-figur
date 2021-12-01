import click
from obliczanie_figur import *

@click.group()
def figure():
    pass
@figure.command()
@click.option('-area', required=False, is_flag=True)
@click.option('-perimeter', required=False, is_flag=True)
@click.argument('side_1', default=1, type=int)
def square(side_1, area, perimeter):
    object = Square(side_1)
    if area:
        click.echo(f"Pole wynosi: {object.area()}")
    elif perimeter:
        click.echo(f"Obwód wynosi: {object.perimeter()}")
    else:
        click.echo("Błędna opcja")


@figure.command()
@click.option('-area', required=False, is_flag=True)
@click.option('-perimeter', required=False, is_flag=True)
@click.argument('side_1', default=1, type=int)
@click.argument('side_2', default=1, type=int)

def rectangle(side_1, side_2, area, perimeter):
    object = Rectangle(side_1, side_2)
    if area:
        click.echo(f"Pole wynosi: {object.area()}")
    elif perimeter:
        click.echo(f"Obwód wynosi: {object.perimeter()}")
    else:
        click.echo("Błędna opcja")

@figure.command()
@click.option('-area', required=False, is_flag=True)
@click.option('-perimeter', required=False, is_flag=True)
@click.argument('height', default=1, type=int)
@click.argument('side_1', default=1, type=int)
@click.argument('side_2', default=1, type=int)
@click.argument('side_3', default=1, type=int)

def triangle(height, side_1, side_2, side_3, area, perimeter):
    object = Triangle(height, side_1, side_2, side_3)
    if area:
        click.echo(f"Pole wynosi: {object.area()}")
    elif perimeter:
        click.echo(f"Obwód wynosi: {object.perimeter()}")
    else:
        click.echo("Błędna opcja")

@figure.command()
@click.option('-area', required=False, is_flag=True)
@click.option('-perimeter', required=False, is_flag=True)
@click.argument('radius', default=1, type=int)

def wheel(radius, area, perimeter):
    object = Wheel(radius)
    if area:
        click.echo(f"Pole wynosi: {object.area()}")
    elif perimeter:
        click.echo(f"Obwód wynosi: {object.perimeter()}")
    else:
        click.echo("Błędna opcja")

if __name__ == '__main__':
    figure()