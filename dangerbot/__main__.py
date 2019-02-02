import argparse
from scout import Scout

parser = argparse.ArgumentParser(prog="DangerBot",
                                 description="A script that plays Urban Dead in order to update the wiki")

parser.add_argument("command", choices=['scout', 'report'],
                    help="scout determines the state of the world; report uses the logs to update the wiki")
parser.add_argument("character_name", help="used for 'scout', the name of the character to move")

args = parser.parse_args()

if args.command == "scout":
    if args.character_name is None:
        raise Exception("Must provide a character name when using the scout command")

    print("Moving the character")
    s = Scout(args.character_name)
    s.scout()

elif args.command == "report":
    print("Updating the wiki")

else:
    print("Unknown command {}".format(args.command))
