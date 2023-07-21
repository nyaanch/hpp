C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(3,2,-1)*ProjM(-1,1)
C     
      SUBROUTINE FFV4P0_3(F1, F2, COUP, M3, W3,V3)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      REAL*8 M3
      REAL*8 P3(0:3)
      COMPLEX*16 V3(6)
      REAL*8 W3
      COMPLEX*16 DENOM
      V3(1) = +F1(1)+F2(1)
      V3(2) = +F1(2)+F2(2)
      P3(0) = -DBLE(V3(1))
      P3(1) = -DBLE(V3(2))
      P3(2) = -DIMAG(V3(2))
      P3(3) = -DIMAG(V3(1))
      DENOM = COUP/(P3(0)**2-P3(1)**2-P3(2)**2-P3(3)**2 - M3 * (M3 -CI
     $ * W3))
      V3(3)= DENOM*(-CI)*(F2(5)*F1(3)+F2(6)*F1(4))
      V3(4)= DENOM*(-CI)*(-F2(6)*F1(3)-F2(5)*F1(4))
      V3(5)= DENOM*(-CI)*(-CI*(F2(6)*F1(3))+CI*(F2(5)*F1(4)))
      V3(6)= DENOM*(-CI)*(-F2(5)*F1(3)+F2(6)*F1(4))
      END


