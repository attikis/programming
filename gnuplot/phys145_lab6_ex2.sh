#!/bin/sh

gnuplot -e 'k=20; h=3; L = 2.8; mg=30; mu(x) = k*x*(1-L/sqrt(x**2 + h**2))/(mg - k*h*(1-L/sqrt(x**2+h**2))); plot [0:1.5] mu(x), "lab6_2019ask2.out" using 2:11; set title "{/Symbol m}(x) as a function of x"; set xlabel "x"; set ylabel "{/Symbol m}(x)"; plot [0:1.5] mu(x), "lab6_2019ask2.out" using 2:1; set term epscairo; set out "lab6_ex2_plot1.eps"; replot; exit'
