def group_by(func,seq):
    dictionary = {}
    values = []
    for value in seq:
        for i in range(len(seq)):
            if func(value) == func(seq[i]):
                values.append(seq[i])
        dictionary[func(value)] = values
        values = []
    return dictionary

def main():
    print(group_by(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
if __name__ == '__main__':
    main()
