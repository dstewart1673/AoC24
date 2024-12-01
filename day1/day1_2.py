#!/usr/bin/env/python

def main():
    list1 = []
    list2 = {}
    diff = 0

    with open('input.txt', 'r') as file:
        for line in file:
            spl = line.replace('\n', '').split('   ')
            list1.append(spl[0])
            if spl[1] in list2:
                list2[spl[1]] += 1
            else:
                list2[spl[1]] = 1

    for x in list1:
        if x in list2:
            diff += int(x) * int(list2[x])

    print(diff)

if __name__ == '__main__':
  main()
