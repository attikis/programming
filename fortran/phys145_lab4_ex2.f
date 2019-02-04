!     gfortran phys145_lab4_ex2.f -o phys145_lab4_ex2.out
!     ./phys145_lab4_ex2.out

      program Check_Of_Transpose_Property
      integer A (20,20), B (20,20), AB (20,20)
      integer AT(20,20), BT(20,20), ABT(20,20), BTAT(20,20)
      integer mA, nA, mB, nB    ! Διαστάσεις των δύο πινάκων
      integer i, j, k           ! Βοηθητικοί δείκτες

      open(unit=8, file='lab4_2019_ask2.input', status='old')
      read(8,*) mA, nA               ! Διαβάζουμε τις διαστάσεις του Α
      do i = 1, mA
         read(8,*) (A(i,j), j=1,nA)  ! Διαβάζουμε μια-μια τις σειρές
      enddo
      read(8,*) mB, nB               ! Διαβάζουμε τις διαστάσεις του B
      do i = 1, mB
         read(8,*) (B(i,j), j=1,nB)  ! Διαβάζουμε μια-μια τις σειρές
      enddo

      if (nA.ne.mB) write(*,*) 'Incompatible dimensions!'
      do i = 1,mA
         do j = 1,nB
            AB(i,j) = 0.d0
            do k = 1,nA
               AB(i,j) = AB(i,j) + A(i,k)*B(k,j)
            enddo
         enddo
      enddo
       
      do i = 1,mA
         do j = 1,nB
            ABT(j,i) = AB(i,j)
         enddo
      enddo

      do i = 1,mA
         do j = 1,nA
            AT(j,i) = A(i,j)
         enddo
      enddo
      
      do i = 1,mB
         do j = 1,nB
            BT(j,i) = B(i,j)
         enddo
      enddo

      do i = 1,nB
         do j = 1,mA
            BTAT(i,j) = 0.d0
            do k = 1,nA
               BTAT(i,j) = BTAT(i,j) + BT(i,k)*AT(k,j)
            enddo
         enddo
      enddo

      write(*,*) '(A*B)^T ='
      do i = 1,nB
         write(*,*) (ABT(i,j), j=1,mA)
      enddo
      write(*,*)
      
      write(*,*) 'B^T * A^T ='
      do i = 1,nB
         write(*,*) (BTAT(i,j), j=1,mA)
      enddo
      stop
      end
