# -*- coding: utf-8 -*-

"""Console script for pyOnvotar."""

import click
import re
import sys
import logging
from .log_helper import config_logging
from .pyOnvotar import answer

@click.command()
@click.argument('dni')
@click.argument('birth')
@click.argument('zip')
def main(dni, birth, zip, args=None):
    """Console script for pyOnvotar."""
    config_logging()
    res = answer(' '.join(sys.argv[1:]))
    print()
    print(res)


if __name__ == "__main__":
    main()
