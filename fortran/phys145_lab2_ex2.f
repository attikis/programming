!     gfortran phys145_lab2_ex2.f -o phys145_lab2_ex2.out
!     ./phys145_lab2_ex2.out

      program volume_conversion

      real*8 liters, convert
      integer gallons, quarts, pints, fl_oz
      character*6 initial_system, answer
      
 1    write(*,*) 'Which system is your volume in? ("USA" or "metric")'
      read (*,*) initial_system

      if (initial_system .ne. "metric") goto 2
      write(*,*) 'How many liters is your volume?'
      read (*,*) liters
      convert = liters/3.7854    ! The volume in gallons (non-integer!!)
      gallons = int(convert)                 ! Ingeger number of gallons
      convert = (convert - int(convert)) *4  ! Leftover volume in quarts
      quarts  = int(convert)
      convert = (convert - int(convert)) *2
      pints   = int(convert)
      convert = (convert - int(convert)) *16 ! Leftover volume in fl.oz.
      fl_oz   = int(convert)                 ! Integer  number of fl.oz.
      write(*,*) 'This volume equals:', gallons, ' gallons,',
     &    quarts, ' quarts,', pints, ' pints,', fl_oz, ' fl.oz.'
      goto 4

 2    if (initial_system .ne. "USA") goto 3
      write(*,*) 'How many gallons/quarts/pints/fl_oz is your volume?'
      read (*,*) gallons, quarts, pints, fl_oz
      liters = 3.7854 * (gallons    + quarts/4.d0 +
     &                   pints/8.d0 + fl_oz/128.d0)
      write(*,*) 'This volume equals:', liters, ' liters'
      goto 4
 3    write(*,*) 'No such system!'
      
 4    write(*,*) 'Do you wish to retry? (answer "yes" if you wish to)'
      read (*,*) answer
      if (answer .eq. 'yes') go to 1

      stop
      end
