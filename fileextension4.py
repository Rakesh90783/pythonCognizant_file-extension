with open("sample.txt") as f:
    with open("sample1.txt", "w") as f1:
        for line in f:
            f1.write(line)