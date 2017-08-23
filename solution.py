#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import getopt


class Solution:
    def __init__(self, n, outputfile):
        self.arrayList = []
        self.array = []
        self.n = n
        self.outputfile = outputfile

    def printArrayList(self):
        l = len(self.arrayList)
        for i in range(len(self.arrayList)):
            print "when max value is %s" % (i + 1)
            for j in range(len(self.arrayList[i])):
                print self.arrayList[i][j]

    def printArrayListCount(self):
        sum = 0
        for i in range(len(self.arrayList)):
            sum += len(self.arrayList[i])
        print "solution count: %s" % sum

    def getDecendingSequence(self, seq):
        dec = sorted(seq, reverse=True)
        return dec

    def getSeedSequence(self, n):
        seedSequence = []
        seedSequence.append(n)
        for i in range(n - 1):
            seedSequence.append(0)
        print "seedSequence is :%s" % seedSequence
        return seedSequence

    def findInArray(self, seq, ar):
        for j in range(len(ar)):
            print j
            if seq == ar[j]:
                return True
            else:
                return False

    def getMaxNumberIndex(self, array):
        i = array.index(max(array))
        return i

    def addIntoArrayList(self, seq):
        if not self.existInDestArray(seq):
            self.arrayList[max(seq) - 1].append(seq)

    def generateIntoArray(self, sourceArray):
        src = sourceArray[:]
        maxNumber = max(src) - 1
        maxNumberIndex = self.getMaxNumberIndex(src)
        src[maxNumberIndex] -= 1

        for i in range(self.n):
            seq = src[:]
            if i == maxNumberIndex:
                continue
            else:
                seq[i] += 1
            if max(seq) <= maxNumber:
                self.addIntoArrayList(seq)

    def existInDestArray(self, seq):
        array = self.arrayList[max(seq) - 1]
        for i in range(len(array)):
            if self.getDecendingSequence(seq) == array[i]:
                return True
        return False

    def run(self):
        for i in range(self.n - 1):
            self.arrayList.append([])

        self.array.append(self.getSeedSequence(self.n))
        self.arrayList.append(self.array)

        m = len(self.arrayList[self.n - 1])
        for i in range(self.n - 1, 0, -1):
            while True:
                for j in range(len(self.arrayList[i])):
                    self.generateIntoArray(self.arrayList[i][j])
                if m == len(self.arrayList[i - 1]):
                    break
                else:
                    m = len(self.arrayList[i - 1])

        self.printArrayList()
        self.printArrayListCount()

        file_object = open(self.outputfile, "a")
        # file_object.write(''.join(map(str, self.arrayList)))
        for i in range(len(self.arrayList)):
            for j in range(len(self.arrayList[i])):
                for k in range(len(self.arrayList[i][j])):
                    file_object.write(str(self.arrayList[i][j][k]))

                    if not k == len(self.arrayList[i][j]) - 1:
                        file_object.write(' ')

                file_object.write('\n')
        file_object.close()
        print "Done."

def main(argv):

    i = 0
    outputfile = ''
    print 'python solution.py -i <input> -o <outputfile>'
    print 'such as: python solution.py -i 8 -o 1.txt'
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["i=","ofile="])
    except getopt.GetoptError:
      print 'test.py -i <input> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <input> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--i"):
         i = int(arg)
      elif opt in ("-o", "--ofile"):
         outputfile = arg
    print 'input number is: ', i
    print 'outputfile is: ', outputfile

    f = open(outputfile, 'a')
    f.truncate()
    f.close()

    for num in range(1, i):
        solution = Solution(num, outputfile)
        solution.run()


if __name__ == "__main__":
    main(sys.argv[1:])

