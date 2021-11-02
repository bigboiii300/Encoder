from time import perf_counter

from src.container import Container

MAX_RANDOM_COUNT = 10000


def main(*args: str):
    file = args[0] == "input"
    input_file = None
    count_random = None
    output_file = None
    start = None
    try:
        try:
            if not file:
                count_random = int(args[1])
                if 0 <= count_random <= MAX_RANDOM_COUNT:
                    pass
                else:
                    raise ValueError
            else:
                input_file = open(args[1], "r")
            output_file = open(args[2], "w")
        except OSError:
            print("Incorrect file")
            exit(1)
        except ValueError:
            print("Incorrect count of random elements")
            exit(1)
        start = perf_counter()
        container = Container.from_file(
            input_file) if file else Container.random_symbols(
            count_random)
        container.output(output_file)
        container.insertion_sort()
        print("\n-----Straight Insertion-----\n", file=output_file)
        container.output(output_file)
    except Exception as exception:
        print(*exception.args, file=output_file)
    finally:
        if not file:
            pass
        else:
            input_file.close()
        output_file.close()
        return perf_counter() - start
