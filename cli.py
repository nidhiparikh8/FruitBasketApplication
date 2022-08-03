"""This module provides the FruitBasket CLI."""
# fruitBasket/cli.py

from typing import Optional

import typer

from fruitBasket import __app_name__, __version__, fruitBasket

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
	
@app.command(name="process")
def process(
    force: bool = typer.Option(
	    None,
		help = "Prompts for csv file then processes and makes output.txt",
    ),
) -> None:
    fruitBasket.ActiveBasket.process()
    