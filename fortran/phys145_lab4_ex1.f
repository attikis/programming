!     gfortran phys145_lab4_ex1.f -o phys145_lab4_ex1.out
!     ./phys145_lab4_ex1.out

      program Cell_Phones
      implicit none
      character*20  name,  nameExpensive,   nameCheap,    namePreferred
      real*8       price,  priceExpensive,  priceCheap,   pricePreferred
      integer     memory, memoryExpensive, memoryCheap,  memoryPreferred
      real*8        grade,  gradeExpensive,  gradeCheap,  gradePreferred
      integer       i,  iExpensive,  iCheap,  iPreferred
      real*8 priceAverage, priceDeviation, gradeAverage, gradeDeviation

      open(unit=8, file='lab4_2019_ask1.input', status='old')
      priceExpensive = 0     ! Αρχικά του δίνουμε πολύ μικρή  τιμή
      priceCheap     = 10000 
      gradePreferred = 0
      priceAverage   = 0.d0
      gradeAverage   = 0.d0
      priceDeviation = 0.d0
      gradeDeviation = 0.d0

      i = 0
 1    read(8,*,end=2) name, price, memory, grade
      i = i+1
      priceAverage   = priceAverage + price
      gradeAverage   = gradeAverage + grade
      priceDeviation = priceDeviation + price**2
      gradeDeviation = gradeDeviation + grade**2

      if (price.gt.priceExpensive) then
         nameExpensive = name
         priceExpensive = price
         memoryExpensive = memory
         gradeExpensive = grade
         iExpensive = i
      endif

      if (price.lt.priceCheap) then
         nameCheap   = name
         priceCheap  = price
         memoryCheap = memory
         gradeCheap  = grade
         iCheap      = i
      endif
      
      if (grade.gt.gradePreferred) then
         namePreferred   = name
         pricePreferred  = price
         memoryPreferred = memory
         gradePreferred  = grade
         iPreferred      = i
      endif

      goto 1

 2    write(*,*) 'The file contained ', i, ' models.'
      write(*,*)             ! Άφησε μια κενή σειρά
      write(*,*) 'Most expensive model (# ', iExpensive, ' on file):'
      write(*,*) 'Name: ',     nameExpensive, 'Price: ', priceExpensive
      write(*,*) 'Memory: ', memoryExpensive, 'Grade: ', gradeExpensive
      write(*,*)
      write(*,*) 'Cheapest model       (# ', iCheap, ' on file):'
      write(*,*) 'Name: ',     nameCheap, 'Price: ', priceCheap
      write(*,*) 'Memory: ', memoryCheap, 'Grade: ', gradeCheap
      write(*,*)
      write(*,*) 'Most preferred model (# ', iPreferred, ' on file):'
      write(*,*) 'Name: ',     namePreferred, 'Price: ', pricePreferred
      write(*,*) 'Memory: ', memoryPreferred, 'Grade: ', gradePreferred
      write(*,*)

      priceAverage   = priceAverage/i
      gradeAverage   = gradeAverage/i
      priceDeviation = sqrt(priceDeviation/i - priceAverage**2)
      gradeDeviation = sqrt(gradeDeviation/i - gradeAverage**2)
      write(*,*) 'Average price/deviation:  ',
     &           priceAverage, priceDeviation
      write(*,*) 'Average grade/deviation:  ',
     &           gradeAverage, gradeDeviation

      stop
      end
