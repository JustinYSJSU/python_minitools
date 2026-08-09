import argparse
import sys
import shutil
from pathlib import Path

parser = argparse.ArgumentParser(prog='artifact_collector', description='fetch test artifacts', epilog='see help')
parser.add_argument('--source-dir', required=True)
parser.add_argument('--output-dir', required=True)
parser.add_argument('--extension-list', nargs='+', required=True)

def search_directory(source_dir, extension_list):
    print("Collecting artifacts...")

    files = [
        path for path in source_dir.rglob("*")
        if path.suffix.lower() in extension_list
    ]
    return files

def copy_files(files, source_dir, output_dir):
    for file in files:
        index = file.parts.index(source_dir)

        mini_path = Path(*file.parts[index:]) # sub part of the path, starting from given source_dir
        mini_path_str = str(Path(*file.parts[index:])).replace("\\", "_") # convert to string with '_' for file naming

        if Path(output_dir/mini_path_str).exists():
            print("File destination exists. Skipping...")
            continue
        
        shutil.copy2(file, output_dir/mini_path_str)
        print(f"Copied: {mini_path}")
    print(f"Collected {len(files)} artifacts")

def main():
    args = parser.parse_args()
    source_dir = args.source_dir
    output_dir = args.output_dir

    # handle source dir not existing
    source_dir_path = Path.cwd() / source_dir
    if not source_dir_path.is_dir():
        print("Source dir not found. Please create it in /python_minitools")
        sys.exit(1)

    # create output dir if not exists
    output_dir_path = Path.cwd() / output_dir
    if not output_dir_path.exists():
        output_dir_path.mkdir(parents=True, exist_ok=True)

    extension_list = [extension.lower() for extension in args.extension_list]
    files = search_directory(source_dir=source_dir_path, extension_list=extension_list)

    copy_files(files=files, source_dir=source_dir, output_dir=output_dir_path)

if __name__ == "__main__":
    main()