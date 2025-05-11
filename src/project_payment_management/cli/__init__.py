# SPDX-FileCopyrightText: 2025-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT
import click

from project_payment_management.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="Project Payment Management")
def project_payment_management():
    click.echo("Hello world!")
