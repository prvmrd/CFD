from __future__ import division
from sympy import *
import numpy as np

x = float(raw_input("Enter x: "))
delx = float(raw_input("Enter DeltaX: "))

def f(float):
	return np.sin(2*np.pi*float)

def anasol(n, x):
	#Analytic solution
	n = Symbol('x')
	y = sin(2*pi*n)
	yprime = y.diff()
	Anasol = yprime.evalf(subs={n: x})
	return Anasol

def cd2(x, delx):
	n = (f(x+delx)-f(x-delx))/(2*delx)
	print "RondF/RondX: %.7f" % n
	return

def cd4(x, delx):
	n = (-f(x+2*delx)+8*f(x+1*delx)-8*f(x-1*delx)+f(x-2*delx))/(12*delx)
	print "RondF/RondX: %.7f" % n
	return



cd2(x, delx)
cd4(x, delx)
print anasol(Symbol('x'), x)
