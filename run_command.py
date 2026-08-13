# RUN IN WSL FOR LINUX

import subprocess
import shlex
import argparse
import sys
import time
parser = argparse.ArgumentParser(prog='run_command', description='run/re-run terminal commands', epilog='see help')
parser.add_argument('--retries', required=True)
parser.add_argument('--delay', required=True)
parser.add_argument('--command', required=True)

def pass_command(retries, delay, command):
    split_command = shlex.split(command)
    retries = int(retries)

    try:
        run_attempt = subprocess.run(split_command, capture_output=True, text=True)
        if run_attempt.returncode != 0 and retries > 0:
            attempts = 0
            while retries > 0 and run_attempt.returncode != 0:
                retries -= 1
                attempts += 1
                print(f"Attempt failed with exit code {run_attempt.returncode}")
                print(f"Retrying in {delay}s...")
                time.sleep(int(delay))
                run_attempt = subprocess.run(split_command, capture_output=True, text=True)
            if run_attempt.returncode != 0:
                print(f"Comamnd failed after {attempts} attempts")
                sys.exit(1)
        print(run_attempt.stdout)
    except FileNotFoundError:
        print("Command not found.")
        sys.exit(1)

def main():
    args = parser.parse_args()
    retries = args.retries
    delay = args.delay
    command = args.command
    pass_command(retries=retries, delay=delay, command=command)

if __name__ == "__main__":
    main()