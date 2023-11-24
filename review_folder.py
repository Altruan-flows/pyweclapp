import os
import subprocess
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor


def review_file(filepath: str, skip_reviewed: bool):
    # Check if the review file already exists
    review_filepath = f"{filepath}.review.md"
    if skip_reviewed and os.path.exists(review_filepath):
        print(f"Skipping review for {filepath} as review already exists.")
        return

    # Use subprocess to call the review.py script for the given file
    subprocess.run(["python", "review.py", "--file", filepath])


def main(folderpath: str, skip_reviewed: bool):
    # Get all files in the folder and subfolders
    all_files = [str(file) for file in Path(folderpath).rglob('*') if file.is_file() and file.name.endswith('.py')]

    # Use ProcessPoolExecutor to call review_file in parallel for all files
    with ProcessPoolExecutor() as executor:
        executor.map(review_file, all_files, [skip_reviewed] * len(all_files))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Automated Code Review Tool for All Files in a Folder")
    parser.add_argument("--folder", type=str, required=True, help="Folder path containing Python files to review")
    parser.add_argument("--skip-reviewed", action="store_true", help="Skip files that have already been reviewed")
    args = parser.parse_args()
    main(args.folder, args.skip_reviewed)
