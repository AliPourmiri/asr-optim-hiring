## Solution description 

The solution is based on a recursive idea whose running time gets controlled by  memoization technique and hence it becomes a dynamic programming problem.

Suppose that T={t_1,...t_n, t_f} denote the set of times when at least one machine is available for sale and t_f is the last day. 
The algorithm goes trough set  T one by one, and decides to buy or not to buy a machine. As soon as the decision is made, the problem becomes smaller because by choosing a machine at t_i we move to future time slot t_j with  increase in the capital. 
  
Define profit(t_1, capital) denote the money made by the company from the first day by initial capital.
One option is not to buy any machine at time t_1 so we have profit(t_2,capital).
However, if we buy a machine at time t_1 we may resell at time t_j with profit p_j then the problem becomes profit(t_j, capital+p_j) 
Let  A=Max_{m,t_j}( profit(t_j, capita+p_j)),
where the maximum is taken over all machines  that are available at time t_1  and t_j's are  all time posibilities in T that we  resell the machine and get positive profit. Then, profit(t_1, capital)=max{A, profit(t_2,capital)}. The same holds for the next time steps t_2,t_3,...,t_n

The running time is polynomial in terms of N (the number of machines), T ( all time steps), C ( the maximum possible money made by the company) 

 - [ ] To run the program: python3  Solution.py
 - [ ] The code perfectly works with python 3.8.5
