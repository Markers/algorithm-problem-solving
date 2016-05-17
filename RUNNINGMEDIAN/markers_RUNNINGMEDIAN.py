# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2016. 5. 17.
'''


import sys
import unittest
import heapq

rl = lambda: sys.stdin.readline()


class Test_Median(unittest.TestCase):
    def test(self):
        pass

class Median():


    def __init__(self,n,a,b):
        self.number = 1983
        self.n = n
        self.a = a
        self.b = b
        self.permutation = []
        self.sum = 0


    def make_permutation(self):
        # self.permutation[0] = self.number
        while len(self.permutation) < self.n:
            if len(self.permutation) == 0:
                self.permutation.append(self.number)
            else:
                self.permutation.append(self.do_formula())

            self.sum += get_median_value(self.permutation)
            # print self.sum


    def do_formula(self):
        self.number = ( self.number * self.a + self.b ) % 20090711
        return self.number

    def get_sum(self):
        return self.sum % 20090711


def get_median_value(iterable):
    # do heapsort & return median value
     h = []
     for value in iterable:
         heapq.heappush(h, value)
     # return [heapq.heappop(h) for i in range(len(h))]

     # 0 1 2 3 -> 4/2=2 -> 2-1 ==> index 1
     # 0 1 2 -> 3/2=1 ->
     pivot = 0
     if len(h) % 2 == 0:
         pivot = len(h)/2 - 1
     else:
         pivot = len(h)/2

     # print [heapq.heappop(h) for i in range(len(h))]
     # print "median : {} ".format(heapq.nsmallest(pivot+1,h))

     return heapq.nsmallest(pivot + 1, h)[-1]


def main():
    for _ in xrange(int(rl())):
        n, a, b = map(int, rl().rstrip().split() )
        median = Median(n,a,b)
        median.make_permutation()
        print median.get_sum()
        # print median.permutation


if __name__ == "__main__":
    main()
