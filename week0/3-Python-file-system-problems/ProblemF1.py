#Implementing cat command
import sys

def main():
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		file1 = open(filename, "r")
		print(file1.read())
		file1.close()


if __name__ == '__main__':
	main()
