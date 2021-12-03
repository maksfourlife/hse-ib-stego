from argparse import ArgumentParser

from stego.commands import eject_command, inject_command


parser = ArgumentParser(
    prog="Stego",
    usage="Used for encoding and decoding stego containers")


parser.add_argument("command", choices=["inject", "eject"])
parser.add_argument("-image", help="Image path", required=True)
parser.add_argument("-container", help="Container path", required=True)
parser.add_argument("-text", help="Text to be injected (or -bits or -file)")
parser.add_argument("-file", help="Path to file to be injected (or -text or -bits) / ejected")
parser.add_argument("-bits", help="Bits to be injected (or -text or -path)")
parser.add_argument("-msgtype", choices=["file", "text", "bits"])
parser.add_argument("-msglen", type=int)

args = parser.parse_args()

if args.command == "inject":
    inject_command(args.image, args.container, args.text, args.file, args.bits)
elif args.command == "eject":
    eject_command(args.container, args.msglen, args.msgtype, args.file)
