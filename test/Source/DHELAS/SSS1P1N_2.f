C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     1
C     
      SUBROUTINE SSS1P1N_2(S1, S3, COUP,S2)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 S1(*)
      COMPLEX*16 S2(3)
      COMPLEX*16 S3(*)
      S2(3)= COUP*(-CI )* S3(3)*S1(3)
      END


