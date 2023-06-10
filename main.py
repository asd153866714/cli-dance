import os
import sys
import time
import argparse

from frames import frames_map


# read command-line argument
def handle_cli_arguments():
    parser = argparse.ArgumentParser(
        description="Simple program with command-line arguments"
    )

    parser.add_argument(
        "-l",
        "--list",
        default=False,
        action="store_true",
        help="Show the list of frames",
    )

    parser.add_argument(
        "-d",
        "--delay",
        metavar="DELAY",
        default=0.3,
        type=float,
        help="Set the frame delay time in seconds",
    )

    parser.add_argument(
        "-f",
        "--frames",
        metavar="FRAMES",
        default="progress",
        type=str,
        help="Display frames",
    )

    args = parser.parse_args()

    if args.list:
        show_frames()
    elif args.frames:
        display_frames(frames_map[args.frames], args.delay)


## show the lsit of frames
def show_frames():
    for key in frames_map.keys():
        print(key)


## display frames
def display_frames(frames, dealy):
    while True:
        for i in range(len(frames)):
            # Print the frame
            print("{}".format(frames[i]))
            time.sleep(dealy)
            os.system("clear")


if __name__ == "__main__":
    handle_cli_arguments()
