# ----------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.13.0 
# SARAH References: arXiv:0806.0538, arXiv:0909.2863, arXiv:1002.0840    
# (c) Florian Staub, 2011  
# ----------------------------------------------------------------------  
# File created at 11:37 on 20.6.2018   
# ----------------------------------------------------------------------  
 
 
from object_library import all_parameters,Parameter 
 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
ZERO=Parameter(name='ZERO', 
                      nature='internal', 
                      type='real', 
                      value='0.0', 
                      texname='0') 
 
Mglu = 	 Parameter(name = 'Mglu', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mglu}', 
	 lhablock = 'MASS', 
	 lhacode = [1000021]) 
 
MC01 = 	 Parameter(name = 'MC01', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC01}', 
	 lhablock = 'MASS', 
	 lhacode = [1000022]) 
 
WC01 = 	 Parameter(name = 'WC01', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC01}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000022]) 
 
MC02 = 	 Parameter(name = 'MC02', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC02}', 
	 lhablock = 'MASS', 
	 lhacode = [1000023]) 
 
WC02 = 	 Parameter(name = 'WC02', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC02}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000023]) 
 
MC03 = 	 Parameter(name = 'MC03', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC03}', 
	 lhablock = 'MASS', 
	 lhacode = [1000025]) 
 
WC03 = 	 Parameter(name = 'WC03', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC03}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000025]) 
 
MC04 = 	 Parameter(name = 'MC04', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC04}', 
	 lhablock = 'MASS', 
	 lhacode = [1000035]) 
 
WC04 = 	 Parameter(name = 'WC04', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC04}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000035]) 
 
MC05 = 	 Parameter(name = 'MC05', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC05}', 
	 lhablock = 'MASS', 
	 lhacode = [6000022]) 
 
WC05 = 	 Parameter(name = 'WC05', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC05}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000022]) 
 
MC06 = 	 Parameter(name = 'MC06', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC06}', 
	 lhablock = 'MASS', 
	 lhacode = [6000023]) 
 
WC06 = 	 Parameter(name = 'WC06', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC06}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000023]) 
 
MC07 = 	 Parameter(name = 'MC07', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC07}', 
	 lhablock = 'MASS', 
	 lhacode = [6000025]) 
 
WC07 = 	 Parameter(name = 'WC07', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC07}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000025]) 
 
MC08 = 	 Parameter(name = 'MC08', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC08}', 
	 lhablock = 'MASS', 
	 lhacode = [6000055]) 
 
WC08 = 	 Parameter(name = 'WC08', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC08}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000055]) 
 
MC09 = 	 Parameter(name = 'MC09', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC09}', 
	 lhablock = 'MASS', 
	 lhacode = [7000022]) 
 
WC09 = 	 Parameter(name = 'WC09', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC09}', 
	 lhablock = 'DECAY', 
	 lhacode = [7000022]) 
 
MC010 = 	 Parameter(name = 'MC010', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC010}', 
	 lhablock = 'MASS', 
	 lhacode = [7000023]) 
 
WC010 = 	 Parameter(name = 'WC010', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC010}', 
	 lhablock = 'DECAY', 
	 lhacode = [7000023]) 
 
MC011 = 	 Parameter(name = 'MC011', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC011}', 
	 lhablock = 'MASS', 
	 lhacode = [7000025]) 
 
WC011 = 	 Parameter(name = 'WC011', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC011}', 
	 lhablock = 'DECAY', 
	 lhacode = [7000025]) 
 
MC012 = 	 Parameter(name = 'MC012', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MC012}', 
	 lhablock = 'MASS', 
	 lhacode = [7000035]) 
 
WC012 = 	 Parameter(name = 'WC012', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WC012}', 
	 lhablock = 'DECAY', 
	 lhacode = [7000035]) 
 
MCA1 = 	 Parameter(name = 'MCA1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MCA1}', 
	 lhablock = 'MASS', 
	 lhacode = [1000024]) 
 
WCA1 = 	 Parameter(name = 'WCA1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WCA1}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000024]) 
 
MCA2 = 	 Parameter(name = 'MCA2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MCA2}', 
	 lhablock = 'MASS', 
	 lhacode = [1000037]) 
 
WCA2 = 	 Parameter(name = 'WCA2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WCA2}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000037]) 
 
MCA3 = 	 Parameter(name = 'MCA3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MCA3}', 
	 lhablock = 'MASS', 
	 lhacode = [6000024]) 
 
WCA3 = 	 Parameter(name = 'WCA3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WCA3}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000024]) 
 
MCA4 = 	 Parameter(name = 'MCA4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MCA4}', 
	 lhablock = 'MASS', 
	 lhacode = [6000037]) 
 
WCA4 = 	 Parameter(name = 'WCA4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WCA4}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000037]) 
 
MCA5 = 	 Parameter(name = 'MCA5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MCA5}', 
	 lhablock = 'MASS', 
	 lhacode = [7000024]) 
 
WCA5 = 	 Parameter(name = 'WCA5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WCA5}', 
	 lhablock = 'DECAY', 
	 lhacode = [7000024]) 
 
MCA6 = 	 Parameter(name = 'MCA6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MCA6}', 
	 lhablock = 'MASS', 
	 lhacode = [7000037]) 
 
WCA6 = 	 Parameter(name = 'WCA6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WCA6}', 
	 lhablock = 'DECAY', 
	 lhacode = [7000037]) 
 
MCmm1 = 	 Parameter(name = 'MCmm1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MCmm1}', 
	 lhablock = 'MASS', 
	 lhacode = [6000044]) 
 
WCmm1 = 	 Parameter(name = 'WCmm1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WCmm1}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000044]) 
 
MCmm2 = 	 Parameter(name = 'MCmm2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MCmm2}', 
	 lhablock = 'MASS', 
	 lhacode = [6000057]) 
 
WCmm2 = 	 Parameter(name = 'WCmm2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WCmm2}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000057]) 
 
Mnu4 = 	 Parameter(name = 'Mnu4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mnu4}', 
	 lhablock = 'MASS', 
	 lhacode = [6000012]) 
 
Wnu4 = 	 Parameter(name = 'Wnu4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wnu4}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000012]) 
 
Mnu5 = 	 Parameter(name = 'Mnu5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mnu5}', 
	 lhablock = 'MASS', 
	 lhacode = [6000014]) 
 
Wnu5 = 	 Parameter(name = 'Wnu5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wnu5}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000014]) 
 
Mnu6 = 	 Parameter(name = 'Mnu6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mnu6}', 
	 lhablock = 'MASS', 
	 lhacode = [6000016]) 
 
Wnu6 = 	 Parameter(name = 'Wnu6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wnu6}', 
	 lhablock = 'DECAY', 
	 lhacode = [6000016]) 
 
Me1 = 	 Parameter(name = 'Me1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.000511, 
	 texname = '\\text{Me1}', 
	 lhablock = 'MASS', 
	 lhacode = [11]) 
 
Me2 = 	 Parameter(name = 'Me2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.105, 
	 texname = '\\text{Me2}', 
	 lhablock = 'MASS', 
	 lhacode = [13]) 
 
Me3 = 	 Parameter(name = 'Me3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.776, 
	 texname = '\\text{Me3}', 
	 lhablock = 'MASS', 
	 lhacode = [15]) 
 
Md1 = 	 Parameter(name = 'Md1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0035, 
	 texname = '\\text{Md1}', 
	 lhablock = 'MASS', 
	 lhacode = [1]) 
 
Md2 = 	 Parameter(name = 'Md2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.104, 
	 texname = '\\text{Md2}', 
	 lhablock = 'MASS', 
	 lhacode = [3]) 
 
Md3 = 	 Parameter(name = 'Md3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 4.2, 
	 texname = '\\text{Md3}', 
	 lhablock = 'MASS', 
	 lhacode = [5]) 
 
Mu1 = 	 Parameter(name = 'Mu1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0015, 
	 texname = '\\text{Mu1}', 
	 lhablock = 'MASS', 
	 lhacode = [2]) 
 
Mu2 = 	 Parameter(name = 'Mu2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.27, 
	 texname = '\\text{Mu2}', 
	 lhablock = 'MASS', 
	 lhacode = [4]) 
 
Mu3 = 	 Parameter(name = 'Mu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 171.2, 
	 texname = '\\text{Mu3}', 
	 lhablock = 'MASS', 
	 lhacode = [6]) 
 
Wu3 = 	 Parameter(name = 'Wu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1.51, 
	 texname = '\\text{Wu3}', 
	 lhablock = 'DECAY', 
	 lhacode = [6]) 
 
Msd1 = 	 Parameter(name = 'Msd1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msd1}', 
	 lhablock = 'MASS', 
	 lhacode = [1000001]) 
 
Wsd1 = 	 Parameter(name = 'Wsd1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsd1}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000001]) 
 
Msd2 = 	 Parameter(name = 'Msd2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msd2}', 
	 lhablock = 'MASS', 
	 lhacode = [1000003]) 
 
Wsd2 = 	 Parameter(name = 'Wsd2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsd2}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000003]) 
 
Msd3 = 	 Parameter(name = 'Msd3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msd3}', 
	 lhablock = 'MASS', 
	 lhacode = [1000005]) 
 
Wsd3 = 	 Parameter(name = 'Wsd3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsd3}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000005]) 
 
Msd4 = 	 Parameter(name = 'Msd4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msd4}', 
	 lhablock = 'MASS', 
	 lhacode = [2000001]) 
 
Wsd4 = 	 Parameter(name = 'Wsd4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsd4}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000001]) 
 
Msd5 = 	 Parameter(name = 'Msd5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msd5}', 
	 lhablock = 'MASS', 
	 lhacode = [2000003]) 
 
Wsd5 = 	 Parameter(name = 'Wsd5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsd5}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000003]) 
 
Msd6 = 	 Parameter(name = 'Msd6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msd6}', 
	 lhablock = 'MASS', 
	 lhacode = [2000005]) 
 
Wsd6 = 	 Parameter(name = 'Wsd6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsd6}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000005]) 
 
Msu1 = 	 Parameter(name = 'Msu1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msu1}', 
	 lhablock = 'MASS', 
	 lhacode = [1000002]) 
 
Wsu1 = 	 Parameter(name = 'Wsu1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsu1}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000002]) 
 
Msu2 = 	 Parameter(name = 'Msu2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msu2}', 
	 lhablock = 'MASS', 
	 lhacode = [1000004]) 
 
Wsu2 = 	 Parameter(name = 'Wsu2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsu2}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000004]) 
 
Msu3 = 	 Parameter(name = 'Msu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msu3}', 
	 lhablock = 'MASS', 
	 lhacode = [1000006]) 
 
Wsu3 = 	 Parameter(name = 'Wsu3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsu3}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000006]) 
 
Msu4 = 	 Parameter(name = 'Msu4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msu4}', 
	 lhablock = 'MASS', 
	 lhacode = [2000002]) 
 
Wsu4 = 	 Parameter(name = 'Wsu4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsu4}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000002]) 
 
Msu5 = 	 Parameter(name = 'Msu5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msu5}', 
	 lhablock = 'MASS', 
	 lhacode = [2000004]) 
 
Wsu5 = 	 Parameter(name = 'Wsu5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsu5}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000004]) 
 
Msu6 = 	 Parameter(name = 'Msu6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Msu6}', 
	 lhablock = 'MASS', 
	 lhacode = [2000006]) 
 
Wsu6 = 	 Parameter(name = 'Wsu6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wsu6}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000006]) 
 
Mse1 = 	 Parameter(name = 'Mse1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mse1}', 
	 lhablock = 'MASS', 
	 lhacode = [1000011]) 
 
Wse1 = 	 Parameter(name = 'Wse1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wse1}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000011]) 
 
Mse2 = 	 Parameter(name = 'Mse2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mse2}', 
	 lhablock = 'MASS', 
	 lhacode = [1000013]) 
 
Wse2 = 	 Parameter(name = 'Wse2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wse2}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000013]) 
 
Mse3 = 	 Parameter(name = 'Mse3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mse3}', 
	 lhablock = 'MASS', 
	 lhacode = [1000015]) 
 
Wse3 = 	 Parameter(name = 'Wse3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wse3}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000015]) 
 
Mse4 = 	 Parameter(name = 'Mse4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mse4}', 
	 lhablock = 'MASS', 
	 lhacode = [2000011]) 
 
Wse4 = 	 Parameter(name = 'Wse4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wse4}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000011]) 
 
Mse5 = 	 Parameter(name = 'Mse5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mse5}', 
	 lhablock = 'MASS', 
	 lhacode = [2000013]) 
 
Wse5 = 	 Parameter(name = 'Wse5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wse5}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000013]) 
 
Mse6 = 	 Parameter(name = 'Mse6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mse6}', 
	 lhablock = 'MASS', 
	 lhacode = [2000015]) 
 
Wse6 = 	 Parameter(name = 'Wse6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Wse6}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000015]) 
 
MSvRe1 = 	 Parameter(name = 'MSvRe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvRe1}', 
	 lhablock = 'MASS', 
	 lhacode = [1000012]) 
 
WSvRe1 = 	 Parameter(name = 'WSvRe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvRe1}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000012]) 
 
MSvRe2 = 	 Parameter(name = 'MSvRe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvRe2}', 
	 lhablock = 'MASS', 
	 lhacode = [1000014]) 
 
WSvRe2 = 	 Parameter(name = 'WSvRe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvRe2}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000014]) 
 
MSvRe3 = 	 Parameter(name = 'MSvRe3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvRe3}', 
	 lhablock = 'MASS', 
	 lhacode = [1000016]) 
 
WSvRe3 = 	 Parameter(name = 'WSvRe3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvRe3}', 
	 lhablock = 'DECAY', 
	 lhacode = [1000016]) 
 
MSvRe4 = 	 Parameter(name = 'MSvRe4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvRe4}', 
	 lhablock = 'MASS', 
	 lhacode = [2000012]) 
 
WSvRe4 = 	 Parameter(name = 'WSvRe4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvRe4}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000012]) 
 
MSvRe5 = 	 Parameter(name = 'MSvRe5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvRe5}', 
	 lhablock = 'MASS', 
	 lhacode = [2000014]) 
 
WSvRe5 = 	 Parameter(name = 'WSvRe5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvRe5}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000014]) 
 
MSvRe6 = 	 Parameter(name = 'MSvRe6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvRe6}', 
	 lhablock = 'MASS', 
	 lhacode = [2000016]) 
 
WSvRe6 = 	 Parameter(name = 'WSvRe6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvRe6}', 
	 lhablock = 'DECAY', 
	 lhacode = [2000016]) 
 
MSvIe1 = 	 Parameter(name = 'MSvIe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvIe1}', 
	 lhablock = 'MASS', 
	 lhacode = [5000012]) 
 
WSvIe1 = 	 Parameter(name = 'WSvIe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvIe1}', 
	 lhablock = 'DECAY', 
	 lhacode = [5000012]) 
 
MSvIe2 = 	 Parameter(name = 'MSvIe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvIe2}', 
	 lhablock = 'MASS', 
	 lhacode = [5000014]) 
 
WSvIe2 = 	 Parameter(name = 'WSvIe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvIe2}', 
	 lhablock = 'DECAY', 
	 lhacode = [5000014]) 
 
MSvIe3 = 	 Parameter(name = 'MSvIe3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvIe3}', 
	 lhablock = 'MASS', 
	 lhacode = [5000016]) 
 
WSvIe3 = 	 Parameter(name = 'WSvIe3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvIe3}', 
	 lhablock = 'DECAY', 
	 lhacode = [5000016]) 
 
MSvIe4 = 	 Parameter(name = 'MSvIe4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvIe4}', 
	 lhablock = 'MASS', 
	 lhacode = [7000012]) 
 
WSvIe4 = 	 Parameter(name = 'WSvIe4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvIe4}', 
	 lhablock = 'DECAY', 
	 lhacode = [7000012]) 
 
MSvIe5 = 	 Parameter(name = 'MSvIe5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvIe5}', 
	 lhablock = 'MASS', 
	 lhacode = [7000014]) 
 
WSvIe5 = 	 Parameter(name = 'WSvIe5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvIe5}', 
	 lhablock = 'DECAY', 
	 lhacode = [7000014]) 
 
MSvIe6 = 	 Parameter(name = 'MSvIe6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MSvIe6}', 
	 lhablock = 'MASS', 
	 lhacode = [7000016]) 
 
WSvIe6 = 	 Parameter(name = 'WSvIe6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WSvIe6}', 
	 lhablock = 'DECAY', 
	 lhacode = [7000016]) 
 
MhhPr1 = 	 Parameter(name = 'MhhPr1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MhhPr1}', 
	 lhablock = 'MASS', 
	 lhacode = [9000045]) 
 
WhhPr1 = 	 Parameter(name = 'WhhPr1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WhhPr1}', 
	 lhablock = 'DECAY', 
	 lhacode = [9000045]) 
 
MhhPr2 = 	 Parameter(name = 'MhhPr2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MhhPr2}', 
	 lhablock = 'MASS', 
	 lhacode = [9100025]) 
 
WhhPr2 = 	 Parameter(name = 'WhhPr2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WhhPr2}', 
	 lhablock = 'DECAY', 
	 lhacode = [9100025]) 
 
MhhLe1 = 	 Parameter(name = 'MhhLe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MhhLe1}', 
	 lhablock = 'MASS', 
	 lhacode = [9100035]) 
 
WhhLe1 = 	 Parameter(name = 'WhhLe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WhhLe1}', 
	 lhablock = 'DECAY', 
	 lhacode = [9100035]) 
 
MhhLe2 = 	 Parameter(name = 'MhhLe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MhhLe2}', 
	 lhablock = 'MASS', 
	 lhacode = [9100045]) 
 
WhhLe2 = 	 Parameter(name = 'WhhLe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WhhLe2}', 
	 lhablock = 'DECAY', 
	 lhacode = [9100045]) 
 
Mhh1 = 	 Parameter(name = 'Mhh1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mhh1}', 
	 lhablock = 'MASS', 
	 lhacode = [25]) 
 
Whh1 = 	 Parameter(name = 'Whh1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Whh1}', 
	 lhablock = 'DECAY', 
	 lhacode = [25]) 
 
Mhh2 = 	 Parameter(name = 'Mhh2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mhh2}', 
	 lhablock = 'MASS', 
	 lhacode = [35]) 
 
Whh2 = 	 Parameter(name = 'Whh2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Whh2}', 
	 lhablock = 'DECAY', 
	 lhacode = [35]) 
 
Mhh3 = 	 Parameter(name = 'Mhh3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mhh3}', 
	 lhablock = 'MASS', 
	 lhacode = [45]) 
 
Whh3 = 	 Parameter(name = 'Whh3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Whh3}', 
	 lhablock = 'DECAY', 
	 lhacode = [45]) 
 
Mhh4 = 	 Parameter(name = 'Mhh4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mhh4}', 
	 lhablock = 'MASS', 
	 lhacode = [9000025]) 
 
Whh4 = 	 Parameter(name = 'Whh4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Whh4}', 
	 lhablock = 'DECAY', 
	 lhacode = [9000025]) 
 
Mhh5 = 	 Parameter(name = 'Mhh5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{Mhh5}', 
	 lhablock = 'MASS', 
	 lhacode = [9000035]) 
 
Whh5 = 	 Parameter(name = 'Whh5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Whh5}', 
	 lhablock = 'DECAY', 
	 lhacode = [9000035]) 
 
MAhLe1 = 	 Parameter(name = 'MAhLe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MAhLe1}', 
	 lhablock = 'MASS', 
	 lhacode = [7100035]) 
 
WAhLe1 = 	 Parameter(name = 'WAhLe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WAhLe1}', 
	 lhablock = 'DECAY', 
	 lhacode = [7100035]) 
 
MAhLe2 = 	 Parameter(name = 'MAhLe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MAhLe2}', 
	 lhablock = 'MASS', 
	 lhacode = [7100045]) 
 
WAhLe2 = 	 Parameter(name = 'WAhLe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WAhLe2}', 
	 lhablock = 'DECAY', 
	 lhacode = [7100045]) 
 
MAhPr1 = 	 Parameter(name = 'MAhPr1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MAhPr1}', 
	 lhablock = 'MASS', 
	 lhacode = [7000045]) 
 
WAhPr1 = 	 Parameter(name = 'WAhPr1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WAhPr1}', 
	 lhablock = 'DECAY', 
	 lhacode = [7000045]) 
 
MAhPr2 = 	 Parameter(name = 'MAhPr2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MAhPr2}', 
	 lhablock = 'MASS', 
	 lhacode = [7100025]) 
 
WAhPr2 = 	 Parameter(name = 'WAhPr2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WAhPr2}', 
	 lhablock = 'DECAY', 
	 lhacode = [7100025]) 
 
MAh3 = 	 Parameter(name = 'MAh3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MAh3}', 
	 lhablock = 'MASS', 
	 lhacode = [36]) 
 
WAh3 = 	 Parameter(name = 'WAh3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WAh3}', 
	 lhablock = 'DECAY', 
	 lhacode = [36]) 
 
MAh4 = 	 Parameter(name = 'MAh4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MAh4}', 
	 lhablock = 'MASS', 
	 lhacode = [46]) 
 
WAh4 = 	 Parameter(name = 'WAh4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WAh4}', 
	 lhablock = 'DECAY', 
	 lhacode = [46]) 
 
MAh5 = 	 Parameter(name = 'MAh5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MAh5}', 
	 lhablock = 'MASS', 
	 lhacode = [9000036]) 
 
WAh5 = 	 Parameter(name = 'WAh5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WAh5}', 
	 lhablock = 'DECAY', 
	 lhacode = [9000036]) 
 
MHpm3 = 	 Parameter(name = 'MHpm3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHpm3}', 
	 lhablock = 'MASS', 
	 lhacode = [37]) 
 
WHpm3 = 	 Parameter(name = 'WHpm3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHpm3}', 
	 lhablock = 'DECAY', 
	 lhacode = [37]) 
 
MHpm4 = 	 Parameter(name = 'MHpm4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHpm4}', 
	 lhablock = 'MASS', 
	 lhacode = [9000037]) 
 
WHpm4 = 	 Parameter(name = 'WHpm4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHpm4}', 
	 lhablock = 'DECAY', 
	 lhacode = [9000037]) 
 
MHpm5 = 	 Parameter(name = 'MHpm5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHpm5}', 
	 lhablock = 'MASS', 
	 lhacode = [9100037]) 
 
WHpm5 = 	 Parameter(name = 'WHpm5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHpm5}', 
	 lhablock = 'DECAY', 
	 lhacode = [9100037]) 
 
MHpm6 = 	 Parameter(name = 'MHpm6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHpm6}', 
	 lhablock = 'MASS', 
	 lhacode = [9200037]) 
 
WHpm6 = 	 Parameter(name = 'WHpm6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHpm6}', 
	 lhablock = 'DECAY', 
	 lhacode = [9200037]) 
 
MHpmLe1 = 	 Parameter(name = 'MHpmLe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHpmLe1}', 
	 lhablock = 'MASS', 
	 lhacode = [9300037]) 
 
WHpmLe1 = 	 Parameter(name = 'WHpmLe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHpmLe1}', 
	 lhablock = 'DECAY', 
	 lhacode = [9300037]) 
 
MHpmLe2 = 	 Parameter(name = 'MHpmLe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHpmLe2}', 
	 lhablock = 'MASS', 
	 lhacode = [9400037]) 
 
WHpmLe2 = 	 Parameter(name = 'WHpmLe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHpmLe2}', 
	 lhablock = 'DECAY', 
	 lhacode = [9400037]) 
 
MHmm1 = 	 Parameter(name = 'MHmm1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHmm1}', 
	 lhablock = 'MASS', 
	 lhacode = [9000055]) 
 
WHmm1 = 	 Parameter(name = 'WHmm1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHmm1}', 
	 lhablock = 'DECAY', 
	 lhacode = [9000055]) 
 
MHmm2 = 	 Parameter(name = 'MHmm2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHmm2}', 
	 lhablock = 'MASS', 
	 lhacode = [9000056]) 
 
WHmm2 = 	 Parameter(name = 'WHmm2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHmm2}', 
	 lhablock = 'DECAY', 
	 lhacode = [9000056]) 
 
MHmmLe1 = 	 Parameter(name = 'MHmmLe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHmmLe1}', 
	 lhablock = 'MASS', 
	 lhacode = [9000057]) 
 
WHmmLe1 = 	 Parameter(name = 'WHmmLe1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHmmLe1}', 
	 lhablock = 'DECAY', 
	 lhacode = [9000057]) 
 
MHmmLe2 = 	 Parameter(name = 'MHmmLe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MHmmLe2}', 
	 lhablock = 'MASS', 
	 lhacode = [9000058]) 
 
WHmmLe2 = 	 Parameter(name = 'WHmmLe2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WHmmLe2}', 
	 lhablock = 'DECAY', 
	 lhacode = [9000058]) 
 
MZ = 	 Parameter(name = 'MZ', 
	 nature = 'external', 
	 type = 'real', 
	 value = 91.1876, 
	 texname = '\\text{MZ}', 
	 lhablock = 'MASS', 
	 lhacode = [23]) 
 
WZ = 	 Parameter(name = 'WZ', 
	 nature = 'external', 
	 type = 'real', 
	 value = 2.4952, 
	 texname = '\\text{WZ}', 
	 lhablock = 'DECAY', 
	 lhacode = [23]) 
 
MZp = 	 Parameter(name = 'MZp', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MZp}', 
	 lhablock = 'MASS', 
	 lhacode = [32]) 
 
WZp = 	 Parameter(name = 'WZp', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WZp}', 
	 lhablock = 'DECAY', 
	 lhacode = [32]) 
 
WWm = 	 Parameter(name = 'WWm', 
	 nature = 'external', 
	 type = 'real', 
	 value = 2.141, 
	 texname = '\\text{WWm}', 
	 lhablock = 'DECAY', 
	 lhacode = [24]) 
 
MWRm = 	 Parameter(name = 'MWRm', 
	 nature = 'external', 
	 type = 'real', 
	 value = 100., 
	 texname = '\\text{MWRm}', 
	 lhablock = 'MASS', 
	 lhacode = [34]) 
 
WWRm = 	 Parameter(name = 'WWRm', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{WWRm}', 
	 lhablock = 'DECAY', 
	 lhacode = [34]) 
 
gBL = 	 Parameter(name='gBL', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{gBL}', 
	 lhablock = 'GAUGE', 
	 lhacode = [4] ) 
 
gR = 	 Parameter(name='gR', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{gR}', 
	 lhablock = 'GAUGE', 
	 lhacode = [1] ) 
 
YL311 = 	 Parameter(name='YL311', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL311}', 
	 lhablock = 'YL3', 
	 lhacode = [1, 1] ) 
 
YL312 = 	 Parameter(name='YL312', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL312}', 
	 lhablock = 'YL3', 
	 lhacode = [1, 2] ) 
 
YL313 = 	 Parameter(name='YL313', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL313}', 
	 lhablock = 'YL3', 
	 lhacode = [1, 3] ) 
 
YL321 = 	 Parameter(name='YL321', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL321}', 
	 lhablock = 'YL3', 
	 lhacode = [2, 1] ) 
 
YL322 = 	 Parameter(name='YL322', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL322}', 
	 lhablock = 'YL3', 
	 lhacode = [2, 2] ) 
 
YL323 = 	 Parameter(name='YL323', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL323}', 
	 lhablock = 'YL3', 
	 lhacode = [2, 3] ) 
 
YL331 = 	 Parameter(name='YL331', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL331}', 
	 lhablock = 'YL3', 
	 lhacode = [3, 1] ) 
 
YL332 = 	 Parameter(name='YL332', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL332}', 
	 lhablock = 'YL3', 
	 lhacode = [3, 2] ) 
 
YL333 = 	 Parameter(name='YL333', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL333}', 
	 lhablock = 'YL3', 
	 lhacode = [3, 3] ) 
 
TL311 = 	 Parameter(name='TL311', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL311}', 
	 lhablock = 'TL3', 
	 lhacode = [1, 1] ) 
 
TL312 = 	 Parameter(name='TL312', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL312}', 
	 lhablock = 'TL3', 
	 lhacode = [1, 2] ) 
 
TL313 = 	 Parameter(name='TL313', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL313}', 
	 lhablock = 'TL3', 
	 lhacode = [1, 3] ) 
 
TL321 = 	 Parameter(name='TL321', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL321}', 
	 lhablock = 'TL3', 
	 lhacode = [2, 1] ) 
 
TL322 = 	 Parameter(name='TL322', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL322}', 
	 lhablock = 'TL3', 
	 lhacode = [2, 2] ) 
 
TL323 = 	 Parameter(name='TL323', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL323}', 
	 lhablock = 'TL3', 
	 lhacode = [2, 3] ) 
 
TL331 = 	 Parameter(name='TL331', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL331}', 
	 lhablock = 'TL3', 
	 lhacode = [3, 1] ) 
 
TL332 = 	 Parameter(name='TL332', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL332}', 
	 lhablock = 'TL3', 
	 lhacode = [3, 2] ) 
 
TL333 = 	 Parameter(name='TL333', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL333}', 
	 lhablock = 'TL3', 
	 lhacode = [3, 3] ) 
 
YL411 = 	 Parameter(name='YL411', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL411}', 
	 lhablock = 'YL4', 
	 lhacode = [1, 1] ) 
 
YL412 = 	 Parameter(name='YL412', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL412}', 
	 lhablock = 'YL4', 
	 lhacode = [1, 2] ) 
 
YL413 = 	 Parameter(name='YL413', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL413}', 
	 lhablock = 'YL4', 
	 lhacode = [1, 3] ) 
 
YL421 = 	 Parameter(name='YL421', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL421}', 
	 lhablock = 'YL4', 
	 lhacode = [2, 1] ) 
 
YL422 = 	 Parameter(name='YL422', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL422}', 
	 lhablock = 'YL4', 
	 lhacode = [2, 2] ) 
 
YL423 = 	 Parameter(name='YL423', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL423}', 
	 lhablock = 'YL4', 
	 lhacode = [2, 3] ) 
 
YL431 = 	 Parameter(name='YL431', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL431}', 
	 lhablock = 'YL4', 
	 lhacode = [3, 1] ) 
 
YL432 = 	 Parameter(name='YL432', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL432}', 
	 lhablock = 'YL4', 
	 lhacode = [3, 2] ) 
 
YL433 = 	 Parameter(name='YL433', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL433}', 
	 lhablock = 'YL4', 
	 lhacode = [3, 3] ) 
 
TL411 = 	 Parameter(name='TL411', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL411}', 
	 lhablock = 'TL4', 
	 lhacode = [1, 1] ) 
 
TL412 = 	 Parameter(name='TL412', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL412}', 
	 lhablock = 'TL4', 
	 lhacode = [1, 2] ) 
 
TL413 = 	 Parameter(name='TL413', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL413}', 
	 lhablock = 'TL4', 
	 lhacode = [1, 3] ) 
 
TL421 = 	 Parameter(name='TL421', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL421}', 
	 lhablock = 'TL4', 
	 lhacode = [2, 1] ) 
 
TL422 = 	 Parameter(name='TL422', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL422}', 
	 lhablock = 'TL4', 
	 lhacode = [2, 2] ) 
 
TL423 = 	 Parameter(name='TL423', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL423}', 
	 lhablock = 'TL4', 
	 lhacode = [2, 3] ) 
 
TL431 = 	 Parameter(name='TL431', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL431}', 
	 lhablock = 'TL4', 
	 lhacode = [3, 1] ) 
 
TL432 = 	 Parameter(name='TL432', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL432}', 
	 lhablock = 'TL4', 
	 lhacode = [3, 2] ) 
 
TL433 = 	 Parameter(name='TL433', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL433}', 
	 lhablock = 'TL4', 
	 lhacode = [3, 3] ) 
 
rYL111 = 	 Parameter(name='rYL111', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL111}', 
	 lhablock = 'YL1', 
	 lhacode = [1, 1] ) 
 
iYL111 = 	 Parameter(name='iYL111', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL111}', 
	 lhablock = 'IMYL1', 
	 lhacode = [1, 1] ) 
 
rYL112 = 	 Parameter(name='rYL112', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL112}', 
	 lhablock = 'YL1', 
	 lhacode = [1, 2] ) 
 
iYL112 = 	 Parameter(name='iYL112', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL112}', 
	 lhablock = 'IMYL1', 
	 lhacode = [1, 2] ) 
 
rYL113 = 	 Parameter(name='rYL113', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL113}', 
	 lhablock = 'YL1', 
	 lhacode = [1, 3] ) 
 
iYL113 = 	 Parameter(name='iYL113', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL113}', 
	 lhablock = 'IMYL1', 
	 lhacode = [1, 3] ) 
 
rYL121 = 	 Parameter(name='rYL121', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL121}', 
	 lhablock = 'YL1', 
	 lhacode = [2, 1] ) 
 
iYL121 = 	 Parameter(name='iYL121', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL121}', 
	 lhablock = 'IMYL1', 
	 lhacode = [2, 1] ) 
 
rYL122 = 	 Parameter(name='rYL122', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL122}', 
	 lhablock = 'YL1', 
	 lhacode = [2, 2] ) 
 
iYL122 = 	 Parameter(name='iYL122', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL122}', 
	 lhablock = 'IMYL1', 
	 lhacode = [2, 2] ) 
 
rYL123 = 	 Parameter(name='rYL123', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL123}', 
	 lhablock = 'YL1', 
	 lhacode = [2, 3] ) 
 
iYL123 = 	 Parameter(name='iYL123', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL123}', 
	 lhablock = 'IMYL1', 
	 lhacode = [2, 3] ) 
 
rYL131 = 	 Parameter(name='rYL131', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL131}', 
	 lhablock = 'YL1', 
	 lhacode = [3, 1] ) 
 
iYL131 = 	 Parameter(name='iYL131', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL131}', 
	 lhablock = 'IMYL1', 
	 lhacode = [3, 1] ) 
 
rYL132 = 	 Parameter(name='rYL132', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL132}', 
	 lhablock = 'YL1', 
	 lhacode = [3, 2] ) 
 
iYL132 = 	 Parameter(name='iYL132', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL132}', 
	 lhablock = 'IMYL1', 
	 lhacode = [3, 2] ) 
 
rYL133 = 	 Parameter(name='rYL133', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL133}', 
	 lhablock = 'YL1', 
	 lhacode = [3, 3] ) 
 
iYL133 = 	 Parameter(name='iYL133', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL133}', 
	 lhablock = 'IMYL1', 
	 lhacode = [3, 3] ) 
 
rTL111 = 	 Parameter(name='rTL111', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL111}', 
	 lhablock = 'TL1', 
	 lhacode = [1, 1] ) 
 
iTL111 = 	 Parameter(name='iTL111', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL111}', 
	 lhablock = 'IMTL1', 
	 lhacode = [1, 1] ) 
 
rTL112 = 	 Parameter(name='rTL112', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL112}', 
	 lhablock = 'TL1', 
	 lhacode = [1, 2] ) 
 
iTL112 = 	 Parameter(name='iTL112', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL112}', 
	 lhablock = 'IMTL1', 
	 lhacode = [1, 2] ) 
 
rTL113 = 	 Parameter(name='rTL113', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL113}', 
	 lhablock = 'TL1', 
	 lhacode = [1, 3] ) 
 
iTL113 = 	 Parameter(name='iTL113', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL113}', 
	 lhablock = 'IMTL1', 
	 lhacode = [1, 3] ) 
 
rTL121 = 	 Parameter(name='rTL121', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL121}', 
	 lhablock = 'TL1', 
	 lhacode = [2, 1] ) 
 
iTL121 = 	 Parameter(name='iTL121', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL121}', 
	 lhablock = 'IMTL1', 
	 lhacode = [2, 1] ) 
 
rTL122 = 	 Parameter(name='rTL122', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL122}', 
	 lhablock = 'TL1', 
	 lhacode = [2, 2] ) 
 
iTL122 = 	 Parameter(name='iTL122', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL122}', 
	 lhablock = 'IMTL1', 
	 lhacode = [2, 2] ) 
 
rTL123 = 	 Parameter(name='rTL123', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL123}', 
	 lhablock = 'TL1', 
	 lhacode = [2, 3] ) 
 
iTL123 = 	 Parameter(name='iTL123', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL123}', 
	 lhablock = 'IMTL1', 
	 lhacode = [2, 3] ) 
 
rTL131 = 	 Parameter(name='rTL131', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL131}', 
	 lhablock = 'TL1', 
	 lhacode = [3, 1] ) 
 
iTL131 = 	 Parameter(name='iTL131', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL131}', 
	 lhablock = 'IMTL1', 
	 lhacode = [3, 1] ) 
 
rTL132 = 	 Parameter(name='rTL132', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL132}', 
	 lhablock = 'TL1', 
	 lhacode = [3, 2] ) 
 
iTL132 = 	 Parameter(name='iTL132', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL132}', 
	 lhablock = 'IMTL1', 
	 lhacode = [3, 2] ) 
 
rTL133 = 	 Parameter(name='rTL133', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL133}', 
	 lhablock = 'TL1', 
	 lhacode = [3, 3] ) 
 
iTL133 = 	 Parameter(name='iTL133', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL133}', 
	 lhablock = 'IMTL1', 
	 lhacode = [3, 3] ) 
 
YL211 = 	 Parameter(name='YL211', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL211}', 
	 lhablock = 'YL2', 
	 lhacode = [1, 1] ) 
 
YL212 = 	 Parameter(name='YL212', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL212}', 
	 lhablock = 'YL2', 
	 lhacode = [1, 2] ) 
 
YL213 = 	 Parameter(name='YL213', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL213}', 
	 lhablock = 'YL2', 
	 lhacode = [1, 3] ) 
 
YL221 = 	 Parameter(name='YL221', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL221}', 
	 lhablock = 'YL2', 
	 lhacode = [2, 1] ) 
 
YL222 = 	 Parameter(name='YL222', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL222}', 
	 lhablock = 'YL2', 
	 lhacode = [2, 2] ) 
 
YL223 = 	 Parameter(name='YL223', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL223}', 
	 lhablock = 'YL2', 
	 lhacode = [2, 3] ) 
 
YL231 = 	 Parameter(name='YL231', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL231}', 
	 lhablock = 'YL2', 
	 lhacode = [3, 1] ) 
 
YL232 = 	 Parameter(name='YL232', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL232}', 
	 lhablock = 'YL2', 
	 lhacode = [3, 2] ) 
 
YL233 = 	 Parameter(name='YL233', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YL233}', 
	 lhablock = 'YL2', 
	 lhacode = [3, 3] ) 
 
TL211 = 	 Parameter(name='TL211', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL211}', 
	 lhablock = 'TL2', 
	 lhacode = [1, 1] ) 
 
TL212 = 	 Parameter(name='TL212', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL212}', 
	 lhablock = 'TL2', 
	 lhacode = [1, 2] ) 
 
TL213 = 	 Parameter(name='TL213', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL213}', 
	 lhablock = 'TL2', 
	 lhacode = [1, 3] ) 
 
TL221 = 	 Parameter(name='TL221', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL221}', 
	 lhablock = 'TL2', 
	 lhacode = [2, 1] ) 
 
TL222 = 	 Parameter(name='TL222', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL222}', 
	 lhablock = 'TL2', 
	 lhacode = [2, 2] ) 
 
TL223 = 	 Parameter(name='TL223', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL223}', 
	 lhablock = 'TL2', 
	 lhacode = [2, 3] ) 
 
TL231 = 	 Parameter(name='TL231', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL231}', 
	 lhablock = 'TL2', 
	 lhacode = [3, 1] ) 
 
TL232 = 	 Parameter(name='TL232', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL232}', 
	 lhablock = 'TL2', 
	 lhacode = [3, 2] ) 
 
TL233 = 	 Parameter(name='TL233', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL233}', 
	 lhablock = 'TL2', 
	 lhacode = [3, 3] ) 
 
rYQ111 = 	 Parameter(name='rYQ111', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ111}', 
	 lhablock = 'YQ1', 
	 lhacode = [1, 1] ) 
 
iYQ111 = 	 Parameter(name='iYQ111', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ111}', 
	 lhablock = 'IMYQ1', 
	 lhacode = [1, 1] ) 
 
rYQ112 = 	 Parameter(name='rYQ112', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ112}', 
	 lhablock = 'YQ1', 
	 lhacode = [1, 2] ) 
 
iYQ112 = 	 Parameter(name='iYQ112', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ112}', 
	 lhablock = 'IMYQ1', 
	 lhacode = [1, 2] ) 
 
rYQ113 = 	 Parameter(name='rYQ113', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ113}', 
	 lhablock = 'YQ1', 
	 lhacode = [1, 3] ) 
 
iYQ113 = 	 Parameter(name='iYQ113', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ113}', 
	 lhablock = 'IMYQ1', 
	 lhacode = [1, 3] ) 
 
rYQ121 = 	 Parameter(name='rYQ121', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ121}', 
	 lhablock = 'YQ1', 
	 lhacode = [2, 1] ) 
 
iYQ121 = 	 Parameter(name='iYQ121', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ121}', 
	 lhablock = 'IMYQ1', 
	 lhacode = [2, 1] ) 
 
rYQ122 = 	 Parameter(name='rYQ122', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ122}', 
	 lhablock = 'YQ1', 
	 lhacode = [2, 2] ) 
 
iYQ122 = 	 Parameter(name='iYQ122', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ122}', 
	 lhablock = 'IMYQ1', 
	 lhacode = [2, 2] ) 
 
rYQ123 = 	 Parameter(name='rYQ123', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ123}', 
	 lhablock = 'YQ1', 
	 lhacode = [2, 3] ) 
 
iYQ123 = 	 Parameter(name='iYQ123', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ123}', 
	 lhablock = 'IMYQ1', 
	 lhacode = [2, 3] ) 
 
rYQ131 = 	 Parameter(name='rYQ131', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ131}', 
	 lhablock = 'YQ1', 
	 lhacode = [3, 1] ) 
 
iYQ131 = 	 Parameter(name='iYQ131', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ131}', 
	 lhablock = 'IMYQ1', 
	 lhacode = [3, 1] ) 
 
rYQ132 = 	 Parameter(name='rYQ132', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ132}', 
	 lhablock = 'YQ1', 
	 lhacode = [3, 2] ) 
 
iYQ132 = 	 Parameter(name='iYQ132', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ132}', 
	 lhablock = 'IMYQ1', 
	 lhacode = [3, 2] ) 
 
rYQ133 = 	 Parameter(name='rYQ133', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ133}', 
	 lhablock = 'YQ1', 
	 lhacode = [3, 3] ) 
 
iYQ133 = 	 Parameter(name='iYQ133', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ133}', 
	 lhablock = 'IMYQ1', 
	 lhacode = [3, 3] ) 
 
rTQ111 = 	 Parameter(name='rTQ111', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ111}', 
	 lhablock = 'TQ1', 
	 lhacode = [1, 1] ) 
 
iTQ111 = 	 Parameter(name='iTQ111', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ111}', 
	 lhablock = 'IMTQ1', 
	 lhacode = [1, 1] ) 
 
rTQ112 = 	 Parameter(name='rTQ112', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ112}', 
	 lhablock = 'TQ1', 
	 lhacode = [1, 2] ) 
 
iTQ112 = 	 Parameter(name='iTQ112', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ112}', 
	 lhablock = 'IMTQ1', 
	 lhacode = [1, 2] ) 
 
rTQ113 = 	 Parameter(name='rTQ113', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ113}', 
	 lhablock = 'TQ1', 
	 lhacode = [1, 3] ) 
 
iTQ113 = 	 Parameter(name='iTQ113', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ113}', 
	 lhablock = 'IMTQ1', 
	 lhacode = [1, 3] ) 
 
rTQ121 = 	 Parameter(name='rTQ121', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ121}', 
	 lhablock = 'TQ1', 
	 lhacode = [2, 1] ) 
 
iTQ121 = 	 Parameter(name='iTQ121', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ121}', 
	 lhablock = 'IMTQ1', 
	 lhacode = [2, 1] ) 
 
rTQ122 = 	 Parameter(name='rTQ122', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ122}', 
	 lhablock = 'TQ1', 
	 lhacode = [2, 2] ) 
 
iTQ122 = 	 Parameter(name='iTQ122', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ122}', 
	 lhablock = 'IMTQ1', 
	 lhacode = [2, 2] ) 
 
rTQ123 = 	 Parameter(name='rTQ123', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ123}', 
	 lhablock = 'TQ1', 
	 lhacode = [2, 3] ) 
 
iTQ123 = 	 Parameter(name='iTQ123', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ123}', 
	 lhablock = 'IMTQ1', 
	 lhacode = [2, 3] ) 
 
rTQ131 = 	 Parameter(name='rTQ131', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ131}', 
	 lhablock = 'TQ1', 
	 lhacode = [3, 1] ) 
 
iTQ131 = 	 Parameter(name='iTQ131', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ131}', 
	 lhablock = 'IMTQ1', 
	 lhacode = [3, 1] ) 
 
rTQ132 = 	 Parameter(name='rTQ132', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ132}', 
	 lhablock = 'TQ1', 
	 lhacode = [3, 2] ) 
 
iTQ132 = 	 Parameter(name='iTQ132', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ132}', 
	 lhablock = 'IMTQ1', 
	 lhacode = [3, 2] ) 
 
rTQ133 = 	 Parameter(name='rTQ133', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ133}', 
	 lhablock = 'TQ1', 
	 lhacode = [3, 3] ) 
 
iTQ133 = 	 Parameter(name='iTQ133', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ133}', 
	 lhablock = 'IMTQ1', 
	 lhacode = [3, 3] ) 
 
rYQ211 = 	 Parameter(name='rYQ211', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ211}', 
	 lhablock = 'YQ2', 
	 lhacode = [1, 1] ) 
 
iYQ211 = 	 Parameter(name='iYQ211', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ211}', 
	 lhablock = 'IMYQ2', 
	 lhacode = [1, 1] ) 
 
rYQ212 = 	 Parameter(name='rYQ212', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ212}', 
	 lhablock = 'YQ2', 
	 lhacode = [1, 2] ) 
 
iYQ212 = 	 Parameter(name='iYQ212', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ212}', 
	 lhablock = 'IMYQ2', 
	 lhacode = [1, 2] ) 
 
rYQ213 = 	 Parameter(name='rYQ213', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ213}', 
	 lhablock = 'YQ2', 
	 lhacode = [1, 3] ) 
 
iYQ213 = 	 Parameter(name='iYQ213', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ213}', 
	 lhablock = 'IMYQ2', 
	 lhacode = [1, 3] ) 
 
rYQ221 = 	 Parameter(name='rYQ221', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ221}', 
	 lhablock = 'YQ2', 
	 lhacode = [2, 1] ) 
 
iYQ221 = 	 Parameter(name='iYQ221', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ221}', 
	 lhablock = 'IMYQ2', 
	 lhacode = [2, 1] ) 
 
rYQ222 = 	 Parameter(name='rYQ222', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ222}', 
	 lhablock = 'YQ2', 
	 lhacode = [2, 2] ) 
 
iYQ222 = 	 Parameter(name='iYQ222', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ222}', 
	 lhablock = 'IMYQ2', 
	 lhacode = [2, 2] ) 
 
rYQ223 = 	 Parameter(name='rYQ223', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ223}', 
	 lhablock = 'YQ2', 
	 lhacode = [2, 3] ) 
 
iYQ223 = 	 Parameter(name='iYQ223', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ223}', 
	 lhablock = 'IMYQ2', 
	 lhacode = [2, 3] ) 
 
rYQ231 = 	 Parameter(name='rYQ231', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ231}', 
	 lhablock = 'YQ2', 
	 lhacode = [3, 1] ) 
 
iYQ231 = 	 Parameter(name='iYQ231', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ231}', 
	 lhablock = 'IMYQ2', 
	 lhacode = [3, 1] ) 
 
rYQ232 = 	 Parameter(name='rYQ232', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ232}', 
	 lhablock = 'YQ2', 
	 lhacode = [3, 2] ) 
 
iYQ232 = 	 Parameter(name='iYQ232', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ232}', 
	 lhablock = 'IMYQ2', 
	 lhacode = [3, 2] ) 
 
rYQ233 = 	 Parameter(name='rYQ233', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ233}', 
	 lhablock = 'YQ2', 
	 lhacode = [3, 3] ) 
 
iYQ233 = 	 Parameter(name='iYQ233', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{YQ233}', 
	 lhablock = 'IMYQ2', 
	 lhacode = [3, 3] ) 
 
rTQ211 = 	 Parameter(name='rTQ211', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ211}', 
	 lhablock = 'TQ2', 
	 lhacode = [1, 1] ) 
 
iTQ211 = 	 Parameter(name='iTQ211', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ211}', 
	 lhablock = 'IMTQ2', 
	 lhacode = [1, 1] ) 
 
rTQ212 = 	 Parameter(name='rTQ212', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ212}', 
	 lhablock = 'TQ2', 
	 lhacode = [1, 2] ) 
 
iTQ212 = 	 Parameter(name='iTQ212', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ212}', 
	 lhablock = 'IMTQ2', 
	 lhacode = [1, 2] ) 
 
rTQ213 = 	 Parameter(name='rTQ213', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ213}', 
	 lhablock = 'TQ2', 
	 lhacode = [1, 3] ) 
 
iTQ213 = 	 Parameter(name='iTQ213', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ213}', 
	 lhablock = 'IMTQ2', 
	 lhacode = [1, 3] ) 
 
rTQ221 = 	 Parameter(name='rTQ221', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ221}', 
	 lhablock = 'TQ2', 
	 lhacode = [2, 1] ) 
 
iTQ221 = 	 Parameter(name='iTQ221', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ221}', 
	 lhablock = 'IMTQ2', 
	 lhacode = [2, 1] ) 
 
rTQ222 = 	 Parameter(name='rTQ222', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ222}', 
	 lhablock = 'TQ2', 
	 lhacode = [2, 2] ) 
 
iTQ222 = 	 Parameter(name='iTQ222', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ222}', 
	 lhablock = 'IMTQ2', 
	 lhacode = [2, 2] ) 
 
rTQ223 = 	 Parameter(name='rTQ223', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ223}', 
	 lhablock = 'TQ2', 
	 lhacode = [2, 3] ) 
 
iTQ223 = 	 Parameter(name='iTQ223', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ223}', 
	 lhablock = 'IMTQ2', 
	 lhacode = [2, 3] ) 
 
rTQ231 = 	 Parameter(name='rTQ231', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ231}', 
	 lhablock = 'TQ2', 
	 lhacode = [3, 1] ) 
 
iTQ231 = 	 Parameter(name='iTQ231', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ231}', 
	 lhablock = 'IMTQ2', 
	 lhacode = [3, 1] ) 
 
rTQ232 = 	 Parameter(name='rTQ232', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ232}', 
	 lhablock = 'TQ2', 
	 lhacode = [3, 2] ) 
 
iTQ232 = 	 Parameter(name='iTQ232', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ232}', 
	 lhablock = 'IMTQ2', 
	 lhacode = [3, 2] ) 
 
rTQ233 = 	 Parameter(name='rTQ233', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ233}', 
	 lhablock = 'TQ2', 
	 lhacode = [3, 3] ) 
 
iTQ233 = 	 Parameter(name='iTQ233', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TQ233}', 
	 lhablock = 'IMTQ2', 
	 lhacode = [3, 3] ) 
 
LAMR = 	 Parameter(name='LAMR', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{LAMR}', 
	 lhablock = 'HLAM', 
	 lhacode = [2] ) 
 
TR = 	 Parameter(name='TR', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TR}', 
	 lhablock = 'MSOFT', 
	 lhacode = [41] ) 
 
LAML = 	 Parameter(name='LAML', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{LAML}', 
	 lhablock = 'HLAM', 
	 lhacode = [1] ) 
 
TL = 	 Parameter(name='TL', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TL}', 
	 lhablock = 'MSOFT', 
	 lhacode = [40] ) 
 
LAM3 = 	 Parameter(name='LAM3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{LAM3}', 
	 lhablock = 'HLAM', 
	 lhacode = [3] ) 
 
T3 = 	 Parameter(name='T3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{T3}', 
	 lhablock = 'MSOFT', 
	 lhacode = [42] ) 
 
LAMS = 	 Parameter(name='LAMS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{LAMS}', 
	 lhablock = 'HLAM', 
	 lhacode = [6] ) 
 
TS = 	 Parameter(name='TS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{TS}', 
	 lhablock = 'MSOFT', 
	 lhacode = [43] ) 
 
VS = 	 Parameter(name='VS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VS}', 
	 lhablock = 'VEVS', 
	 lhacode = [7] ) 
 
V1R = 	 Parameter(name='V1R', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{V1R}', 
	 lhablock = 'VEVS', 
	 lhacode = [4] ) 
 
V2R = 	 Parameter(name='V2R', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{V2R}', 
	 lhablock = 'VEVS', 
	 lhacode = [5] ) 
 
rZZ11 = 	 Parameter(name='rZZ11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ11}', 
	 lhablock = 'ZZMIX', 
	 lhacode = [1, 1] ) 
 
iZZ11 = 	 Parameter(name='iZZ11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ11}', 
	 lhablock = 'IMZZMIX', 
	 lhacode = [1, 1] ) 
 
rZZ12 = 	 Parameter(name='rZZ12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ12}', 
	 lhablock = 'ZZMIX', 
	 lhacode = [1, 2] ) 
 
iZZ12 = 	 Parameter(name='iZZ12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ12}', 
	 lhablock = 'IMZZMIX', 
	 lhacode = [1, 2] ) 
 
rZZ13 = 	 Parameter(name='rZZ13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ13}', 
	 lhablock = 'ZZMIX', 
	 lhacode = [1, 3] ) 
 
iZZ13 = 	 Parameter(name='iZZ13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ13}', 
	 lhablock = 'IMZZMIX', 
	 lhacode = [1, 3] ) 
 
rZZ21 = 	 Parameter(name='rZZ21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ21}', 
	 lhablock = 'ZZMIX', 
	 lhacode = [2, 1] ) 
 
iZZ21 = 	 Parameter(name='iZZ21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ21}', 
	 lhablock = 'IMZZMIX', 
	 lhacode = [2, 1] ) 
 
rZZ22 = 	 Parameter(name='rZZ22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ22}', 
	 lhablock = 'ZZMIX', 
	 lhacode = [2, 2] ) 
 
iZZ22 = 	 Parameter(name='iZZ22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ22}', 
	 lhablock = 'IMZZMIX', 
	 lhacode = [2, 2] ) 
 
rZZ23 = 	 Parameter(name='rZZ23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ23}', 
	 lhablock = 'ZZMIX', 
	 lhacode = [2, 3] ) 
 
iZZ23 = 	 Parameter(name='iZZ23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ23}', 
	 lhablock = 'IMZZMIX', 
	 lhacode = [2, 3] ) 
 
rZZ31 = 	 Parameter(name='rZZ31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ31}', 
	 lhablock = 'ZZMIX', 
	 lhacode = [3, 1] ) 
 
iZZ31 = 	 Parameter(name='iZZ31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ31}', 
	 lhablock = 'IMZZMIX', 
	 lhacode = [3, 1] ) 
 
rZZ32 = 	 Parameter(name='rZZ32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ32}', 
	 lhablock = 'ZZMIX', 
	 lhacode = [3, 2] ) 
 
iZZ32 = 	 Parameter(name='iZZ32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ32}', 
	 lhablock = 'IMZZMIX', 
	 lhacode = [3, 2] ) 
 
rZZ33 = 	 Parameter(name='rZZ33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ33}', 
	 lhablock = 'ZZMIX', 
	 lhacode = [3, 3] ) 
 
iZZ33 = 	 Parameter(name='iZZ33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZZ33}', 
	 lhablock = 'IMZZMIX', 
	 lhacode = [3, 3] ) 
 
rNN1k1 = 	 Parameter(name='rNN1k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 1] ) 
 
iNN1k1 = 	 Parameter(name='iNN1k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 1] ) 
 
rNN1k2 = 	 Parameter(name='rNN1k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 2] ) 
 
iNN1k2 = 	 Parameter(name='iNN1k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 2] ) 
 
rNN1k3 = 	 Parameter(name='rNN1k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 3] ) 
 
iNN1k3 = 	 Parameter(name='iNN1k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 3] ) 
 
rNN1k4 = 	 Parameter(name='rNN1k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 4] ) 
 
iNN1k4 = 	 Parameter(name='iNN1k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 4] ) 
 
rNN1k5 = 	 Parameter(name='rNN1k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 5] ) 
 
iNN1k5 = 	 Parameter(name='iNN1k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 5] ) 
 
rNN1k6 = 	 Parameter(name='rNN1k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 6] ) 
 
iNN1k6 = 	 Parameter(name='iNN1k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 6] ) 
 
rNN1k7 = 	 Parameter(name='rNN1k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 7] ) 
 
iNN1k7 = 	 Parameter(name='iNN1k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 7] ) 
 
rNN1k8 = 	 Parameter(name='rNN1k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 8] ) 
 
iNN1k8 = 	 Parameter(name='iNN1k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 8] ) 
 
rNN1k9 = 	 Parameter(name='rNN1k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 9] ) 
 
iNN1k9 = 	 Parameter(name='iNN1k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 9] ) 
 
rNN1k10 = 	 Parameter(name='rNN1k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 10] ) 
 
iNN1k10 = 	 Parameter(name='iNN1k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 10] ) 
 
rNN1k11 = 	 Parameter(name='rNN1k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 11] ) 
 
iNN1k11 = 	 Parameter(name='iNN1k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 11] ) 
 
rNN1k12 = 	 Parameter(name='rNN1k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [1, 12] ) 
 
iNN1k12 = 	 Parameter(name='iNN1k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN1k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [1, 12] ) 
 
rNN2k1 = 	 Parameter(name='rNN2k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 1] ) 
 
iNN2k1 = 	 Parameter(name='iNN2k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 1] ) 
 
rNN2k2 = 	 Parameter(name='rNN2k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 2] ) 
 
iNN2k2 = 	 Parameter(name='iNN2k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 2] ) 
 
rNN2k3 = 	 Parameter(name='rNN2k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 3] ) 
 
iNN2k3 = 	 Parameter(name='iNN2k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 3] ) 
 
rNN2k4 = 	 Parameter(name='rNN2k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 4] ) 
 
iNN2k4 = 	 Parameter(name='iNN2k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 4] ) 
 
rNN2k5 = 	 Parameter(name='rNN2k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 5] ) 
 
iNN2k5 = 	 Parameter(name='iNN2k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 5] ) 
 
rNN2k6 = 	 Parameter(name='rNN2k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 6] ) 
 
iNN2k6 = 	 Parameter(name='iNN2k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 6] ) 
 
rNN2k7 = 	 Parameter(name='rNN2k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 7] ) 
 
iNN2k7 = 	 Parameter(name='iNN2k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 7] ) 
 
rNN2k8 = 	 Parameter(name='rNN2k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 8] ) 
 
iNN2k8 = 	 Parameter(name='iNN2k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 8] ) 
 
rNN2k9 = 	 Parameter(name='rNN2k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 9] ) 
 
iNN2k9 = 	 Parameter(name='iNN2k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 9] ) 
 
rNN2k10 = 	 Parameter(name='rNN2k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 10] ) 
 
iNN2k10 = 	 Parameter(name='iNN2k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 10] ) 
 
rNN2k11 = 	 Parameter(name='rNN2k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 11] ) 
 
iNN2k11 = 	 Parameter(name='iNN2k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 11] ) 
 
rNN2k12 = 	 Parameter(name='rNN2k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [2, 12] ) 
 
iNN2k12 = 	 Parameter(name='iNN2k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN2k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [2, 12] ) 
 
rNN3k1 = 	 Parameter(name='rNN3k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 1] ) 
 
iNN3k1 = 	 Parameter(name='iNN3k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 1] ) 
 
rNN3k2 = 	 Parameter(name='rNN3k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 2] ) 
 
iNN3k2 = 	 Parameter(name='iNN3k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 2] ) 
 
rNN3k3 = 	 Parameter(name='rNN3k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 3] ) 
 
iNN3k3 = 	 Parameter(name='iNN3k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 3] ) 
 
rNN3k4 = 	 Parameter(name='rNN3k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 4] ) 
 
iNN3k4 = 	 Parameter(name='iNN3k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 4] ) 
 
rNN3k5 = 	 Parameter(name='rNN3k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 5] ) 
 
iNN3k5 = 	 Parameter(name='iNN3k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 5] ) 
 
rNN3k6 = 	 Parameter(name='rNN3k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 6] ) 
 
iNN3k6 = 	 Parameter(name='iNN3k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 6] ) 
 
rNN3k7 = 	 Parameter(name='rNN3k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 7] ) 
 
iNN3k7 = 	 Parameter(name='iNN3k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 7] ) 
 
rNN3k8 = 	 Parameter(name='rNN3k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 8] ) 
 
iNN3k8 = 	 Parameter(name='iNN3k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 8] ) 
 
rNN3k9 = 	 Parameter(name='rNN3k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 9] ) 
 
iNN3k9 = 	 Parameter(name='iNN3k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 9] ) 
 
rNN3k10 = 	 Parameter(name='rNN3k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 10] ) 
 
iNN3k10 = 	 Parameter(name='iNN3k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 10] ) 
 
rNN3k11 = 	 Parameter(name='rNN3k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 11] ) 
 
iNN3k11 = 	 Parameter(name='iNN3k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 11] ) 
 
rNN3k12 = 	 Parameter(name='rNN3k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [3, 12] ) 
 
iNN3k12 = 	 Parameter(name='iNN3k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN3k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [3, 12] ) 
 
rNN4k1 = 	 Parameter(name='rNN4k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 1] ) 
 
iNN4k1 = 	 Parameter(name='iNN4k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 1] ) 
 
rNN4k2 = 	 Parameter(name='rNN4k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 2] ) 
 
iNN4k2 = 	 Parameter(name='iNN4k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 2] ) 
 
rNN4k3 = 	 Parameter(name='rNN4k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 3] ) 
 
iNN4k3 = 	 Parameter(name='iNN4k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 3] ) 
 
rNN4k4 = 	 Parameter(name='rNN4k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 4] ) 
 
iNN4k4 = 	 Parameter(name='iNN4k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 4] ) 
 
rNN4k5 = 	 Parameter(name='rNN4k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 5] ) 
 
iNN4k5 = 	 Parameter(name='iNN4k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 5] ) 
 
rNN4k6 = 	 Parameter(name='rNN4k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 6] ) 
 
iNN4k6 = 	 Parameter(name='iNN4k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 6] ) 
 
rNN4k7 = 	 Parameter(name='rNN4k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 7] ) 
 
iNN4k7 = 	 Parameter(name='iNN4k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 7] ) 
 
rNN4k8 = 	 Parameter(name='rNN4k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 8] ) 
 
iNN4k8 = 	 Parameter(name='iNN4k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 8] ) 
 
rNN4k9 = 	 Parameter(name='rNN4k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 9] ) 
 
iNN4k9 = 	 Parameter(name='iNN4k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 9] ) 
 
rNN4k10 = 	 Parameter(name='rNN4k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 10] ) 
 
iNN4k10 = 	 Parameter(name='iNN4k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 10] ) 
 
rNN4k11 = 	 Parameter(name='rNN4k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 11] ) 
 
iNN4k11 = 	 Parameter(name='iNN4k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 11] ) 
 
rNN4k12 = 	 Parameter(name='rNN4k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [4, 12] ) 
 
iNN4k12 = 	 Parameter(name='iNN4k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN4k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [4, 12] ) 
 
rNN5k1 = 	 Parameter(name='rNN5k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 1] ) 
 
iNN5k1 = 	 Parameter(name='iNN5k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 1] ) 
 
rNN5k2 = 	 Parameter(name='rNN5k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 2] ) 
 
iNN5k2 = 	 Parameter(name='iNN5k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 2] ) 
 
rNN5k3 = 	 Parameter(name='rNN5k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 3] ) 
 
iNN5k3 = 	 Parameter(name='iNN5k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 3] ) 
 
rNN5k4 = 	 Parameter(name='rNN5k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 4] ) 
 
iNN5k4 = 	 Parameter(name='iNN5k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 4] ) 
 
rNN5k5 = 	 Parameter(name='rNN5k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 5] ) 
 
iNN5k5 = 	 Parameter(name='iNN5k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 5] ) 
 
rNN5k6 = 	 Parameter(name='rNN5k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 6] ) 
 
iNN5k6 = 	 Parameter(name='iNN5k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 6] ) 
 
rNN5k7 = 	 Parameter(name='rNN5k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 7] ) 
 
iNN5k7 = 	 Parameter(name='iNN5k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 7] ) 
 
rNN5k8 = 	 Parameter(name='rNN5k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 8] ) 
 
iNN5k8 = 	 Parameter(name='iNN5k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 8] ) 
 
rNN5k9 = 	 Parameter(name='rNN5k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 9] ) 
 
iNN5k9 = 	 Parameter(name='iNN5k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 9] ) 
 
rNN5k10 = 	 Parameter(name='rNN5k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 10] ) 
 
iNN5k10 = 	 Parameter(name='iNN5k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 10] ) 
 
rNN5k11 = 	 Parameter(name='rNN5k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 11] ) 
 
iNN5k11 = 	 Parameter(name='iNN5k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 11] ) 
 
rNN5k12 = 	 Parameter(name='rNN5k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [5, 12] ) 
 
iNN5k12 = 	 Parameter(name='iNN5k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN5k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [5, 12] ) 
 
rNN6k1 = 	 Parameter(name='rNN6k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 1] ) 
 
iNN6k1 = 	 Parameter(name='iNN6k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 1] ) 
 
rNN6k2 = 	 Parameter(name='rNN6k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 2] ) 
 
iNN6k2 = 	 Parameter(name='iNN6k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 2] ) 
 
rNN6k3 = 	 Parameter(name='rNN6k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 3] ) 
 
iNN6k3 = 	 Parameter(name='iNN6k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 3] ) 
 
rNN6k4 = 	 Parameter(name='rNN6k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 4] ) 
 
iNN6k4 = 	 Parameter(name='iNN6k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 4] ) 
 
rNN6k5 = 	 Parameter(name='rNN6k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 5] ) 
 
iNN6k5 = 	 Parameter(name='iNN6k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 5] ) 
 
rNN6k6 = 	 Parameter(name='rNN6k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 6] ) 
 
iNN6k6 = 	 Parameter(name='iNN6k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 6] ) 
 
rNN6k7 = 	 Parameter(name='rNN6k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 7] ) 
 
iNN6k7 = 	 Parameter(name='iNN6k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 7] ) 
 
rNN6k8 = 	 Parameter(name='rNN6k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 8] ) 
 
iNN6k8 = 	 Parameter(name='iNN6k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 8] ) 
 
rNN6k9 = 	 Parameter(name='rNN6k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 9] ) 
 
iNN6k9 = 	 Parameter(name='iNN6k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 9] ) 
 
rNN6k10 = 	 Parameter(name='rNN6k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 10] ) 
 
iNN6k10 = 	 Parameter(name='iNN6k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 10] ) 
 
rNN6k11 = 	 Parameter(name='rNN6k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 11] ) 
 
iNN6k11 = 	 Parameter(name='iNN6k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 11] ) 
 
rNN6k12 = 	 Parameter(name='rNN6k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [6, 12] ) 
 
iNN6k12 = 	 Parameter(name='iNN6k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN6k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [6, 12] ) 
 
rNN7k1 = 	 Parameter(name='rNN7k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 1] ) 
 
iNN7k1 = 	 Parameter(name='iNN7k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 1] ) 
 
rNN7k2 = 	 Parameter(name='rNN7k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 2] ) 
 
iNN7k2 = 	 Parameter(name='iNN7k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 2] ) 
 
rNN7k3 = 	 Parameter(name='rNN7k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 3] ) 
 
iNN7k3 = 	 Parameter(name='iNN7k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 3] ) 
 
rNN7k4 = 	 Parameter(name='rNN7k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 4] ) 
 
iNN7k4 = 	 Parameter(name='iNN7k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 4] ) 
 
rNN7k5 = 	 Parameter(name='rNN7k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 5] ) 
 
iNN7k5 = 	 Parameter(name='iNN7k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 5] ) 
 
rNN7k6 = 	 Parameter(name='rNN7k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 6] ) 
 
iNN7k6 = 	 Parameter(name='iNN7k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 6] ) 
 
rNN7k7 = 	 Parameter(name='rNN7k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 7] ) 
 
iNN7k7 = 	 Parameter(name='iNN7k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 7] ) 
 
rNN7k8 = 	 Parameter(name='rNN7k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 8] ) 
 
iNN7k8 = 	 Parameter(name='iNN7k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 8] ) 
 
rNN7k9 = 	 Parameter(name='rNN7k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 9] ) 
 
iNN7k9 = 	 Parameter(name='iNN7k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 9] ) 
 
rNN7k10 = 	 Parameter(name='rNN7k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 10] ) 
 
iNN7k10 = 	 Parameter(name='iNN7k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 10] ) 
 
rNN7k11 = 	 Parameter(name='rNN7k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 11] ) 
 
iNN7k11 = 	 Parameter(name='iNN7k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 11] ) 
 
rNN7k12 = 	 Parameter(name='rNN7k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [7, 12] ) 
 
iNN7k12 = 	 Parameter(name='iNN7k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN7k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [7, 12] ) 
 
rNN8k1 = 	 Parameter(name='rNN8k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 1] ) 
 
iNN8k1 = 	 Parameter(name='iNN8k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 1] ) 
 
rNN8k2 = 	 Parameter(name='rNN8k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 2] ) 
 
iNN8k2 = 	 Parameter(name='iNN8k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 2] ) 
 
rNN8k3 = 	 Parameter(name='rNN8k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 3] ) 
 
iNN8k3 = 	 Parameter(name='iNN8k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 3] ) 
 
rNN8k4 = 	 Parameter(name='rNN8k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 4] ) 
 
iNN8k4 = 	 Parameter(name='iNN8k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 4] ) 
 
rNN8k5 = 	 Parameter(name='rNN8k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 5] ) 
 
iNN8k5 = 	 Parameter(name='iNN8k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 5] ) 
 
rNN8k6 = 	 Parameter(name='rNN8k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 6] ) 
 
iNN8k6 = 	 Parameter(name='iNN8k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 6] ) 
 
rNN8k7 = 	 Parameter(name='rNN8k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 7] ) 
 
iNN8k7 = 	 Parameter(name='iNN8k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 7] ) 
 
rNN8k8 = 	 Parameter(name='rNN8k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 8] ) 
 
iNN8k8 = 	 Parameter(name='iNN8k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 8] ) 
 
rNN8k9 = 	 Parameter(name='rNN8k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 9] ) 
 
iNN8k9 = 	 Parameter(name='iNN8k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 9] ) 
 
rNN8k10 = 	 Parameter(name='rNN8k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 10] ) 
 
iNN8k10 = 	 Parameter(name='iNN8k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 10] ) 
 
rNN8k11 = 	 Parameter(name='rNN8k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 11] ) 
 
iNN8k11 = 	 Parameter(name='iNN8k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 11] ) 
 
rNN8k12 = 	 Parameter(name='rNN8k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [8, 12] ) 
 
iNN8k12 = 	 Parameter(name='iNN8k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN8k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [8, 12] ) 
 
rNN9k1 = 	 Parameter(name='rNN9k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 1] ) 
 
iNN9k1 = 	 Parameter(name='iNN9k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 1] ) 
 
rNN9k2 = 	 Parameter(name='rNN9k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 2] ) 
 
iNN9k2 = 	 Parameter(name='iNN9k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 2] ) 
 
rNN9k3 = 	 Parameter(name='rNN9k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 3] ) 
 
iNN9k3 = 	 Parameter(name='iNN9k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 3] ) 
 
rNN9k4 = 	 Parameter(name='rNN9k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 4] ) 
 
iNN9k4 = 	 Parameter(name='iNN9k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 4] ) 
 
rNN9k5 = 	 Parameter(name='rNN9k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 5] ) 
 
iNN9k5 = 	 Parameter(name='iNN9k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 5] ) 
 
rNN9k6 = 	 Parameter(name='rNN9k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 6] ) 
 
iNN9k6 = 	 Parameter(name='iNN9k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 6] ) 
 
rNN9k7 = 	 Parameter(name='rNN9k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 7] ) 
 
iNN9k7 = 	 Parameter(name='iNN9k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 7] ) 
 
rNN9k8 = 	 Parameter(name='rNN9k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 8] ) 
 
iNN9k8 = 	 Parameter(name='iNN9k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 8] ) 
 
rNN9k9 = 	 Parameter(name='rNN9k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 9] ) 
 
iNN9k9 = 	 Parameter(name='iNN9k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 9] ) 
 
rNN9k10 = 	 Parameter(name='rNN9k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 10] ) 
 
iNN9k10 = 	 Parameter(name='iNN9k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 10] ) 
 
rNN9k11 = 	 Parameter(name='rNN9k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 11] ) 
 
iNN9k11 = 	 Parameter(name='iNN9k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 11] ) 
 
rNN9k12 = 	 Parameter(name='rNN9k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [9, 12] ) 
 
iNN9k12 = 	 Parameter(name='iNN9k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN9k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [9, 12] ) 
 
rNN10k1 = 	 Parameter(name='rNN10k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 1] ) 
 
iNN10k1 = 	 Parameter(name='iNN10k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 1] ) 
 
rNN10k2 = 	 Parameter(name='rNN10k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 2] ) 
 
iNN10k2 = 	 Parameter(name='iNN10k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 2] ) 
 
rNN10k3 = 	 Parameter(name='rNN10k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 3] ) 
 
iNN10k3 = 	 Parameter(name='iNN10k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 3] ) 
 
rNN10k4 = 	 Parameter(name='rNN10k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 4] ) 
 
iNN10k4 = 	 Parameter(name='iNN10k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 4] ) 
 
rNN10k5 = 	 Parameter(name='rNN10k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 5] ) 
 
iNN10k5 = 	 Parameter(name='iNN10k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 5] ) 
 
rNN10k6 = 	 Parameter(name='rNN10k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 6] ) 
 
iNN10k6 = 	 Parameter(name='iNN10k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 6] ) 
 
rNN10k7 = 	 Parameter(name='rNN10k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 7] ) 
 
iNN10k7 = 	 Parameter(name='iNN10k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 7] ) 
 
rNN10k8 = 	 Parameter(name='rNN10k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 8] ) 
 
iNN10k8 = 	 Parameter(name='iNN10k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 8] ) 
 
rNN10k9 = 	 Parameter(name='rNN10k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 9] ) 
 
iNN10k9 = 	 Parameter(name='iNN10k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 9] ) 
 
rNN10k10 = 	 Parameter(name='rNN10k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 10] ) 
 
iNN10k10 = 	 Parameter(name='iNN10k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 10] ) 
 
rNN10k11 = 	 Parameter(name='rNN10k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 11] ) 
 
iNN10k11 = 	 Parameter(name='iNN10k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 11] ) 
 
rNN10k12 = 	 Parameter(name='rNN10k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [10, 12] ) 
 
iNN10k12 = 	 Parameter(name='iNN10k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN10k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [10, 12] ) 
 
rNN11k1 = 	 Parameter(name='rNN11k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 1] ) 
 
iNN11k1 = 	 Parameter(name='iNN11k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 1] ) 
 
rNN11k2 = 	 Parameter(name='rNN11k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 2] ) 
 
iNN11k2 = 	 Parameter(name='iNN11k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 2] ) 
 
rNN11k3 = 	 Parameter(name='rNN11k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 3] ) 
 
iNN11k3 = 	 Parameter(name='iNN11k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 3] ) 
 
rNN11k4 = 	 Parameter(name='rNN11k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 4] ) 
 
iNN11k4 = 	 Parameter(name='iNN11k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 4] ) 
 
rNN11k5 = 	 Parameter(name='rNN11k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 5] ) 
 
iNN11k5 = 	 Parameter(name='iNN11k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 5] ) 
 
rNN11k6 = 	 Parameter(name='rNN11k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 6] ) 
 
iNN11k6 = 	 Parameter(name='iNN11k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 6] ) 
 
rNN11k7 = 	 Parameter(name='rNN11k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 7] ) 
 
iNN11k7 = 	 Parameter(name='iNN11k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 7] ) 
 
rNN11k8 = 	 Parameter(name='rNN11k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 8] ) 
 
iNN11k8 = 	 Parameter(name='iNN11k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 8] ) 
 
rNN11k9 = 	 Parameter(name='rNN11k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 9] ) 
 
iNN11k9 = 	 Parameter(name='iNN11k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 9] ) 
 
rNN11k10 = 	 Parameter(name='rNN11k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 10] ) 
 
iNN11k10 = 	 Parameter(name='iNN11k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 10] ) 
 
rNN11k11 = 	 Parameter(name='rNN11k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 11] ) 
 
iNN11k11 = 	 Parameter(name='iNN11k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 11] ) 
 
rNN11k12 = 	 Parameter(name='rNN11k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [11, 12] ) 
 
iNN11k12 = 	 Parameter(name='iNN11k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN11k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [11, 12] ) 
 
rNN12k1 = 	 Parameter(name='rNN12k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k1}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 1] ) 
 
iNN12k1 = 	 Parameter(name='iNN12k1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k1}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 1] ) 
 
rNN12k2 = 	 Parameter(name='rNN12k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k2}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 2] ) 
 
iNN12k2 = 	 Parameter(name='iNN12k2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k2}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 2] ) 
 
rNN12k3 = 	 Parameter(name='rNN12k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k3}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 3] ) 
 
iNN12k3 = 	 Parameter(name='iNN12k3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k3}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 3] ) 
 
rNN12k4 = 	 Parameter(name='rNN12k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k4}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 4] ) 
 
iNN12k4 = 	 Parameter(name='iNN12k4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k4}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 4] ) 
 
rNN12k5 = 	 Parameter(name='rNN12k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k5}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 5] ) 
 
iNN12k5 = 	 Parameter(name='iNN12k5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k5}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 5] ) 
 
rNN12k6 = 	 Parameter(name='rNN12k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k6}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 6] ) 
 
iNN12k6 = 	 Parameter(name='iNN12k6', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k6}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 6] ) 
 
rNN12k7 = 	 Parameter(name='rNN12k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k7}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 7] ) 
 
iNN12k7 = 	 Parameter(name='iNN12k7', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k7}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 7] ) 
 
rNN12k8 = 	 Parameter(name='rNN12k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k8}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 8] ) 
 
iNN12k8 = 	 Parameter(name='iNN12k8', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k8}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 8] ) 
 
rNN12k9 = 	 Parameter(name='rNN12k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k9}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 9] ) 
 
iNN12k9 = 	 Parameter(name='iNN12k9', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k9}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 9] ) 
 
rNN12k10 = 	 Parameter(name='rNN12k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k10}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 10] ) 
 
iNN12k10 = 	 Parameter(name='iNN12k10', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k10}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 10] ) 
 
rNN12k11 = 	 Parameter(name='rNN12k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k11}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 11] ) 
 
iNN12k11 = 	 Parameter(name='iNN12k11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k11}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 11] ) 
 
rNN12k12 = 	 Parameter(name='rNN12k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k12}', 
	 lhablock = 'NMIX', 
	 lhacode = [12, 12] ) 
 
iNN12k12 = 	 Parameter(name='iNN12k12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{NN12k12}', 
	 lhablock = 'IMNMIX', 
	 lhacode = [12, 12] ) 
 
rUU11 = 	 Parameter(name='rUU11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU11}', 
	 lhablock = 'UMIX', 
	 lhacode = [1, 1] ) 
 
iUU11 = 	 Parameter(name='iUU11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU11}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [1, 1] ) 
 
rUU12 = 	 Parameter(name='rUU12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU12}', 
	 lhablock = 'UMIX', 
	 lhacode = [1, 2] ) 
 
iUU12 = 	 Parameter(name='iUU12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU12}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [1, 2] ) 
 
rUU13 = 	 Parameter(name='rUU13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU13}', 
	 lhablock = 'UMIX', 
	 lhacode = [1, 3] ) 
 
iUU13 = 	 Parameter(name='iUU13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU13}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [1, 3] ) 
 
rUU14 = 	 Parameter(name='rUU14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU14}', 
	 lhablock = 'UMIX', 
	 lhacode = [1, 4] ) 
 
iUU14 = 	 Parameter(name='iUU14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU14}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [1, 4] ) 
 
rUU15 = 	 Parameter(name='rUU15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU15}', 
	 lhablock = 'UMIX', 
	 lhacode = [1, 5] ) 
 
iUU15 = 	 Parameter(name='iUU15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU15}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [1, 5] ) 
 
rUU16 = 	 Parameter(name='rUU16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU16}', 
	 lhablock = 'UMIX', 
	 lhacode = [1, 6] ) 
 
iUU16 = 	 Parameter(name='iUU16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU16}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [1, 6] ) 
 
rUU21 = 	 Parameter(name='rUU21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU21}', 
	 lhablock = 'UMIX', 
	 lhacode = [2, 1] ) 
 
iUU21 = 	 Parameter(name='iUU21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU21}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [2, 1] ) 
 
rUU22 = 	 Parameter(name='rUU22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU22}', 
	 lhablock = 'UMIX', 
	 lhacode = [2, 2] ) 
 
iUU22 = 	 Parameter(name='iUU22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU22}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [2, 2] ) 
 
rUU23 = 	 Parameter(name='rUU23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU23}', 
	 lhablock = 'UMIX', 
	 lhacode = [2, 3] ) 
 
iUU23 = 	 Parameter(name='iUU23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU23}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [2, 3] ) 
 
rUU24 = 	 Parameter(name='rUU24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU24}', 
	 lhablock = 'UMIX', 
	 lhacode = [2, 4] ) 
 
iUU24 = 	 Parameter(name='iUU24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU24}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [2, 4] ) 
 
rUU25 = 	 Parameter(name='rUU25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU25}', 
	 lhablock = 'UMIX', 
	 lhacode = [2, 5] ) 
 
iUU25 = 	 Parameter(name='iUU25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU25}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [2, 5] ) 
 
rUU26 = 	 Parameter(name='rUU26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU26}', 
	 lhablock = 'UMIX', 
	 lhacode = [2, 6] ) 
 
iUU26 = 	 Parameter(name='iUU26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU26}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [2, 6] ) 
 
rUU31 = 	 Parameter(name='rUU31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU31}', 
	 lhablock = 'UMIX', 
	 lhacode = [3, 1] ) 
 
iUU31 = 	 Parameter(name='iUU31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU31}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [3, 1] ) 
 
rUU32 = 	 Parameter(name='rUU32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU32}', 
	 lhablock = 'UMIX', 
	 lhacode = [3, 2] ) 
 
iUU32 = 	 Parameter(name='iUU32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU32}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [3, 2] ) 
 
rUU33 = 	 Parameter(name='rUU33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU33}', 
	 lhablock = 'UMIX', 
	 lhacode = [3, 3] ) 
 
iUU33 = 	 Parameter(name='iUU33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU33}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [3, 3] ) 
 
rUU34 = 	 Parameter(name='rUU34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU34}', 
	 lhablock = 'UMIX', 
	 lhacode = [3, 4] ) 
 
iUU34 = 	 Parameter(name='iUU34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU34}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [3, 4] ) 
 
rUU35 = 	 Parameter(name='rUU35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU35}', 
	 lhablock = 'UMIX', 
	 lhacode = [3, 5] ) 
 
iUU35 = 	 Parameter(name='iUU35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU35}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [3, 5] ) 
 
rUU36 = 	 Parameter(name='rUU36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU36}', 
	 lhablock = 'UMIX', 
	 lhacode = [3, 6] ) 
 
iUU36 = 	 Parameter(name='iUU36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU36}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [3, 6] ) 
 
rUU41 = 	 Parameter(name='rUU41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU41}', 
	 lhablock = 'UMIX', 
	 lhacode = [4, 1] ) 
 
iUU41 = 	 Parameter(name='iUU41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU41}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [4, 1] ) 
 
rUU42 = 	 Parameter(name='rUU42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU42}', 
	 lhablock = 'UMIX', 
	 lhacode = [4, 2] ) 
 
iUU42 = 	 Parameter(name='iUU42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU42}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [4, 2] ) 
 
rUU43 = 	 Parameter(name='rUU43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU43}', 
	 lhablock = 'UMIX', 
	 lhacode = [4, 3] ) 
 
iUU43 = 	 Parameter(name='iUU43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU43}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [4, 3] ) 
 
rUU44 = 	 Parameter(name='rUU44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU44}', 
	 lhablock = 'UMIX', 
	 lhacode = [4, 4] ) 
 
iUU44 = 	 Parameter(name='iUU44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU44}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [4, 4] ) 
 
rUU45 = 	 Parameter(name='rUU45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU45}', 
	 lhablock = 'UMIX', 
	 lhacode = [4, 5] ) 
 
iUU45 = 	 Parameter(name='iUU45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU45}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [4, 5] ) 
 
rUU46 = 	 Parameter(name='rUU46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU46}', 
	 lhablock = 'UMIX', 
	 lhacode = [4, 6] ) 
 
iUU46 = 	 Parameter(name='iUU46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU46}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [4, 6] ) 
 
rUU51 = 	 Parameter(name='rUU51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU51}', 
	 lhablock = 'UMIX', 
	 lhacode = [5, 1] ) 
 
iUU51 = 	 Parameter(name='iUU51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU51}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [5, 1] ) 
 
rUU52 = 	 Parameter(name='rUU52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU52}', 
	 lhablock = 'UMIX', 
	 lhacode = [5, 2] ) 
 
iUU52 = 	 Parameter(name='iUU52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU52}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [5, 2] ) 
 
rUU53 = 	 Parameter(name='rUU53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU53}', 
	 lhablock = 'UMIX', 
	 lhacode = [5, 3] ) 
 
iUU53 = 	 Parameter(name='iUU53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU53}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [5, 3] ) 
 
rUU54 = 	 Parameter(name='rUU54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU54}', 
	 lhablock = 'UMIX', 
	 lhacode = [5, 4] ) 
 
iUU54 = 	 Parameter(name='iUU54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU54}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [5, 4] ) 
 
rUU55 = 	 Parameter(name='rUU55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU55}', 
	 lhablock = 'UMIX', 
	 lhacode = [5, 5] ) 
 
iUU55 = 	 Parameter(name='iUU55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU55}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [5, 5] ) 
 
rUU56 = 	 Parameter(name='rUU56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU56}', 
	 lhablock = 'UMIX', 
	 lhacode = [5, 6] ) 
 
iUU56 = 	 Parameter(name='iUU56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU56}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [5, 6] ) 
 
rUU61 = 	 Parameter(name='rUU61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU61}', 
	 lhablock = 'UMIX', 
	 lhacode = [6, 1] ) 
 
iUU61 = 	 Parameter(name='iUU61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU61}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [6, 1] ) 
 
rUU62 = 	 Parameter(name='rUU62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU62}', 
	 lhablock = 'UMIX', 
	 lhacode = [6, 2] ) 
 
iUU62 = 	 Parameter(name='iUU62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU62}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [6, 2] ) 
 
rUU63 = 	 Parameter(name='rUU63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU63}', 
	 lhablock = 'UMIX', 
	 lhacode = [6, 3] ) 
 
iUU63 = 	 Parameter(name='iUU63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU63}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [6, 3] ) 
 
rUU64 = 	 Parameter(name='rUU64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU64}', 
	 lhablock = 'UMIX', 
	 lhacode = [6, 4] ) 
 
iUU64 = 	 Parameter(name='iUU64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU64}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [6, 4] ) 
 
rUU65 = 	 Parameter(name='rUU65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU65}', 
	 lhablock = 'UMIX', 
	 lhacode = [6, 5] ) 
 
iUU65 = 	 Parameter(name='iUU65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU65}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [6, 5] ) 
 
rUU66 = 	 Parameter(name='rUU66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU66}', 
	 lhablock = 'UMIX', 
	 lhacode = [6, 6] ) 
 
iUU66 = 	 Parameter(name='iUU66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UU66}', 
	 lhablock = 'IMUMIX', 
	 lhacode = [6, 6] ) 
 
rVV11 = 	 Parameter(name='rVV11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV11}', 
	 lhablock = 'VMIX', 
	 lhacode = [1, 1] ) 
 
iVV11 = 	 Parameter(name='iVV11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV11}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [1, 1] ) 
 
rVV12 = 	 Parameter(name='rVV12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV12}', 
	 lhablock = 'VMIX', 
	 lhacode = [1, 2] ) 
 
iVV12 = 	 Parameter(name='iVV12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV12}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [1, 2] ) 
 
rVV13 = 	 Parameter(name='rVV13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV13}', 
	 lhablock = 'VMIX', 
	 lhacode = [1, 3] ) 
 
iVV13 = 	 Parameter(name='iVV13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV13}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [1, 3] ) 
 
rVV14 = 	 Parameter(name='rVV14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV14}', 
	 lhablock = 'VMIX', 
	 lhacode = [1, 4] ) 
 
iVV14 = 	 Parameter(name='iVV14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV14}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [1, 4] ) 
 
rVV15 = 	 Parameter(name='rVV15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV15}', 
	 lhablock = 'VMIX', 
	 lhacode = [1, 5] ) 
 
iVV15 = 	 Parameter(name='iVV15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV15}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [1, 5] ) 
 
rVV16 = 	 Parameter(name='rVV16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV16}', 
	 lhablock = 'VMIX', 
	 lhacode = [1, 6] ) 
 
iVV16 = 	 Parameter(name='iVV16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV16}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [1, 6] ) 
 
rVV21 = 	 Parameter(name='rVV21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV21}', 
	 lhablock = 'VMIX', 
	 lhacode = [2, 1] ) 
 
iVV21 = 	 Parameter(name='iVV21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV21}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [2, 1] ) 
 
rVV22 = 	 Parameter(name='rVV22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV22}', 
	 lhablock = 'VMIX', 
	 lhacode = [2, 2] ) 
 
iVV22 = 	 Parameter(name='iVV22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV22}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [2, 2] ) 
 
rVV23 = 	 Parameter(name='rVV23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV23}', 
	 lhablock = 'VMIX', 
	 lhacode = [2, 3] ) 
 
iVV23 = 	 Parameter(name='iVV23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV23}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [2, 3] ) 
 
rVV24 = 	 Parameter(name='rVV24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV24}', 
	 lhablock = 'VMIX', 
	 lhacode = [2, 4] ) 
 
iVV24 = 	 Parameter(name='iVV24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV24}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [2, 4] ) 
 
rVV25 = 	 Parameter(name='rVV25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV25}', 
	 lhablock = 'VMIX', 
	 lhacode = [2, 5] ) 
 
iVV25 = 	 Parameter(name='iVV25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV25}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [2, 5] ) 
 
rVV26 = 	 Parameter(name='rVV26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV26}', 
	 lhablock = 'VMIX', 
	 lhacode = [2, 6] ) 
 
iVV26 = 	 Parameter(name='iVV26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV26}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [2, 6] ) 
 
rVV31 = 	 Parameter(name='rVV31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV31}', 
	 lhablock = 'VMIX', 
	 lhacode = [3, 1] ) 
 
iVV31 = 	 Parameter(name='iVV31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV31}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [3, 1] ) 
 
rVV32 = 	 Parameter(name='rVV32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV32}', 
	 lhablock = 'VMIX', 
	 lhacode = [3, 2] ) 
 
iVV32 = 	 Parameter(name='iVV32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV32}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [3, 2] ) 
 
rVV33 = 	 Parameter(name='rVV33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV33}', 
	 lhablock = 'VMIX', 
	 lhacode = [3, 3] ) 
 
iVV33 = 	 Parameter(name='iVV33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV33}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [3, 3] ) 
 
rVV34 = 	 Parameter(name='rVV34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV34}', 
	 lhablock = 'VMIX', 
	 lhacode = [3, 4] ) 
 
iVV34 = 	 Parameter(name='iVV34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV34}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [3, 4] ) 
 
rVV35 = 	 Parameter(name='rVV35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV35}', 
	 lhablock = 'VMIX', 
	 lhacode = [3, 5] ) 
 
iVV35 = 	 Parameter(name='iVV35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV35}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [3, 5] ) 
 
rVV36 = 	 Parameter(name='rVV36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV36}', 
	 lhablock = 'VMIX', 
	 lhacode = [3, 6] ) 
 
iVV36 = 	 Parameter(name='iVV36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV36}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [3, 6] ) 
 
rVV41 = 	 Parameter(name='rVV41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV41}', 
	 lhablock = 'VMIX', 
	 lhacode = [4, 1] ) 
 
iVV41 = 	 Parameter(name='iVV41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV41}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [4, 1] ) 
 
rVV42 = 	 Parameter(name='rVV42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV42}', 
	 lhablock = 'VMIX', 
	 lhacode = [4, 2] ) 
 
iVV42 = 	 Parameter(name='iVV42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV42}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [4, 2] ) 
 
rVV43 = 	 Parameter(name='rVV43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV43}', 
	 lhablock = 'VMIX', 
	 lhacode = [4, 3] ) 
 
iVV43 = 	 Parameter(name='iVV43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV43}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [4, 3] ) 
 
rVV44 = 	 Parameter(name='rVV44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV44}', 
	 lhablock = 'VMIX', 
	 lhacode = [4, 4] ) 
 
iVV44 = 	 Parameter(name='iVV44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV44}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [4, 4] ) 
 
rVV45 = 	 Parameter(name='rVV45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV45}', 
	 lhablock = 'VMIX', 
	 lhacode = [4, 5] ) 
 
iVV45 = 	 Parameter(name='iVV45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV45}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [4, 5] ) 
 
rVV46 = 	 Parameter(name='rVV46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV46}', 
	 lhablock = 'VMIX', 
	 lhacode = [4, 6] ) 
 
iVV46 = 	 Parameter(name='iVV46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV46}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [4, 6] ) 
 
rVV51 = 	 Parameter(name='rVV51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV51}', 
	 lhablock = 'VMIX', 
	 lhacode = [5, 1] ) 
 
iVV51 = 	 Parameter(name='iVV51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV51}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [5, 1] ) 
 
rVV52 = 	 Parameter(name='rVV52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV52}', 
	 lhablock = 'VMIX', 
	 lhacode = [5, 2] ) 
 
iVV52 = 	 Parameter(name='iVV52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV52}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [5, 2] ) 
 
rVV53 = 	 Parameter(name='rVV53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV53}', 
	 lhablock = 'VMIX', 
	 lhacode = [5, 3] ) 
 
iVV53 = 	 Parameter(name='iVV53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV53}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [5, 3] ) 
 
rVV54 = 	 Parameter(name='rVV54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV54}', 
	 lhablock = 'VMIX', 
	 lhacode = [5, 4] ) 
 
iVV54 = 	 Parameter(name='iVV54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV54}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [5, 4] ) 
 
rVV55 = 	 Parameter(name='rVV55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV55}', 
	 lhablock = 'VMIX', 
	 lhacode = [5, 5] ) 
 
iVV55 = 	 Parameter(name='iVV55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV55}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [5, 5] ) 
 
rVV56 = 	 Parameter(name='rVV56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV56}', 
	 lhablock = 'VMIX', 
	 lhacode = [5, 6] ) 
 
iVV56 = 	 Parameter(name='iVV56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV56}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [5, 6] ) 
 
rVV61 = 	 Parameter(name='rVV61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV61}', 
	 lhablock = 'VMIX', 
	 lhacode = [6, 1] ) 
 
iVV61 = 	 Parameter(name='iVV61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV61}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [6, 1] ) 
 
rVV62 = 	 Parameter(name='rVV62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV62}', 
	 lhablock = 'VMIX', 
	 lhacode = [6, 2] ) 
 
iVV62 = 	 Parameter(name='iVV62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV62}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [6, 2] ) 
 
rVV63 = 	 Parameter(name='rVV63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV63}', 
	 lhablock = 'VMIX', 
	 lhacode = [6, 3] ) 
 
iVV63 = 	 Parameter(name='iVV63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV63}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [6, 3] ) 
 
rVV64 = 	 Parameter(name='rVV64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV64}', 
	 lhablock = 'VMIX', 
	 lhacode = [6, 4] ) 
 
iVV64 = 	 Parameter(name='iVV64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV64}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [6, 4] ) 
 
rVV65 = 	 Parameter(name='rVV65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV65}', 
	 lhablock = 'VMIX', 
	 lhacode = [6, 5] ) 
 
iVV65 = 	 Parameter(name='iVV65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV65}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [6, 5] ) 
 
rVV66 = 	 Parameter(name='rVV66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV66}', 
	 lhablock = 'VMIX', 
	 lhacode = [6, 6] ) 
 
iVV66 = 	 Parameter(name='iVV66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{VV66}', 
	 lhablock = 'IMVMIX', 
	 lhacode = [6, 6] ) 
 
Rd11 = 	 Parameter(name='Rd11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd11}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [1, 1] ) 
 
Rd12 = 	 Parameter(name='Rd12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd12}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [1, 2] ) 
 
Rd13 = 	 Parameter(name='Rd13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd13}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [1, 3] ) 
 
Rd14 = 	 Parameter(name='Rd14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd14}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [1, 4] ) 
 
Rd15 = 	 Parameter(name='Rd15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd15}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [1, 5] ) 
 
Rd16 = 	 Parameter(name='Rd16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd16}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [1, 6] ) 
 
Rd21 = 	 Parameter(name='Rd21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd21}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [2, 1] ) 
 
Rd22 = 	 Parameter(name='Rd22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd22}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [2, 2] ) 
 
Rd23 = 	 Parameter(name='Rd23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd23}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [2, 3] ) 
 
Rd24 = 	 Parameter(name='Rd24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd24}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [2, 4] ) 
 
Rd25 = 	 Parameter(name='Rd25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd25}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [2, 5] ) 
 
Rd26 = 	 Parameter(name='Rd26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd26}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [2, 6] ) 
 
Rd31 = 	 Parameter(name='Rd31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd31}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [3, 1] ) 
 
Rd32 = 	 Parameter(name='Rd32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd32}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [3, 2] ) 
 
Rd33 = 	 Parameter(name='Rd33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd33}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [3, 3] ) 
 
Rd34 = 	 Parameter(name='Rd34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd34}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [3, 4] ) 
 
Rd35 = 	 Parameter(name='Rd35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd35}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [3, 5] ) 
 
Rd36 = 	 Parameter(name='Rd36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd36}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [3, 6] ) 
 
Rd41 = 	 Parameter(name='Rd41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd41}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [4, 1] ) 
 
Rd42 = 	 Parameter(name='Rd42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd42}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [4, 2] ) 
 
Rd43 = 	 Parameter(name='Rd43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd43}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [4, 3] ) 
 
Rd44 = 	 Parameter(name='Rd44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd44}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [4, 4] ) 
 
Rd45 = 	 Parameter(name='Rd45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd45}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [4, 5] ) 
 
Rd46 = 	 Parameter(name='Rd46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd46}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [4, 6] ) 
 
Rd51 = 	 Parameter(name='Rd51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd51}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [5, 1] ) 
 
Rd52 = 	 Parameter(name='Rd52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd52}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [5, 2] ) 
 
Rd53 = 	 Parameter(name='Rd53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd53}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [5, 3] ) 
 
Rd54 = 	 Parameter(name='Rd54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd54}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [5, 4] ) 
 
Rd55 = 	 Parameter(name='Rd55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd55}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [5, 5] ) 
 
Rd56 = 	 Parameter(name='Rd56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd56}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [5, 6] ) 
 
Rd61 = 	 Parameter(name='Rd61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd61}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [6, 1] ) 
 
Rd62 = 	 Parameter(name='Rd62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd62}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [6, 2] ) 
 
Rd63 = 	 Parameter(name='Rd63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd63}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [6, 3] ) 
 
Rd64 = 	 Parameter(name='Rd64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd64}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [6, 4] ) 
 
Rd65 = 	 Parameter(name='Rd65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd65}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [6, 5] ) 
 
Rd66 = 	 Parameter(name='Rd66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rd66}', 
	 lhablock = 'DSQMIX', 
	 lhacode = [6, 6] ) 
 
Ru11 = 	 Parameter(name='Ru11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru11}', 
	 lhablock = 'USQMIX', 
	 lhacode = [1, 1] ) 
 
Ru12 = 	 Parameter(name='Ru12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru12}', 
	 lhablock = 'USQMIX', 
	 lhacode = [1, 2] ) 
 
Ru13 = 	 Parameter(name='Ru13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru13}', 
	 lhablock = 'USQMIX', 
	 lhacode = [1, 3] ) 
 
Ru14 = 	 Parameter(name='Ru14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru14}', 
	 lhablock = 'USQMIX', 
	 lhacode = [1, 4] ) 
 
Ru15 = 	 Parameter(name='Ru15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru15}', 
	 lhablock = 'USQMIX', 
	 lhacode = [1, 5] ) 
 
Ru16 = 	 Parameter(name='Ru16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru16}', 
	 lhablock = 'USQMIX', 
	 lhacode = [1, 6] ) 
 
Ru21 = 	 Parameter(name='Ru21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru21}', 
	 lhablock = 'USQMIX', 
	 lhacode = [2, 1] ) 
 
Ru22 = 	 Parameter(name='Ru22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru22}', 
	 lhablock = 'USQMIX', 
	 lhacode = [2, 2] ) 
 
Ru23 = 	 Parameter(name='Ru23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru23}', 
	 lhablock = 'USQMIX', 
	 lhacode = [2, 3] ) 
 
Ru24 = 	 Parameter(name='Ru24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru24}', 
	 lhablock = 'USQMIX', 
	 lhacode = [2, 4] ) 
 
Ru25 = 	 Parameter(name='Ru25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru25}', 
	 lhablock = 'USQMIX', 
	 lhacode = [2, 5] ) 
 
Ru26 = 	 Parameter(name='Ru26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru26}', 
	 lhablock = 'USQMIX', 
	 lhacode = [2, 6] ) 
 
Ru31 = 	 Parameter(name='Ru31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru31}', 
	 lhablock = 'USQMIX', 
	 lhacode = [3, 1] ) 
 
Ru32 = 	 Parameter(name='Ru32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru32}', 
	 lhablock = 'USQMIX', 
	 lhacode = [3, 2] ) 
 
Ru33 = 	 Parameter(name='Ru33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru33}', 
	 lhablock = 'USQMIX', 
	 lhacode = [3, 3] ) 
 
Ru34 = 	 Parameter(name='Ru34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru34}', 
	 lhablock = 'USQMIX', 
	 lhacode = [3, 4] ) 
 
Ru35 = 	 Parameter(name='Ru35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru35}', 
	 lhablock = 'USQMIX', 
	 lhacode = [3, 5] ) 
 
Ru36 = 	 Parameter(name='Ru36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru36}', 
	 lhablock = 'USQMIX', 
	 lhacode = [3, 6] ) 
 
Ru41 = 	 Parameter(name='Ru41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru41}', 
	 lhablock = 'USQMIX', 
	 lhacode = [4, 1] ) 
 
Ru42 = 	 Parameter(name='Ru42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru42}', 
	 lhablock = 'USQMIX', 
	 lhacode = [4, 2] ) 
 
Ru43 = 	 Parameter(name='Ru43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru43}', 
	 lhablock = 'USQMIX', 
	 lhacode = [4, 3] ) 
 
Ru44 = 	 Parameter(name='Ru44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru44}', 
	 lhablock = 'USQMIX', 
	 lhacode = [4, 4] ) 
 
Ru45 = 	 Parameter(name='Ru45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru45}', 
	 lhablock = 'USQMIX', 
	 lhacode = [4, 5] ) 
 
Ru46 = 	 Parameter(name='Ru46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru46}', 
	 lhablock = 'USQMIX', 
	 lhacode = [4, 6] ) 
 
Ru51 = 	 Parameter(name='Ru51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru51}', 
	 lhablock = 'USQMIX', 
	 lhacode = [5, 1] ) 
 
Ru52 = 	 Parameter(name='Ru52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru52}', 
	 lhablock = 'USQMIX', 
	 lhacode = [5, 2] ) 
 
Ru53 = 	 Parameter(name='Ru53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru53}', 
	 lhablock = 'USQMIX', 
	 lhacode = [5, 3] ) 
 
Ru54 = 	 Parameter(name='Ru54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru54}', 
	 lhablock = 'USQMIX', 
	 lhacode = [5, 4] ) 
 
Ru55 = 	 Parameter(name='Ru55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru55}', 
	 lhablock = 'USQMIX', 
	 lhacode = [5, 5] ) 
 
Ru56 = 	 Parameter(name='Ru56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru56}', 
	 lhablock = 'USQMIX', 
	 lhacode = [5, 6] ) 
 
Ru61 = 	 Parameter(name='Ru61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru61}', 
	 lhablock = 'USQMIX', 
	 lhacode = [6, 1] ) 
 
Ru62 = 	 Parameter(name='Ru62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru62}', 
	 lhablock = 'USQMIX', 
	 lhacode = [6, 2] ) 
 
Ru63 = 	 Parameter(name='Ru63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru63}', 
	 lhablock = 'USQMIX', 
	 lhacode = [6, 3] ) 
 
Ru64 = 	 Parameter(name='Ru64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru64}', 
	 lhablock = 'USQMIX', 
	 lhacode = [6, 4] ) 
 
Ru65 = 	 Parameter(name='Ru65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru65}', 
	 lhablock = 'USQMIX', 
	 lhacode = [6, 5] ) 
 
Ru66 = 	 Parameter(name='Ru66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Ru66}', 
	 lhablock = 'USQMIX', 
	 lhacode = [6, 6] ) 
 
Rl11 = 	 Parameter(name='Rl11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl11}', 
	 lhablock = 'SELMIX', 
	 lhacode = [1, 1] ) 
 
Rl12 = 	 Parameter(name='Rl12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl12}', 
	 lhablock = 'SELMIX', 
	 lhacode = [1, 2] ) 
 
Rl13 = 	 Parameter(name='Rl13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl13}', 
	 lhablock = 'SELMIX', 
	 lhacode = [1, 3] ) 
 
Rl14 = 	 Parameter(name='Rl14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl14}', 
	 lhablock = 'SELMIX', 
	 lhacode = [1, 4] ) 
 
Rl15 = 	 Parameter(name='Rl15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl15}', 
	 lhablock = 'SELMIX', 
	 lhacode = [1, 5] ) 
 
Rl16 = 	 Parameter(name='Rl16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl16}', 
	 lhablock = 'SELMIX', 
	 lhacode = [1, 6] ) 
 
Rl21 = 	 Parameter(name='Rl21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl21}', 
	 lhablock = 'SELMIX', 
	 lhacode = [2, 1] ) 
 
Rl22 = 	 Parameter(name='Rl22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl22}', 
	 lhablock = 'SELMIX', 
	 lhacode = [2, 2] ) 
 
Rl23 = 	 Parameter(name='Rl23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl23}', 
	 lhablock = 'SELMIX', 
	 lhacode = [2, 3] ) 
 
Rl24 = 	 Parameter(name='Rl24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl24}', 
	 lhablock = 'SELMIX', 
	 lhacode = [2, 4] ) 
 
Rl25 = 	 Parameter(name='Rl25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl25}', 
	 lhablock = 'SELMIX', 
	 lhacode = [2, 5] ) 
 
Rl26 = 	 Parameter(name='Rl26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl26}', 
	 lhablock = 'SELMIX', 
	 lhacode = [2, 6] ) 
 
Rl31 = 	 Parameter(name='Rl31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl31}', 
	 lhablock = 'SELMIX', 
	 lhacode = [3, 1] ) 
 
Rl32 = 	 Parameter(name='Rl32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl32}', 
	 lhablock = 'SELMIX', 
	 lhacode = [3, 2] ) 
 
Rl33 = 	 Parameter(name='Rl33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl33}', 
	 lhablock = 'SELMIX', 
	 lhacode = [3, 3] ) 
 
Rl34 = 	 Parameter(name='Rl34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl34}', 
	 lhablock = 'SELMIX', 
	 lhacode = [3, 4] ) 
 
Rl35 = 	 Parameter(name='Rl35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl35}', 
	 lhablock = 'SELMIX', 
	 lhacode = [3, 5] ) 
 
Rl36 = 	 Parameter(name='Rl36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl36}', 
	 lhablock = 'SELMIX', 
	 lhacode = [3, 6] ) 
 
Rl41 = 	 Parameter(name='Rl41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl41}', 
	 lhablock = 'SELMIX', 
	 lhacode = [4, 1] ) 
 
Rl42 = 	 Parameter(name='Rl42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl42}', 
	 lhablock = 'SELMIX', 
	 lhacode = [4, 2] ) 
 
Rl43 = 	 Parameter(name='Rl43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl43}', 
	 lhablock = 'SELMIX', 
	 lhacode = [4, 3] ) 
 
Rl44 = 	 Parameter(name='Rl44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl44}', 
	 lhablock = 'SELMIX', 
	 lhacode = [4, 4] ) 
 
Rl45 = 	 Parameter(name='Rl45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl45}', 
	 lhablock = 'SELMIX', 
	 lhacode = [4, 5] ) 
 
Rl46 = 	 Parameter(name='Rl46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl46}', 
	 lhablock = 'SELMIX', 
	 lhacode = [4, 6] ) 
 
Rl51 = 	 Parameter(name='Rl51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl51}', 
	 lhablock = 'SELMIX', 
	 lhacode = [5, 1] ) 
 
Rl52 = 	 Parameter(name='Rl52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl52}', 
	 lhablock = 'SELMIX', 
	 lhacode = [5, 2] ) 
 
Rl53 = 	 Parameter(name='Rl53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl53}', 
	 lhablock = 'SELMIX', 
	 lhacode = [5, 3] ) 
 
Rl54 = 	 Parameter(name='Rl54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl54}', 
	 lhablock = 'SELMIX', 
	 lhacode = [5, 4] ) 
 
Rl55 = 	 Parameter(name='Rl55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl55}', 
	 lhablock = 'SELMIX', 
	 lhacode = [5, 5] ) 
 
Rl56 = 	 Parameter(name='Rl56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl56}', 
	 lhablock = 'SELMIX', 
	 lhacode = [5, 6] ) 
 
Rl61 = 	 Parameter(name='Rl61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl61}', 
	 lhablock = 'SELMIX', 
	 lhacode = [6, 1] ) 
 
Rl62 = 	 Parameter(name='Rl62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl62}', 
	 lhablock = 'SELMIX', 
	 lhacode = [6, 2] ) 
 
Rl63 = 	 Parameter(name='Rl63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl63}', 
	 lhablock = 'SELMIX', 
	 lhacode = [6, 3] ) 
 
Rl64 = 	 Parameter(name='Rl64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl64}', 
	 lhablock = 'SELMIX', 
	 lhacode = [6, 4] ) 
 
Rl65 = 	 Parameter(name='Rl65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl65}', 
	 lhablock = 'SELMIX', 
	 lhacode = [6, 5] ) 
 
Rl66 = 	 Parameter(name='Rl66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{Rl66}', 
	 lhablock = 'SELMIX', 
	 lhacode = [6, 6] ) 
 
RnRe11 = 	 Parameter(name='RnRe11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe11}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [1, 1] ) 
 
RnRe12 = 	 Parameter(name='RnRe12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe12}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [1, 2] ) 
 
RnRe13 = 	 Parameter(name='RnRe13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe13}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [1, 3] ) 
 
RnRe14 = 	 Parameter(name='RnRe14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe14}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [1, 4] ) 
 
RnRe15 = 	 Parameter(name='RnRe15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe15}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [1, 5] ) 
 
RnRe16 = 	 Parameter(name='RnRe16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe16}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [1, 6] ) 
 
RnRe21 = 	 Parameter(name='RnRe21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe21}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [2, 1] ) 
 
RnRe22 = 	 Parameter(name='RnRe22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe22}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [2, 2] ) 
 
RnRe23 = 	 Parameter(name='RnRe23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe23}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [2, 3] ) 
 
RnRe24 = 	 Parameter(name='RnRe24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe24}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [2, 4] ) 
 
RnRe25 = 	 Parameter(name='RnRe25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe25}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [2, 5] ) 
 
RnRe26 = 	 Parameter(name='RnRe26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe26}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [2, 6] ) 
 
RnRe31 = 	 Parameter(name='RnRe31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe31}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [3, 1] ) 
 
RnRe32 = 	 Parameter(name='RnRe32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe32}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [3, 2] ) 
 
RnRe33 = 	 Parameter(name='RnRe33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe33}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [3, 3] ) 
 
RnRe34 = 	 Parameter(name='RnRe34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe34}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [3, 4] ) 
 
RnRe35 = 	 Parameter(name='RnRe35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe35}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [3, 5] ) 
 
RnRe36 = 	 Parameter(name='RnRe36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe36}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [3, 6] ) 
 
RnRe41 = 	 Parameter(name='RnRe41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe41}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [4, 1] ) 
 
RnRe42 = 	 Parameter(name='RnRe42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe42}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [4, 2] ) 
 
RnRe43 = 	 Parameter(name='RnRe43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe43}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [4, 3] ) 
 
RnRe44 = 	 Parameter(name='RnRe44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe44}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [4, 4] ) 
 
RnRe45 = 	 Parameter(name='RnRe45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe45}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [4, 5] ) 
 
RnRe46 = 	 Parameter(name='RnRe46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe46}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [4, 6] ) 
 
RnRe51 = 	 Parameter(name='RnRe51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe51}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [5, 1] ) 
 
RnRe52 = 	 Parameter(name='RnRe52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe52}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [5, 2] ) 
 
RnRe53 = 	 Parameter(name='RnRe53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe53}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [5, 3] ) 
 
RnRe54 = 	 Parameter(name='RnRe54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe54}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [5, 4] ) 
 
RnRe55 = 	 Parameter(name='RnRe55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe55}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [5, 5] ) 
 
RnRe56 = 	 Parameter(name='RnRe56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe56}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [5, 6] ) 
 
RnRe61 = 	 Parameter(name='RnRe61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe61}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [6, 1] ) 
 
RnRe62 = 	 Parameter(name='RnRe62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe62}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [6, 2] ) 
 
RnRe63 = 	 Parameter(name='RnRe63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe63}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [6, 3] ) 
 
RnRe64 = 	 Parameter(name='RnRe64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe64}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [6, 4] ) 
 
RnRe65 = 	 Parameter(name='RnRe65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe65}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [6, 5] ) 
 
RnRe66 = 	 Parameter(name='RnRe66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnRe66}', 
	 lhablock = 'SNUMIXRE', 
	 lhacode = [6, 6] ) 
 
RnIm11 = 	 Parameter(name='RnIm11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm11}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [1, 1] ) 
 
RnIm12 = 	 Parameter(name='RnIm12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm12}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [1, 2] ) 
 
RnIm13 = 	 Parameter(name='RnIm13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm13}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [1, 3] ) 
 
RnIm14 = 	 Parameter(name='RnIm14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm14}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [1, 4] ) 
 
RnIm15 = 	 Parameter(name='RnIm15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm15}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [1, 5] ) 
 
RnIm16 = 	 Parameter(name='RnIm16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm16}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [1, 6] ) 
 
RnIm21 = 	 Parameter(name='RnIm21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm21}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [2, 1] ) 
 
RnIm22 = 	 Parameter(name='RnIm22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm22}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [2, 2] ) 
 
RnIm23 = 	 Parameter(name='RnIm23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm23}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [2, 3] ) 
 
RnIm24 = 	 Parameter(name='RnIm24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm24}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [2, 4] ) 
 
RnIm25 = 	 Parameter(name='RnIm25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm25}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [2, 5] ) 
 
RnIm26 = 	 Parameter(name='RnIm26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm26}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [2, 6] ) 
 
RnIm31 = 	 Parameter(name='RnIm31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm31}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [3, 1] ) 
 
RnIm32 = 	 Parameter(name='RnIm32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm32}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [3, 2] ) 
 
RnIm33 = 	 Parameter(name='RnIm33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm33}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [3, 3] ) 
 
RnIm34 = 	 Parameter(name='RnIm34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm34}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [3, 4] ) 
 
RnIm35 = 	 Parameter(name='RnIm35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm35}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [3, 5] ) 
 
RnIm36 = 	 Parameter(name='RnIm36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm36}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [3, 6] ) 
 
RnIm41 = 	 Parameter(name='RnIm41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm41}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [4, 1] ) 
 
RnIm42 = 	 Parameter(name='RnIm42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm42}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [4, 2] ) 
 
RnIm43 = 	 Parameter(name='RnIm43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm43}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [4, 3] ) 
 
RnIm44 = 	 Parameter(name='RnIm44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm44}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [4, 4] ) 
 
RnIm45 = 	 Parameter(name='RnIm45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm45}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [4, 5] ) 
 
RnIm46 = 	 Parameter(name='RnIm46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm46}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [4, 6] ) 
 
RnIm51 = 	 Parameter(name='RnIm51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm51}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [5, 1] ) 
 
RnIm52 = 	 Parameter(name='RnIm52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm52}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [5, 2] ) 
 
RnIm53 = 	 Parameter(name='RnIm53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm53}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [5, 3] ) 
 
RnIm54 = 	 Parameter(name='RnIm54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm54}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [5, 4] ) 
 
RnIm55 = 	 Parameter(name='RnIm55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm55}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [5, 5] ) 
 
RnIm56 = 	 Parameter(name='RnIm56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm56}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [5, 6] ) 
 
RnIm61 = 	 Parameter(name='RnIm61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm61}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [6, 1] ) 
 
RnIm62 = 	 Parameter(name='RnIm62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm62}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [6, 2] ) 
 
RnIm63 = 	 Parameter(name='RnIm63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm63}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [6, 3] ) 
 
RnIm64 = 	 Parameter(name='RnIm64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm64}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [6, 4] ) 
 
RnIm65 = 	 Parameter(name='RnIm65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm65}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [6, 5] ) 
 
RnIm66 = 	 Parameter(name='RnIm66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{RnIm66}', 
	 lhablock = 'SNUMIXIM', 
	 lhacode = [6, 6] ) 
 
USP11 = 	 Parameter(name='USP11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{USP11}', 
	 lhablock = 'UHP', 
	 lhacode = [1, 1] ) 
 
USP12 = 	 Parameter(name='USP12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{USP12}', 
	 lhablock = 'UHP', 
	 lhacode = [1, 2] ) 
 
USP21 = 	 Parameter(name='USP21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{USP21}', 
	 lhablock = 'UHP', 
	 lhacode = [2, 1] ) 
 
USP22 = 	 Parameter(name='USP22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{USP22}', 
	 lhablock = 'UHP', 
	 lhacode = [2, 2] ) 
 
USL11 = 	 Parameter(name='USL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{USL11}', 
	 lhablock = 'UHL', 
	 lhacode = [1, 1] ) 
 
USL12 = 	 Parameter(name='USL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{USL12}', 
	 lhablock = 'UHL', 
	 lhacode = [1, 2] ) 
 
USL21 = 	 Parameter(name='USL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{USL21}', 
	 lhablock = 'UHL', 
	 lhacode = [2, 1] ) 
 
USL22 = 	 Parameter(name='USL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{USL22}', 
	 lhablock = 'UHL', 
	 lhacode = [2, 2] ) 
 
ZH11 = 	 Parameter(name='ZH11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH11}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [1, 1] ) 
 
ZH12 = 	 Parameter(name='ZH12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH12}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [1, 2] ) 
 
ZH13 = 	 Parameter(name='ZH13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH13}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [1, 3] ) 
 
ZH14 = 	 Parameter(name='ZH14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH14}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [1, 4] ) 
 
ZH15 = 	 Parameter(name='ZH15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH15}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [1, 5] ) 
 
ZH21 = 	 Parameter(name='ZH21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH21}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [2, 1] ) 
 
ZH22 = 	 Parameter(name='ZH22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH22}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [2, 2] ) 
 
ZH23 = 	 Parameter(name='ZH23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH23}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [2, 3] ) 
 
ZH24 = 	 Parameter(name='ZH24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH24}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [2, 4] ) 
 
ZH25 = 	 Parameter(name='ZH25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH25}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [2, 5] ) 
 
ZH31 = 	 Parameter(name='ZH31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH31}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [3, 1] ) 
 
ZH32 = 	 Parameter(name='ZH32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH32}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [3, 2] ) 
 
ZH33 = 	 Parameter(name='ZH33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH33}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [3, 3] ) 
 
ZH34 = 	 Parameter(name='ZH34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH34}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [3, 4] ) 
 
ZH35 = 	 Parameter(name='ZH35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH35}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [3, 5] ) 
 
ZH41 = 	 Parameter(name='ZH41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH41}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [4, 1] ) 
 
ZH42 = 	 Parameter(name='ZH42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH42}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [4, 2] ) 
 
ZH43 = 	 Parameter(name='ZH43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH43}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [4, 3] ) 
 
ZH44 = 	 Parameter(name='ZH44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH44}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [4, 4] ) 
 
ZH45 = 	 Parameter(name='ZH45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH45}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [4, 5] ) 
 
ZH51 = 	 Parameter(name='ZH51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH51}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [5, 1] ) 
 
ZH52 = 	 Parameter(name='ZH52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH52}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [5, 2] ) 
 
ZH53 = 	 Parameter(name='ZH53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH53}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [5, 3] ) 
 
ZH54 = 	 Parameter(name='ZH54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH54}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [5, 4] ) 
 
ZH55 = 	 Parameter(name='ZH55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZH55}', 
	 lhablock = 'SCALARMIX', 
	 lhacode = [5, 5] ) 
 
UPL11 = 	 Parameter(name='UPL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPL11}', 
	 lhablock = 'UPL', 
	 lhacode = [1, 1] ) 
 
UPL12 = 	 Parameter(name='UPL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPL12}', 
	 lhablock = 'UPL', 
	 lhacode = [1, 2] ) 
 
UPL21 = 	 Parameter(name='UPL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPL21}', 
	 lhablock = 'UPL', 
	 lhacode = [2, 1] ) 
 
UPL22 = 	 Parameter(name='UPL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPL22}', 
	 lhablock = 'UPL', 
	 lhacode = [2, 2] ) 
 
UPPr11 = 	 Parameter(name='UPPr11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPPr11}', 
	 lhablock = 'UPPR', 
	 lhacode = [1, 1] ) 
 
UPPr12 = 	 Parameter(name='UPPr12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPPr12}', 
	 lhablock = 'UPPR', 
	 lhacode = [1, 2] ) 
 
UPPr21 = 	 Parameter(name='UPPr21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPPr21}', 
	 lhablock = 'UPPR', 
	 lhacode = [2, 1] ) 
 
UPPr22 = 	 Parameter(name='UPPr22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPPr22}', 
	 lhablock = 'UPPR', 
	 lhacode = [2, 2] ) 
 
UP11 = 	 Parameter(name='UP11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP11}', 
	 lhablock = 'AMIX', 
	 lhacode = [1, 1] ) 
 
UP12 = 	 Parameter(name='UP12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP12}', 
	 lhablock = 'AMIX', 
	 lhacode = [1, 2] ) 
 
UP13 = 	 Parameter(name='UP13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP13}', 
	 lhablock = 'AMIX', 
	 lhacode = [1, 3] ) 
 
UP14 = 	 Parameter(name='UP14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP14}', 
	 lhablock = 'AMIX', 
	 lhacode = [1, 4] ) 
 
UP15 = 	 Parameter(name='UP15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP15}', 
	 lhablock = 'AMIX', 
	 lhacode = [1, 5] ) 
 
UP21 = 	 Parameter(name='UP21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP21}', 
	 lhablock = 'AMIX', 
	 lhacode = [2, 1] ) 
 
UP22 = 	 Parameter(name='UP22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP22}', 
	 lhablock = 'AMIX', 
	 lhacode = [2, 2] ) 
 
UP23 = 	 Parameter(name='UP23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP23}', 
	 lhablock = 'AMIX', 
	 lhacode = [2, 3] ) 
 
UP24 = 	 Parameter(name='UP24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP24}', 
	 lhablock = 'AMIX', 
	 lhacode = [2, 4] ) 
 
UP25 = 	 Parameter(name='UP25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP25}', 
	 lhablock = 'AMIX', 
	 lhacode = [2, 5] ) 
 
UP31 = 	 Parameter(name='UP31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP31}', 
	 lhablock = 'AMIX', 
	 lhacode = [3, 1] ) 
 
UP32 = 	 Parameter(name='UP32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP32}', 
	 lhablock = 'AMIX', 
	 lhacode = [3, 2] ) 
 
UP33 = 	 Parameter(name='UP33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP33}', 
	 lhablock = 'AMIX', 
	 lhacode = [3, 3] ) 
 
UP34 = 	 Parameter(name='UP34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP34}', 
	 lhablock = 'AMIX', 
	 lhacode = [3, 4] ) 
 
UP35 = 	 Parameter(name='UP35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP35}', 
	 lhablock = 'AMIX', 
	 lhacode = [3, 5] ) 
 
UP41 = 	 Parameter(name='UP41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP41}', 
	 lhablock = 'AMIX', 
	 lhacode = [4, 1] ) 
 
UP42 = 	 Parameter(name='UP42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP42}', 
	 lhablock = 'AMIX', 
	 lhacode = [4, 2] ) 
 
UP43 = 	 Parameter(name='UP43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP43}', 
	 lhablock = 'AMIX', 
	 lhacode = [4, 3] ) 
 
UP44 = 	 Parameter(name='UP44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP44}', 
	 lhablock = 'AMIX', 
	 lhacode = [4, 4] ) 
 
UP45 = 	 Parameter(name='UP45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP45}', 
	 lhablock = 'AMIX', 
	 lhacode = [4, 5] ) 
 
UP51 = 	 Parameter(name='UP51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP51}', 
	 lhablock = 'AMIX', 
	 lhacode = [5, 1] ) 
 
UP52 = 	 Parameter(name='UP52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP52}', 
	 lhablock = 'AMIX', 
	 lhacode = [5, 2] ) 
 
UP53 = 	 Parameter(name='UP53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP53}', 
	 lhablock = 'AMIX', 
	 lhacode = [5, 3] ) 
 
UP54 = 	 Parameter(name='UP54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP54}', 
	 lhablock = 'AMIX', 
	 lhacode = [5, 4] ) 
 
UP55 = 	 Parameter(name='UP55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UP55}', 
	 lhablock = 'AMIX', 
	 lhacode = [5, 5] ) 
 
UC11 = 	 Parameter(name='UC11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC11}', 
	 lhablock = 'CHMIX', 
	 lhacode = [1, 1] ) 
 
UC12 = 	 Parameter(name='UC12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC12}', 
	 lhablock = 'CHMIX', 
	 lhacode = [1, 2] ) 
 
UC13 = 	 Parameter(name='UC13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC13}', 
	 lhablock = 'CHMIX', 
	 lhacode = [1, 3] ) 
 
UC14 = 	 Parameter(name='UC14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC14}', 
	 lhablock = 'CHMIX', 
	 lhacode = [1, 4] ) 
 
UC15 = 	 Parameter(name='UC15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC15}', 
	 lhablock = 'CHMIX', 
	 lhacode = [1, 5] ) 
 
UC16 = 	 Parameter(name='UC16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC16}', 
	 lhablock = 'CHMIX', 
	 lhacode = [1, 6] ) 
 
UC21 = 	 Parameter(name='UC21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC21}', 
	 lhablock = 'CHMIX', 
	 lhacode = [2, 1] ) 
 
UC22 = 	 Parameter(name='UC22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC22}', 
	 lhablock = 'CHMIX', 
	 lhacode = [2, 2] ) 
 
UC23 = 	 Parameter(name='UC23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC23}', 
	 lhablock = 'CHMIX', 
	 lhacode = [2, 3] ) 
 
UC24 = 	 Parameter(name='UC24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC24}', 
	 lhablock = 'CHMIX', 
	 lhacode = [2, 4] ) 
 
UC25 = 	 Parameter(name='UC25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC25}', 
	 lhablock = 'CHMIX', 
	 lhacode = [2, 5] ) 
 
UC26 = 	 Parameter(name='UC26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC26}', 
	 lhablock = 'CHMIX', 
	 lhacode = [2, 6] ) 
 
UC31 = 	 Parameter(name='UC31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC31}', 
	 lhablock = 'CHMIX', 
	 lhacode = [3, 1] ) 
 
UC32 = 	 Parameter(name='UC32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC32}', 
	 lhablock = 'CHMIX', 
	 lhacode = [3, 2] ) 
 
UC33 = 	 Parameter(name='UC33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC33}', 
	 lhablock = 'CHMIX', 
	 lhacode = [3, 3] ) 
 
UC34 = 	 Parameter(name='UC34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC34}', 
	 lhablock = 'CHMIX', 
	 lhacode = [3, 4] ) 
 
UC35 = 	 Parameter(name='UC35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC35}', 
	 lhablock = 'CHMIX', 
	 lhacode = [3, 5] ) 
 
UC36 = 	 Parameter(name='UC36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC36}', 
	 lhablock = 'CHMIX', 
	 lhacode = [3, 6] ) 
 
UC41 = 	 Parameter(name='UC41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC41}', 
	 lhablock = 'CHMIX', 
	 lhacode = [4, 1] ) 
 
UC42 = 	 Parameter(name='UC42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC42}', 
	 lhablock = 'CHMIX', 
	 lhacode = [4, 2] ) 
 
UC43 = 	 Parameter(name='UC43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC43}', 
	 lhablock = 'CHMIX', 
	 lhacode = [4, 3] ) 
 
UC44 = 	 Parameter(name='UC44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC44}', 
	 lhablock = 'CHMIX', 
	 lhacode = [4, 4] ) 
 
UC45 = 	 Parameter(name='UC45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC45}', 
	 lhablock = 'CHMIX', 
	 lhacode = [4, 5] ) 
 
UC46 = 	 Parameter(name='UC46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC46}', 
	 lhablock = 'CHMIX', 
	 lhacode = [4, 6] ) 
 
UC51 = 	 Parameter(name='UC51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC51}', 
	 lhablock = 'CHMIX', 
	 lhacode = [5, 1] ) 
 
UC52 = 	 Parameter(name='UC52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC52}', 
	 lhablock = 'CHMIX', 
	 lhacode = [5, 2] ) 
 
UC53 = 	 Parameter(name='UC53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC53}', 
	 lhablock = 'CHMIX', 
	 lhacode = [5, 3] ) 
 
UC54 = 	 Parameter(name='UC54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC54}', 
	 lhablock = 'CHMIX', 
	 lhacode = [5, 4] ) 
 
UC55 = 	 Parameter(name='UC55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC55}', 
	 lhablock = 'CHMIX', 
	 lhacode = [5, 5] ) 
 
UC56 = 	 Parameter(name='UC56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC56}', 
	 lhablock = 'CHMIX', 
	 lhacode = [5, 6] ) 
 
UC61 = 	 Parameter(name='UC61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC61}', 
	 lhablock = 'CHMIX', 
	 lhacode = [6, 1] ) 
 
UC62 = 	 Parameter(name='UC62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC62}', 
	 lhablock = 'CHMIX', 
	 lhacode = [6, 2] ) 
 
UC63 = 	 Parameter(name='UC63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC63}', 
	 lhablock = 'CHMIX', 
	 lhacode = [6, 3] ) 
 
UC64 = 	 Parameter(name='UC64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC64}', 
	 lhablock = 'CHMIX', 
	 lhacode = [6, 4] ) 
 
UC65 = 	 Parameter(name='UC65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC65}', 
	 lhablock = 'CHMIX', 
	 lhacode = [6, 5] ) 
 
UC66 = 	 Parameter(name='UC66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UC66}', 
	 lhablock = 'CHMIX', 
	 lhacode = [6, 6] ) 
 
UCL11 = 	 Parameter(name='UCL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCL11}', 
	 lhablock = 'CHLMIX', 
	 lhacode = [1, 1] ) 
 
UCL12 = 	 Parameter(name='UCL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCL12}', 
	 lhablock = 'CHLMIX', 
	 lhacode = [1, 2] ) 
 
UCL21 = 	 Parameter(name='UCL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCL21}', 
	 lhablock = 'CHLMIX', 
	 lhacode = [2, 1] ) 
 
UCL22 = 	 Parameter(name='UCL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCL22}', 
	 lhablock = 'CHLMIX', 
	 lhacode = [2, 2] ) 
 
UCC11 = 	 Parameter(name='UCC11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCC11}', 
	 lhablock = 'DHMIX', 
	 lhacode = [1, 1] ) 
 
UCC12 = 	 Parameter(name='UCC12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCC12}', 
	 lhablock = 'DHMIX', 
	 lhacode = [1, 2] ) 
 
UCC21 = 	 Parameter(name='UCC21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCC21}', 
	 lhablock = 'DHMIX', 
	 lhacode = [2, 1] ) 
 
UCC22 = 	 Parameter(name='UCC22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCC22}', 
	 lhablock = 'DHMIX', 
	 lhacode = [2, 2] ) 
 
UCCL11 = 	 Parameter(name='UCCL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCCL11}', 
	 lhablock = 'DHLMIX', 
	 lhacode = [1, 1] ) 
 
UCCL12 = 	 Parameter(name='UCCL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCCL12}', 
	 lhablock = 'DHLMIX', 
	 lhacode = [1, 2] ) 
 
UCCL21 = 	 Parameter(name='UCCL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCCL21}', 
	 lhablock = 'DHLMIX', 
	 lhacode = [2, 1] ) 
 
UCCL22 = 	 Parameter(name='UCCL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UCCL22}', 
	 lhablock = 'DHLMIX', 
	 lhacode = [2, 2] ) 
 
rUMM11 = 	 Parameter(name='rUMM11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UMM11}', 
	 lhablock = 'UMM', 
	 lhacode = [1, 1] ) 
 
iUMM11 = 	 Parameter(name='iUMM11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UMM11}', 
	 lhablock = 'IMUMM', 
	 lhacode = [1, 1] ) 
 
rUMM12 = 	 Parameter(name='rUMM12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UMM12}', 
	 lhablock = 'UMM', 
	 lhacode = [1, 2] ) 
 
iUMM12 = 	 Parameter(name='iUMM12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UMM12}', 
	 lhablock = 'IMUMM', 
	 lhacode = [1, 2] ) 
 
rUMM21 = 	 Parameter(name='rUMM21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UMM21}', 
	 lhablock = 'UMM', 
	 lhacode = [2, 1] ) 
 
iUMM21 = 	 Parameter(name='iUMM21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UMM21}', 
	 lhablock = 'IMUMM', 
	 lhacode = [2, 1] ) 
 
rUMM22 = 	 Parameter(name='rUMM22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UMM22}', 
	 lhablock = 'UMM', 
	 lhacode = [2, 2] ) 
 
iUMM22 = 	 Parameter(name='iUMM22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UMM22}', 
	 lhablock = 'IMUMM', 
	 lhacode = [2, 2] ) 
 
rUPP11 = 	 Parameter(name='rUPP11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPP11}', 
	 lhablock = 'UPP', 
	 lhacode = [1, 1] ) 
 
iUPP11 = 	 Parameter(name='iUPP11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPP11}', 
	 lhablock = 'IMUPP', 
	 lhacode = [1, 1] ) 
 
rUPP12 = 	 Parameter(name='rUPP12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPP12}', 
	 lhablock = 'UPP', 
	 lhacode = [1, 2] ) 
 
iUPP12 = 	 Parameter(name='iUPP12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPP12}', 
	 lhablock = 'IMUPP', 
	 lhacode = [1, 2] ) 
 
rUPP21 = 	 Parameter(name='rUPP21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPP21}', 
	 lhablock = 'UPP', 
	 lhacode = [2, 1] ) 
 
iUPP21 = 	 Parameter(name='iUPP21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPP21}', 
	 lhablock = 'IMUPP', 
	 lhacode = [2, 1] ) 
 
rUPP22 = 	 Parameter(name='rUPP22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPP22}', 
	 lhablock = 'UPP', 
	 lhacode = [2, 2] ) 
 
iUPP22 = 	 Parameter(name='iUPP22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UPP22}', 
	 lhablock = 'IMUPP', 
	 lhacode = [2, 2] ) 
 
rUV11 = 	 Parameter(name='rUV11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV11}', 
	 lhablock = 'PMNS', 
	 lhacode = [1, 1] ) 
 
iUV11 = 	 Parameter(name='iUV11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV11}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [1, 1] ) 
 
rUV12 = 	 Parameter(name='rUV12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV12}', 
	 lhablock = 'PMNS', 
	 lhacode = [1, 2] ) 
 
iUV12 = 	 Parameter(name='iUV12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV12}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [1, 2] ) 
 
rUV13 = 	 Parameter(name='rUV13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV13}', 
	 lhablock = 'PMNS', 
	 lhacode = [1, 3] ) 
 
iUV13 = 	 Parameter(name='iUV13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV13}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [1, 3] ) 
 
rUV14 = 	 Parameter(name='rUV14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV14}', 
	 lhablock = 'PMNS', 
	 lhacode = [1, 4] ) 
 
iUV14 = 	 Parameter(name='iUV14', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV14}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [1, 4] ) 
 
rUV15 = 	 Parameter(name='rUV15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV15}', 
	 lhablock = 'PMNS', 
	 lhacode = [1, 5] ) 
 
iUV15 = 	 Parameter(name='iUV15', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV15}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [1, 5] ) 
 
rUV16 = 	 Parameter(name='rUV16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV16}', 
	 lhablock = 'PMNS', 
	 lhacode = [1, 6] ) 
 
iUV16 = 	 Parameter(name='iUV16', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV16}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [1, 6] ) 
 
rUV21 = 	 Parameter(name='rUV21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV21}', 
	 lhablock = 'PMNS', 
	 lhacode = [2, 1] ) 
 
iUV21 = 	 Parameter(name='iUV21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV21}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [2, 1] ) 
 
rUV22 = 	 Parameter(name='rUV22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV22}', 
	 lhablock = 'PMNS', 
	 lhacode = [2, 2] ) 
 
iUV22 = 	 Parameter(name='iUV22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV22}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [2, 2] ) 
 
rUV23 = 	 Parameter(name='rUV23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV23}', 
	 lhablock = 'PMNS', 
	 lhacode = [2, 3] ) 
 
iUV23 = 	 Parameter(name='iUV23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV23}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [2, 3] ) 
 
rUV24 = 	 Parameter(name='rUV24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV24}', 
	 lhablock = 'PMNS', 
	 lhacode = [2, 4] ) 
 
iUV24 = 	 Parameter(name='iUV24', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV24}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [2, 4] ) 
 
rUV25 = 	 Parameter(name='rUV25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV25}', 
	 lhablock = 'PMNS', 
	 lhacode = [2, 5] ) 
 
iUV25 = 	 Parameter(name='iUV25', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV25}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [2, 5] ) 
 
rUV26 = 	 Parameter(name='rUV26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV26}', 
	 lhablock = 'PMNS', 
	 lhacode = [2, 6] ) 
 
iUV26 = 	 Parameter(name='iUV26', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV26}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [2, 6] ) 
 
rUV31 = 	 Parameter(name='rUV31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV31}', 
	 lhablock = 'PMNS', 
	 lhacode = [3, 1] ) 
 
iUV31 = 	 Parameter(name='iUV31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV31}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [3, 1] ) 
 
rUV32 = 	 Parameter(name='rUV32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV32}', 
	 lhablock = 'PMNS', 
	 lhacode = [3, 2] ) 
 
iUV32 = 	 Parameter(name='iUV32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV32}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [3, 2] ) 
 
rUV33 = 	 Parameter(name='rUV33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV33}', 
	 lhablock = 'PMNS', 
	 lhacode = [3, 3] ) 
 
iUV33 = 	 Parameter(name='iUV33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV33}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [3, 3] ) 
 
rUV34 = 	 Parameter(name='rUV34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV34}', 
	 lhablock = 'PMNS', 
	 lhacode = [3, 4] ) 
 
iUV34 = 	 Parameter(name='iUV34', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV34}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [3, 4] ) 
 
rUV35 = 	 Parameter(name='rUV35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV35}', 
	 lhablock = 'PMNS', 
	 lhacode = [3, 5] ) 
 
iUV35 = 	 Parameter(name='iUV35', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV35}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [3, 5] ) 
 
rUV36 = 	 Parameter(name='rUV36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV36}', 
	 lhablock = 'PMNS', 
	 lhacode = [3, 6] ) 
 
iUV36 = 	 Parameter(name='iUV36', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV36}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [3, 6] ) 
 
rUV41 = 	 Parameter(name='rUV41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV41}', 
	 lhablock = 'PMNS', 
	 lhacode = [4, 1] ) 
 
iUV41 = 	 Parameter(name='iUV41', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV41}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [4, 1] ) 
 
rUV42 = 	 Parameter(name='rUV42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV42}', 
	 lhablock = 'PMNS', 
	 lhacode = [4, 2] ) 
 
iUV42 = 	 Parameter(name='iUV42', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV42}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [4, 2] ) 
 
rUV43 = 	 Parameter(name='rUV43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV43}', 
	 lhablock = 'PMNS', 
	 lhacode = [4, 3] ) 
 
iUV43 = 	 Parameter(name='iUV43', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV43}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [4, 3] ) 
 
rUV44 = 	 Parameter(name='rUV44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV44}', 
	 lhablock = 'PMNS', 
	 lhacode = [4, 4] ) 
 
iUV44 = 	 Parameter(name='iUV44', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV44}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [4, 4] ) 
 
rUV45 = 	 Parameter(name='rUV45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV45}', 
	 lhablock = 'PMNS', 
	 lhacode = [4, 5] ) 
 
iUV45 = 	 Parameter(name='iUV45', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV45}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [4, 5] ) 
 
rUV46 = 	 Parameter(name='rUV46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV46}', 
	 lhablock = 'PMNS', 
	 lhacode = [4, 6] ) 
 
iUV46 = 	 Parameter(name='iUV46', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV46}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [4, 6] ) 
 
rUV51 = 	 Parameter(name='rUV51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV51}', 
	 lhablock = 'PMNS', 
	 lhacode = [5, 1] ) 
 
iUV51 = 	 Parameter(name='iUV51', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV51}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [5, 1] ) 
 
rUV52 = 	 Parameter(name='rUV52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV52}', 
	 lhablock = 'PMNS', 
	 lhacode = [5, 2] ) 
 
iUV52 = 	 Parameter(name='iUV52', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV52}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [5, 2] ) 
 
rUV53 = 	 Parameter(name='rUV53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV53}', 
	 lhablock = 'PMNS', 
	 lhacode = [5, 3] ) 
 
iUV53 = 	 Parameter(name='iUV53', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV53}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [5, 3] ) 
 
rUV54 = 	 Parameter(name='rUV54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV54}', 
	 lhablock = 'PMNS', 
	 lhacode = [5, 4] ) 
 
iUV54 = 	 Parameter(name='iUV54', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV54}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [5, 4] ) 
 
rUV55 = 	 Parameter(name='rUV55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV55}', 
	 lhablock = 'PMNS', 
	 lhacode = [5, 5] ) 
 
iUV55 = 	 Parameter(name='iUV55', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV55}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [5, 5] ) 
 
rUV56 = 	 Parameter(name='rUV56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV56}', 
	 lhablock = 'PMNS', 
	 lhacode = [5, 6] ) 
 
iUV56 = 	 Parameter(name='iUV56', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV56}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [5, 6] ) 
 
rUV61 = 	 Parameter(name='rUV61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV61}', 
	 lhablock = 'PMNS', 
	 lhacode = [6, 1] ) 
 
iUV61 = 	 Parameter(name='iUV61', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV61}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [6, 1] ) 
 
rUV62 = 	 Parameter(name='rUV62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV62}', 
	 lhablock = 'PMNS', 
	 lhacode = [6, 2] ) 
 
iUV62 = 	 Parameter(name='iUV62', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV62}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [6, 2] ) 
 
rUV63 = 	 Parameter(name='rUV63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV63}', 
	 lhablock = 'PMNS', 
	 lhacode = [6, 3] ) 
 
iUV63 = 	 Parameter(name='iUV63', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV63}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [6, 3] ) 
 
rUV64 = 	 Parameter(name='rUV64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV64}', 
	 lhablock = 'PMNS', 
	 lhacode = [6, 4] ) 
 
iUV64 = 	 Parameter(name='iUV64', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV64}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [6, 4] ) 
 
rUV65 = 	 Parameter(name='rUV65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV65}', 
	 lhablock = 'PMNS', 
	 lhacode = [6, 5] ) 
 
iUV65 = 	 Parameter(name='iUV65', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV65}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [6, 5] ) 
 
rUV66 = 	 Parameter(name='rUV66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV66}', 
	 lhablock = 'PMNS', 
	 lhacode = [6, 6] ) 
 
iUV66 = 	 Parameter(name='iUV66', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{UV66}', 
	 lhablock = 'IMPMNS', 
	 lhacode = [6, 6] ) 
 
rZEL11 = 	 Parameter(name='rZEL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL11}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 1] ) 
 
iZEL11 = 	 Parameter(name='iZEL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL11}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 1] ) 
 
rZEL12 = 	 Parameter(name='rZEL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL12}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 2] ) 
 
iZEL12 = 	 Parameter(name='iZEL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL12}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 2] ) 
 
rZEL13 = 	 Parameter(name='rZEL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL13}', 
	 lhablock = 'UELMIX', 
	 lhacode = [1, 3] ) 
 
iZEL13 = 	 Parameter(name='iZEL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL13}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [1, 3] ) 
 
rZEL21 = 	 Parameter(name='rZEL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL21}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 1] ) 
 
iZEL21 = 	 Parameter(name='iZEL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL21}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 1] ) 
 
rZEL22 = 	 Parameter(name='rZEL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL22}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 2] ) 
 
iZEL22 = 	 Parameter(name='iZEL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL22}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 2] ) 
 
rZEL23 = 	 Parameter(name='rZEL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL23}', 
	 lhablock = 'UELMIX', 
	 lhacode = [2, 3] ) 
 
iZEL23 = 	 Parameter(name='iZEL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL23}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [2, 3] ) 
 
rZEL31 = 	 Parameter(name='rZEL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL31}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 1] ) 
 
iZEL31 = 	 Parameter(name='iZEL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL31}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 1] ) 
 
rZEL32 = 	 Parameter(name='rZEL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL32}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 2] ) 
 
iZEL32 = 	 Parameter(name='iZEL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL32}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 2] ) 
 
rZEL33 = 	 Parameter(name='rZEL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL33}', 
	 lhablock = 'UELMIX', 
	 lhacode = [3, 3] ) 
 
iZEL33 = 	 Parameter(name='iZEL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZEL33}', 
	 lhablock = 'IMUELMIX', 
	 lhacode = [3, 3] ) 
 
rZER11 = 	 Parameter(name='rZER11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER11}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 1] ) 
 
iZER11 = 	 Parameter(name='iZER11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER11}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 1] ) 
 
rZER12 = 	 Parameter(name='rZER12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER12}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 2] ) 
 
iZER12 = 	 Parameter(name='iZER12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER12}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 2] ) 
 
rZER13 = 	 Parameter(name='rZER13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER13}', 
	 lhablock = 'UERMIX', 
	 lhacode = [1, 3] ) 
 
iZER13 = 	 Parameter(name='iZER13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER13}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [1, 3] ) 
 
rZER21 = 	 Parameter(name='rZER21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER21}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 1] ) 
 
iZER21 = 	 Parameter(name='iZER21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER21}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 1] ) 
 
rZER22 = 	 Parameter(name='rZER22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER22}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 2] ) 
 
iZER22 = 	 Parameter(name='iZER22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER22}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 2] ) 
 
rZER23 = 	 Parameter(name='rZER23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER23}', 
	 lhablock = 'UERMIX', 
	 lhacode = [2, 3] ) 
 
iZER23 = 	 Parameter(name='iZER23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER23}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [2, 3] ) 
 
rZER31 = 	 Parameter(name='rZER31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER31}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 1] ) 
 
iZER31 = 	 Parameter(name='iZER31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER31}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 1] ) 
 
rZER32 = 	 Parameter(name='rZER32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER32}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 2] ) 
 
iZER32 = 	 Parameter(name='iZER32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER32}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 2] ) 
 
rZER33 = 	 Parameter(name='rZER33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER33}', 
	 lhablock = 'UERMIX', 
	 lhacode = [3, 3] ) 
 
iZER33 = 	 Parameter(name='iZER33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZER33}', 
	 lhablock = 'IMUERMIX', 
	 lhacode = [3, 3] ) 
 
rZDL11 = 	 Parameter(name='rZDL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL11}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 1] ) 
 
iZDL11 = 	 Parameter(name='iZDL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL11}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 1] ) 
 
rZDL12 = 	 Parameter(name='rZDL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL12}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 2] ) 
 
iZDL12 = 	 Parameter(name='iZDL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL12}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 2] ) 
 
rZDL13 = 	 Parameter(name='rZDL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL13}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [1, 3] ) 
 
iZDL13 = 	 Parameter(name='iZDL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL13}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [1, 3] ) 
 
rZDL21 = 	 Parameter(name='rZDL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL21}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 1] ) 
 
iZDL21 = 	 Parameter(name='iZDL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL21}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 1] ) 
 
rZDL22 = 	 Parameter(name='rZDL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL22}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 2] ) 
 
iZDL22 = 	 Parameter(name='iZDL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL22}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 2] ) 
 
rZDL23 = 	 Parameter(name='rZDL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL23}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [2, 3] ) 
 
iZDL23 = 	 Parameter(name='iZDL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL23}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [2, 3] ) 
 
rZDL31 = 	 Parameter(name='rZDL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL31}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 1] ) 
 
iZDL31 = 	 Parameter(name='iZDL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL31}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 1] ) 
 
rZDL32 = 	 Parameter(name='rZDL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL32}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 2] ) 
 
iZDL32 = 	 Parameter(name='iZDL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL32}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 2] ) 
 
rZDL33 = 	 Parameter(name='rZDL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL33}', 
	 lhablock = 'UDLMIX', 
	 lhacode = [3, 3] ) 
 
iZDL33 = 	 Parameter(name='iZDL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDL33}', 
	 lhablock = 'IMUDLMIX', 
	 lhacode = [3, 3] ) 
 
rZDR11 = 	 Parameter(name='rZDR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR11}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 1] ) 
 
iZDR11 = 	 Parameter(name='iZDR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR11}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 1] ) 
 
rZDR12 = 	 Parameter(name='rZDR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR12}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 2] ) 
 
iZDR12 = 	 Parameter(name='iZDR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR12}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 2] ) 
 
rZDR13 = 	 Parameter(name='rZDR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR13}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [1, 3] ) 
 
iZDR13 = 	 Parameter(name='iZDR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR13}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [1, 3] ) 
 
rZDR21 = 	 Parameter(name='rZDR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR21}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 1] ) 
 
iZDR21 = 	 Parameter(name='iZDR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR21}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 1] ) 
 
rZDR22 = 	 Parameter(name='rZDR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR22}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 2] ) 
 
iZDR22 = 	 Parameter(name='iZDR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR22}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 2] ) 
 
rZDR23 = 	 Parameter(name='rZDR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR23}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [2, 3] ) 
 
iZDR23 = 	 Parameter(name='iZDR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR23}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [2, 3] ) 
 
rZDR31 = 	 Parameter(name='rZDR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR31}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 1] ) 
 
iZDR31 = 	 Parameter(name='iZDR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR31}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 1] ) 
 
rZDR32 = 	 Parameter(name='rZDR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR32}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 2] ) 
 
iZDR32 = 	 Parameter(name='iZDR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR32}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 2] ) 
 
rZDR33 = 	 Parameter(name='rZDR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR33}', 
	 lhablock = 'UDRMIX', 
	 lhacode = [3, 3] ) 
 
iZDR33 = 	 Parameter(name='iZDR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZDR33}', 
	 lhablock = 'IMUDRMIX', 
	 lhacode = [3, 3] ) 
 
rZUL11 = 	 Parameter(name='rZUL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL11}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 1] ) 
 
iZUL11 = 	 Parameter(name='iZUL11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL11}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 1] ) 
 
rZUL12 = 	 Parameter(name='rZUL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL12}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 2] ) 
 
iZUL12 = 	 Parameter(name='iZUL12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL12}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 2] ) 
 
rZUL13 = 	 Parameter(name='rZUL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL13}', 
	 lhablock = 'UULMIX', 
	 lhacode = [1, 3] ) 
 
iZUL13 = 	 Parameter(name='iZUL13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL13}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [1, 3] ) 
 
rZUL21 = 	 Parameter(name='rZUL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL21}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 1] ) 
 
iZUL21 = 	 Parameter(name='iZUL21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL21}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 1] ) 
 
rZUL22 = 	 Parameter(name='rZUL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL22}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 2] ) 
 
iZUL22 = 	 Parameter(name='iZUL22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL22}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 2] ) 
 
rZUL23 = 	 Parameter(name='rZUL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL23}', 
	 lhablock = 'UULMIX', 
	 lhacode = [2, 3] ) 
 
iZUL23 = 	 Parameter(name='iZUL23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL23}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [2, 3] ) 
 
rZUL31 = 	 Parameter(name='rZUL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL31}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 1] ) 
 
iZUL31 = 	 Parameter(name='iZUL31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL31}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 1] ) 
 
rZUL32 = 	 Parameter(name='rZUL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL32}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 2] ) 
 
iZUL32 = 	 Parameter(name='iZUL32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL32}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 2] ) 
 
rZUL33 = 	 Parameter(name='rZUL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL33}', 
	 lhablock = 'UULMIX', 
	 lhacode = [3, 3] ) 
 
iZUL33 = 	 Parameter(name='iZUL33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUL33}', 
	 lhablock = 'IMUULMIX', 
	 lhacode = [3, 3] ) 
 
rZUR11 = 	 Parameter(name='rZUR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR11}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 1] ) 
 
iZUR11 = 	 Parameter(name='iZUR11', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR11}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 1] ) 
 
rZUR12 = 	 Parameter(name='rZUR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR12}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 2] ) 
 
iZUR12 = 	 Parameter(name='iZUR12', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR12}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 2] ) 
 
rZUR13 = 	 Parameter(name='rZUR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR13}', 
	 lhablock = 'UURMIX', 
	 lhacode = [1, 3] ) 
 
iZUR13 = 	 Parameter(name='iZUR13', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR13}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [1, 3] ) 
 
rZUR21 = 	 Parameter(name='rZUR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR21}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 1] ) 
 
iZUR21 = 	 Parameter(name='iZUR21', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR21}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 1] ) 
 
rZUR22 = 	 Parameter(name='rZUR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR22}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 2] ) 
 
iZUR22 = 	 Parameter(name='iZUR22', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR22}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 2] ) 
 
rZUR23 = 	 Parameter(name='rZUR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR23}', 
	 lhablock = 'UURMIX', 
	 lhacode = [2, 3] ) 
 
iZUR23 = 	 Parameter(name='iZUR23', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR23}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [2, 3] ) 
 
rZUR31 = 	 Parameter(name='rZUR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR31}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 1] ) 
 
iZUR31 = 	 Parameter(name='iZUR31', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR31}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 1] ) 
 
rZUR32 = 	 Parameter(name='rZUR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR32}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 2] ) 
 
iZUR32 = 	 Parameter(name='iZUR32', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR32}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 2] ) 
 
rZUR33 = 	 Parameter(name='rZUR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR33}', 
	 lhablock = 'UURMIX', 
	 lhacode = [3, 3] ) 
 
iZUR33 = 	 Parameter(name='iZUR33', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{ZUR33}', 
	 lhablock = 'IMUURMIX', 
	 lhacode = [3, 3] ) 
 
TW = 	 Parameter(name='TW', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.5, 
	 texname = '\\text{TW}', 
	 lhablock = 'THETAW', 
	 lhacode = [1] ) 
 
aEWM1 = 	 Parameter(name='aEWM1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 137.035999679, 
	 texname = '\\text{aEWM1}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [1] ) 
 
aS = 	 Parameter(name='aS', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.119, 
	 texname = '\\text{aS}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [3] ) 
 
betaH = 	 Parameter(name='betaH', 
	 nature = 'external', 
	 type = 'real', 
	 value = 1., 
	 texname = '\\text{betaH}', 
	 lhablock = 'BETA', 
	 lhacode = [1] ) 
 
Gf = 	 Parameter(name='Gf', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0.0000116639, 
	 texname = '\\text{Gf}', 
	 lhablock = 'SMINPUTS', 
	 lhacode = [2] ) 
 
YL111 = 	 Parameter(name='YL111', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYL111 + complex(0,1)*iYL111', 
	 texname = '\\text{YL111}' ) 
 
YL112 = 	 Parameter(name='YL112', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYL112 + complex(0,1)*iYL112', 
	 texname = '\\text{YL112}' ) 
 
YL113 = 	 Parameter(name='YL113', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYL113 + complex(0,1)*iYL113', 
	 texname = '\\text{YL113}' ) 
 
YL121 = 	 Parameter(name='YL121', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYL121 + complex(0,1)*iYL121', 
	 texname = '\\text{YL121}' ) 
 
YL122 = 	 Parameter(name='YL122', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYL122 + complex(0,1)*iYL122', 
	 texname = '\\text{YL122}' ) 
 
YL123 = 	 Parameter(name='YL123', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYL123 + complex(0,1)*iYL123', 
	 texname = '\\text{YL123}' ) 
 
YL131 = 	 Parameter(name='YL131', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYL131 + complex(0,1)*iYL131', 
	 texname = '\\text{YL131}' ) 
 
YL132 = 	 Parameter(name='YL132', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYL132 + complex(0,1)*iYL132', 
	 texname = '\\text{YL132}' ) 
 
YL133 = 	 Parameter(name='YL133', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYL133 + complex(0,1)*iYL133', 
	 texname = '\\text{YL133}' ) 
 
TL111 = 	 Parameter(name='TL111', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTL111 + complex(0,1)*iTL111', 
	 texname = '\\text{TL111}' ) 
 
TL112 = 	 Parameter(name='TL112', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTL112 + complex(0,1)*iTL112', 
	 texname = '\\text{TL112}' ) 
 
TL113 = 	 Parameter(name='TL113', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTL113 + complex(0,1)*iTL113', 
	 texname = '\\text{TL113}' ) 
 
TL121 = 	 Parameter(name='TL121', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTL121 + complex(0,1)*iTL121', 
	 texname = '\\text{TL121}' ) 
 
TL122 = 	 Parameter(name='TL122', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTL122 + complex(0,1)*iTL122', 
	 texname = '\\text{TL122}' ) 
 
TL123 = 	 Parameter(name='TL123', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTL123 + complex(0,1)*iTL123', 
	 texname = '\\text{TL123}' ) 
 
TL131 = 	 Parameter(name='TL131', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTL131 + complex(0,1)*iTL131', 
	 texname = '\\text{TL131}' ) 
 
TL132 = 	 Parameter(name='TL132', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTL132 + complex(0,1)*iTL132', 
	 texname = '\\text{TL132}' ) 
 
TL133 = 	 Parameter(name='TL133', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTL133 + complex(0,1)*iTL133', 
	 texname = '\\text{TL133}' ) 
 
YQ111 = 	 Parameter(name='YQ111', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ111 + complex(0,1)*iYQ111', 
	 texname = '\\text{YQ111}' ) 
 
YQ112 = 	 Parameter(name='YQ112', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ112 + complex(0,1)*iYQ112', 
	 texname = '\\text{YQ112}' ) 
 
YQ113 = 	 Parameter(name='YQ113', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ113 + complex(0,1)*iYQ113', 
	 texname = '\\text{YQ113}' ) 
 
YQ121 = 	 Parameter(name='YQ121', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ121 + complex(0,1)*iYQ121', 
	 texname = '\\text{YQ121}' ) 
 
YQ122 = 	 Parameter(name='YQ122', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ122 + complex(0,1)*iYQ122', 
	 texname = '\\text{YQ122}' ) 
 
YQ123 = 	 Parameter(name='YQ123', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ123 + complex(0,1)*iYQ123', 
	 texname = '\\text{YQ123}' ) 
 
YQ131 = 	 Parameter(name='YQ131', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ131 + complex(0,1)*iYQ131', 
	 texname = '\\text{YQ131}' ) 
 
YQ132 = 	 Parameter(name='YQ132', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ132 + complex(0,1)*iYQ132', 
	 texname = '\\text{YQ132}' ) 
 
YQ133 = 	 Parameter(name='YQ133', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ133 + complex(0,1)*iYQ133', 
	 texname = '\\text{YQ133}' ) 
 
TQ111 = 	 Parameter(name='TQ111', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ111 + complex(0,1)*iTQ111', 
	 texname = '\\text{TQ111}' ) 
 
TQ112 = 	 Parameter(name='TQ112', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ112 + complex(0,1)*iTQ112', 
	 texname = '\\text{TQ112}' ) 
 
TQ113 = 	 Parameter(name='TQ113', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ113 + complex(0,1)*iTQ113', 
	 texname = '\\text{TQ113}' ) 
 
TQ121 = 	 Parameter(name='TQ121', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ121 + complex(0,1)*iTQ121', 
	 texname = '\\text{TQ121}' ) 
 
TQ122 = 	 Parameter(name='TQ122', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ122 + complex(0,1)*iTQ122', 
	 texname = '\\text{TQ122}' ) 
 
TQ123 = 	 Parameter(name='TQ123', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ123 + complex(0,1)*iTQ123', 
	 texname = '\\text{TQ123}' ) 
 
TQ131 = 	 Parameter(name='TQ131', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ131 + complex(0,1)*iTQ131', 
	 texname = '\\text{TQ131}' ) 
 
TQ132 = 	 Parameter(name='TQ132', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ132 + complex(0,1)*iTQ132', 
	 texname = '\\text{TQ132}' ) 
 
TQ133 = 	 Parameter(name='TQ133', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ133 + complex(0,1)*iTQ133', 
	 texname = '\\text{TQ133}' ) 
 
YQ211 = 	 Parameter(name='YQ211', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ211 + complex(0,1)*iYQ211', 
	 texname = '\\text{YQ211}' ) 
 
YQ212 = 	 Parameter(name='YQ212', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ212 + complex(0,1)*iYQ212', 
	 texname = '\\text{YQ212}' ) 
 
YQ213 = 	 Parameter(name='YQ213', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ213 + complex(0,1)*iYQ213', 
	 texname = '\\text{YQ213}' ) 
 
YQ221 = 	 Parameter(name='YQ221', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ221 + complex(0,1)*iYQ221', 
	 texname = '\\text{YQ221}' ) 
 
YQ222 = 	 Parameter(name='YQ222', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ222 + complex(0,1)*iYQ222', 
	 texname = '\\text{YQ222}' ) 
 
YQ223 = 	 Parameter(name='YQ223', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ223 + complex(0,1)*iYQ223', 
	 texname = '\\text{YQ223}' ) 
 
YQ231 = 	 Parameter(name='YQ231', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ231 + complex(0,1)*iYQ231', 
	 texname = '\\text{YQ231}' ) 
 
YQ232 = 	 Parameter(name='YQ232', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ232 + complex(0,1)*iYQ232', 
	 texname = '\\text{YQ232}' ) 
 
YQ233 = 	 Parameter(name='YQ233', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rYQ233 + complex(0,1)*iYQ233', 
	 texname = '\\text{YQ233}' ) 
 
TQ211 = 	 Parameter(name='TQ211', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ211 + complex(0,1)*iTQ211', 
	 texname = '\\text{TQ211}' ) 
 
TQ212 = 	 Parameter(name='TQ212', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ212 + complex(0,1)*iTQ212', 
	 texname = '\\text{TQ212}' ) 
 
TQ213 = 	 Parameter(name='TQ213', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ213 + complex(0,1)*iTQ213', 
	 texname = '\\text{TQ213}' ) 
 
TQ221 = 	 Parameter(name='TQ221', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ221 + complex(0,1)*iTQ221', 
	 texname = '\\text{TQ221}' ) 
 
TQ222 = 	 Parameter(name='TQ222', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ222 + complex(0,1)*iTQ222', 
	 texname = '\\text{TQ222}' ) 
 
TQ223 = 	 Parameter(name='TQ223', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ223 + complex(0,1)*iTQ223', 
	 texname = '\\text{TQ223}' ) 
 
TQ231 = 	 Parameter(name='TQ231', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ231 + complex(0,1)*iTQ231', 
	 texname = '\\text{TQ231}' ) 
 
TQ232 = 	 Parameter(name='TQ232', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ232 + complex(0,1)*iTQ232', 
	 texname = '\\text{TQ232}' ) 
 
TQ233 = 	 Parameter(name='TQ233', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rTQ233 + complex(0,1)*iTQ233', 
	 texname = '\\text{TQ233}' ) 
 
ZZ11 = 	 Parameter(name='ZZ11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ11 + complex(0,1)*iZZ11', 
	 texname = '\\text{ZZ11}' ) 
 
ZZ12 = 	 Parameter(name='ZZ12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ12 + complex(0,1)*iZZ12', 
	 texname = '\\text{ZZ12}' ) 
 
ZZ13 = 	 Parameter(name='ZZ13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ13 + complex(0,1)*iZZ13', 
	 texname = '\\text{ZZ13}' ) 
 
ZZ21 = 	 Parameter(name='ZZ21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ21 + complex(0,1)*iZZ21', 
	 texname = '\\text{ZZ21}' ) 
 
ZZ22 = 	 Parameter(name='ZZ22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ22 + complex(0,1)*iZZ22', 
	 texname = '\\text{ZZ22}' ) 
 
ZZ23 = 	 Parameter(name='ZZ23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ23 + complex(0,1)*iZZ23', 
	 texname = '\\text{ZZ23}' ) 
 
ZZ31 = 	 Parameter(name='ZZ31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ31 + complex(0,1)*iZZ31', 
	 texname = '\\text{ZZ31}' ) 
 
ZZ32 = 	 Parameter(name='ZZ32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ32 + complex(0,1)*iZZ32', 
	 texname = '\\text{ZZ32}' ) 
 
ZZ33 = 	 Parameter(name='ZZ33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZZ33 + complex(0,1)*iZZ33', 
	 texname = '\\text{ZZ33}' ) 
 
NN1k1 = 	 Parameter(name='NN1k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k1 + complex(0,1)*iNN1k1', 
	 texname = '\\text{NN1k1}' ) 
 
NN1k2 = 	 Parameter(name='NN1k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k2 + complex(0,1)*iNN1k2', 
	 texname = '\\text{NN1k2}' ) 
 
NN1k3 = 	 Parameter(name='NN1k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k3 + complex(0,1)*iNN1k3', 
	 texname = '\\text{NN1k3}' ) 
 
NN1k4 = 	 Parameter(name='NN1k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k4 + complex(0,1)*iNN1k4', 
	 texname = '\\text{NN1k4}' ) 
 
NN1k5 = 	 Parameter(name='NN1k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k5 + complex(0,1)*iNN1k5', 
	 texname = '\\text{NN1k5}' ) 
 
NN1k6 = 	 Parameter(name='NN1k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k6 + complex(0,1)*iNN1k6', 
	 texname = '\\text{NN1k6}' ) 
 
NN1k7 = 	 Parameter(name='NN1k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k7 + complex(0,1)*iNN1k7', 
	 texname = '\\text{NN1k7}' ) 
 
NN1k8 = 	 Parameter(name='NN1k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k8 + complex(0,1)*iNN1k8', 
	 texname = '\\text{NN1k8}' ) 
 
NN1k9 = 	 Parameter(name='NN1k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k9 + complex(0,1)*iNN1k9', 
	 texname = '\\text{NN1k9}' ) 
 
NN1k10 = 	 Parameter(name='NN1k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k10 + complex(0,1)*iNN1k10', 
	 texname = '\\text{NN1k10}' ) 
 
NN1k11 = 	 Parameter(name='NN1k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k11 + complex(0,1)*iNN1k11', 
	 texname = '\\text{NN1k11}' ) 
 
NN1k12 = 	 Parameter(name='NN1k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN1k12 + complex(0,1)*iNN1k12', 
	 texname = '\\text{NN1k12}' ) 
 
NN2k1 = 	 Parameter(name='NN2k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k1 + complex(0,1)*iNN2k1', 
	 texname = '\\text{NN2k1}' ) 
 
NN2k2 = 	 Parameter(name='NN2k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k2 + complex(0,1)*iNN2k2', 
	 texname = '\\text{NN2k2}' ) 
 
NN2k3 = 	 Parameter(name='NN2k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k3 + complex(0,1)*iNN2k3', 
	 texname = '\\text{NN2k3}' ) 
 
NN2k4 = 	 Parameter(name='NN2k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k4 + complex(0,1)*iNN2k4', 
	 texname = '\\text{NN2k4}' ) 
 
NN2k5 = 	 Parameter(name='NN2k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k5 + complex(0,1)*iNN2k5', 
	 texname = '\\text{NN2k5}' ) 
 
NN2k6 = 	 Parameter(name='NN2k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k6 + complex(0,1)*iNN2k6', 
	 texname = '\\text{NN2k6}' ) 
 
NN2k7 = 	 Parameter(name='NN2k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k7 + complex(0,1)*iNN2k7', 
	 texname = '\\text{NN2k7}' ) 
 
NN2k8 = 	 Parameter(name='NN2k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k8 + complex(0,1)*iNN2k8', 
	 texname = '\\text{NN2k8}' ) 
 
NN2k9 = 	 Parameter(name='NN2k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k9 + complex(0,1)*iNN2k9', 
	 texname = '\\text{NN2k9}' ) 
 
NN2k10 = 	 Parameter(name='NN2k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k10 + complex(0,1)*iNN2k10', 
	 texname = '\\text{NN2k10}' ) 
 
NN2k11 = 	 Parameter(name='NN2k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k11 + complex(0,1)*iNN2k11', 
	 texname = '\\text{NN2k11}' ) 
 
NN2k12 = 	 Parameter(name='NN2k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN2k12 + complex(0,1)*iNN2k12', 
	 texname = '\\text{NN2k12}' ) 
 
NN3k1 = 	 Parameter(name='NN3k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k1 + complex(0,1)*iNN3k1', 
	 texname = '\\text{NN3k1}' ) 
 
NN3k2 = 	 Parameter(name='NN3k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k2 + complex(0,1)*iNN3k2', 
	 texname = '\\text{NN3k2}' ) 
 
NN3k3 = 	 Parameter(name='NN3k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k3 + complex(0,1)*iNN3k3', 
	 texname = '\\text{NN3k3}' ) 
 
NN3k4 = 	 Parameter(name='NN3k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k4 + complex(0,1)*iNN3k4', 
	 texname = '\\text{NN3k4}' ) 
 
NN3k5 = 	 Parameter(name='NN3k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k5 + complex(0,1)*iNN3k5', 
	 texname = '\\text{NN3k5}' ) 
 
NN3k6 = 	 Parameter(name='NN3k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k6 + complex(0,1)*iNN3k6', 
	 texname = '\\text{NN3k6}' ) 
 
NN3k7 = 	 Parameter(name='NN3k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k7 + complex(0,1)*iNN3k7', 
	 texname = '\\text{NN3k7}' ) 
 
NN3k8 = 	 Parameter(name='NN3k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k8 + complex(0,1)*iNN3k8', 
	 texname = '\\text{NN3k8}' ) 
 
NN3k9 = 	 Parameter(name='NN3k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k9 + complex(0,1)*iNN3k9', 
	 texname = '\\text{NN3k9}' ) 
 
NN3k10 = 	 Parameter(name='NN3k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k10 + complex(0,1)*iNN3k10', 
	 texname = '\\text{NN3k10}' ) 
 
NN3k11 = 	 Parameter(name='NN3k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k11 + complex(0,1)*iNN3k11', 
	 texname = '\\text{NN3k11}' ) 
 
NN3k12 = 	 Parameter(name='NN3k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN3k12 + complex(0,1)*iNN3k12', 
	 texname = '\\text{NN3k12}' ) 
 
NN4k1 = 	 Parameter(name='NN4k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k1 + complex(0,1)*iNN4k1', 
	 texname = '\\text{NN4k1}' ) 
 
NN4k2 = 	 Parameter(name='NN4k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k2 + complex(0,1)*iNN4k2', 
	 texname = '\\text{NN4k2}' ) 
 
NN4k3 = 	 Parameter(name='NN4k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k3 + complex(0,1)*iNN4k3', 
	 texname = '\\text{NN4k3}' ) 
 
NN4k4 = 	 Parameter(name='NN4k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k4 + complex(0,1)*iNN4k4', 
	 texname = '\\text{NN4k4}' ) 
 
NN4k5 = 	 Parameter(name='NN4k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k5 + complex(0,1)*iNN4k5', 
	 texname = '\\text{NN4k5}' ) 
 
NN4k6 = 	 Parameter(name='NN4k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k6 + complex(0,1)*iNN4k6', 
	 texname = '\\text{NN4k6}' ) 
 
NN4k7 = 	 Parameter(name='NN4k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k7 + complex(0,1)*iNN4k7', 
	 texname = '\\text{NN4k7}' ) 
 
NN4k8 = 	 Parameter(name='NN4k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k8 + complex(0,1)*iNN4k8', 
	 texname = '\\text{NN4k8}' ) 
 
NN4k9 = 	 Parameter(name='NN4k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k9 + complex(0,1)*iNN4k9', 
	 texname = '\\text{NN4k9}' ) 
 
NN4k10 = 	 Parameter(name='NN4k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k10 + complex(0,1)*iNN4k10', 
	 texname = '\\text{NN4k10}' ) 
 
NN4k11 = 	 Parameter(name='NN4k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k11 + complex(0,1)*iNN4k11', 
	 texname = '\\text{NN4k11}' ) 
 
NN4k12 = 	 Parameter(name='NN4k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN4k12 + complex(0,1)*iNN4k12', 
	 texname = '\\text{NN4k12}' ) 
 
NN5k1 = 	 Parameter(name='NN5k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k1 + complex(0,1)*iNN5k1', 
	 texname = '\\text{NN5k1}' ) 
 
NN5k2 = 	 Parameter(name='NN5k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k2 + complex(0,1)*iNN5k2', 
	 texname = '\\text{NN5k2}' ) 
 
NN5k3 = 	 Parameter(name='NN5k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k3 + complex(0,1)*iNN5k3', 
	 texname = '\\text{NN5k3}' ) 
 
NN5k4 = 	 Parameter(name='NN5k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k4 + complex(0,1)*iNN5k4', 
	 texname = '\\text{NN5k4}' ) 
 
NN5k5 = 	 Parameter(name='NN5k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k5 + complex(0,1)*iNN5k5', 
	 texname = '\\text{NN5k5}' ) 
 
NN5k6 = 	 Parameter(name='NN5k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k6 + complex(0,1)*iNN5k6', 
	 texname = '\\text{NN5k6}' ) 
 
NN5k7 = 	 Parameter(name='NN5k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k7 + complex(0,1)*iNN5k7', 
	 texname = '\\text{NN5k7}' ) 
 
NN5k8 = 	 Parameter(name='NN5k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k8 + complex(0,1)*iNN5k8', 
	 texname = '\\text{NN5k8}' ) 
 
NN5k9 = 	 Parameter(name='NN5k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k9 + complex(0,1)*iNN5k9', 
	 texname = '\\text{NN5k9}' ) 
 
NN5k10 = 	 Parameter(name='NN5k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k10 + complex(0,1)*iNN5k10', 
	 texname = '\\text{NN5k10}' ) 
 
NN5k11 = 	 Parameter(name='NN5k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k11 + complex(0,1)*iNN5k11', 
	 texname = '\\text{NN5k11}' ) 
 
NN5k12 = 	 Parameter(name='NN5k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN5k12 + complex(0,1)*iNN5k12', 
	 texname = '\\text{NN5k12}' ) 
 
NN6k1 = 	 Parameter(name='NN6k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k1 + complex(0,1)*iNN6k1', 
	 texname = '\\text{NN6k1}' ) 
 
NN6k2 = 	 Parameter(name='NN6k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k2 + complex(0,1)*iNN6k2', 
	 texname = '\\text{NN6k2}' ) 
 
NN6k3 = 	 Parameter(name='NN6k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k3 + complex(0,1)*iNN6k3', 
	 texname = '\\text{NN6k3}' ) 
 
NN6k4 = 	 Parameter(name='NN6k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k4 + complex(0,1)*iNN6k4', 
	 texname = '\\text{NN6k4}' ) 
 
NN6k5 = 	 Parameter(name='NN6k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k5 + complex(0,1)*iNN6k5', 
	 texname = '\\text{NN6k5}' ) 
 
NN6k6 = 	 Parameter(name='NN6k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k6 + complex(0,1)*iNN6k6', 
	 texname = '\\text{NN6k6}' ) 
 
NN6k7 = 	 Parameter(name='NN6k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k7 + complex(0,1)*iNN6k7', 
	 texname = '\\text{NN6k7}' ) 
 
NN6k8 = 	 Parameter(name='NN6k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k8 + complex(0,1)*iNN6k8', 
	 texname = '\\text{NN6k8}' ) 
 
NN6k9 = 	 Parameter(name='NN6k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k9 + complex(0,1)*iNN6k9', 
	 texname = '\\text{NN6k9}' ) 
 
NN6k10 = 	 Parameter(name='NN6k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k10 + complex(0,1)*iNN6k10', 
	 texname = '\\text{NN6k10}' ) 
 
NN6k11 = 	 Parameter(name='NN6k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k11 + complex(0,1)*iNN6k11', 
	 texname = '\\text{NN6k11}' ) 
 
NN6k12 = 	 Parameter(name='NN6k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN6k12 + complex(0,1)*iNN6k12', 
	 texname = '\\text{NN6k12}' ) 
 
NN7k1 = 	 Parameter(name='NN7k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k1 + complex(0,1)*iNN7k1', 
	 texname = '\\text{NN7k1}' ) 
 
NN7k2 = 	 Parameter(name='NN7k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k2 + complex(0,1)*iNN7k2', 
	 texname = '\\text{NN7k2}' ) 
 
NN7k3 = 	 Parameter(name='NN7k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k3 + complex(0,1)*iNN7k3', 
	 texname = '\\text{NN7k3}' ) 
 
NN7k4 = 	 Parameter(name='NN7k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k4 + complex(0,1)*iNN7k4', 
	 texname = '\\text{NN7k4}' ) 
 
NN7k5 = 	 Parameter(name='NN7k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k5 + complex(0,1)*iNN7k5', 
	 texname = '\\text{NN7k5}' ) 
 
NN7k6 = 	 Parameter(name='NN7k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k6 + complex(0,1)*iNN7k6', 
	 texname = '\\text{NN7k6}' ) 
 
NN7k7 = 	 Parameter(name='NN7k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k7 + complex(0,1)*iNN7k7', 
	 texname = '\\text{NN7k7}' ) 
 
NN7k8 = 	 Parameter(name='NN7k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k8 + complex(0,1)*iNN7k8', 
	 texname = '\\text{NN7k8}' ) 
 
NN7k9 = 	 Parameter(name='NN7k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k9 + complex(0,1)*iNN7k9', 
	 texname = '\\text{NN7k9}' ) 
 
NN7k10 = 	 Parameter(name='NN7k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k10 + complex(0,1)*iNN7k10', 
	 texname = '\\text{NN7k10}' ) 
 
NN7k11 = 	 Parameter(name='NN7k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k11 + complex(0,1)*iNN7k11', 
	 texname = '\\text{NN7k11}' ) 
 
NN7k12 = 	 Parameter(name='NN7k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN7k12 + complex(0,1)*iNN7k12', 
	 texname = '\\text{NN7k12}' ) 
 
NN8k1 = 	 Parameter(name='NN8k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k1 + complex(0,1)*iNN8k1', 
	 texname = '\\text{NN8k1}' ) 
 
NN8k2 = 	 Parameter(name='NN8k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k2 + complex(0,1)*iNN8k2', 
	 texname = '\\text{NN8k2}' ) 
 
NN8k3 = 	 Parameter(name='NN8k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k3 + complex(0,1)*iNN8k3', 
	 texname = '\\text{NN8k3}' ) 
 
NN8k4 = 	 Parameter(name='NN8k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k4 + complex(0,1)*iNN8k4', 
	 texname = '\\text{NN8k4}' ) 
 
NN8k5 = 	 Parameter(name='NN8k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k5 + complex(0,1)*iNN8k5', 
	 texname = '\\text{NN8k5}' ) 
 
NN8k6 = 	 Parameter(name='NN8k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k6 + complex(0,1)*iNN8k6', 
	 texname = '\\text{NN8k6}' ) 
 
NN8k7 = 	 Parameter(name='NN8k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k7 + complex(0,1)*iNN8k7', 
	 texname = '\\text{NN8k7}' ) 
 
NN8k8 = 	 Parameter(name='NN8k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k8 + complex(0,1)*iNN8k8', 
	 texname = '\\text{NN8k8}' ) 
 
NN8k9 = 	 Parameter(name='NN8k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k9 + complex(0,1)*iNN8k9', 
	 texname = '\\text{NN8k9}' ) 
 
NN8k10 = 	 Parameter(name='NN8k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k10 + complex(0,1)*iNN8k10', 
	 texname = '\\text{NN8k10}' ) 
 
NN8k11 = 	 Parameter(name='NN8k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k11 + complex(0,1)*iNN8k11', 
	 texname = '\\text{NN8k11}' ) 
 
NN8k12 = 	 Parameter(name='NN8k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN8k12 + complex(0,1)*iNN8k12', 
	 texname = '\\text{NN8k12}' ) 
 
NN9k1 = 	 Parameter(name='NN9k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k1 + complex(0,1)*iNN9k1', 
	 texname = '\\text{NN9k1}' ) 
 
NN9k2 = 	 Parameter(name='NN9k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k2 + complex(0,1)*iNN9k2', 
	 texname = '\\text{NN9k2}' ) 
 
NN9k3 = 	 Parameter(name='NN9k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k3 + complex(0,1)*iNN9k3', 
	 texname = '\\text{NN9k3}' ) 
 
NN9k4 = 	 Parameter(name='NN9k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k4 + complex(0,1)*iNN9k4', 
	 texname = '\\text{NN9k4}' ) 
 
NN9k5 = 	 Parameter(name='NN9k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k5 + complex(0,1)*iNN9k5', 
	 texname = '\\text{NN9k5}' ) 
 
NN9k6 = 	 Parameter(name='NN9k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k6 + complex(0,1)*iNN9k6', 
	 texname = '\\text{NN9k6}' ) 
 
NN9k7 = 	 Parameter(name='NN9k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k7 + complex(0,1)*iNN9k7', 
	 texname = '\\text{NN9k7}' ) 
 
NN9k8 = 	 Parameter(name='NN9k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k8 + complex(0,1)*iNN9k8', 
	 texname = '\\text{NN9k8}' ) 
 
NN9k9 = 	 Parameter(name='NN9k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k9 + complex(0,1)*iNN9k9', 
	 texname = '\\text{NN9k9}' ) 
 
NN9k10 = 	 Parameter(name='NN9k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k10 + complex(0,1)*iNN9k10', 
	 texname = '\\text{NN9k10}' ) 
 
NN9k11 = 	 Parameter(name='NN9k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k11 + complex(0,1)*iNN9k11', 
	 texname = '\\text{NN9k11}' ) 
 
NN9k12 = 	 Parameter(name='NN9k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN9k12 + complex(0,1)*iNN9k12', 
	 texname = '\\text{NN9k12}' ) 
 
NN10k1 = 	 Parameter(name='NN10k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k1 + complex(0,1)*iNN10k1', 
	 texname = '\\text{NN10k1}' ) 
 
NN10k2 = 	 Parameter(name='NN10k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k2 + complex(0,1)*iNN10k2', 
	 texname = '\\text{NN10k2}' ) 
 
NN10k3 = 	 Parameter(name='NN10k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k3 + complex(0,1)*iNN10k3', 
	 texname = '\\text{NN10k3}' ) 
 
NN10k4 = 	 Parameter(name='NN10k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k4 + complex(0,1)*iNN10k4', 
	 texname = '\\text{NN10k4}' ) 
 
NN10k5 = 	 Parameter(name='NN10k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k5 + complex(0,1)*iNN10k5', 
	 texname = '\\text{NN10k5}' ) 
 
NN10k6 = 	 Parameter(name='NN10k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k6 + complex(0,1)*iNN10k6', 
	 texname = '\\text{NN10k6}' ) 
 
NN10k7 = 	 Parameter(name='NN10k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k7 + complex(0,1)*iNN10k7', 
	 texname = '\\text{NN10k7}' ) 
 
NN10k8 = 	 Parameter(name='NN10k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k8 + complex(0,1)*iNN10k8', 
	 texname = '\\text{NN10k8}' ) 
 
NN10k9 = 	 Parameter(name='NN10k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k9 + complex(0,1)*iNN10k9', 
	 texname = '\\text{NN10k9}' ) 
 
NN10k10 = 	 Parameter(name='NN10k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k10 + complex(0,1)*iNN10k10', 
	 texname = '\\text{NN10k10}' ) 
 
NN10k11 = 	 Parameter(name='NN10k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k11 + complex(0,1)*iNN10k11', 
	 texname = '\\text{NN10k11}' ) 
 
NN10k12 = 	 Parameter(name='NN10k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN10k12 + complex(0,1)*iNN10k12', 
	 texname = '\\text{NN10k12}' ) 
 
NN11k1 = 	 Parameter(name='NN11k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k1 + complex(0,1)*iNN11k1', 
	 texname = '\\text{NN11k1}' ) 
 
NN11k2 = 	 Parameter(name='NN11k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k2 + complex(0,1)*iNN11k2', 
	 texname = '\\text{NN11k2}' ) 
 
NN11k3 = 	 Parameter(name='NN11k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k3 + complex(0,1)*iNN11k3', 
	 texname = '\\text{NN11k3}' ) 
 
NN11k4 = 	 Parameter(name='NN11k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k4 + complex(0,1)*iNN11k4', 
	 texname = '\\text{NN11k4}' ) 
 
NN11k5 = 	 Parameter(name='NN11k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k5 + complex(0,1)*iNN11k5', 
	 texname = '\\text{NN11k5}' ) 
 
NN11k6 = 	 Parameter(name='NN11k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k6 + complex(0,1)*iNN11k6', 
	 texname = '\\text{NN11k6}' ) 
 
NN11k7 = 	 Parameter(name='NN11k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k7 + complex(0,1)*iNN11k7', 
	 texname = '\\text{NN11k7}' ) 
 
NN11k8 = 	 Parameter(name='NN11k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k8 + complex(0,1)*iNN11k8', 
	 texname = '\\text{NN11k8}' ) 
 
NN11k9 = 	 Parameter(name='NN11k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k9 + complex(0,1)*iNN11k9', 
	 texname = '\\text{NN11k9}' ) 
 
NN11k10 = 	 Parameter(name='NN11k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k10 + complex(0,1)*iNN11k10', 
	 texname = '\\text{NN11k10}' ) 
 
NN11k11 = 	 Parameter(name='NN11k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k11 + complex(0,1)*iNN11k11', 
	 texname = '\\text{NN11k11}' ) 
 
NN11k12 = 	 Parameter(name='NN11k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN11k12 + complex(0,1)*iNN11k12', 
	 texname = '\\text{NN11k12}' ) 
 
NN12k1 = 	 Parameter(name='NN12k1', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k1 + complex(0,1)*iNN12k1', 
	 texname = '\\text{NN12k1}' ) 
 
NN12k2 = 	 Parameter(name='NN12k2', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k2 + complex(0,1)*iNN12k2', 
	 texname = '\\text{NN12k2}' ) 
 
NN12k3 = 	 Parameter(name='NN12k3', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k3 + complex(0,1)*iNN12k3', 
	 texname = '\\text{NN12k3}' ) 
 
NN12k4 = 	 Parameter(name='NN12k4', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k4 + complex(0,1)*iNN12k4', 
	 texname = '\\text{NN12k4}' ) 
 
NN12k5 = 	 Parameter(name='NN12k5', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k5 + complex(0,1)*iNN12k5', 
	 texname = '\\text{NN12k5}' ) 
 
NN12k6 = 	 Parameter(name='NN12k6', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k6 + complex(0,1)*iNN12k6', 
	 texname = '\\text{NN12k6}' ) 
 
NN12k7 = 	 Parameter(name='NN12k7', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k7 + complex(0,1)*iNN12k7', 
	 texname = '\\text{NN12k7}' ) 
 
NN12k8 = 	 Parameter(name='NN12k8', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k8 + complex(0,1)*iNN12k8', 
	 texname = '\\text{NN12k8}' ) 
 
NN12k9 = 	 Parameter(name='NN12k9', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k9 + complex(0,1)*iNN12k9', 
	 texname = '\\text{NN12k9}' ) 
 
NN12k10 = 	 Parameter(name='NN12k10', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k10 + complex(0,1)*iNN12k10', 
	 texname = '\\text{NN12k10}' ) 
 
NN12k11 = 	 Parameter(name='NN12k11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k11 + complex(0,1)*iNN12k11', 
	 texname = '\\text{NN12k11}' ) 
 
NN12k12 = 	 Parameter(name='NN12k12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rNN12k12 + complex(0,1)*iNN12k12', 
	 texname = '\\text{NN12k12}' ) 
 
UU11 = 	 Parameter(name='UU11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU11 + complex(0,1)*iUU11', 
	 texname = '\\text{UU11}' ) 
 
UU12 = 	 Parameter(name='UU12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU12 + complex(0,1)*iUU12', 
	 texname = '\\text{UU12}' ) 
 
UU13 = 	 Parameter(name='UU13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU13 + complex(0,1)*iUU13', 
	 texname = '\\text{UU13}' ) 
 
UU14 = 	 Parameter(name='UU14', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU14 + complex(0,1)*iUU14', 
	 texname = '\\text{UU14}' ) 
 
UU15 = 	 Parameter(name='UU15', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU15 + complex(0,1)*iUU15', 
	 texname = '\\text{UU15}' ) 
 
UU16 = 	 Parameter(name='UU16', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU16 + complex(0,1)*iUU16', 
	 texname = '\\text{UU16}' ) 
 
UU21 = 	 Parameter(name='UU21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU21 + complex(0,1)*iUU21', 
	 texname = '\\text{UU21}' ) 
 
UU22 = 	 Parameter(name='UU22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU22 + complex(0,1)*iUU22', 
	 texname = '\\text{UU22}' ) 
 
UU23 = 	 Parameter(name='UU23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU23 + complex(0,1)*iUU23', 
	 texname = '\\text{UU23}' ) 
 
UU24 = 	 Parameter(name='UU24', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU24 + complex(0,1)*iUU24', 
	 texname = '\\text{UU24}' ) 
 
UU25 = 	 Parameter(name='UU25', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU25 + complex(0,1)*iUU25', 
	 texname = '\\text{UU25}' ) 
 
UU26 = 	 Parameter(name='UU26', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU26 + complex(0,1)*iUU26', 
	 texname = '\\text{UU26}' ) 
 
UU31 = 	 Parameter(name='UU31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU31 + complex(0,1)*iUU31', 
	 texname = '\\text{UU31}' ) 
 
UU32 = 	 Parameter(name='UU32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU32 + complex(0,1)*iUU32', 
	 texname = '\\text{UU32}' ) 
 
UU33 = 	 Parameter(name='UU33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU33 + complex(0,1)*iUU33', 
	 texname = '\\text{UU33}' ) 
 
UU34 = 	 Parameter(name='UU34', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU34 + complex(0,1)*iUU34', 
	 texname = '\\text{UU34}' ) 
 
UU35 = 	 Parameter(name='UU35', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU35 + complex(0,1)*iUU35', 
	 texname = '\\text{UU35}' ) 
 
UU36 = 	 Parameter(name='UU36', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU36 + complex(0,1)*iUU36', 
	 texname = '\\text{UU36}' ) 
 
UU41 = 	 Parameter(name='UU41', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU41 + complex(0,1)*iUU41', 
	 texname = '\\text{UU41}' ) 
 
UU42 = 	 Parameter(name='UU42', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU42 + complex(0,1)*iUU42', 
	 texname = '\\text{UU42}' ) 
 
UU43 = 	 Parameter(name='UU43', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU43 + complex(0,1)*iUU43', 
	 texname = '\\text{UU43}' ) 
 
UU44 = 	 Parameter(name='UU44', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU44 + complex(0,1)*iUU44', 
	 texname = '\\text{UU44}' ) 
 
UU45 = 	 Parameter(name='UU45', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU45 + complex(0,1)*iUU45', 
	 texname = '\\text{UU45}' ) 
 
UU46 = 	 Parameter(name='UU46', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU46 + complex(0,1)*iUU46', 
	 texname = '\\text{UU46}' ) 
 
UU51 = 	 Parameter(name='UU51', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU51 + complex(0,1)*iUU51', 
	 texname = '\\text{UU51}' ) 
 
UU52 = 	 Parameter(name='UU52', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU52 + complex(0,1)*iUU52', 
	 texname = '\\text{UU52}' ) 
 
UU53 = 	 Parameter(name='UU53', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU53 + complex(0,1)*iUU53', 
	 texname = '\\text{UU53}' ) 
 
UU54 = 	 Parameter(name='UU54', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU54 + complex(0,1)*iUU54', 
	 texname = '\\text{UU54}' ) 
 
UU55 = 	 Parameter(name='UU55', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU55 + complex(0,1)*iUU55', 
	 texname = '\\text{UU55}' ) 
 
UU56 = 	 Parameter(name='UU56', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU56 + complex(0,1)*iUU56', 
	 texname = '\\text{UU56}' ) 
 
UU61 = 	 Parameter(name='UU61', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU61 + complex(0,1)*iUU61', 
	 texname = '\\text{UU61}' ) 
 
UU62 = 	 Parameter(name='UU62', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU62 + complex(0,1)*iUU62', 
	 texname = '\\text{UU62}' ) 
 
UU63 = 	 Parameter(name='UU63', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU63 + complex(0,1)*iUU63', 
	 texname = '\\text{UU63}' ) 
 
UU64 = 	 Parameter(name='UU64', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU64 + complex(0,1)*iUU64', 
	 texname = '\\text{UU64}' ) 
 
UU65 = 	 Parameter(name='UU65', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU65 + complex(0,1)*iUU65', 
	 texname = '\\text{UU65}' ) 
 
UU66 = 	 Parameter(name='UU66', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUU66 + complex(0,1)*iUU66', 
	 texname = '\\text{UU66}' ) 
 
VV11 = 	 Parameter(name='VV11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV11 + complex(0,1)*iVV11', 
	 texname = '\\text{VV11}' ) 
 
VV12 = 	 Parameter(name='VV12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV12 + complex(0,1)*iVV12', 
	 texname = '\\text{VV12}' ) 
 
VV13 = 	 Parameter(name='VV13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV13 + complex(0,1)*iVV13', 
	 texname = '\\text{VV13}' ) 
 
VV14 = 	 Parameter(name='VV14', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV14 + complex(0,1)*iVV14', 
	 texname = '\\text{VV14}' ) 
 
VV15 = 	 Parameter(name='VV15', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV15 + complex(0,1)*iVV15', 
	 texname = '\\text{VV15}' ) 
 
VV16 = 	 Parameter(name='VV16', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV16 + complex(0,1)*iVV16', 
	 texname = '\\text{VV16}' ) 
 
VV21 = 	 Parameter(name='VV21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV21 + complex(0,1)*iVV21', 
	 texname = '\\text{VV21}' ) 
 
VV22 = 	 Parameter(name='VV22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV22 + complex(0,1)*iVV22', 
	 texname = '\\text{VV22}' ) 
 
VV23 = 	 Parameter(name='VV23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV23 + complex(0,1)*iVV23', 
	 texname = '\\text{VV23}' ) 
 
VV24 = 	 Parameter(name='VV24', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV24 + complex(0,1)*iVV24', 
	 texname = '\\text{VV24}' ) 
 
VV25 = 	 Parameter(name='VV25', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV25 + complex(0,1)*iVV25', 
	 texname = '\\text{VV25}' ) 
 
VV26 = 	 Parameter(name='VV26', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV26 + complex(0,1)*iVV26', 
	 texname = '\\text{VV26}' ) 
 
VV31 = 	 Parameter(name='VV31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV31 + complex(0,1)*iVV31', 
	 texname = '\\text{VV31}' ) 
 
VV32 = 	 Parameter(name='VV32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV32 + complex(0,1)*iVV32', 
	 texname = '\\text{VV32}' ) 
 
VV33 = 	 Parameter(name='VV33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV33 + complex(0,1)*iVV33', 
	 texname = '\\text{VV33}' ) 
 
VV34 = 	 Parameter(name='VV34', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV34 + complex(0,1)*iVV34', 
	 texname = '\\text{VV34}' ) 
 
VV35 = 	 Parameter(name='VV35', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV35 + complex(0,1)*iVV35', 
	 texname = '\\text{VV35}' ) 
 
VV36 = 	 Parameter(name='VV36', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV36 + complex(0,1)*iVV36', 
	 texname = '\\text{VV36}' ) 
 
VV41 = 	 Parameter(name='VV41', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV41 + complex(0,1)*iVV41', 
	 texname = '\\text{VV41}' ) 
 
VV42 = 	 Parameter(name='VV42', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV42 + complex(0,1)*iVV42', 
	 texname = '\\text{VV42}' ) 
 
VV43 = 	 Parameter(name='VV43', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV43 + complex(0,1)*iVV43', 
	 texname = '\\text{VV43}' ) 
 
VV44 = 	 Parameter(name='VV44', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV44 + complex(0,1)*iVV44', 
	 texname = '\\text{VV44}' ) 
 
VV45 = 	 Parameter(name='VV45', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV45 + complex(0,1)*iVV45', 
	 texname = '\\text{VV45}' ) 
 
VV46 = 	 Parameter(name='VV46', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV46 + complex(0,1)*iVV46', 
	 texname = '\\text{VV46}' ) 
 
VV51 = 	 Parameter(name='VV51', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV51 + complex(0,1)*iVV51', 
	 texname = '\\text{VV51}' ) 
 
VV52 = 	 Parameter(name='VV52', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV52 + complex(0,1)*iVV52', 
	 texname = '\\text{VV52}' ) 
 
VV53 = 	 Parameter(name='VV53', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV53 + complex(0,1)*iVV53', 
	 texname = '\\text{VV53}' ) 
 
VV54 = 	 Parameter(name='VV54', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV54 + complex(0,1)*iVV54', 
	 texname = '\\text{VV54}' ) 
 
VV55 = 	 Parameter(name='VV55', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV55 + complex(0,1)*iVV55', 
	 texname = '\\text{VV55}' ) 
 
VV56 = 	 Parameter(name='VV56', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV56 + complex(0,1)*iVV56', 
	 texname = '\\text{VV56}' ) 
 
VV61 = 	 Parameter(name='VV61', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV61 + complex(0,1)*iVV61', 
	 texname = '\\text{VV61}' ) 
 
VV62 = 	 Parameter(name='VV62', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV62 + complex(0,1)*iVV62', 
	 texname = '\\text{VV62}' ) 
 
VV63 = 	 Parameter(name='VV63', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV63 + complex(0,1)*iVV63', 
	 texname = '\\text{VV63}' ) 
 
VV64 = 	 Parameter(name='VV64', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV64 + complex(0,1)*iVV64', 
	 texname = '\\text{VV64}' ) 
 
VV65 = 	 Parameter(name='VV65', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV65 + complex(0,1)*iVV65', 
	 texname = '\\text{VV65}' ) 
 
VV66 = 	 Parameter(name='VV66', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rVV66 + complex(0,1)*iVV66', 
	 texname = '\\text{VV66}' ) 
 
UMM11 = 	 Parameter(name='UMM11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUMM11 + complex(0,1)*iUMM11', 
	 texname = '\\text{UMM11}' ) 
 
UMM12 = 	 Parameter(name='UMM12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUMM12 + complex(0,1)*iUMM12', 
	 texname = '\\text{UMM12}' ) 
 
UMM21 = 	 Parameter(name='UMM21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUMM21 + complex(0,1)*iUMM21', 
	 texname = '\\text{UMM21}' ) 
 
UMM22 = 	 Parameter(name='UMM22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUMM22 + complex(0,1)*iUMM22', 
	 texname = '\\text{UMM22}' ) 
 
UPP11 = 	 Parameter(name='UPP11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUPP11 + complex(0,1)*iUPP11', 
	 texname = '\\text{UPP11}' ) 
 
UPP12 = 	 Parameter(name='UPP12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUPP12 + complex(0,1)*iUPP12', 
	 texname = '\\text{UPP12}' ) 
 
UPP21 = 	 Parameter(name='UPP21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUPP21 + complex(0,1)*iUPP21', 
	 texname = '\\text{UPP21}' ) 
 
UPP22 = 	 Parameter(name='UPP22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUPP22 + complex(0,1)*iUPP22', 
	 texname = '\\text{UPP22}' ) 
 
UV11 = 	 Parameter(name='UV11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV11 + complex(0,1)*iUV11', 
	 texname = '\\text{UV11}' ) 
 
UV12 = 	 Parameter(name='UV12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV12 + complex(0,1)*iUV12', 
	 texname = '\\text{UV12}' ) 
 
UV13 = 	 Parameter(name='UV13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV13 + complex(0,1)*iUV13', 
	 texname = '\\text{UV13}' ) 
 
UV14 = 	 Parameter(name='UV14', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV14 + complex(0,1)*iUV14', 
	 texname = '\\text{UV14}' ) 
 
UV15 = 	 Parameter(name='UV15', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV15 + complex(0,1)*iUV15', 
	 texname = '\\text{UV15}' ) 
 
UV16 = 	 Parameter(name='UV16', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV16 + complex(0,1)*iUV16', 
	 texname = '\\text{UV16}' ) 
 
UV21 = 	 Parameter(name='UV21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV21 + complex(0,1)*iUV21', 
	 texname = '\\text{UV21}' ) 
 
UV22 = 	 Parameter(name='UV22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV22 + complex(0,1)*iUV22', 
	 texname = '\\text{UV22}' ) 
 
UV23 = 	 Parameter(name='UV23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV23 + complex(0,1)*iUV23', 
	 texname = '\\text{UV23}' ) 
 
UV24 = 	 Parameter(name='UV24', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV24 + complex(0,1)*iUV24', 
	 texname = '\\text{UV24}' ) 
 
UV25 = 	 Parameter(name='UV25', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV25 + complex(0,1)*iUV25', 
	 texname = '\\text{UV25}' ) 
 
UV26 = 	 Parameter(name='UV26', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV26 + complex(0,1)*iUV26', 
	 texname = '\\text{UV26}' ) 
 
UV31 = 	 Parameter(name='UV31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV31 + complex(0,1)*iUV31', 
	 texname = '\\text{UV31}' ) 
 
UV32 = 	 Parameter(name='UV32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV32 + complex(0,1)*iUV32', 
	 texname = '\\text{UV32}' ) 
 
UV33 = 	 Parameter(name='UV33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV33 + complex(0,1)*iUV33', 
	 texname = '\\text{UV33}' ) 
 
UV34 = 	 Parameter(name='UV34', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV34 + complex(0,1)*iUV34', 
	 texname = '\\text{UV34}' ) 
 
UV35 = 	 Parameter(name='UV35', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV35 + complex(0,1)*iUV35', 
	 texname = '\\text{UV35}' ) 
 
UV36 = 	 Parameter(name='UV36', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV36 + complex(0,1)*iUV36', 
	 texname = '\\text{UV36}' ) 
 
UV41 = 	 Parameter(name='UV41', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV41 + complex(0,1)*iUV41', 
	 texname = '\\text{UV41}' ) 
 
UV42 = 	 Parameter(name='UV42', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV42 + complex(0,1)*iUV42', 
	 texname = '\\text{UV42}' ) 
 
UV43 = 	 Parameter(name='UV43', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV43 + complex(0,1)*iUV43', 
	 texname = '\\text{UV43}' ) 
 
UV44 = 	 Parameter(name='UV44', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV44 + complex(0,1)*iUV44', 
	 texname = '\\text{UV44}' ) 
 
UV45 = 	 Parameter(name='UV45', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV45 + complex(0,1)*iUV45', 
	 texname = '\\text{UV45}' ) 
 
UV46 = 	 Parameter(name='UV46', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV46 + complex(0,1)*iUV46', 
	 texname = '\\text{UV46}' ) 
 
UV51 = 	 Parameter(name='UV51', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV51 + complex(0,1)*iUV51', 
	 texname = '\\text{UV51}' ) 
 
UV52 = 	 Parameter(name='UV52', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV52 + complex(0,1)*iUV52', 
	 texname = '\\text{UV52}' ) 
 
UV53 = 	 Parameter(name='UV53', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV53 + complex(0,1)*iUV53', 
	 texname = '\\text{UV53}' ) 
 
UV54 = 	 Parameter(name='UV54', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV54 + complex(0,1)*iUV54', 
	 texname = '\\text{UV54}' ) 
 
UV55 = 	 Parameter(name='UV55', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV55 + complex(0,1)*iUV55', 
	 texname = '\\text{UV55}' ) 
 
UV56 = 	 Parameter(name='UV56', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV56 + complex(0,1)*iUV56', 
	 texname = '\\text{UV56}' ) 
 
UV61 = 	 Parameter(name='UV61', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV61 + complex(0,1)*iUV61', 
	 texname = '\\text{UV61}' ) 
 
UV62 = 	 Parameter(name='UV62', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV62 + complex(0,1)*iUV62', 
	 texname = '\\text{UV62}' ) 
 
UV63 = 	 Parameter(name='UV63', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV63 + complex(0,1)*iUV63', 
	 texname = '\\text{UV63}' ) 
 
UV64 = 	 Parameter(name='UV64', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV64 + complex(0,1)*iUV64', 
	 texname = '\\text{UV64}' ) 
 
UV65 = 	 Parameter(name='UV65', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV65 + complex(0,1)*iUV65', 
	 texname = '\\text{UV65}' ) 
 
UV66 = 	 Parameter(name='UV66', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rUV66 + complex(0,1)*iUV66', 
	 texname = '\\text{UV66}' ) 
 
ZEL11 = 	 Parameter(name='ZEL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL11 + complex(0,1)*iZEL11', 
	 texname = '\\text{ZEL11}' ) 
 
ZEL12 = 	 Parameter(name='ZEL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL12 + complex(0,1)*iZEL12', 
	 texname = '\\text{ZEL12}' ) 
 
ZEL13 = 	 Parameter(name='ZEL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL13 + complex(0,1)*iZEL13', 
	 texname = '\\text{ZEL13}' ) 
 
ZEL21 = 	 Parameter(name='ZEL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL21 + complex(0,1)*iZEL21', 
	 texname = '\\text{ZEL21}' ) 
 
ZEL22 = 	 Parameter(name='ZEL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL22 + complex(0,1)*iZEL22', 
	 texname = '\\text{ZEL22}' ) 
 
ZEL23 = 	 Parameter(name='ZEL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL23 + complex(0,1)*iZEL23', 
	 texname = '\\text{ZEL23}' ) 
 
ZEL31 = 	 Parameter(name='ZEL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL31 + complex(0,1)*iZEL31', 
	 texname = '\\text{ZEL31}' ) 
 
ZEL32 = 	 Parameter(name='ZEL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL32 + complex(0,1)*iZEL32', 
	 texname = '\\text{ZEL32}' ) 
 
ZEL33 = 	 Parameter(name='ZEL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZEL33 + complex(0,1)*iZEL33', 
	 texname = '\\text{ZEL33}' ) 
 
ZER11 = 	 Parameter(name='ZER11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER11 + complex(0,1)*iZER11', 
	 texname = '\\text{ZER11}' ) 
 
ZER12 = 	 Parameter(name='ZER12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER12 + complex(0,1)*iZER12', 
	 texname = '\\text{ZER12}' ) 
 
ZER13 = 	 Parameter(name='ZER13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER13 + complex(0,1)*iZER13', 
	 texname = '\\text{ZER13}' ) 
 
ZER21 = 	 Parameter(name='ZER21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER21 + complex(0,1)*iZER21', 
	 texname = '\\text{ZER21}' ) 
 
ZER22 = 	 Parameter(name='ZER22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER22 + complex(0,1)*iZER22', 
	 texname = '\\text{ZER22}' ) 
 
ZER23 = 	 Parameter(name='ZER23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER23 + complex(0,1)*iZER23', 
	 texname = '\\text{ZER23}' ) 
 
ZER31 = 	 Parameter(name='ZER31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER31 + complex(0,1)*iZER31', 
	 texname = '\\text{ZER31}' ) 
 
ZER32 = 	 Parameter(name='ZER32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER32 + complex(0,1)*iZER32', 
	 texname = '\\text{ZER32}' ) 
 
ZER33 = 	 Parameter(name='ZER33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZER33 + complex(0,1)*iZER33', 
	 texname = '\\text{ZER33}' ) 
 
ZDL11 = 	 Parameter(name='ZDL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL11 + complex(0,1)*iZDL11', 
	 texname = '\\text{ZDL11}' ) 
 
ZDL12 = 	 Parameter(name='ZDL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL12 + complex(0,1)*iZDL12', 
	 texname = '\\text{ZDL12}' ) 
 
ZDL13 = 	 Parameter(name='ZDL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL13 + complex(0,1)*iZDL13', 
	 texname = '\\text{ZDL13}' ) 
 
ZDL21 = 	 Parameter(name='ZDL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL21 + complex(0,1)*iZDL21', 
	 texname = '\\text{ZDL21}' ) 
 
ZDL22 = 	 Parameter(name='ZDL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL22 + complex(0,1)*iZDL22', 
	 texname = '\\text{ZDL22}' ) 
 
ZDL23 = 	 Parameter(name='ZDL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL23 + complex(0,1)*iZDL23', 
	 texname = '\\text{ZDL23}' ) 
 
ZDL31 = 	 Parameter(name='ZDL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL31 + complex(0,1)*iZDL31', 
	 texname = '\\text{ZDL31}' ) 
 
ZDL32 = 	 Parameter(name='ZDL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL32 + complex(0,1)*iZDL32', 
	 texname = '\\text{ZDL32}' ) 
 
ZDL33 = 	 Parameter(name='ZDL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDL33 + complex(0,1)*iZDL33', 
	 texname = '\\text{ZDL33}' ) 
 
ZDR11 = 	 Parameter(name='ZDR11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR11 + complex(0,1)*iZDR11', 
	 texname = '\\text{ZDR11}' ) 
 
ZDR12 = 	 Parameter(name='ZDR12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR12 + complex(0,1)*iZDR12', 
	 texname = '\\text{ZDR12}' ) 
 
ZDR13 = 	 Parameter(name='ZDR13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR13 + complex(0,1)*iZDR13', 
	 texname = '\\text{ZDR13}' ) 
 
ZDR21 = 	 Parameter(name='ZDR21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR21 + complex(0,1)*iZDR21', 
	 texname = '\\text{ZDR21}' ) 
 
ZDR22 = 	 Parameter(name='ZDR22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR22 + complex(0,1)*iZDR22', 
	 texname = '\\text{ZDR22}' ) 
 
ZDR23 = 	 Parameter(name='ZDR23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR23 + complex(0,1)*iZDR23', 
	 texname = '\\text{ZDR23}' ) 
 
ZDR31 = 	 Parameter(name='ZDR31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR31 + complex(0,1)*iZDR31', 
	 texname = '\\text{ZDR31}' ) 
 
ZDR32 = 	 Parameter(name='ZDR32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR32 + complex(0,1)*iZDR32', 
	 texname = '\\text{ZDR32}' ) 
 
ZDR33 = 	 Parameter(name='ZDR33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZDR33 + complex(0,1)*iZDR33', 
	 texname = '\\text{ZDR33}' ) 
 
ZUL11 = 	 Parameter(name='ZUL11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL11 + complex(0,1)*iZUL11', 
	 texname = '\\text{ZUL11}' ) 
 
ZUL12 = 	 Parameter(name='ZUL12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL12 + complex(0,1)*iZUL12', 
	 texname = '\\text{ZUL12}' ) 
 
ZUL13 = 	 Parameter(name='ZUL13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL13 + complex(0,1)*iZUL13', 
	 texname = '\\text{ZUL13}' ) 
 
ZUL21 = 	 Parameter(name='ZUL21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL21 + complex(0,1)*iZUL21', 
	 texname = '\\text{ZUL21}' ) 
 
ZUL22 = 	 Parameter(name='ZUL22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL22 + complex(0,1)*iZUL22', 
	 texname = '\\text{ZUL22}' ) 
 
ZUL23 = 	 Parameter(name='ZUL23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL23 + complex(0,1)*iZUL23', 
	 texname = '\\text{ZUL23}' ) 
 
ZUL31 = 	 Parameter(name='ZUL31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL31 + complex(0,1)*iZUL31', 
	 texname = '\\text{ZUL31}' ) 
 
ZUL32 = 	 Parameter(name='ZUL32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL32 + complex(0,1)*iZUL32', 
	 texname = '\\text{ZUL32}' ) 
 
ZUL33 = 	 Parameter(name='ZUL33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUL33 + complex(0,1)*iZUL33', 
	 texname = '\\text{ZUL33}' ) 
 
ZUR11 = 	 Parameter(name='ZUR11', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR11 + complex(0,1)*iZUR11', 
	 texname = '\\text{ZUR11}' ) 
 
ZUR12 = 	 Parameter(name='ZUR12', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR12 + complex(0,1)*iZUR12', 
	 texname = '\\text{ZUR12}' ) 
 
ZUR13 = 	 Parameter(name='ZUR13', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR13 + complex(0,1)*iZUR13', 
	 texname = '\\text{ZUR13}' ) 
 
ZUR21 = 	 Parameter(name='ZUR21', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR21 + complex(0,1)*iZUR21', 
	 texname = '\\text{ZUR21}' ) 
 
ZUR22 = 	 Parameter(name='ZUR22', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR22 + complex(0,1)*iZUR22', 
	 texname = '\\text{ZUR22}' ) 
 
ZUR23 = 	 Parameter(name='ZUR23', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR23 + complex(0,1)*iZUR23', 
	 texname = '\\text{ZUR23}' ) 
 
ZUR31 = 	 Parameter(name='ZUR31', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR31 + complex(0,1)*iZUR31', 
	 texname = '\\text{ZUR31}' ) 
 
ZUR32 = 	 Parameter(name='ZUR32', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR32 + complex(0,1)*iZUR32', 
	 texname = '\\text{ZUR32}' ) 
 
ZUR33 = 	 Parameter(name='ZUR33', 
	 nature = 'internal', 
	 type = 'complex', 
	 value = 'rZUR33 + complex(0,1)*iZUR33', 
	 texname = '\\text{ZUR33}' ) 
 
G = 	 Parameter(name='G', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)', 
	 texname = 'G') 
 
el = 	 Parameter(name='el', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(1/aEWM1)*cmath.sqrt(cmath.pi)', 
	 texname = 'el') 
 
MWm = 	 Parameter(name='MWm', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (MZ**2*cmath.pi)/(cmath.sqrt(2)*aEWM1*Gf)))', 
	 texname = 'MWm') 
 
gL = 	 Parameter(name='gL', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'el*1./cmath.sin(TW)', 
	 texname = 'gL') 
 
v = 	 Parameter(name='v', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '2*cmath.sqrt(MWm**2/gL**2)', 
	 texname = 'v') 
 
V1 = 	 Parameter(name='V1', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'v*cmath.cos(betaH)', 
	 texname = 'V1') 
 
V2 = 	 Parameter(name='V2', 
	 nature = 'internal', 
	 type = 'real', 
	 value = 'v*cmath.sin(betaH)', 
	 texname = 'V2') 
 
RXiWLm = 	 Parameter(name='RXiWLm', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.', 
	 texname = 'RXiWLm') 
 
RXiWRm = 	 Parameter(name='RXiWRm', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.', 
	 texname = 'RXiWRm') 
 
RXiZ = 	 Parameter(name='RXiZ', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.', 
	 texname = 'RXiZ') 
 
RXiZp = 	 Parameter(name='RXiZp', 
	 nature = 'internal', 
	 type = 'real', 
	 value = '1.', 
	 texname = 'RXiZp') 
 
HPP1 = 	 Parameter(name='HPP1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP1}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [25,22,22] ) 
 
HGG1 = 	 Parameter(name='HGG1', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG1}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [25,21,21] ) 
 
HPP2 = 	 Parameter(name='HPP2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP2}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [35,22,22] ) 
 
HGG2 = 	 Parameter(name='HGG2', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG2}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [35,21,21] ) 
 
HPP3 = 	 Parameter(name='HPP3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP3}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [45,22,22] ) 
 
HGG3 = 	 Parameter(name='HGG3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG3}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [45,21,21] ) 
 
HPP4 = 	 Parameter(name='HPP4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP4}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [9000025,22,22] ) 
 
HGG4 = 	 Parameter(name='HGG4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG4}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [9000025,21,21] ) 
 
HPP5 = 	 Parameter(name='HPP5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HPP5}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [9000035,22,22] ) 
 
HGG5 = 	 Parameter(name='HGG5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{HGG5}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [9000035,21,21] ) 
 
APP3 = 	 Parameter(name='APP3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{APP3}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [36,22,22] ) 
 
AGG3 = 	 Parameter(name='AGG3', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{AGG3}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [36,21,21] ) 
 
APP4 = 	 Parameter(name='APP4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{APP4}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [46,22,22] ) 
 
AGG4 = 	 Parameter(name='AGG4', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{AGG4}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [46,21,21] ) 
 
APP5 = 	 Parameter(name='APP5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{APP5}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [9000036,22,22] ) 
 
AGG5 = 	 Parameter(name='AGG5', 
	 nature = 'external', 
	 type = 'real', 
	 value = 0., 
	 texname = '\\text{AGG5}', 
	 lhablock = 'EFFHIGGSCOUPLINGS', 
	 lhacode = [9000036,21,21] ) 
 
