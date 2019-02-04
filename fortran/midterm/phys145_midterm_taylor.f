!     gfortran phys145_midterm_exp.f -o phys145_midterm_exp.out
!     ./phys145_midterm_exp.out
!     http://users.monash.edu.au/~johnl/astro/linux/fortran-primer.pdf page 26
      
      implicit none
      real a,x,f,fd,fdd,y

      f(x)=log(x)
      fd(x)=1.0/x
      fdd(x)=-1.0/x**2
      a=1
      x=1.1

      y=f(a)+fd(a)*(x-a)+fdd(a)*(x-a)**2/2.0
      print*,'x=',x,' f(x)=',y
      end
