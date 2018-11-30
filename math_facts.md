## Sum of digits
The sum of the digits of any number N to base 10 is equal to N minus some multiple of 9.  
```
def superDigit(n, k):  
    return(int(n*k) % 9 or 9)  
```
(a+b)%x = ((a%x)+(b%x))%x  
Funny fact: an algorithmic task with sum of digits was actualy executing faster without using these facts (just simple recurision + minor optimisations).
