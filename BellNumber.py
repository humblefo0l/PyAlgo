"""
Bell Numbers (Number of ways to Partition a Set)
Given a set of n elements, find number of ways of partitioning it.
Examples:

Input:  n = 2
Output: Number of ways = 2
Explanation: Let the set be {1, 2}
            { {1}, {2} }
            { {1, 2} }

Input:  n = 3
Output: Number of ways = 5
Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }.

What is a Bell Number?
Let S(n, k) be total number of partitions of n elements into k sets. The value of n’th Bell Number is sum of S(n, k) for k = 1 to n.

 Bell(n) =  \sum_{k=0}^{n}S(n,k)

Value of S(n, k) can be defined recursively as, S(n+1, k) = k*S(n, k) + S(n, k-1)

How does above recursive formula work?
When we add a (n+1)’th element to k partitions, there are two possibilities.
1) It is added as a single element set to existing partitions, i.e, S(n, k-1)
2) It is added to all sets of every partition, i.e., k*S(n, k)

S(n, k) is called Stirling numbers of the second kind





First few Bell numbers are 1, 1, 2, 5, 15, 52, 203, ….

A Simple Method to compute n’th Bell Number is to one by one compute S(n, k) for k = 1 to n and return sum of all computed values. Refer this for computation of S(n, k).

A Better Method is to use Bell Triangle. Below is a sample Bell Triangle for first few Bell Numbers.

1
1 2
2 3 5
5 7 10 15
15 20 27 37 52
The triangle is constructed using below formula.

// If this is first column of current row 'i'
If j == 0
   // Then copy last entry of previous row
   // Note that i'th row has i entries
   Bell(i, j) = Bell(i-1, i-1)

// If this is not first column of current row
Else
   // Then this element is sum of previous element
   // in current row and the element just above the
   // previous element
   Bell(i, j) = Bell(i-1, j-1) + Bell(i, j-1)
Interpretation
Then Bell(n, k) counts the number of partitions of the set {1, 2, …, n + 1} in which the element k + 1 is the largest element that can be alone in its set.

For example, Bell(3, 2) is 3, it is count of number of partitions of {1, 2, 3, 4} in which 3 is the largest singleton element. There are three such partitions:

    {1}, {2, 4}, {3}
    {1, 4}, {2}, {3}
    {1, 2, 4}, {3}.
"""

def bellNumber(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1

    for i in range(1, n+1):

        bell[i][0] = bell[i-1][i-1]

        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

    return bell[n][0]
# Driver program
for n in range(6):
    print('Bell Number', n, 'is', bellNumber(n))

#Time Complexity of above solution is O(n2). We will soon be discussing other
# more efficient methods of computing Bell Numbers.