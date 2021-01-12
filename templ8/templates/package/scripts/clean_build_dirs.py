#!/usr/bin/env python3

import argparse
import os
import subprocess
from distutils.util import strtobool

parser = argparse.ArgumentParser(description="Remove target directories")
parser.add_argument("-p", "--project-dir", help="Project root", required=True)
parser.add_argument(
    "-t", "--target-dirs", nargs="+", help="Directories to remove", required=True
)
cli_arguments = vars(parser.parse_args())

project_dir = cli_arguments["project_dir"]
target_dirs = cli_arguments["target_dirs"]

for directory in target_dirs:
    target_dir = os.path.normpath(os.path.join(project_dir, directory))

    try:
        if strtobool(input(f"Would you like to remove {target_dir}?\n")):
            print(f"Removing {target_dir}")

            try:
                subprocess.check_call(["rm", "-rf", target_dir])
                print(f"Removed {target_dir}")

            except (OSError, subprocess.CalledProcessError):
                print(f"Could not remove {target_dir}")

        else:
            print(f"Skipping {target_dir}")

    except ValueError:
        print(f"Unrecognised response - skipping {target_dir}")
