# Implementation of the HyperLogLog Algorithm



## Here is the github repository for HyperLogLog. Let's work in each our Python file and then combine the work later! I think that will be the easiest! 

### Notes:

#### 32-bit unsigned representation of integers: 

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
