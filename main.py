import math
import random
import copy





def annealing():
  #Initalize random place for the array using function and return it
  # Retrun [array , no of cells , no of connections ]
  file = open("d1.txt", "r")
  placement, dict , numberOfCells , numberOfConnections = random_initalize(file)

  size = [len(placement) , len(placement[0])]
 
   #Use HPWL and Get inital cose
  
  nets = getConnectionsArray(file , numberOfConnections)
  
  cL = HPWL(size , nets, dict)
  T = 500* cL # initial temp
  # Tf = pow(5*10, -6) * cL / numberOfConnections
  Tf = 1
  moves = 10 * numberOfCells
  count =0
  while T > Tf:
    # print(cL)
    #pick 2 random number in the range of cells
    index1 = [random.randint(0 , len(placement)-1), random.randint(0     , len(placement[0])-1)]
    index2 = [random.randint(0 , len(placement)-1), random.randint(0     , len(placement[0])-1)]
    while index1 == index2 :
      index2 = [random.randint(0 , len(placement)-1),               
      random.randint(0 , len(placement[0])-1)]
    
    #swap in the current array and return with new array
    newPlacement , newDict = swap(placement , index1 , index2, dict)
    n = HPWL(size, nets, newDict)
    deltaL = n-cL
    if deltaL < 0:
      placement = copy.deepcopy(newPlacement)
      dict = newDict.copy()
      cL = n
      storePlacement = copy.deepcopy(placement)
      storeL = cL
    else:
      value = -deltaL / T 
      e = math.exp(value)
      rand = random.uniform(0,1)
      if rand < e:
        placement = copy.deepcopy(newPlacement)
        dict = newDict.copy() 
        cL = n
    count = count +1
    if(count == moves):
      T = 0.95 * T
      count =0


  if(storeL < cL):
    placement = copy.deepcopy(storePlacement)
    cL = storeL
  print("\n") 
  for i in placement:
    print(i )
  print("\n")
  print( cL)

    














def random_initalize(file):
  
 ## s = "10 3 4 4-3 0 1 2-2 2 0-2 1 2"
  ##s = s.split("-")
  ##print(s)
  ##temp=[]
  
  ##for k in s:
  ##    x = k.split(" ")
    ##  temp.append(x)
  
##  s = temp
  line =file.readline()
  line=line.split()
    
      # dimension of board and number of bombs
      # (I'm using hard coded values as an example)
  width = line[2]
  height = line[3]
  b = line[0]
  xx= line[1]
  #width = s[0][2]
  #height = s[0][3]
  #b = s[0][0]

  temp = int(height)

  tempx = int(width)
  tempb= int(b)
  tempff=int(xx)

    #creates the board
  board = []
  for i in range(temp):
      # create a new array for every row
      board.append([-1] * tempx)
      
  counter=0
  x=0
  y=0
  new_dict={}
  for i in range(tempb):
      while (board[x][y]!=-1):
          x = random.randint(0, temp - 1)
          y = random.randint(0, tempx - 1)
      board[x][y] = counter 
      new_dict[counter] = [x,y]
# printing result
      counter=counter+1
  # print(board)
  # print(new_dict)

    
  # for i in board:
  #   print(i)

  return board, new_dict, tempb , tempff













def getConnectionsArray(file, numberOfConnections):
  nets = []
  for i in range(numberOfConnections):
    l = file.readline()
    connection = l.split()
    connection.pop(0)
    con=[]
    for j in connection:
      temp=int(j)
      con.append(temp)
    connection=con
    nets.append(connection)

  return nets

# def get_index(dict, cellCurrent):
  
#   return [-1,-1]


  
def HPWL(size, nets ,dict):

  iijj=[]
  hpwl = 0 
  for i in nets:
    maxI = 0
    minI =size[0]
    maxJ = 0
    minJ =size[1]
    
    for j in i:
      iijj=[]
      cellCurrent = j
      # iijj = get_index(dict, cellCurrent)
      iijj = dict[cellCurrent]
      # zz = iijj[0]
      # temmm=int(zz)
      ii=iijj[0]
      jj=iijj[1]
      
      if(ii >= maxI):
        maxI = ii
      if(jj >= maxJ):
        maxJ = jj
        
      if(ii <= minI):
        minI = ii
      if(jj <= minJ):
        minJ = jj
    hpwl = hpwl + (maxI - minI) + (maxJ - minJ) 
  return hpwl


def swap(placement, i1, i2, dict):

  cell1 = placement[i1[0]][i1[1]]
  cell2 = placement[i2[0]][i2[1]]

  new_dict = dict.copy()

  if(cell1 == -1 and cell2 == -1):
    a = 0
  elif (cell1 == -1):
    new_dict[cell2] = i1
  elif(cell2 ==-1):
    new_dict[cell1] = i2
  else:
    temp2 = new_dict[cell1]
    new_dict[cell1] = new_dict[cell2]
    new_dict[cell2] = temp2

  
  new_array = copy.deepcopy(placement)
  temp = new_array[i1[0]][i1[1]]
  new_array[i1[0]][i1[1]] = new_array[i2[0]][i2[1]]
  new_array[i2[0]][i2[1]] = temp

    





  
  
  
  
  
  return new_array , new_dict




annealing()