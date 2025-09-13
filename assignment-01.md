

# CMPS 2200 Assignment 1

**Name:**___Petra Radmanovic______


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
. Yes, it is. 
 2^{n+1} = 2*2^n
since 2 is a constant, 2^{n+1} still belongs in O(2^n) and constant can be ignored for big O notation
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  No, 2^{2^n} is growing at a speed much larger than 2^n since the exponent is always 2^n. This since other power growth takes longer, it would not be upper bounded simply by 2^n. When plugging in values for n, 2^{2^n} will grow much faster than 2^n. Also, since the emponent is so significatnly larger, it also cannot be reduced to a constant for larger growth. 
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  No, it does not.
when taking the limit as n appraches infinity, n^1.01 / log2 n appraoches infinity, meaning n^1.01 grows at a faster rate than log2 n. sSo, n^1.01 is not upper bounded by log^2 n.
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  Going along with the previous question, Yes n^1.01 is in omega of log2n. this is becuase since the limit appraches infinity, log2n is below n^1.01 when n gets progressively larger, meaning it is the lower bound,
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  No, it is not.
The square root of n can also be written as n^0.5, meaning it is a polynomial. Whean taking the limit as n appraches inifinity for n^0.5/(log n) ^3 approaches infinity, meaning n^0.5 eventually is consistently above (log n)^3, so it is not upper bounded. 
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  
Yes, it is. Again, since the limit would be evaluated to infinity, sqare root of n is lower bounded by (log n)^3

2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  
.  
.  THe fibonacci function takes a number input, and creates a future series of numbers where it takes the number before it, and the number 2 numbers before it and sums them together to get the next number. As the sequence progresses, the space between sequential numbers grows. 
.  
.  The function works by having a base case for when the number is 0 and 1, and then if it is any larger the function calls itself to get the previous two numbers recursivley and then sum them together for the next result. so the function would get the next number in the sequence. x is the x-ith place in the sequence. 
.  
. 
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  
.  Both the Work and Span of this implementaiton would be O(n) becuase the for loop loops over each element, and then does a constant amount of work per element. since there is no parallelism, the span is no different since there is only one path taken, not multiple that we can calculate the longest one of. 
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
.  When the recursive program is run sequentially, the same amount of work is done consistently for each node, so the amount of work is propportional to the number of nodes, or O(n). 

When done sequentially, work and span are the same. This is becuase the two sides are dependent on one another, so even if the span for each one is S(n/2), since there are two of them it would be 2*S(n/2) or just S(n), meaning it is consistent and would be O(n)
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  When each recursive call spawns a new thread, the work remains consistent but the span changes since the longest possible run changes and it is not dependent on any other value. Parallelism doesnt change total number of operations, which is consistnent with the number of nodes or O(n). However, now the span does end up being S(n) + S(n/2) +S(n/4) ...etc The combine is a constant, so the span ends up being S(log n)
.  
.  
.  
.  
.  
.  

