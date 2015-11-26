from __future__ import division
from sympy import *
import numpy as np

x = float(raw_input("Enter x: "))
delx = float(raw_input("Enter DeltaX: "))
def f(float):
	return np.sin(2*np.pi*float)

#Function for Analytic solution
def anasol(n, x):
	#Analytic solution
	n = Symbol('x')
	y = sin(2*pi*n)
	yprime = y.diff()
	Anasol = yprime.evalf(subs={n: x})
	return Anasol
a = anasol(Symbol('x'), x)

# Function for Centeral Diffrence Method from Second derivative
def cd2(x, delx):
	print "Centeral Diffrence Method for Second Derivative"
	n = (f(x+delx)-f(x-delx))/(2*delx)
	print "RondF/RondX: %.7f" % n
	error = abs((n-a)/a)*100
	print "Error Percentage is: %.2f" % error + '%\n'
	return

# Function for Centeral Diffrence Method from Fourth derivative
def cd4(x, delx):
	print "Centeral Diffrence Method for Fourth Derivative"
	n = (-f(x+2*delx)+8*f(x+1*delx)-8*f(x-1*delx)+f(x-2*delx))/(12*delx)
	print "RondF/RondX: %.7f" % n
	error = abs((n-a)/a)*100
	print "Error Percentage is: %.2f" % error + '%\n'
	return

print "Analytic sollution is %0.7f" % a
print "\n"

cd2(x, delx)
cd4(x, delx)
