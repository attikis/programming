!     gfortran phys145_lab2_ex1.f -o phys145_lab2_ex1.out
!     ./phys145_lab2_ex1.out
      program triangle_area_and_angles

      real*8 A, B, C, area, angleA, angleB, angleC, t, R, rho
      real*8 pi, RadiansToDegrees
      

 1    write(*,*) 'What are the lengths of the sides of the triangle?'
      read(*,*) A, B, C
      if (A.lt.B+C .and. A.gt.abs(B-C)) goto 2 
      write(*,*) 'These lengths cannot make a triangle. Try again!'
      goto 1

 2    t      = (A+B+C)/2
      area   = sqrt(t*(t-A)*(t-B)*(t-C))
      angleA = asin(2 * area / (B * C))
      angleB = asin(2 * area / (C * A))
      angleC = asin(2 * area / (A * B))
      pi = acos(-1.d0)

      if (A**2 .gt. B**2+C**2) angleA = pi - angleA
      if (B**2 .gt. C**2+A**2) angleB = pi - angleB
      if (C**2 .gt. A**2+B**2) angleC = pi - angleC
      
      RadiansToDegrees = 360 / (2 * pi)
      angleA = angleA * RadiansToDegrees
      angleB = angleB * RadiansToDegrees
      angleC = angleC * RadiansToDegrees

      R =A*B*C/(4*area)
      rho =area/t
      
      write(*,*) 'area = ', area
      write(*,*) 'The angles opposite the three sides are: '
      write(*,*) angleA, angleB, angleC
      write(*,*) 'Radii of circumscribed and inscribed circles:', R, rho
      stop
      end
