#!/bin/sh

gnuplot -e 'plot "phys145_lab5_ex2.input" using 1:3; set title "x as a function of t, without errors"; set xlabel "t"; set ylabel "x(t)"; plot "phys145_lab5_ex2.input" using 1:3; set term epscairo; set out "lab5_2019_ask2_plot1.eps"; replot; exit'

gnuplot -e 'set title "y as a function of t, with horizontal and vertical errors"; set xlabel "t"; set ylabel "y(t)";  plot "phys145_lab5_ex2.input" using 1:5:($1-$2):($1+ $2):($5-$6):($5+$6) with xyerrorlines; set term epscairo; set out "lab5_2019_ask2_plot2.eps"; replot; exit'

gnuplot -e 'set title "KITSCH !!"; unset border; unset tics; unset key; set linetype 1 lw 6 lc rgb "green" pointtype 6; set size ratio 0.9; plot "phys145_lab5_ex2.input" using 3:5 with lines; set term epscairo; set out "lab5_2019_ask2_plot2.eps"; replot; exit'
