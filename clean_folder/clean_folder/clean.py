import os
import argparse

def clean_folder(path):


    print(f"Cleaning folder: {path}")


def main():
    parser = argparse.ArgumentParser(description='Clean a folder')
    parser.add_argument('folder_path', type=str, help='Path to the folder')
    args = parser.parse_args()
    
    clean_folder(args.folder_path)

if __name__ == "__main__":
    main()