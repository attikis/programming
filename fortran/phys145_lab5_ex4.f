!     gfortran phys145_lab5_ex4.f -o phys145_lab5_ex4.out
!     ./phys145_lab5_ex4.out

      real*8 function average(v,n)
      integer n, i
      real*8 v(n)
      average = 0.d0
      do i = 1, n
         average = average + v(i)
      enddo
      average = average/n
      return
      end

      real*8 function deviation(v,n)
      integer n, i
      real*8 v(n), sum
      sum       = 0.d0
      deviation = 0.d0
      do i = 1, n
         sum = sum + v(i)
         deviation = deviation + v(i)**2
      enddo
      sum = sum/n
      deviation = sqrt(deviation/n - sum**2)
      return
      end

      program Averages_and_Deviations_in_Prices_and_Ratings
      implicit none
      character*20 name(100)
      real*8 features(100,3), average, deviation
      integer i,j,n

      open(unit=8, file='lab4_2019_ask1.input', status='old')

      do i = 1, 100
         read(8,*,end=1) name(i), (features(i,j), j = 1, 3)
      enddo
      write(*,*) 'WARNING: Reached a limit of 100 models !!'
 1    n = i-1
      write(*,2) average(features,      n), deviation(features,      n)
      write(*,3) average(features(1,3), n), deviation(features(1,3), n)
 2    format('Average price: ', F7.2, ', deviation: ', F7.2)
 3    format('Average rating: ', F7.2, ', deviation: ', F7.2)
      stop
      end
