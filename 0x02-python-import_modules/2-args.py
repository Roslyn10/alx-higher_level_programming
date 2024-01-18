#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    def print_arguments():
        num_arguments = len(sys.argv) - 1
        arguments_list = sys.argv[1:]

        if num_arguments == 0:
            print("0 arguments.")
        elif num_arguments == 1:
            print("1 argument:")
            print("1:", arguments_list[0])
        else:
            print("{} arguments:".format(num_arguments))
            for i, arg in enumerate(arguments_list, start=1):
                print("{}: {}".format(i, arg))

    print_arguments()
