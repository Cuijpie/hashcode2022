
def main():
    file = open('a.txt', 'r')

    header = file.readline()
    print(header)

    for line in file.readlines():
        print(line.strip().split(" "))


if __name__ == '__main__':
    main()
