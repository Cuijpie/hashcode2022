
def main():
    file = open('a.txt', 'r')

    count = 0
    # Strips the newline character
    for line in file.readlines():
        count += 1
        print("Line{}: {}".format(count, line.strip()))


if __name__ == '__main__':
    main()
