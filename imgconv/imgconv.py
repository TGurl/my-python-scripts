#!/usr/bin/env python
import click

@click.command()
@click.option('-d', type=click.Choice(['archives', 'usb', 'keep']),
              help='Final destination')
def main(d):
    print(d)


if __name__ == "__main__":
    main()
