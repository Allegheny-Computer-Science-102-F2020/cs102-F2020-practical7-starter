"""Define the command-line interface for the cartesiancreator program."""

from typing import List


import typer


from cartesiancreator import cartesian


def main(
    first: List[int] = typer.Option([]),
    second: List[int] = typer.Option([]),
):
    """Compute the Cartesian product of two sets using the set discrete structure."""
    # create a set of the input numbers in the first list
    first_set = set(first)
    # create a set of the input number in the second list
    second_set = set(second)
    # compute the Cartesian produce of the two sets
    cartesian_product_set = cartesian.cartesian_product(first_set, second_set)
    # display the two input sets
    typer.echo("")
    typer.echo("Welcome to the Cartesian product calculator!")
    typer.echo("")
    typer.echo(f"First set: {first_set}")
    typer.echo("")
    typer.echo(f"Second set: {second_set}")
    typer.echo("")
    typer.echo(
        f"Address of generator for Cartesian produce of sets: {cartesian_product_set}"
    )
    typer.echo("")
    typer.echo(f"Cartesian product of sets: {list(cartesian_product_set)}")
    typer.echo("")


if __name__ == "__main__":
    # call the main function in this module
    typer.run(main)
