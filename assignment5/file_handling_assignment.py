#!/usr/bin/python3

# file_handling_assignment.py

def create_file():
    """
    Create a new text file named "my_file.txt" in write mode ('w)
    and write three lines of text to it.
    """
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with a mix of string and number:42 is the answer\n")
    except PermissionError:
        print("Permission denied ro create the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File creation process completed.")


def read_file():
    """
    Read the contents of the file "my_file.txt" in read mode ('r)
    and display them on the console
    """
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of my_file.txt:")
            print(content)
    except FileExistsError:
        print("File not found.")
    except Exception as e:
        print("An error occured", e)


def append_file():
    """
    Opens "my_file_txt" in append mode ('a') and
    adds three lines of the text to the existing content.
    """
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("987654\n")
            file.write("Appending another line\n")
    except PermissionError:
        print("Permision denied to append to the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File appending proccess completed.")


def main():
    create_file()
    read_file()
    append_file()


if __name__ == "__main__":
    main()
