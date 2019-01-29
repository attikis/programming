!     gfortran phys145_lab3_ex2.f -o phys145_lab3_ex2.out
!     ./phys145_lab3_ex2.out

      program series
      real*8 sum, term, pi, piEstimate
      integer n

      sum = 0.d0
      n=0
 1    n=n+1
      term = 1.d0/n**4
      if(term.lt.1.d-5) goto 2
      sum = sum + term
      goto 1
      
 2    n = n - 1
      pi = acos(-1.d0)
      piEstimate = (sum * 90)**0.25d0
      write(*,*) 'Exact value of pi:', pi
      write(*,*) 'Estimate    of pi:', piEstimate
      stop
      end
