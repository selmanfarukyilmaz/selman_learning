line = input()
def split_and_join(line):
    a = line.split(" ");
    a = "-".join(a)
    return a;

result = split_and_join(line)
print(result)