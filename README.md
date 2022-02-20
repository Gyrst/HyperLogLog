# Implementation of the HyperLogLog Algorithm

## 1.0 Introduction

The following report provides a description of an implementation of HyperLogLog,
which is an efficient algorithm used for estimating a number of distinct elements in a given input stream. The implementation makes use of a few smaller functions, implemented and tested independently before assembling the algorithm. The functions, described in more detail in the next section, are hash, rho and registers. Based on the registers, HyperLogLog produces an estimate of the stream cardinality. The total space usage to produce the result is m log(log n) bits, where m is the number of registers and n is the size of the input stream.

## 2.0 Implementations

### 2.1 Hash Function

The hash algorithm used for hyperLogLog is implemented using bitwise operations. A helper function is used that returns the number of set bits in a given input value. We use the given matrix A containing 32 32 − bit integers to calculate the hash. For each value n from the input stream, the helper function is applied to the result of multiplying n with a single element from A (bitwise A[i]&n). Then the operation &1 is applied to the result, what corresponds to modulo 2 operation - if it evaluates to 0, the integer is even, if it’s 1, the integer is odd. Next the result is multiplied by ith power of 2, what is done by applying a left shift i to the result (<< i). These operations are done in a for loop, with i being in range 0 − 32. With each iteration the results are accumulated to return a final hash value of n.

### 2.2 Rho
The Rho method returns the position of the first 1 in the binary representation. The bitwise right shift was used where we start with shifting 32 − i (where i iterates over range 33) and then checks whether the current bit in this position is a 1 by using the bitwise AND operator. It returns i when it finds the first bit, otherwise it returns None.

### 2.3 Registers
The registers function combines both the hash function, rho and also introduces another hash-function f(x), which purpose is to calculate an index for each input value. This index is used to map a value to certain ”bin” in the register M - M[index]. When m is of size 1024, we use a right shift of 21 to get indexes between 0 − 1023. When we have the index for our input, we calculate the hash value of it using our hash function. Then we apply the rho function on this hash value and store the rho value for the hashed input under in the index given by f(x) in our register. If the current value at this position is smaller than the new value found, the current value is then replaced. The function then returns M with its values.

### 2.4 HyperLogLog

At last, hyperLogLog algorithm uses the results provided by registers to produce the desired output. The implementation follows the pseudocode provided in the problem description. We use the provided ”magic” constant αm = 0.7213/(1 + 1.079/m) for the raw estimate and calculate the number of empty registers. Based on these values the final estimate is returned: for smaller cardinalities and at least one non-empty register linear counting is used; for larger estimates, large range correction is applied instead.

## 3.0 Experiments

See the report pdf for experiment details.

## 4.0 Notes from Class (Applied Algorithms):

### 32-bit unsigned representation of integers: 

- Note that in order to enforce 32-bit unsigned representation
of integers, you need to take a bitwise AND with the mask 0xffffffff.
That is, assuming x is an integer, the 32-bit unsigned representation can be
recovered by the expression x & 0xffffffff.
- If your solution is not accepted by CodeJudge, 
check that you are using the correct bit order; the solution is written assuming that most sig-
nificant bit, the leftmost bit, is bit number 32, and the least significant bit,
the rightmost bit, is bit number 1, and that the first row of the matrix is row
number 1 and corresponds to the least significant bit.
-Implement the function ρ for k = 32.
- HyperLogLog makes heavy use of the function ρ : {0, 1} k → N defined by
ρ(x) = min{i | x k−i+1 = 1}, that is, ρ(x) is equals the position of the first
1 in the binary representation of the integer x read from left to right. That
is, for k = 8, and if x = 10101010, then ρ(x) = 1, if x = 00110011, then ρ(x) = 3, and if x = 00000001, then ρ(x) = 8. 
- Note that ρ(0) is undefined.
- ρ(h(x)) means that you first compute the hash value for the input element x, then compute the corresponding first one-bit position for the element. You do this for each element in the set {1,2,…,10^6}, that is, every positive integer from 1 to 1000000. 
- This is what you do empirically. You are then supposed to compare the distribution of the ρ values to what the theory predicts; and the theory assumes that the hash function is perfectly random. Your hash function is not, it is deterministic.
- The part “random y ∈ {0,1}^k” means that y is a random k-bit vector selected among all k-bit vectors; that is, {0,1}^k is the set of all k-bit vectors. That means that y is such that every bit is selected such that it is 1 at probability 0.5, independent of all other bits.
- The theory predicts us that if y is chosen at random, then we have Pr[ρ(y) = i] = 2^(-i). That is, the probability that the random bit vector y has its first 1 in the position i, counting from the left, is 2^(-i). To see why, consider the set of all bit k-bit vectors. Exactly half of those have the leftmost bit set to 1. Among the remaining half, exactly half of those start with the bit pattern 01, so 1/4 of the bit vectors have ρ(01…) = 2. And of the remaining 1/4, exactly half start with the bit pattern 001, so we have ρ(001) = 3 for exactly 1/8 of the vectors. So, if we chose y truly randomly, we would expect the distribution of ρ-values to be in agreement with this theory.

- Now the empirical question is how well do the hash values with our actual hash map resemble those of randomly chosen bit vectors? We need to create an empirical distribution of the ρ-values. If the hash function h truly mapped all input vectors into completely random vectors, we would expect that, among the 1 million inputs, approximately half would have ρ value of 1, about 1/4 would have value of 2 and so on. This is what you are supposed to explore.
