!     gfortran phys145_lab6_ex1.f -o phys145_lab6_ex1.out
!     ./phys145_lab6_ex1.out

      program arctan
      implicit none
      real*8 error, pi2
      real*8 y, x, x1, x2, xavg, epsilon, initialtime, finaltime
      integer i
      pi2 = 1.5707963267948 ! pi/2

      write(*,*) "What precision do you require?"
      read(*,*) epsilon
      write(*,*) "Please input value of y:"
      read(*,*) y

! =================================================================      
!     First we try the Bisection algorithm method
! =================================================================
      call cpu_time(initialtime) !  record start time

!     Do-loop from 1 to 10000 for precice time measurement
      do i=1, 10000
         x1 = -pi2 + 1.d-7 ! tan(-90) = infty
         x2 = +pi2 - 1.d-7 ! tan(+90) = infty
 1       xavg = (x1+x2)/2
!     write(*,*) 'x1 = ', x1, " x2 = ", x2
!     Check if both operants are the same (left to right)
         if ((tan(x1) - y).lt.0 .eqv. (tan(xavg) - y) .lt.0) then
!            write(*,*) 'x1 = ', x1
            x1 = xavg
         else
!            write(*,*) 'x2 = ', x2
            x2 = xavg
         endif
         if (abs(x1-x2) .gt. epsilon) goto 1
      enddo

!     Save final time
      call cpu_time(finaltime)
      
!     Print solution
      write(*,*) 'Bisection algorithm: arctan(', y, ') = ', (x1+x2)/2
      write(*,*) 'Time elapsed: ', (finaltime-initialtime)/10000
      write(*,*)

! =================================================================
!     Now the Newton-Raphson method
! =================================================================
      call cpu_time(initialtime)
      do i = 1, 10000
         x = 0
 2       error = (tan(x) -y ) * cos(x)**2 !! f(x)/f'(x)
         x = x - error
         if (abs(error) .gt. epsilon) goto 2
      enddo

!     Save final time
      call cpu_time(finaltime)
      
!     Print solution
      write(*,*) 'Newton-Raphson algorithm: arctan(' , y,  ' ) = ', x
      write(*,*) 'Time elapsed: ', (finaltime-initialtime)/10000

!     Terminate program
      stop
      end
