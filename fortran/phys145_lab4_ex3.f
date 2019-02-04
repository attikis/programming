!     gfortran phys145_lab4_ex1.f -o phys145_lab4_ex3.out
!     ./phys145_lab4_ex3.out

      program Sorting_Cell_Phones
      implicit none

      character*20 name(100), nameSorted(100), nameTemporary
      real*8 type(3,100), typeSorted(3,100), typeTemporary
      integer i, j, k, n
      real*8 most_common_memory, current_memory
      integer most_common_frequency, current_frequency

      open(unit=8, file='lab4_2019_ask1.input', status='old')
      
      do i = 1, 100             ! Διαβάζουμε έως 100 ονόματα
         read(8,*,end=1) name(i), (type(j,i), j = 1, 3)
      enddo
      write(*,*) 'WARNING: Reached a limit of 100 models !!'
 1    n = i-1

      nameSorted = name
      typeSorted = type

C     ****************** Αρχίζει η αλφαβητική ταξινόμηση *******************
      do i = 1, n-1             ! Θα ταξινομήσουμε το i-οστό μοντέλο
         do j = i+1, n          ! Το συγκρίνουμε με τα επόμενα μοντέλα
            if(nameSorted(i).gt.nameSorted(j)) then
               nameTemporary = nameSorted(j) ! Ανταλλαγή του j-οστού
               nameSorted(j) = nameSorted(i) ! μοντέλου με το i-οστό
               nameSorted(i) = nameTemporary
               do k = 1, 3
                  typeTemporary   = typeSorted(k,j) ! Ανταλλαγή χαρακτηρι-
                  typeSorted(k,j) = typeSorted(k,i) ! στικών του i-οστού
                  typeSorted(k,i) = typeTemporary ! και j-οστού μοντέλου
               enddo
            endif
         enddo
      enddo

      open(unit=3, file='lab4_2019_ask3.output1', status='new')
      write(3,*) 'Name of model          Price',
     & '                     Memory                     Rating'
      do i = 1, n
        write(3,*) nameSorted(i), (typeSorted(k,i), k = 1, 3)
      enddo
      close(3)

C     ************* Αρχίζει η ταξινόμηση ως προς αύξουσα τιμή **************
      do i = 1, n-1             ! Θα ταξινομήσουμε το i-οστό μοντέλο
         do j = i+1, n          ! Το συγκρίνουμε με τα επόμενα μοντέλα
            if(typeSorted(1,i).gt.typeSorted(1,j)) then
               nameTemporary = nameSorted(j) ! Ανταλλαγή του j-οστού
               nameSorted(j) = nameSorted(i) ! μοντέλου με το i-οστό
               nameSorted(i) = nameTemporary
               do k = 1, 3
                  typeTemporary   = typeSorted(k,j) ! Ανταλλαγή χαρακτηρι-
                  typeSorted(k,j) = typeSorted(k,i) ! στικών του i-οστού
                  typeSorted(k,i) = typeTemporary ! και j-οστού μοντέλου
               enddo
            endif
         enddo
      enddo
      open(unit=3, file='lab4_2019_ask3.output2', status='new')
      write(3,*) 'Name of model          Price',
     & '                     Memory                     Rating'
      do i = 1, n
         write(3,*) nameSorted(i), (typeSorted(k,i), k = 1, 3)
      enddo
      close(3)
      
C     Τώρα που οι τιμές είναι ταξινομημένες, η ενδιάμεση τιμή είναι απλώς:
      write(*,*) 'Median price: ', typeSorted(1, (n+1)/2)
      
C     ************* Αρχίζει η ταξινόμηση ως προς φθίνουσα τιμή *************
      do i = 1, n-1             ! Θα ταξινομήσουμε το i-οστό μοντέλο
         do j = i+1, n          ! Το συγκρίνουμε με τα επόμενα μοντέλα
            if(typeSorted(1,i).lt.typeSorted(1,j)) then
               nameTemporary = nameSorted(j) ! Ανταλλαγή του j-οστού
               nameSorted(j) = nameSorted(i) ! μοντέλου με το i-οστό
               nameSorted(i) = nameTemporary
               do k = 1, 3
                  typeTemporary   = typeSorted(k,j) ! Ανταλλαγή χαρακτηρι-
                  typeSorted(k,j) = typeSorted(k,i) ! στικών του i-οστού
                  typeSorted(k,i) = typeTemporary ! και j-οστού μοντέλου
               enddo
            endif
         enddo
      enddo

      open(unit=3, file='lab4_2019_ask3.output3', status='new')
      write(3,*) 'Name of model          Price',
     & '                     Memory                     Rating'
      do i = 1, n
         write(3,*) nameSorted(i), (typeSorted(k,i), k = 1, 3)
      enddo
      close(3)

C     *************** Αρχίζει η ταξινόμηση ως προς τη μνήμη ****************
      do i = 1, n-1             ! Θα ταξινομήσουμε το i-οστό μοντέλο
         do j = i+1, n          ! Το συγκρίνουμε με τα επόμενα μοντέλα
            if(typeSorted(2,i).gt.typeSorted(2,j)) then
               nameTemporary = nameSorted(j) ! Ανταλλαγή του j-οστού
               nameSorted(j) = nameSorted(i) ! μοντέλου με το i-οστό
               nameSorted(i) = nameTemporary
               do k = 1, 3
                  typeTemporary   = typeSorted(k,j) ! Ανταλλαγή χαρακτηρι-
                  typeSorted(k,j) = typeSorted(k,i) ! στικών του i-οστού
                  typeSorted(k,i) = typeTemporary ! και j-οστού μοντέλου
               enddo
            endif
         enddo
      enddo
      open(unit=3, file='lab4_2019_ask3.output4', status='new')
      write(3,*) 'Name of model          Price',
     & '                     Memory                     Rating'
      do i = 1, n
         write(3,*) nameSorted(i), (typeSorted(k,i), k = 1, 3)
      enddo
      close(3)

C     Τώρα που τα μοντέλα είναι ταξινομημένα ως προς τη μνήμη τους,
C     μπορούμε να ελέγξουμε ποια μνήμη εμφανίζεται τις πιο πολλές φορές
      most_common_memory    = -1 ! Αρχικό μέγεθος της πιο συχνής μνήμης
      most_common_frequency =  0 ! Πόσες φορές εμφανίστηκε η μνήμη αυτή;
      current_memory        = -1 ! Ποια μνήμη διερευνούμε τώρα;
      current_frequency     =  0 ! Πόσες φορές εμφανίστηκε η μνήμη αυτή;
      do i = 1, n
         if (typeSorted(2,i).eq.current_memory) then
            current_frequency = current_frequency + 1
         else
            if (current_frequency .gt. most_common_frequency) then
               most_common_frequency = current_frequency
               most_common_memory    = current_memory
            endif
            current_memory    = typeSorted(2,i)
            current_frequency = 1
         endif
      enddo
      if (current_frequency .gt. most_common_frequency) then
         most_common_frequency = current_frequency
         most_common_memory    = current_memory
      endif

      write(*,*) 'Most common memory:    ', most_common_memory
      write(*,*) 'Number of occurences: ' , most_common_frequency
C     *************** Αρχίζει η ταξινόμηση ως προς το βαθμό ****************
      do i = 1, n-1             ! Θα ταξινομήσουμε το i-οστό μοντέλο
         do j = i+1, n          ! Το συγκρίνουμε με τα επόμενα μοντέλα
            if(typeSorted(3,i).gt.typeSorted(3,j)) then
               nameTemporary = nameSorted(j) ! Ανταλλαγή του j-οστού
               nameSorted(j) = nameSorted(i) ! μοντέλου με το i-οστό
               nameSorted(i) = nameTemporary
               do k = 1, 3
                  typeTemporary   = typeSorted(k,j) ! Ανταλλαγή χαρακτηρι-
                  typeSorted(k,j) = typeSorted(k,i) ! στικών του i-οστού
                  typeSorted(k,i) = typeTemporary ! και j-οστού μοντέλου
               enddo
            endif
         enddo
      enddo
      open(unit=3, file='lab4_2019_ask3.output5', status='new')
      write(3,*) 'Name of model          Price',
     & '                     Memory                     Rating'
      do i = 1, n
         write(3,*) nameSorted(i), (typeSorted(k,i), k = 1, 3)
      enddo
      close(3)
      
      stop
      end
      

