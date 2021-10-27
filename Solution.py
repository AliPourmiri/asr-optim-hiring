#The user can execute the file in terminal in a directory where the input file is available
#and the solutions will be printed in terminal
# note that  it is supposed that the input file in "input.txt"

from collections import defaultdict

class Machine:         # we orgenise machine features as a class for better accessibility
    def __init__(self, release_time,  price, resell, profit_rate):
        self.release_time = release_time
        self.profit_rate = profit_rate
        self.price = price
        self.resell = resell

        
    def get_profit(self,time):
        return self.resell-self.price + (time-1-self.release_time)*self.profit_rate
    
    def release(self):
        return self.release_time

    def get_price(self):
        return self.price 
    def __str__(self):
        return 'releasTime:'+str(self.release_time) +' price:'+ str(self.price) + ' resell:'+str(self.resell)+' profit rate:'+ str(self.profit_rate) 
    

def profit_maximizer(machines_list,times_list, cap): # This function receives list of initial capital\\
                                                        # list of machies and buying times,
    if len(machines_list)==0:
        return cap
    if cap == 0:
        return 0
    
    memo, machines_times, times_list = dict(), defaultdict(list), sorted(times_list)
    length = len(times_list)
    
    for m  in machines_list:                     # Here it builds a dictionary (hash table) of times and machines
                                                 # keys are times and items are machines
        machines_times[m.release()].append(m)
    
    def helper(memo, index, cap):                # this is  a recursive procedure whose running time gets
                                                 # controned by memoisation (memo dictianry)
        if (index, cap) in memo:
            return memo[index,cap]
        if index>=length-1:
            memo[index, cap] = cap 
            return cap
        time = times_list[index]
        machines = machines_times[time]
        tmp = helper(memo, index+1, cap)
        for m in machines:
            for j in range(index+1, length):
                prof = m.get_profit(times_list[j])
                if m.get_price()<=cap and prof>0:
                    tmp = max(tmp, helper(memo, j, cap+prof))
                     
        memo[index, cap]= tmp
        return tmp
                               
        
    return helper(memo,0,cap)    
                    
                               
                    
                   
                    
                    
def main_function(): # This function reads the file "input.txt" and calls profit maximizer function.       
    file = open('instance.txt', 'r')
    count = 1
    while True:
        Case=file.readline()   
        Case=list(map(int, Case.split(' ')))
        if sum(Case)==0:
            break
        machines_list = []
        times_list = set()
        for i in range(Case[0]):
            line=file.readline()
            L=list(map(int, line.split(' ')))
            machines_list.append(Machine(L[0],L[1],L[2],L[3]))
            times_list.add(L[0])
        times_list.add(Case[2]+1)       
        times_list = list(times_list)
        ans = profit_maximizer(machines_list, times_list, Case[1]) # call the profit maximizer function for each cas
        print(" Case {c}:".format(c=count), ans )
        count+=1
        
main_function()
    
