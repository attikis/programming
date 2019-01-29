!     gfortran phys145_lab3_ex3.f -o phys145_lab3_ex3.out
!     ./phys145_lab3_ex3.out

      program GCD_LCM
      integer a, b, atemp, btemp, y
      write(*,*) '          A           B        GCD(A,B)   LCM(A,B)'
      write(*,*) '==================================================='

      do a = 2, 10
         do b = 2, a-1
            atemp = a
            btemp = b
 1          y = mod(atemp, btemp)
            if (y.eq.0) goto 2
            atemp = btemp     
            btemp = y         
            goto 1
 2          write(*,*) a, b, btemp, a*b/btemp
         enddo
      enddo

      write(*,*) '==================================================='
      stop
      end
