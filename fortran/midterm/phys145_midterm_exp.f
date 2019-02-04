!     gfortran phys145_midterm_exp.f -o phys145_midterm_exp.out
!     ./phys145_midterm_exp.out
!     http://users.monash.edu.au/~johnl/astro/linux/fortran-primer.pdf page 27
      implicit none
      real x,sum,fac,pi
      integer n

      pi=4.0*atan(1.0)
      x=3.0-pi
      sum=0

      do n=0,4
         sum=sum+x**n/fac(n)
      enddo

      print*,x,sum
      end

      function fac(n)

      implicit none
      real fac,prod
      integer n,i

      if(n.eq.0)then
         fac=1.0
         return
      endif

      prod=1.0
      do i=1,n
         prod=prod*i
      enddo

      fac=prod
      end
