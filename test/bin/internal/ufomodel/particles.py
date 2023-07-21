# ----------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.13.0 
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840    
# (c) Florian Staub, 2011  
# ----------------------------------------------------------------------  
# File created at 11:31 on 20.6.2018   
# ----------------------------------------------------------------------  
 
 
from __future__ import division 
from object_library import all_particles,Particle 
import parameters as Param 


glu = Particle(pdg_code =1000021, 
	 name = 'glu' ,
	 antiname = 'glu' ,
	 spin = 2 ,
	 color = 8 ,
	 mass = Param.Mglu ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'scurly' ,
	 charge = 0 ,
	 texname = 'glu' ,
	 antitexname = 'glu' ) 
 
C01 = Particle(pdg_code =1000022, 
	 name = 'C01' ,
	 antiname = 'C01' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC01 ,
	 width = Param.WC01 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C01' ,
	 antitexname = 'C01' ) 
 
C02 = Particle(pdg_code =1000023, 
	 name = 'C02' ,
	 antiname = 'C02' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC02 ,
	 width = Param.WC02 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C02' ,
	 antitexname = 'C02' ) 
 
C03 = Particle(pdg_code =1000025, 
	 name = 'C03' ,
	 antiname = 'C03' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC03 ,
	 width = Param.WC03 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C03' ,
	 antitexname = 'C03' ) 
 
C04 = Particle(pdg_code =1000035, 
	 name = 'C04' ,
	 antiname = 'C04' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC04 ,
	 width = Param.WC04 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C04' ,
	 antitexname = 'C04' ) 
 
C05 = Particle(pdg_code =6000022, 
	 name = 'C05' ,
	 antiname = 'C05' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC05 ,
	 width = Param.WC05 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C05' ,
	 antitexname = 'C05' ) 
 
C06 = Particle(pdg_code =6000023, 
	 name = 'C06' ,
	 antiname = 'C06' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC06 ,
	 width = Param.WC06 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C06' ,
	 antitexname = 'C06' ) 
 
C07 = Particle(pdg_code =6000025, 
	 name = 'C07' ,
	 antiname = 'C07' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC07 ,
	 width = Param.WC07 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C07' ,
	 antitexname = 'C07' ) 
 
C08 = Particle(pdg_code =6000055, 
	 name = 'C08' ,
	 antiname = 'C08' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC08 ,
	 width = Param.WC08 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C08' ,
	 antitexname = 'C08' ) 
 
C09 = Particle(pdg_code =7000022, 
	 name = 'C09' ,
	 antiname = 'C09' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC09 ,
	 width = Param.WC09 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C09' ,
	 antitexname = 'C09' ) 
 
C010 = Particle(pdg_code =7000023, 
	 name = 'C010' ,
	 antiname = 'C010' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC010 ,
	 width = Param.WC010 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C010' ,
	 antitexname = 'C010' ) 
 
C011 = Particle(pdg_code =7000025, 
	 name = 'C011' ,
	 antiname = 'C011' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC011 ,
	 width = Param.WC011 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C011' ,
	 antitexname = 'C011' ) 
 
C012 = Particle(pdg_code =7000035, 
	 name = 'C012' ,
	 antiname = 'C012' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MC012 ,
	 width = Param.WC012 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 0 ,
	 texname = 'C012' ,
	 antitexname = 'C012' ) 
 
CA1bar = Particle(pdg_code =1000024, 
	 name = 'CA1bar' ,
	 antiname = 'CA1' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MCA1 ,
	 width = Param.WCA1 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 1 ,
	 texname = 'CA1bar' ,
	 antitexname = 'CA1' ) 
 
CA1 = CA1bar.anti() 
 
 
CA2bar = Particle(pdg_code =1000037, 
	 name = 'CA2bar' ,
	 antiname = 'CA2' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MCA2 ,
	 width = Param.WCA2 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 1 ,
	 texname = 'CA2bar' ,
	 antitexname = 'CA2' ) 
 
CA2 = CA2bar.anti() 
 
 
CA3bar = Particle(pdg_code =6000024, 
	 name = 'CA3bar' ,
	 antiname = 'CA3' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MCA3 ,
	 width = Param.WCA3 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 1 ,
	 texname = 'CA3bar' ,
	 antitexname = 'CA3' ) 
 
CA3 = CA3bar.anti() 
 
 
CA4bar = Particle(pdg_code =6000037, 
	 name = 'CA4bar' ,
	 antiname = 'CA4' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MCA4 ,
	 width = Param.WCA4 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 1 ,
	 texname = 'CA4bar' ,
	 antitexname = 'CA4' ) 
 
CA4 = CA4bar.anti() 
 
 
CA5bar = Particle(pdg_code =7000024, 
	 name = 'CA5bar' ,
	 antiname = 'CA5' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MCA5 ,
	 width = Param.WCA5 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 1 ,
	 texname = 'CA5bar' ,
	 antitexname = 'CA5' ) 
 
CA5 = CA5bar.anti() 
 
 
CA6bar = Particle(pdg_code =7000037, 
	 name = 'CA6bar' ,
	 antiname = 'CA6' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MCA6 ,
	 width = Param.WCA6 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 1 ,
	 texname = 'CA6bar' ,
	 antitexname = 'CA6' ) 
 
CA6 = CA6bar.anti() 
 
 
Cmm1bar = Particle(pdg_code =6000044, 
	 name = 'Cmm1bar' ,
	 antiname = 'Cmm1' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MCmm1 ,
	 width = Param.WCmm1 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 2 ,
	 texname = 'Cmm1bar' ,
	 antitexname = 'Cmm1' ) 
 
Cmm1 = Cmm1bar.anti() 
 
 
Cmm2bar = Particle(pdg_code =6000057, 
	 name = 'Cmm2bar' ,
	 antiname = 'Cmm2' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.MCmm2 ,
	 width = Param.WCmm2 ,
	 GhostNumber = 0, 
	 line = 'swavy' ,
	 charge = 2 ,
	 texname = 'Cmm2bar' ,
	 antitexname = 'Cmm2' ) 
 
Cmm2 = Cmm2bar.anti() 
 
 
nu1 = Particle(pdg_code =12, 
	 name = 'nu1' ,
	 antiname = 'nu1' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = 0 ,
	 texname = 'nu1' ,
	 antitexname = 'nu1' ) 
 
nu2 = Particle(pdg_code =14, 
	 name = 'nu2' ,
	 antiname = 'nu2' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = 0 ,
	 texname = 'nu2' ,
	 antitexname = 'nu2' ) 
 
nu3 = Particle(pdg_code =16, 
	 name = 'nu3' ,
	 antiname = 'nu3' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = 0 ,
	 texname = 'nu3' ,
	 antitexname = 'nu3' ) 
 
nu4 = Particle(pdg_code =6000012, 
	 name = 'nu4' ,
	 antiname = 'nu4' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.Mnu4 ,
	 width = Param.Wnu4 ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = 0 ,
	 texname = 'nu4' ,
	 antitexname = 'nu4' ) 
 
nu5 = Particle(pdg_code =6000014, 
	 name = 'nu5' ,
	 antiname = 'nu5' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.Mnu5 ,
	 width = Param.Wnu5 ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = 0 ,
	 texname = 'nu5' ,
	 antitexname = 'nu5' ) 
 
nu6 = Particle(pdg_code =6000016, 
	 name = 'nu6' ,
	 antiname = 'nu6' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.Mnu6 ,
	 width = Param.Wnu6 ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = 0 ,
	 texname = 'nu6' ,
	 antitexname = 'nu6' ) 
 
e1 = Particle(pdg_code =11, 
	 name = 'e1' ,
	 antiname = 'e1bar' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.Me1 ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = -1 ,
	 texname = 'e1' ,
	 antitexname = 'e1bar' ) 
 
e1bar = e1.anti() 
 
 
e2 = Particle(pdg_code =13, 
	 name = 'e2' ,
	 antiname = 'e2bar' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.Me2 ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = -1 ,
	 texname = 'e2' ,
	 antitexname = 'e2bar' ) 
 
e2bar = e2.anti() 
 
 
e3 = Particle(pdg_code =15, 
	 name = 'e3' ,
	 antiname = 'e3bar' ,
	 spin = 2 ,
	 color = 1 ,
	 mass = Param.Me3 ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = -1 ,
	 texname = 'e3' ,
	 antitexname = 'e3bar' ) 
 
e3bar = e3.anti() 
 
 
d1 = Particle(pdg_code =1, 
	 name = 'd1' ,
	 antiname = 'd1bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Md1 ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = -1/3 ,
	 texname = 'd1' ,
	 antitexname = 'd1bar' ) 
 
d1bar = d1.anti() 
 
 
d2 = Particle(pdg_code =3, 
	 name = 'd2' ,
	 antiname = 'd2bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Md2 ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = -1/3 ,
	 texname = 'd2' ,
	 antitexname = 'd2bar' ) 
 
d2bar = d2.anti() 
 
 
d3 = Particle(pdg_code =5, 
	 name = 'd3' ,
	 antiname = 'd3bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Md3 ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = -1/3 ,
	 texname = 'd3' ,
	 antitexname = 'd3bar' ) 
 
d3bar = d3.anti() 
 
 
u1 = Particle(pdg_code =2, 
	 name = 'u1' ,
	 antiname = 'u1bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Mu1 ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = 2/3 ,
	 texname = 'u1' ,
	 antitexname = 'u1bar' ) 
 
u1bar = u1.anti() 
 
 
u2 = Particle(pdg_code =4, 
	 name = 'u2' ,
	 antiname = 'u2bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Mu2 ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = 2/3 ,
	 texname = 'u2' ,
	 antitexname = 'u2bar' ) 
 
u2bar = u2.anti() 
 
 
u3 = Particle(pdg_code =6, 
	 name = 'u3' ,
	 antiname = 'u3bar' ,
	 spin = 2 ,
	 color = 3 ,
	 mass = Param.Mu3 ,
	 width = Param.Wu3 ,
	 GhostNumber = 0, 
	 line = 'straight' ,
	 charge = 2/3 ,
	 texname = 'u3' ,
	 antitexname = 'u3bar' ) 
 
u3bar = u3.anti() 
 
 
sd1 = Particle(pdg_code =1000001, 
	 name = 'sd1' ,
	 antiname = 'sd1c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msd1 ,
	 width = Param.Wsd1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1/3 ,
	 texname = 'sd1' ,
	 antitexname = 'sd1c' ) 
 
sd1c = sd1.anti() 
 
 
sd2 = Particle(pdg_code =1000003, 
	 name = 'sd2' ,
	 antiname = 'sd2c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msd2 ,
	 width = Param.Wsd2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1/3 ,
	 texname = 'sd2' ,
	 antitexname = 'sd2c' ) 
 
sd2c = sd2.anti() 
 
 
sd3 = Particle(pdg_code =1000005, 
	 name = 'sd3' ,
	 antiname = 'sd3c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msd3 ,
	 width = Param.Wsd3 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1/3 ,
	 texname = 'sd3' ,
	 antitexname = 'sd3c' ) 
 
sd3c = sd3.anti() 
 
 
sd4 = Particle(pdg_code =2000001, 
	 name = 'sd4' ,
	 antiname = 'sd4c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msd4 ,
	 width = Param.Wsd4 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1/3 ,
	 texname = 'sd4' ,
	 antitexname = 'sd4c' ) 
 
sd4c = sd4.anti() 
 
 
sd5 = Particle(pdg_code =2000003, 
	 name = 'sd5' ,
	 antiname = 'sd5c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msd5 ,
	 width = Param.Wsd5 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1/3 ,
	 texname = 'sd5' ,
	 antitexname = 'sd5c' ) 
 
sd5c = sd5.anti() 
 
 
sd6 = Particle(pdg_code =2000005, 
	 name = 'sd6' ,
	 antiname = 'sd6c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msd6 ,
	 width = Param.Wsd6 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1/3 ,
	 texname = 'sd6' ,
	 antitexname = 'sd6c' ) 
 
sd6c = sd6.anti() 
 
 
su1 = Particle(pdg_code =1000002, 
	 name = 'su1' ,
	 antiname = 'su1c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msu1 ,
	 width = Param.Wsu1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 2/3 ,
	 texname = 'su1' ,
	 antitexname = 'su1c' ) 
 
su1c = su1.anti() 
 
 
su2 = Particle(pdg_code =1000004, 
	 name = 'su2' ,
	 antiname = 'su2c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msu2 ,
	 width = Param.Wsu2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 2/3 ,
	 texname = 'su2' ,
	 antitexname = 'su2c' ) 
 
su2c = su2.anti() 
 
 
su3 = Particle(pdg_code =1000006, 
	 name = 'su3' ,
	 antiname = 'su3c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msu3 ,
	 width = Param.Wsu3 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 2/3 ,
	 texname = 'su3' ,
	 antitexname = 'su3c' ) 
 
su3c = su3.anti() 
 
 
su4 = Particle(pdg_code =2000002, 
	 name = 'su4' ,
	 antiname = 'su4c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msu4 ,
	 width = Param.Wsu4 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 2/3 ,
	 texname = 'su4' ,
	 antitexname = 'su4c' ) 
 
su4c = su4.anti() 
 
 
su5 = Particle(pdg_code =2000004, 
	 name = 'su5' ,
	 antiname = 'su5c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msu5 ,
	 width = Param.Wsu5 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 2/3 ,
	 texname = 'su5' ,
	 antitexname = 'su5c' ) 
 
su5c = su5.anti() 
 
 
su6 = Particle(pdg_code =2000006, 
	 name = 'su6' ,
	 antiname = 'su6c' ,
	 spin = 1 ,
	 color = 3 ,
	 mass = Param.Msu6 ,
	 width = Param.Wsu6 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 2/3 ,
	 texname = 'su6' ,
	 antitexname = 'su6c' ) 
 
su6c = su6.anti() 
 
 
se1 = Particle(pdg_code =1000011, 
	 name = 'se1' ,
	 antiname = 'se1c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mse1 ,
	 width = Param.Wse1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'se1' ,
	 antitexname = 'se1c' ) 
 
se1c = se1.anti() 
 
 
se2 = Particle(pdg_code =1000013, 
	 name = 'se2' ,
	 antiname = 'se2c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mse2 ,
	 width = Param.Wse2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'se2' ,
	 antitexname = 'se2c' ) 
 
se2c = se2.anti() 
 
 
se3 = Particle(pdg_code =1000015, 
	 name = 'se3' ,
	 antiname = 'se3c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mse3 ,
	 width = Param.Wse3 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'se3' ,
	 antitexname = 'se3c' ) 
 
se3c = se3.anti() 
 
 
se4 = Particle(pdg_code =2000011, 
	 name = 'se4' ,
	 antiname = 'se4c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mse4 ,
	 width = Param.Wse4 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'se4' ,
	 antitexname = 'se4c' ) 
 
se4c = se4.anti() 
 
 
se5 = Particle(pdg_code =2000013, 
	 name = 'se5' ,
	 antiname = 'se5c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mse5 ,
	 width = Param.Wse5 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'se5' ,
	 antitexname = 'se5c' ) 
 
se5c = se5.anti() 
 
 
se6 = Particle(pdg_code =2000015, 
	 name = 'se6' ,
	 antiname = 'se6c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mse6 ,
	 width = Param.Wse6 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'se6' ,
	 antitexname = 'se6c' ) 
 
se6c = se6.anti() 
 
 
SvRe1 = Particle(pdg_code =1000012, 
	 name = 'SvRe1' ,
	 antiname = 'SvRe1' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvRe1 ,
	 width = Param.WSvRe1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvRe1' ,
	 antitexname = 'SvRe1' ) 
 
SvRe2 = Particle(pdg_code =1000014, 
	 name = 'SvRe2' ,
	 antiname = 'SvRe2' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvRe2 ,
	 width = Param.WSvRe2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvRe2' ,
	 antitexname = 'SvRe2' ) 
 
SvRe3 = Particle(pdg_code =1000016, 
	 name = 'SvRe3' ,
	 antiname = 'SvRe3' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvRe3 ,
	 width = Param.WSvRe3 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvRe3' ,
	 antitexname = 'SvRe3' ) 
 
SvRe4 = Particle(pdg_code =2000012, 
	 name = 'SvRe4' ,
	 antiname = 'SvRe4' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvRe4 ,
	 width = Param.WSvRe4 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvRe4' ,
	 antitexname = 'SvRe4' ) 
 
SvRe5 = Particle(pdg_code =2000014, 
	 name = 'SvRe5' ,
	 antiname = 'SvRe5' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvRe5 ,
	 width = Param.WSvRe5 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvRe5' ,
	 antitexname = 'SvRe5' ) 
 
SvRe6 = Particle(pdg_code =2000016, 
	 name = 'SvRe6' ,
	 antiname = 'SvRe6' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvRe6 ,
	 width = Param.WSvRe6 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvRe6' ,
	 antitexname = 'SvRe6' ) 
 
SvIe1 = Particle(pdg_code =5000012, 
	 name = 'SvIe1' ,
	 antiname = 'SvIe1' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvIe1 ,
	 width = Param.WSvIe1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvIe1' ,
	 antitexname = 'SvIe1' ) 
 
SvIe2 = Particle(pdg_code =5000014, 
	 name = 'SvIe2' ,
	 antiname = 'SvIe2' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvIe2 ,
	 width = Param.WSvIe2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvIe2' ,
	 antitexname = 'SvIe2' ) 
 
SvIe3 = Particle(pdg_code =5000016, 
	 name = 'SvIe3' ,
	 antiname = 'SvIe3' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvIe3 ,
	 width = Param.WSvIe3 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvIe3' ,
	 antitexname = 'SvIe3' ) 
 
SvIe4 = Particle(pdg_code =7000012, 
	 name = 'SvIe4' ,
	 antiname = 'SvIe4' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvIe4 ,
	 width = Param.WSvIe4 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvIe4' ,
	 antitexname = 'SvIe4' ) 
 
SvIe5 = Particle(pdg_code =7000014, 
	 name = 'SvIe5' ,
	 antiname = 'SvIe5' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvIe5 ,
	 width = Param.WSvIe5 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvIe5' ,
	 antitexname = 'SvIe5' ) 
 
SvIe6 = Particle(pdg_code =7000016, 
	 name = 'SvIe6' ,
	 antiname = 'SvIe6' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MSvIe6 ,
	 width = Param.WSvIe6 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'SvIe6' ,
	 antitexname = 'SvIe6' ) 
 
hhPr1 = Particle(pdg_code =9000045, 
	 name = 'hhPr1' ,
	 antiname = 'hhPr1' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MhhPr1 ,
	 width = Param.WhhPr1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'hhPr1' ,
	 antitexname = 'hhPr1' ) 
 
hhPr2 = Particle(pdg_code =9100025, 
	 name = 'hhPr2' ,
	 antiname = 'hhPr2' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MhhPr2 ,
	 width = Param.WhhPr2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'hhPr2' ,
	 antitexname = 'hhPr2' ) 
 
hhLe1 = Particle(pdg_code =9100035, 
	 name = 'hhLe1' ,
	 antiname = 'hhLe1' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MhhLe1 ,
	 width = Param.WhhLe1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'hhLe1' ,
	 antitexname = 'hhLe1' ) 
 
hhLe2 = Particle(pdg_code =9100045, 
	 name = 'hhLe2' ,
	 antiname = 'hhLe2' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MhhLe2 ,
	 width = Param.WhhLe2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'hhLe2' ,
	 antitexname = 'hhLe2' ) 
 
hh1 = Particle(pdg_code =25, 
	 name = 'hh1' ,
	 antiname = 'hh1' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mhh1 ,
	 width = Param.Whh1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'hh1' ,
	 antitexname = 'hh1' ) 
 
hh2 = Particle(pdg_code =35, 
	 name = 'hh2' ,
	 antiname = 'hh2' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mhh2 ,
	 width = Param.Whh2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'hh2' ,
	 antitexname = 'hh2' ) 
 
hh3 = Particle(pdg_code =45, 
	 name = 'hh3' ,
	 antiname = 'hh3' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mhh3 ,
	 width = Param.Whh3 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'hh3' ,
	 antitexname = 'hh3' ) 
 
hh4 = Particle(pdg_code =9000025, 
	 name = 'hh4' ,
	 antiname = 'hh4' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mhh4 ,
	 width = Param.Whh4 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'hh4' ,
	 antitexname = 'hh4' ) 
 
hh5 = Particle(pdg_code =9000035, 
	 name = 'hh5' ,
	 antiname = 'hh5' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.Mhh5 ,
	 width = Param.Whh5 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'hh5' ,
	 antitexname = 'hh5' ) 
 
AhLe1 = Particle(pdg_code =7100035, 
	 name = 'AhLe1' ,
	 antiname = 'AhLe1' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MAhLe1 ,
	 width = Param.WAhLe1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'AhLe1' ,
	 antitexname = 'AhLe1' ) 
 
AhLe2 = Particle(pdg_code =7100045, 
	 name = 'AhLe2' ,
	 antiname = 'AhLe2' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MAhLe2 ,
	 width = Param.WAhLe2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'AhLe2' ,
	 antitexname = 'AhLe2' ) 
 
AhPr1 = Particle(pdg_code =7000045, 
	 name = 'AhPr1' ,
	 antiname = 'AhPr1' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MAhPr1 ,
	 width = Param.WAhPr1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'AhPr1' ,
	 antitexname = 'AhPr1' ) 
 
AhPr2 = Particle(pdg_code =7100025, 
	 name = 'AhPr2' ,
	 antiname = 'AhPr2' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MAhPr2 ,
	 width = Param.WAhPr2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'AhPr2' ,
	 antitexname = 'AhPr2' ) 
 
Ah1 = Particle(pdg_code =999900, 
	 name = 'Ah1' ,
	 antiname = 'Ah1' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 GoldstoneBoson = True ,
	 texname = 'Ah1' ,
	 antitexname = 'Ah1' ) 
 
Ah2 = Particle(pdg_code =999901, 
	 name = 'Ah2' ,
	 antiname = 'Ah2' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 GoldstoneBoson = True ,
	 texname = 'Ah2' ,
	 antitexname = 'Ah2' ) 
 
Ah3 = Particle(pdg_code =36, 
	 name = 'Ah3' ,
	 antiname = 'Ah3' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MAh3 ,
	 width = Param.WAh3 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'Ah3' ,
	 antitexname = 'Ah3' ) 
 
Ah4 = Particle(pdg_code =46, 
	 name = 'Ah4' ,
	 antiname = 'Ah4' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MAh4 ,
	 width = Param.WAh4 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'Ah4' ,
	 antitexname = 'Ah4' ) 
 
Ah5 = Particle(pdg_code =9000036, 
	 name = 'Ah5' ,
	 antiname = 'Ah5' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MAh5 ,
	 width = Param.WAh5 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = 0 ,
	 texname = 'Ah5' ,
	 antitexname = 'Ah5' ) 
 
Hpm1 = Particle(pdg_code =999902, 
	 name = 'Hpm1' ,
	 antiname = 'Hpm1c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 GoldstoneBoson = True ,
	 texname = 'Hpm1' ,
	 antitexname = 'Hpm1c' ) 
 
Hpm1c = Hpm1.anti() 
 
 
Hpm2 = Particle(pdg_code =999903, 
	 name = 'Hpm2' ,
	 antiname = 'Hpm2c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 GoldstoneBoson = True ,
	 texname = 'Hpm2' ,
	 antitexname = 'Hpm2c' ) 
 
Hpm2c = Hpm2.anti() 
 
 
Hpm3 = Particle(pdg_code =-37, 
	 name = 'Hpm3' ,
	 antiname = 'Hpm3c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MHpm3 ,
	 width = Param.WHpm3 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'Hpm3' ,
	 antitexname = 'Hpm3c' ) 
 
Hpm3c = Hpm3.anti() 
 
 
Hpm4 = Particle(pdg_code =-9000037, 
	 name = 'Hpm4' ,
	 antiname = 'Hpm4c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MHpm4 ,
	 width = Param.WHpm4 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'Hpm4' ,
	 antitexname = 'Hpm4c' ) 
 
Hpm4c = Hpm4.anti() 
 
 
Hpm5 = Particle(pdg_code =-9100037, 
	 name = 'Hpm5' ,
	 antiname = 'Hpm5c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MHpm5 ,
	 width = Param.WHpm5 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'Hpm5' ,
	 antitexname = 'Hpm5c' ) 
 
Hpm5c = Hpm5.anti() 
 
 
Hpm6 = Particle(pdg_code =-9200037, 
	 name = 'Hpm6' ,
	 antiname = 'Hpm6c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MHpm6 ,
	 width = Param.WHpm6 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'Hpm6' ,
	 antitexname = 'Hpm6c' ) 
 
Hpm6c = Hpm6.anti() 
 
 
HpmLe1 = Particle(pdg_code =-9300037, 
	 name = 'HpmLe1' ,
	 antiname = 'HpmLe1c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MHpmLe1 ,
	 width = Param.WHpmLe1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'HpmLe1' ,
	 antitexname = 'HpmLe1c' ) 
 
HpmLe1c = HpmLe1.anti() 
 
 
HpmLe2 = Particle(pdg_code =-9400037, 
	 name = 'HpmLe2' ,
	 antiname = 'HpmLe2c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MHpmLe2 ,
	 width = Param.WHpmLe2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -1 ,
	 texname = 'HpmLe2' ,
	 antitexname = 'HpmLe2c' ) 
 
HpmLe2c = HpmLe2.anti() 
 
 
Hmm1 = Particle(pdg_code =-9000055, 
	 name = 'Hmm1' ,
	 antiname = 'Hmm1c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MHmm1 ,
	 width = Param.WHmm1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -2 ,
	 texname = 'Hmm1' ,
	 antitexname = 'Hmm1c' ) 
 
Hmm1c = Hmm1.anti() 
 
 
Hmm2 = Particle(pdg_code =-9000056, 
	 name = 'Hmm2' ,
	 antiname = 'Hmm2c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MHmm2 ,
	 width = Param.WHmm2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -2 ,
	 texname = 'Hmm2' ,
	 antitexname = 'Hmm2c' ) 
 
Hmm2c = Hmm2.anti() 
 
 
HmmLe1 = Particle(pdg_code =-9000057, 
	 name = 'HmmLe1' ,
	 antiname = 'HmmLe1c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MHmmLe1 ,
	 width = Param.WHmmLe1 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -2 ,
	 texname = 'HmmLe1' ,
	 antitexname = 'HmmLe1c' ) 
 
HmmLe1c = HmmLe1.anti() 
 
 
HmmLe2 = Particle(pdg_code =-9000058, 
	 name = 'HmmLe2' ,
	 antiname = 'HmmLe2c' ,
	 spin = 1 ,
	 color = 1 ,
	 mass = Param.MHmmLe2 ,
	 width = Param.WHmmLe2 ,
	 GhostNumber = 0, 
	 line = 'dashed' ,
	 charge = -2 ,
	 texname = 'HmmLe2' ,
	 antitexname = 'HmmLe2c' ) 
 
HmmLe2c = HmmLe2.anti() 
 
 
g = Particle(pdg_code =21, 
	 name = 'g' ,
	 antiname = 'g' ,
	 spin = 3 ,
	 color = 8 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'wavy' ,
	 charge = 0 ,
	 texname = 'g' ,
	 antitexname = 'g' ) 
 
A = Particle(pdg_code =22, 
	 name = 'A' ,
	 antiname = 'A' ,
	 spin = 3 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 0, 
	 line = 'wavy' ,
	 charge = 0 ,
	 texname = 'A' ,
	 antitexname = 'A' ) 
 
Z = Particle(pdg_code =23, 
	 name = 'Z' ,
	 antiname = 'Z' ,
	 spin = 3 ,
	 color = 1 ,
	 mass = Param.MZ ,
	 width = Param.WZ ,
	 GhostNumber = 0, 
	 line = 'wavy' ,
	 charge = 0 ,
	 texname = 'Z' ,
	 antitexname = 'Z' ) 
 
Zp = Particle(pdg_code =32, 
	 name = 'Zp' ,
	 antiname = 'Zp' ,
	 spin = 3 ,
	 color = 1 ,
	 mass = Param.MZp ,
	 width = Param.WZp ,
	 GhostNumber = 0, 
	 line = 'wavy' ,
	 charge = 0 ,
	 texname = 'Zp' ,
	 antitexname = 'Zp' ) 
 
Wm = Particle(pdg_code =-24, 
	 name = 'Wm' ,
	 antiname = 'Wmc' ,
	 spin = 3 ,
	 color = 1 ,
	 mass = Param.MWm ,
	 width = Param.WWm ,
	 GhostNumber = 0, 
	 line = 'wavy' ,
	 charge = -1 ,
	 texname = 'Wm' ,
	 antitexname = 'Wmc' ) 
 
Wmc = Wm.anti() 
 
 
WRm = Particle(pdg_code =-34, 
	 name = 'WRm' ,
	 antiname = 'WRmc' ,
	 spin = 3 ,
	 color = 1 ,
	 mass = Param.MWRm ,
	 width = Param.WWRm ,
	 GhostNumber = 0, 
	 line = 'wavy' ,
	 charge = -1 ,
	 texname = 'WRm' ,
	 antitexname = 'WRmc' ) 
 
WRmc = WRm.anti() 
 
 
gG = Particle(pdg_code =999904, 
	 name = 'gG' ,
	 antiname = 'gGc' ,
	 spin = -1 ,
	 color = 8 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 1, 
	 line = 'dotted' ,
	 charge = 0 ,
	 texname = 'gG' ,
	 antitexname = 'gGc' ) 
 
gGc = gG.anti() 
 
 
gP = Particle(pdg_code =999905, 
	 name = 'gP' ,
	 antiname = 'gPc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.ZERO ,
	 width = Param.ZERO ,
	 GhostNumber = 1, 
	 line = 'dotted' ,
	 charge = 0 ,
	 texname = 'gP' ,
	 antitexname = 'gPc' ) 
 
gPc = gP.anti() 
 
 
gZ = Particle(pdg_code =999906, 
	 name = 'gZ' ,
	 antiname = 'gZc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.MZ ,
	 width = Param.WZ ,
	 GhostNumber = 1, 
	 line = 'dotted' ,
	 charge = 0 ,
	 texname = 'gZ' ,
	 antitexname = 'gZc' ) 
 
gZc = gZ.anti() 
 
 
gZp = Particle(pdg_code =999907, 
	 name = 'gZp' ,
	 antiname = 'gZpc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.MZp ,
	 width = Param.WZp ,
	 GhostNumber = 1, 
	 line = 'dotted' ,
	 charge = 0 ,
	 texname = 'gZp' ,
	 antitexname = 'gZpc' ) 
 
gZpc = gZp.anti() 
 
 
gWLm = Particle(pdg_code =999908, 
	 name = 'gWLm' ,
	 antiname = 'gWLmc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.MWm ,
	 width = Param.WWm ,
	 GhostNumber = 1, 
	 line = 'dotted' ,
	 charge = -1 ,
	 texname = 'gWLm' ,
	 antitexname = 'gWLmc' ) 
 
gWLmc = gWLm.anti() 
 
 
gWLC = Particle(pdg_code =999909, 
	 name = 'gWLC' ,
	 antiname = 'gWLCc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.MWm ,
	 width = Param.WWm ,
	 GhostNumber = 1, 
	 line = 'dotted' ,
	 charge = 1 ,
	 texname = 'gWLC' ,
	 antitexname = 'gWLCc' ) 
 
gWLCc = gWLC.anti() 
 
 
gWRm = Particle(pdg_code =999910, 
	 name = 'gWRm' ,
	 antiname = 'gWRmc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.MWRm ,
	 width = Param.WWRm ,
	 GhostNumber = 1, 
	 line = 'dotted' ,
	 charge = -1 ,
	 texname = 'gWRm' ,
	 antitexname = 'gWRmc' ) 
 
gWRmc = gWRm.anti() 
 
 
gWRC = Particle(pdg_code =999911, 
	 name = 'gWRC' ,
	 antiname = 'gWRCc' ,
	 spin = -1 ,
	 color = 1 ,
	 mass = Param.MWRm ,
	 width = Param.WWRm ,
	 GhostNumber = 1, 
	 line = 'dotted' ,
	 charge = 1 ,
	 texname = 'gWRC' ,
	 antitexname = 'gWRCc' ) 
 
gWRCc = gWRC.anti() 
 
 
