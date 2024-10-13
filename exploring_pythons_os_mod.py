import os

def list_directory_contents(full_path='.'):
    with os.scandir(full_path) as entries:
        for entry in entries:
            if entry.is_file() or entry.is_dir():
                print(entry.name)

def main():
    while True:
        try:
            print(f"Files and Directories in '% s':".path)
            directory_path = input("Please enter the directory you would like to work with: ")
            if os.path.isdir(directory_path):
                list_directory_contents(directory_path)
        except NotADirectoryError:
            print(f"ERROR: {directory_path} is not a directory.")
        except PermissionError:
            print(f"ERROR: You do not have permission to work with {directory_path}")
        except IOError:
            print("An unexpected error has occurred.")
        except Exception as e:
            print(f"An error {e} has occurred.")
        break_input = input("Type 'exit' to stop working with directories, or press Enter to continue: ")
        if break_input.lower() == 'exit':
            break

main()