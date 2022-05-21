new_file = open("sample.txt", "w")
with open("sample1.txt", "r") as f:
    new_file.write(f.read())

new_file.close()
