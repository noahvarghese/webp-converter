#!/usr/bin/python

from PIL import Image
import PIL
import os
import sys
import glob
import getopt

help_menu = ("Exactly one file type must be specified\n\n" +
             "png\t--png/-p\tSaves as a PNG\n" +
             "jpg\t--jpg/-j\tSaves as a JPEG\n" +
             "webp\t--webp/-w\tSaves as the WEBP format\n\n" +
             "file name\t--file/-f\tThe path of the image to convert\n" +
             "destination\t--destination/-d\tThe save destination of the converted file, will default to current location [optional]\n" +
             "help\t--help/-h\tPrints this menu\n")


def load_args() -> {"file_type": str, "file_name": str, "destination": str}:
    try:
        opts, args = getopt.getopt(sys.argv[1:], "pjwf:d:h", [
                                   "destination=", "help", "file=", "webp", "jpg", "png"])
    except:
        sys.exit(help_menu)

    args = {"file_type": "", "file_name": "", "destination": ""}

    for (opt, arg) in opts:
        if opt in ('-p', '--png'):
            args["file_type"] = "png"
        elif opt in ('-j', '--jpg'):
            args["file_type"] = "jpg"
        elif opt in ('-w', '--webp'):
            args["file_type"] = "webp"
        elif opt in ('-d', '--destination'):
            args["destination"] = arg
        elif opt in ('-f', '--file'):
            args["file_name"] = arg
        else:
            sys.exit(help_menu)

    return args


def check_args(args: {"file_type": str, "file_name": str, "destination": str}) -> {"file_type": str, "file_name": str, "destination": str}:
    exists = check_file_exists(args["file_name"])

    if exists == False:
        sys.exit("File " + args["file_name"] + " does not exist")

    check_file_type(args["file_type"])
    args["destination"] = check_save_destination(args["destination"],
                                                 args["file_name"], args["file_type"])

    return args


def check_file_type(file_type: str = "") -> bool:
    if file_type == "" or str(type(file_type)) != "<class 'str'>":
        sys.exit("Invalid file type " + file_type)
    else:
        return True


def check_file_exists(file_name: str = "") -> bool:
    return os.path.exists(file_name)


def check_save_destination(destination: str = "", file_name: str = "", file_type: str = "") -> str:
    if destination == "" or str(type(destination)) != "<class 'str'>":
        parts = file_name.split(".")
        parts[-1] = file_type
        seperator = "."
        destination = seperator.join(parts)

    exists = check_file_exists(destination)

    if exists == True:
        sys.exit(
            "Destination file already exists, overwrite functionality not included")
    else:
        return destination


def convert_image(args: {"file_name": str, "file_type": str, "destination": str}):
    print("Converting image " + args["file_name"] + " to " + args["file_type"])
    image = Image.open(args["file_name"])
    image = image.convert("RGB")
    image.save(args["destination"], args["file_type"])


def main():
    args = load_args()
    args = check_args(args)
    convert_image(args)
    return


main()
