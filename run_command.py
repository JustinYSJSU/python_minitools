# RUN IN WSL FOR LINUX

import subprocess
import shlex
import argparse

parser = argparse.ArgumentParser(prog='run_command', description='run/re-run terminal commands', epilog='see help')
parser.add_argument('--retries', required=True)
parser.add_argument('--delay', required=True)
parser.add_argument('--command', required=True)

def pass_command(retries, delay, command):
    split_command = shlex.split(command)

    subprocess.run([split_command[0]])

def main():
    args = parser.parse_args()
    retries = args.retries
    delay = args.delay
    command = args.command
    pass_command(retries=retries, delay=delay, command=command)

if __name__ == "__main__":
    main()