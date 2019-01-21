import argparse


parser = argparse.ArgumentParser(prog="DangerBot",
                                 description="A script that plays Urban Dead in order to update the wiki")

parser.add_argument("command", choices=['scout', 'report'],
                    help="scout determines the state of the world; report uses the logs to update the wiki")

args = parser.parse_args()

if args.command == "scout":
    print("Moving the characters")
elif args.command == "report":
    print("Updating the wiki")
else:
    print("Unknown command {}".format(args.command))
