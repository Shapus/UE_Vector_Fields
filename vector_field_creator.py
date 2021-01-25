#
#
#Create vector fields in .fga format for UnrealEngine
#
#
#Change result in P(), Q(), R() functions for different creating vector field
#Change i, j, k for scaling vector field size
#Change file_name to set output file name
#IDK what "-2400.000000,-800.000000,-800.000000,-800.000000,800.000000,800.000000" params do, should test it
#
#


from math import *

file_name = "vector_field"
i = 32
j = 32
k = 32

def P(x,y,z,*args):
    result = x
    return str(result)

def Q(x,y,z,*args):
    result = y
    return str(result)

def R(x,y,z,*args):
    result = z
    return str(result)



f = open(file_name+'.fga', 'w')
f.write(str(i)+
        ","+str(j)+
        ","+str(k)+",\n")
f.write("-2400.000000,-800.000000,-800.000000,\n-800.000000,800.000000,800.000000,\n")
for x in range(-16,15):
    for y in range(-16,15):
        for z in range(-16,15):
            vector_length = sqrt(pow(x,2)+pow(y,2)+pow(z,2))
            f.write(P(x,y,z,vector_length)+","+Q(x,y,z,vector_length)+","+R(x,y,z,vector_length))
            if(x,y,z < i*j*k):
                f.write(",\n")
f.close()
                
