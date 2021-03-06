import argparse

def main():
    parser = argparse.ArgumentParser(description='Show some lines from a large file')
    parser.add_argument('FILE', help='target file')
    parser.add_argument('--lines', '-l', type=int, default=5,
                        help='number of lines to show')
    args = parser.parse_args()

    f = open(args.FILE)
    i=0
    print('-------------------')
    for line in f:
        if i >= args.lines:
            break
        print(line.strip())
        i += 1
    f.close()
    print('-------------------')

if __name__ == '__main__':
    main()
