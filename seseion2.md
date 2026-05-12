P -> can sort

Knapsack Fractional
7 objects, capacity 15

| Object | Value | Weight | Profit/Weight |
|--------|-------|--------|---------------|
| 1      | 10    | 2      | 5             |
| 2      | 5     | 3      | 1.67          |
| 3      | 15    | 5      | 3             |
| 4      | 7     | 7      | 1             |
| 5      | 6     | 1      | 6             |
| 6      | 18    | 4      | 4.5           |
| 7      | 3     | 3      | 1             |

| Object | Fraction Taken | Weight Left |
|--------|----------------|-------------|
| 5      | 1              | 14          |
| 1      | 1              | 12          |
| 6      | 1              | 8           |
| 3      | 1              | 3           |
| 2      | 1              | 0           |
| 4      | 0              | 0           |
| 7      | 0              | 0           |

Object 1: value/weight = 10/2 = 5
Profit by weight: 5, 5/3, 15/5, 7/7, 6/1, 18/4, 3/3
Profit by weight: 5, 1.67, 3, 1, 6, 4.5, 3
Sort by profit/weight: Object 1
