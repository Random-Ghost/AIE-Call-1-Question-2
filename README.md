# Code Explanation
From what I remember of the question, we were to create a memoized algorithm in the first part and find the number of comparisons and sums in the algorithm in the second part.

## First part
From the formula given, we have
```math
tie(i, j) =
\begin{cases}
  x_j & i = 1 \\
  x_{n - 1 - i} & j = n - 1\\
  max(tie(i - 1, j + 1), tie(i - 1, j) + tie(i, j + 1)) & otherwise
\end{cases}
```
We are to find $\ tie(n - 1, 0) \$. Writing the memoized algorithm is pretty straightfoward.

## Second part
If we look at the memo, we see it has a size of $\ n^2 \$. Assuming we have $\ x = (1, 2, 3, 4, 5) \$, the initialized memo is
```math
\begin{bmatrix}
1 & 2 & 3 & 4 & 5 \\
-1 & -1 & -1 & -1 & 4 \\
-1 & -1 & -1 & -1 & 3 \\
-1 & -1 & -1 & -1 & 2 \\
-1 & -1 & -1 & -1 & 1 \\
\end{bmatrix}
```
There are $` (n - 1)^2 `$ unknown values. To find $\ tie(n - 1, 0) \$, we have to find all the values. For each computation, we need to add the right and top values and compare it to the top-right value. So we have 2 operations per value, giving us $` 2(n - 1)^2 `$ in total.
