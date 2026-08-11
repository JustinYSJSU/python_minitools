import subprocess
import argparse

parser = argparse.ArgumentParser(prog='run_command', description='run/re-run terminal commands', epilog='see help')
parser.add_argument('--retries', required=True)
parser.add_argument('--delay', required=True)
parser.add_argument('--command', required=True)

args = parser.parse_args()
print(args.retries)
print(args.delay)
print(args.command)
