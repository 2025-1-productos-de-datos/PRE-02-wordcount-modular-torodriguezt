from homework.src.wordcount import main
import sys

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    main(input_dir, output_dir)
