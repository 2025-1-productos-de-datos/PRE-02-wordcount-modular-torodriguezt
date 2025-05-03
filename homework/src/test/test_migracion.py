from homework.src.wordcount import main
import os

def test_migracion():
    input_dir = "data/input"
    output_dir = "data/output"

    main(input_dir, output_dir)

    output_file = os.path.join(output_dir, "wordcount.tsv")
    if not os.path.exists(output_file):
        raise FileNotFoundError("El archivo wordcount.tsv no existe.")

    results = {}
    with open(output_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        key, value = line.strip().split("\t")
        results[key] = value

    assert results.get("computational", 0) == "3"
    assert results.get("analytics", 0) == "5"
