#from scipy.stats import beta
from scipy.integrate import quad

import math

a = 200
b = 0.80
 
def beta_1(a,b):
     
    '''uses gamma function or inbuilt math.gamma() to compute values of beta function'''
     
    #beta = math.gamma(a)*math.gamma(b)/math.gamma(a+b)
    beta = math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a+b))
    return beta


solution = beta_1(a,b);
print ("beta_value = ",solution)


#from scipy.integrate import quad

def integrand(solution):
    return solution

ans, err = quad(integrand, 0, 20)
print ("integration value ={0}, error value={1}",ans, err)



