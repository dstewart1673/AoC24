#!/usr/bin/env/python

from heapq import heappop, heappush

def main():
    list1 = []
    list2 = []
    diff = 0

    with open("input.txt", "r") as file:
        for line in file:
            spl = line.split("   ")
            heappush(list1, spl[0])
            heappush(list2, spl[1])

    while len(list1) > 0:
        diff += abs(int(heappop(list1)) - int(heappop(list2)))

    print(diff)

if __name__ == '__main__':
  main()
