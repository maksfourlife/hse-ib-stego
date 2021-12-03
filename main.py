from argparse import ArgumentParser

from stego.commands import eject_command, inject_command

import warnings
warnings.filterwarnings("ignore")


parser = ArgumentParser(
    prog="Stego",
    usage="Used for to from and ejecting from stego containers")


subparsers = parser.add_subparsers(dest="command", help="Command")

types = ["file", "text", "bits"]

inject_parser = subparsers.add_parser("inject")

inject_parser.add_argument("-image",
    help="Path to image inject message to",
    required=True)
inject_parser.add_argument("-container",
    help="Path to store container with injected message",
    required=True)

inject_parser.add_argument("-input",
    help="Input text, bits or file path",
    required=True)

inject_parser.add_argument("-type",
    help="Input type",
    choices=types,
    required=True)

eject_parser = subparsers.add_parser("eject")

eject_parser.add_argument("-container",
    help="Path to container with injected message",
    required=True)

eject_parser.add_argument("-length",
    help="Injected message length",
    required=True,
    type=int)

eject_parser.add_argument("-type",
    help="Output type",
    choices=types,
    required=True)

eject_parser.add_argument("-out",
    help="Path to write msg if its file")

args = parser.parse_args()

if args.command == "inject":
    inject_command(args.image, args.container, args.input, args.type)
elif args.command == "eject":
    eject_command(args.container, args.length, args.type, args.out)
