"""PyTypes: Enhanced Python with static/runtime type checking and new language features

Author: foxy pirate cove / Fnaf
License: GNU General Public License v2.0 only (GPL-2.0)
Version: 3.13.1

CLI Entrypoint
"""

from argparse import (
	ArgumentParser,
	_SubParsersAction,
	Namespace
)
from pathlib import Path
from sys import argv

from . import __version__


def main() -> None:
	argument_parser: ArgumentParser = ArgumentParser(
		prog='pytypes',
		description='Enhanced Python with static/runtime type checking and new language features',
	)
	argument_parser.add_argument(
		'--version',
		'-V',
		action='version',
		version=f'PyTypes v{__version__}'
	)
	subparsers: _SubParsersAction[ArgumentParser] = argument_parser.add_subparsers(
		dest='command',
		metavar='<command>'
	)

	command_execute: ArgumentParser = subparsers.add_parser(
		'execute',
		help='Execute a PyTypes file or start a REPL'
	)
	command_execute.add_argument(
		'file',
		metavar='<file>',
		nargs='?',
		type=Path,
		help='File to execute. Start an interractive REPL if not provided'
	)

	command_typecheck: ArgumentParser = subparsers.add_parser(
		'type-check',
		help='Type-check a PyTypes file.'
	)
	command_typecheck.add_argument(
		'file',
		metavar='<file>',
		type=Path,
		help='File to type-check'
	)

	command_transpile: ArgumentParser = subparsers.add_parser(
		'transpile',
		help='Transpile a PyTypes file to Python.'
	)
	command_transpile.add_argument(
		'file',
		metavar='<file>',
		type=Path,
		help='File to transpile'
	)

	args: Namespace = argument_parser.parse_args()
