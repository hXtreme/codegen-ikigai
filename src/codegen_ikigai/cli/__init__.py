# SPDX-FileCopyrightText: 2026-present Harsh Parekh <harsh_parekh@outlook.com>
#
# SPDX-License-Identifier: MIT
import click

from codegen_ikigai.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="codegen-ikigai")
def codegen_ikigai():
    click.echo("Hello world!")
