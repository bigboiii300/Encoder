from sys import argv

import src.main

if __name__ == "__main__":
    if len(argv) == 4 and (
            argv[1] == "input" or argv[1] == "rnd" and argv[2].isdigit()):
        print("%.7f" % src.main.main(*argv[1:]), "seconds")
    else:
        print("For tests: python main.py input <input_file> <output_file>\n"
              "For random: python main.py rnd <count_of_elements> <output_file>")
