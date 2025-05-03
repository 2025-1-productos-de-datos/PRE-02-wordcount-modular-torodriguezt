import os

from ._internals.read_all_lines import read_all_lines
from ._internals.preprocess_lines import preprocess_lines
from ._internals.split_into_words import split_into_words
from ._internals.count_words import count_words
from ._internals.write_word_counts import write_word_counts


def main(input_dir: str, output_dir: str):
    input_path = input_dir 
    output_path = os.path.join(output_dir, "wordcount.tsv") 

    lines = read_all_lines(input_path)
    cleaned_lines = preprocess_lines(lines)
    words = split_into_words(cleaned_lines)
    results = count_words(words)
    write_word_counts(results, output_path)

if __name__ == "__main__":
    main()