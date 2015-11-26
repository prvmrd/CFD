from __future__ import division
from sympy import *
import numpy as np

x = float(raw_input("Enter x: "))
delx = float(raw_input("Enter DeltaX: "))

def f(float):
	return 1/4*float**2

def anasol(x):
	#Analytic solution
	X = Symbol('x')
	y = 1/4*X**2
	yprime = y.diff(X)
	f = lambdify(X, yprime, 'numpy')
	c = f(np.ones(1))
	AnalyticSol = c[0] * x
	return AnalyticSol


def fd(x, delx):
	print "Forward Diffrence Method"
	n = (f(x+delx)-f(x))/delx
	error = abs(((n-anasol(x))/anasol(x)) * 100)
	print "RondF/RondX: %.2f" % n
	print "Error Percentage is: %.2f\n" % error
	return 

def bd(x, delx):
	print "Forward Diffrence Method"
	n = (f(x)-f(x-delx))/delx
	error = abs(((n-anasol(x))/anasol(x)) * 100)
	print "RondF/RondX: %.3f" % n
	print "Error Percentage is: %.2f\n" % error
	return

def cd(x, delx):
	print "Centeral Diffrence Method"
	n = (f(x+delx)-f(x-delx))/(2*delx)
	error = abs(((n-anasol(x))/anasol(x)) * 100)
	print "RondF/RondX: %.3f" % n
	print "Error Percentage is: %.2f\n" % error
	return

def run():
	print "1: Forward difference"
	print "2: Backward difference"
	print "3: Central difference"
	print "4: All Methods"
	method = int(raw_input("Enter your prefrred method: "))
	print "\n"
	if method == 1:
		fd(x, delx)
	if method == 2:
		bd(x, delx)
	if method == 3:
		cd(x, delx)	
	if method == 4:
		fd(x, delx), bd(x, delx), cd(x, delx)
run()
