!     gfortran phys145_lab3_ex1.f -o phys145_lab3_ex1.out
!     ./phys145_lab3_ex1.out

      program integer powers
      integer i
      
      write(*,*) 'The first 4 powers of integer numbers 1 through 10'
      write(*,*)
     & '       number       1st         2nd         3rd         4th'
      do i = 1, 10
         write(*,*) i, i**1, i**2, i**3, i**4
      enddo
      stop
      end
