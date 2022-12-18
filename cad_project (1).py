truthtable=[[0,0,0,0],[0,0,1,1],[0,1,0,1],[0,1,1,0],[1,0,0,1],[1,0,1,1],[1,1,0,0],[1,1,1,1]]           #for a given truth table
print(truthtable[1][2])

for i in range (8):                     # printing the output 
  print(truthtable[i][3])

for i in range(8):                            #Reducing the leaf nodes
   if(truthtable[i][3]==1):
       truthtable[i][3]=200                   
   elif(truthtable[i][3]==0):
      truthtable[i][3]=100
print(truthtable)

y1=[1]                                   ##performing a logic operation to reduce the isomorphic nodes
for i in range(1,4):
    if((truthtable[0][3]==truthtable[2*i][3]) and (truthtable[1][3]==truthtable[(2*i)+1][3])):
       y1.append(1)
    else :
       y1.append(0)
print(y1)

y2=y1
if(y1[1]==1):
  y2[0]=1
  y2[1]=1
elif(y1[1]==0):
  y2[0]=1
  y2[1]=2

if(y1[2]==1):
  y2[0]=1
  y2[2]=1
elif(y1[2]==0):
  y2[0]=1
  y2[2]=3

if(y1[3]==1):
  y2[0]=1
  y2[3]=1
elif(y1[3]==0):
  y2[0]=1
  y2[3]=4

for i in range(2,4):
    if((truthtable[2][3]==truthtable[2*i][3]) and (truthtable[3][3]==truthtable[(2*i)+1][3])):
       if(y2[1]==0):
         y2[i]=(0)
       elif(y2[1]==1):
         y2[i]=(1)
       elif(y2[1]==2):
         y2[i]=(2)
    else :
      if(y2[i]==0):
       y2[i]=(3)
print(y2)

y3=y2
if(y2[2]==2):
  y3=y2
  y3[2]=2
elif(y2[2]==0):
  y3=y2
  y3[2]=3
for i in range(3,4):
    if((truthtable[4][3]==truthtable[2*i][3]) and (truthtable[5][3]==truthtable[(2*i)+1][3])):
       if(y2[2]==2):
         y3[3]=2
       elif(y2[2]==1):
         y3[3]=1
       elif(y2[2]==0):
         y3[3]=3
    else :
      if(y2[i]==0):
       y3[3]=4
print(y3)

print(truthtable)    # printing the truth-table after reducing the leaf nodes

flagc0=0
flagc1=0
flagc2=0
flagc3=0

if(truthtable[0][3]==truthtable[1][3]):
  flagc0=1
  if(truthtable[0][3]==200):
   flagc0_connected_to=1
  else:
    flagc0_connected_to=0
if(truthtable[2][3]==truthtable[3][3]):
  flagc1=1
  if(truthtable[2][3]==200):
   flagc1_connected_to=1
  else:
    flagc1_connected_to=0
if(truthtable[4][3]==truthtable[5][3]):
  flagc2=1
  if(truthtable[4][3]==200):
   flagc2_connected_to=1
  else:
    flagc2_connected_to=0
if(truthtable[6][3]==truthtable[7][3]):
  flagc3=1
  if(truthtable[6][3]==200):
   flagc3_connected_to=1
  else:
    flagc3_connected_to=0

if y3[0]==1:                                                         ## checking for the isomorphic nodes
    truthtable[0][2]=300
    truthtable[1][2]=300
if y3[1]==1:
    truthtable[2][2]=300
    truthtable[3][2]=300
elif y3[1]==2:
    truthtable[2][2]=400
    truthtable[3][2]=400
if y3[2]==1:
    truthtable[4][2]=300
    truthtable[5][2]=300
elif y3[2]==2:
    truthtable[4][2]=400
    truthtable[5][2]=400
elif y3[2]==3:
    truthtable[4][2]=500
    truthtable[5][2]=500
if y3[3]==1:
    truthtable[6][2]=300
    truthtable[7][2]=300
elif y3[3]==2:
    truthtable[6][2]=400
    truthtable[7][2]=400
elif y3[3]==3:
    truthtable[6][2]=500
    truthtable[7][2]=500
elif y3[3]==4:
    truthtable[6][2]=600
    truthtable[7][2]=600
  
print(truthtable)

for i in range (2):                                        # checking for the redundancy nodes after performing isomorphic operation
  if truthtable[i][2]==truthtable[i+2][2]:
    truthtable[i][1]=-1
    truthtable[i+2][1]=-1
for i in range (4,6):
  if truthtable[i][2]==truthtable[i+2][2]:
    truthtable[i][1]=-1
    truthtable[i+2][1]=-1
print(truthtable)

print("A"+" B"+"  C"+"   F" )                             #  printing the truth table
for i in range(8):
    for j in range(4):
        print(truthtable[i][j], end = " ")
    print()

import graphviz                                         # implementing ROBDD using graphviz library

u = graphviz.Digraph('unix', filename='unix.gv',node_attr={'color': 'lightblue2', 'style': 'filled'})
def sasi0():
 
  u.edge('A', 'B0',label="0")
def sasi1():
   u.edge('A', 'B1',label="1")
def shreyansh0():
    if(truthtable[0][2]==300):
      if(truthtable[0][3] == truthtable[1][3] and truthtable[1][3]==100):
         u.edge('B0','0',label="0")
      elif(truthtable[0][3] == truthtable[1][3] and truthtable[1][3]==200):  
         u.edge('B0','1',label="0")
      else:
        u.edge('B0','C0',label="0")
    if(truthtable[0][2]==400):
      if(truthtable[2][3] == truthtable[3][3] and truthtable[3][3]==100):
         u.edge('B0','0',label="0")
      elif(truthtable[2][3] == truthtable[3][3] and truthtable[3][3]==200):  
         u.edge('B0','1',label="0")
      else:
        u.edge('B0','C1',label="0")
    if(truthtable[0][2]==500):
      if(truthtable[4][3] == truthtable[5][3] and truthtable[5][3]==100):
         u.edge('B0','0',label="0")
      elif(truthtable[4][3] == truthtable[5][3] and truthtable[5][3]==200):  
         u.edge('B0','1',label="0")
      else:
        u.edge('B0','C2',label="0")
    if(truthtable[0][2]==600):
      if(truthtable[6][3] == truthtable[7][3] and truthtable[7][3]==100):
         u.edge('B0','0',label="0")
      elif(truthtable[6][3] == truthtable[7][3] and truthtable[7][3]==200):  
         u.edge('B0','1',label="0")
      else:
        u.edge('B0','C3',label="0")
def shreyansh1():
    if(truthtable[2][2]==300):
      if(truthtable[0][3] == truthtable[1][3] and truthtable[1][3]==100):
         u.edge('B0','0',label="1")
      elif(truthtable[0][3] == truthtable[1][3] and truthtable[1][3]==200):  
         u.edge('B0','1',label="1")
      else:
        u.edge('B0','C0',label="1")
    if(truthtable[2][2]==400):
      if(truthtable[2][3] == truthtable[3][3] and truthtable[3][3]==100):
         u.edge('B0','0',label="1")
      elif(truthtable[2][3] == truthtable[3][3] and truthtable[3][3]==200):  
         u.edge('B0','1',label="1")
      else:
        u.edge('B0','C1',label="1")
    if(truthtable[2][2]==500):
      if(truthtable[4][3] == truthtable[5][3] and truthtable[5][3]==100):
         u.edge('B0','0',label="1")
      elif(truthtable[4][3] == truthtable[5][3] and truthtable[5][3]==200):  
         u.edge('B0','1',label="1")
      else:
        u.edge('B0','C2',label="1")
    if(truthtable[2][2]==600):
      if(truthtable[6][3] == truthtable[7][3] and truthtable[7][3]==100):
         u.edge('B0','0',label="1")
      elif(truthtable[6][3] == truthtable[7][3] and truthtable[7][3]==200):  
         u.edge('B0','1',label="1")
      else:
        u.edge('B0','C3',label="1")
def shreyansh2():
    if(truthtable[4][2]==300):
      if(truthtable[0][3] == truthtable[1][3] and truthtable[1][3]==100):
         u.edge('B1','0',label="0")
      elif(truthtable[0][3] == truthtable[1][3] and truthtable[1][3]==200):  
         u.edge('B1','1',label="0")
      else:
        u.edge('B1','C0',label="0")
    if(truthtable[4][2]==400):
      if(truthtable[2][3] == truthtable[3][3] and truthtable[3][3]==100):
         u.edge('B1','0',label="0")
      elif(truthtable[2][3] == truthtable[3][3] and truthtable[3][3]==200):  
         u.edge('B1','1',label="0")
      else:
        u.edge('B1','C1',label="0")
    if(truthtable[4][2]==500):
      if(truthtable[4][3] == truthtable[5][3] and truthtable[5][3]==100):
         u.edge('B1','0',label="0")
      elif(truthtable[4][3] == truthtable[5][3] and truthtable[5][3]==200):  
         u.edge('B1','1',label="0")
      else:
        u.edge('B1','C2',label="0")
    if(truthtable[4][2]==600):
      if(truthtable[6][3] == truthtable[7][3] and truthtable[7][3]==100):
         u.edge('B1','0',label="0")
      elif(truthtable[6][3] == truthtable[7][3] and truthtable[7][3]==200):  
         u.edge('B1','1',label="0")
      else:
        u.edge('B1','C3',label="0")
def shreyansh3():
    if(truthtable[6][2]==300):
      if(truthtable[0][3] == truthtable[1][3] and truthtable[1][3]==100):
         u.edge('B1','0',label="1")
      elif(truthtable[0][3] == truthtable[1][3] and truthtable[1][3]==200):  
         u.edge('B1','1',label="1")
      else:
        u.edge('B1','C0',label="1")
    if(truthtable[6][2]==400):
      if(truthtable[2][3] == truthtable[3][3] and truthtable[3][3]==100):
         u.edge('B1','0',label="1")
      elif(truthtable[2][3] == truthtable[3][3] and truthtable[3][3]==200):  
         u.edge('B1','1',label="1")
      else:
        u.edge('B1','C1',label="1")
    if(truthtable[6][2]==500):
      if(truthtable[4][3] == truthtable[5][3] and truthtable[5][3]==100):
         u.edge('B1','0',label="1")
      elif(truthtable[4][3] == truthtable[5][3] and truthtable[5][3]==200):  
         u.edge('B1','1',label="1")
      else:
        u.edge('B1','C2',label="1")
    if(truthtable[6][2]==600):
      if(truthtable[6][3] == truthtable[7][3] and truthtable[7][3]==100):
         u.edge('B1','0',label="1")
      elif(truthtable[6][3] == truthtable[7][3] and truthtable[7][3]==200):  
         u.edge('B1','1',label="1")
      else:
        u.edge('B1','C3',label="1")

f300=0
f400=0
f500=0
f600=0

for i in range (4):
 if(truthtable[2*i][2]==300):
   f300=f300+1
 if(truthtable[2*i][2]==400):
   f400=f400+1
 if(truthtable[2*i][2]==500):
   f500=f500+1
 if(truthtable[2*i][2]==600):
   f600=f600+1

if(f300!=0 and (truthtable[0][3] != truthtable[1][3])):
  u.node('C0')
if(f400!=0 and (truthtable[2][3] != truthtable[3][3])):
  u.node('C1')
if(f500!=0 and (truthtable[4][3] != truthtable[5][3])):
  u.node('C2')
if(f600!=0 and (truthtable[6][3] != truthtable[7][3])):
  u.node('C3')

if(truthtable[0][1]==-1):
  u.edge('A','C0',label="0")



else:
    sasi0()  
    shreyansh0()
    shreyansh1()





if(truthtable[4][1]==-1):
    if(truthtable[4][2]==400):
      u.edge('A','C1',label="1")
    if(truthtable[4][2]==300):
      u.edge('A','C0',label="0") 

else:
    sasi1()
    shreyansh2()
    shreyansh3()



if(f300!=0 and (truthtable[0][3] != truthtable[1][3])):
    if(truthtable[1][3]==200):
     u.edge('C0', '1',label="1")
    elif(truthtable[1][3]==100):
     u.edge('C0', '0',label="1")
    if(truthtable[0][3]==200):
     u.edge('C0', '1',label="0")
    elif(truthtable[0][3]==100):
     u.edge('C0', '0',label="0")

if(f400!=0 and (truthtable[2][3] != truthtable[3][3])):
    if(truthtable[3][3]==200):
     u.edge('C1', '1',label="1")
    elif(truthtable[3][3]==100):
     u.edge('C1', '0',label="1")
    if(truthtable[2][3]==200):
     u.edge('C1', '1',label="0")
    elif(truthtable[2][3]==100):
     u.edge('C1', '0',label="0")

if(f500!=0 and (truthtable[4][3] != truthtable[5][3])):
    if(truthtable[5][3]==200):
     u.edge('C2', '1',label="1")
    elif(truthtable[5][3]==100):
     u.edge('C2', '0',label="1")
    if(truthtable[4][3]==200):
     u.edge('C2', '1',label="0")
    elif(truthtable[4][3]==100):
     u.edge('C2', '0',label="0")
if(f600!=0 and (truthtable[6][3] != truthtable[7][3])):
    if(truthtable[7][3]==200):
     u.edge('C3', '1',label="1")
    elif(truthtable[7][3]==100):
     u.edge('C3', '0',label="1")
    if(truthtable[6][3]==200):
     u.edge('C3', '1',label="0")
    elif(truthtable[6][3]==100):
     u.edge('C3', '0',label="0")

u.view()