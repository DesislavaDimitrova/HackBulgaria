#Implementing cat command for multiple arguments
import sys

def main():
    for i in sys.argv[1:]:
        filename = i
        file1 = open(filename, "r")
        print(file1.read())
        file1.close()


if __name__ == '__main__':
    main()
