#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import getopt
import math


class Solution:
    def __init__(self, n, k, outputfile):
        self.arrayList = []
        self.n = n
        self.k = k
        self.outputfile = outputfile
        self.maxInResult = self.k - self.n + 1
        self.minInResult = int(math.ceil(float(self.k) / float(self.n)))
        print "self.maxInResult: %s" % self.maxInResult
        print "self.minInResult: %s" % self.minInResult

    def getSeedSequence(self):
        seedSequence = []
        seedSequence.append(self.k - self.n + 1)
        for i in range(self.n - 1):
             seedSequence.append(1)
        print "seedSequence is :%s" % seedSequence
        return seedSequence

    def printArrayList(self):
        l = len(self.arrayList)
        print "self.arrayList length is: %s" % l
        for i in range(len(self.arrayList)):
            print "when max value is %s" % (i + self.minInResult)
            for j in range(len(self.arrayList[i])):
                print self.arrayList[i][j]

    def printArrayListCount(self):
        print "solution count: %s" % self.getSolutionCount()

    def getSolutionCount(self):
        sum = 0
        for i in range(len(self.arrayList)):
            sum += len(self.arrayList[i])
        return sum

    def getDecendingSequence(self, seq):
        dec = sorted(seq, reverse=True)
        return dec

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
        # If it does not exist in the two-dimensional target array, then seq is added to the array which the max value is max(seq)
        if not self.existInDestArray(seq):
            self.arrayList[max(seq) - self.minInResult].append(seq)

    def generateIntoArray(self, sourceArray):
        src = sourceArray[:]
        # Get the maximum value in the array
        maxNumber = max(src) - 1
        # Get the location of the maximum value in the array
        maxNumberIndex = self.getMaxNumberIndex(src)
        # After subtracting 1 from the maximum value of the position, increase 1 to another position
        src[maxNumberIndex] -= 1

        for i in range(self.n):
            seq = src[:]
            # If the position is the one you minus 1 before, skip, otherwise add 1 to this position
            if i == maxNumberIndex:
                continue
            else:
                seq[i] += 1
            # Determines if the maximum value does not exceed the maximum value in this array, added to the target two-dimensional array
            if max(seq) <= maxNumber:
                # print seq
                self.addIntoArrayList(seq)

    def existInDestArray(self, seq):
        # this array is the one which max value equals max(seq) in the two-dimensional target array
        array = self.arrayList[max(seq) - self.minInResult]
        decendSeq = self.getDecendingSequence(seq)
        for i in range(len(array)):
            # Contrast after descending order 
            if decendSeq == array[i]:
                return True
        return False

    def run(self):
        # Initialize the two-dimensional target array
        for i in range(self.maxInResult - self.minInResult + 1):
            self.arrayList.append([])
        print "len(self.arrayList): %s" % len(self.arrayList)
        self.arrayList[self.maxInResult - self.minInResult].append(self.getSeedSequence())

        # m is the current calculated maximum number of elements of self.arrayList[i + self.minInResult-1]
        m = len(self.arrayList[self.maxInResult - self.minInResult - 1])
        for i in range(self.maxInResult - self.minInResult, 0, -1):
            while True:
                for j in range(len(self.arrayList[i])):
                    self.generateIntoArray(self.arrayList[i][j])

                # Exit from this while loop when m no longer changes, otherwise update the value of m
                if m == len(self.arrayList[i - 1]):
                    break
                else:
                    m = len(self.arrayList[i - 1])

        self.printArrayList()
        self.printArrayListCount()

        file_object = open(self.outputfile, "a")
        for i in range(len(self.arrayList)):
            for j in range(len(self.arrayList[i])):
                for k in range(len(self.arrayList[i][j])):
                    file_object.write(str(self.arrayList[i][j][k]))

                    if not k == len(self.arrayList[i][j]) - 1:
                        file_object.write(' ')

                file_object.write('\n')
        file_object.write(':%s\n' % self.getSolutionCount())
        file_object.close()
        print "Done."

        return self.arrayList

def main(argv):
    # test number
    # k=10, n=5, result=7
    # k=12, n=5, result=13
    # k=15, n=5, result=30
    # k=15, n=10, result=7

    n = 0
    k = 0
    outputfile = ''
    print 'python solution.py -n <input n> -k <input k> -o <outputfile>'
    print 'such as: python .\solution.py -n 5 -k 10 -o 1.txt'
    try:
      opts, args = getopt.getopt(argv,"h:n:k:o:",["n=","ofile="])
    except getopt.GetoptError:
      print 'python solution.py -n <input n> -k <input k> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print 'python solution.py -n <input n> -k <input k> -o <outputfile>'
         sys.exit()
        elif opt in ("-n", "--n"):
         n = int(arg)
        elif opt in ("-k", "--k"):
         k = int(arg)
        elif opt in ("-o", "--ofile"):
         outputfile = arg
    print 'input n is: ', n
    print 'input k is: ', k
    print 'outputfile is: ', outputfile

    f = open(outputfile, 'a')
    f.truncate()
    f.close()

    solution = Solution(n, k, outputfile)
    array = solution.run()

if __name__ == "__main__":
    main(sys.argv[1:])
