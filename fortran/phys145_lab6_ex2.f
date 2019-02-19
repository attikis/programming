!     gfortran phys145_lab6_ex2.f -o phys145_lab6_ex2.out
!     ./phys145_lab6_ex2.out > lab6_2019ask2.out
!
!     gnuplot
!     plot 'lab6_2019ask2.out' using 2:1
!     k  = 20
!     h  = 3
!     L  = 2.8
!     mg = 30
!     mu(x) = k*x*(1-L/sqrt(x**2 + h**2))/(mg - k*h*(1-L/sqrt(x**2+h**2)))
!     plot [0:1.5] mu(x), "lab6_2019ask2.out" using 2:1

! =================================================================      
!     Function definition
! =================================================================
      real*8 function f(x)
      real*8 x, k, h, L, mg, mu
      common /dedomena/ k, h, L, mg, mu
      f = (1 - L/sqrt(x**2 + h**2))*k
      f = -x*f + mu*(mg - h*f)
      return
      end

! =================================================================      
!     Main program
! =================================================================
      program isorropia
      implicit none

      integer i
      real*8 x, k, h, L, mg, mu
      real*8 x1, x2, xAVG, f
      common /dedomena/  k, h, L, mg, mu
      ! k = 20 means for 1kg mass the extension is 0.5m (F= k dx => dx = 9.81/20 ~ 0.5 m)
      data k, h, L, mg
     &     /20, 3, 2.8, 30/

      do i = 1, 20
         mu = i*1.d-2 ! coeff. of static friction: mu = 0.01, 0.02, 0.03, ...
         x1 = 0
         x2 = 10 ! max dx is less than 10m
 1       xAVG = (x1+x2)/2
         if (f(x1).lt.0 .eqv. f(xAVG).lt.0) then
            x1 = xAVG
         else
            x2 = xAVG
         endif

         if (abs(x1-x2) .gt. 1.d-6) goto 1

!     Print the values of mu and xmax(mu) for subsequent plotting
         write (*, 2) mu, (x1+x2)/2
      enddo

 2    format(F8.3, 2X, F10.6)

!     Terminate program
      stop
      end
