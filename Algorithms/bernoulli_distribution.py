import numpy as np
 
class bernoulli():
    def pmf(x,p):
        """
        probability mass function        
        """
        f = p**x*(1-p)**(1-x)
        return f
    
    def mean(p):
        """
        expected value of bernoulli random variable
        """
        return p
    
    def var(p):
        """
        variance of bernoulli random variable
        """
        return p*(1-p)
    
    def std(p):
        """
        standart deviation of bernoulli random variable
        """
        return bernoulli.var(p)**(1/2)
    
    def rvs(p,size=1):
        """
        random variates
        """
        rvs = np.array([])
        for i in range(0,size):
            if np.random.rand() <= p:
                a=1
                rvs = np.append(rvs,a)
            else:
                a=0
                rvs = np.append(rvs,a)
        return rvs
       
       
p=0.2 # probability of having an accident

bernoulli.mean(p) # return -> 0.2
bernoulli.var(p) # return -> 0.16
bernoulli.std(p) # return -> 0.4

bernoulli.rvs(p,size=10) 
#return-> array([0., 0., 0., 0., 1., 0., 1., 0., 0., 1.])
