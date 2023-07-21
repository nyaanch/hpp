ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP3()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_30976 = 1.000000D+00/6.000000D+00*MDL_COMPLEXI*(MDL_GBL
     $ *MDL_CONJG__ZZ12+3.000000D+00*MDL_GR*MDL_CONJG__ZZ32)
      GC_30982 = 1.000000D+00/6.000000D+00*MDL_COMPLEXI*(MDL_GBL
     $ *MDL_CONJG__ZZ13+3.000000D+00*MDL_GR*MDL_CONJG__ZZ33)
      GC_31207 = -(MDL_HGG1*MDL_COMPLEXI)
      GC_31209 = -(MDL_HGG2*MDL_COMPLEXI)
      GC_31211 = -(MDL_HGG3*MDL_COMPLEXI)
      GC_31213 = -(MDL_HGG4*MDL_COMPLEXI)
      GC_31215 = -(MDL_HGG5*MDL_COMPLEXI)
      END
