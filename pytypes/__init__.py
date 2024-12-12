__version__ = "0.0.1"

from argparse import ArgumentParser, Namespace


def main() -> None:
	argument_parser: ArgumentParser = ArgumentParser(
		prog="pytypes",
		description="PyTypes extends Python with type safety, access control, namespaces, and other features",
	)
	argument_parser.add_argument(
		"command",
		metavar="command",
		nargs="?",
		choices=["execute", "type-check", "transpile"],
		default="execute",
		help="The command to execute. Available commands: execute, type-check, transpile. Default execute.",
	)
	argument_parser.add_argument(
		"file",
		nargs="?",
		help="The file to process. If not specified, execute will start a REPL, other commands will fail.",
	)
	args: Namespace = argument_parser.parse_args()

	if args.command != "execute" and args.file is None:
		argument_parser.error(
			f"A file must be specified for the command '{args.command}'."
		)


if __name__ == "__main__":
	main()
