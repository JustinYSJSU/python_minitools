import argparse

parser = argparse.ArgumentParser(prog='artifact_collector', description='fetch test artifacts', epilog='see help')
parser.add_argument('source-dir')
parser.add_argument('output-dir')