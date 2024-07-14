# Algorithmic Triangle Counting: Exact, Approximate, and Streaming Methods

## Overview
We implemented and evaluated three algorithms for triangle counting in graphs: DOULION, TRIÈST-base, and TRIÈST-improved. 

Tests were conducted on three categories of graph sizes: small, medium, and large. 

For DOULION, the performance was analyzed across various probabilities of the sparsification parameter, focusing on running time and triangle count accuracy. 

For TRIÈST-base and TRIÈST-improved, different memory parameter values (M) were tested to compare running times and the accuracy of triangle estimations.

## Results
The findings indicated that DOULION performed well across all graph sizes, with the best results at specific probabilities (e.g., $p$ = $0.77$ for small graphs). 

TRIÈST-improved consistently outperformed TRIÈST-base in terms of triangle count accuracy, especially with smaller memory sizes, although both versions exhibited similar running times. 

Overall, TRIÈST-improved showed significantly lower absolute error in predictions compared to the base version, making it a more reliable choice for accurate triangle counting with limited memory resources.








