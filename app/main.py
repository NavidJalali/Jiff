from os import listdir
from sys import argv
from imageio import imread, get_writer


path_to_src = "./src/"
fps = 30.0


def print_usage():
    print("\n" + "_" * 64)
    print("Simply type:")
    print("jiff <optional: FPS>")
    print("_" * 64 + "\n")


def are_args_correct():
    if len(argv) != 2:
        if len(argv) == 1:
            print("No FPS specified. The default is 30FPS.")
        else:
            print(len(argv))
            print("ERR: Unexpected Argument Count")
            print_usage()
            return False
    try:
        if len(argv) == 2:
            if argv[1] == "--help" or argv[1] == "-h":
                print_usage()
                return False
            else:
                fps = float(argv[1])
    except Exception as e:
        print(e)
        return False

    return True


def main():
    if are_args_correct():
        if len(argv) == 2:
            fps = float(argv[1])
        try:
            pics = listdir(path=path_to_src)
            with get_writer("./output.gif", mode="I", fps=fps) as writer:
                for pic in pics:
                    writer.append_data(imread(f"{path_to_src}{pic}"))
                print(f"{fps} Done!")
        except Exception as e:
            print(f"ERR: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
