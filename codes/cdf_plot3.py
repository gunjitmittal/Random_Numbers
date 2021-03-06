#Importing numpy, scipy, mpmath and pyplot
from math import e, log
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
# import subprocess
# import shlex
#end if



x = np.linspace(-1,10,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
cdf = []
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('/Users/Shared/probability/manual/codes/uni.dat',dtype='double')
randvar2 = [ -1 * 2 * log(1-sample, e) for sample in randvar]
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar2 < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list


def V_pdf(x):
	if x>=-0.3:
		return (1 - np.exp(-x/2))

vec_v_pdf = scipy.vectorize(V_pdf)

plt.plot(x,vec_v_pdf(x))
plt.plot(x.T,err, "o")#plotting the CDF
# plt.plot(x.T,err)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
# plt.savefig('../figs/uni_cdf.pdf')
# plt.savefig('../figs/uni_cdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
