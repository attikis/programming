!     gfortran phys145_lab5_ex3.f -o phys145_lab5_ex3.out
!     ./phys145_lab5_ex3.out

      subroutine matrixmultiply(A,B,C,mB,nB,mC,nC,nmax) ! A = B*C
      integer mB, nB, mC, nC, nmax, i, j, k
      real*8 A(nmax,nmax), B(nmax,nmax), C(nmax,nmax)

      do i = 1, mB
         do j = 1, nC
            A(i,j) = 0.d0
            do k = 1, nB
               A(i,j) = A(i,j) + B(i,k) * C(k,j)
            enddo
         enddo
      enddo
      return
      end

      subroutine matrixtranspose(Atr,A,mA,nA,nmax) ! Atr = transpose(A) integer mA, nA, nmax, i, j
      integer mA, nA, nmax, i, j
      real*8 Atr(nmax,nmax), A(nmax,nmax)

      do i = 1, mA
         do j = 1, nA
            Atr(j,i) = A(i,j)
         enddo
      enddo
      return
      end

      program Check_Of_Transpose_Property
      real*8 A (20,20), B (20,20), AB (20,20)
      real*8 AT(20,20), BT(20,20), ABT(20,20), BTAT(20,20)
      integer i, j, mA, nA, mB, nB

      open(unit=8, file='lab4_2019_ask2.input', status='old')

      read(8,*) mA, nA
      do i = 1, mA
         read(8,*) (A(i,j), j=1,nA)
      enddo
      
      read(8,*) mB, nB
      do i = 1, mB
         read(8,*) (B(i,j), j=1,nB) ! Διαβάζουμε μια-μια τις σειρές
      enddo

      if (nA.ne.mB) write(*,*) 'Incompatible dimensions!'

      call matrixmultiply (AB, A, B, mA,nA,mB,nB,20) ! Όλες οι πράξεις τώρα
      call matrixtranspose(ABT, AB, mA, nB,      20)
      call matrixtranspose(AT,  A,  mA, nA,      20)
      call matrixtranspose(BT,  B,  mB, nB,      20)
      call matrixmultiply (BTAT,BT,AT,nB,mB,nA,mA,20)

      write(*,*) '(A*B)^T ='
      do i = 1,nB
         write(*,1) (ABT(i,j), j=1,mA)
      enddo
      write(*,*)
      write(*,*) 'B^T * A^T ='
      do i = 1,nB
         write(*,1) (BTAT(i,j), j=1,mA) ! Αφήνουμε μια κενή σειρά
      enddo
 1    format(20(2X,F7.2))
      stop
      end
