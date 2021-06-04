import numpy as np
import math
def frewkwensi(arr, n, m,luas,baris,kolom,matrix):
    print('input(matrix)')
    print(matrix)
    # Hashmap
    hash = [0 for i in range(n)]
    probality = [0 for i in range(n)]
    cp2 = [0 for i in range(n)]
    # Traverse all array elements
    i = 0
    while (i < n):         
        # Update the frequency of array[i]
        hash[arr[i]] += 1
        probality[arr[i] - 1] += 1
        cp2[arr[i] - 1] += 1
        # Increase the index
        i += 1        
#    print('frewkwensi')
#    for i in range(m):         
       #  print(hash[i])         
#   print('frewkwensi/luas(probalitas)')     
    for i in range(m):        
        probality[i]= hash[i]/luas
        #  print(probality[i])
#    print('cumulative probability/CP')
    sum=0     
    for element in probality:
        sum+=element
    #    print(sum)        
    #print('cumulative probability*20')
    sum=0
    for i in range(m):
        sum+=probality[i]
        cp2[i]= sum*20
    #    print(cp2[i])
    #    print('digenapkan')
        cp2[i]= math.floor(cp2[i])
    #    print(cp2[i])
    print('Output')
    k=(baris,kolom)
    output=np.zeros(k)
    i=0
    j=0
    for i in range(baris):
       for j in range(kolom):
            output[i,j]=cp2[matrix[i,j]]
    print(output)
    
#Main Program            
matrix = np.array([[ 3, 2, 4, 5],
           [ 7, 7, 8, 2],
           [3, 1, 2, 3],
           [5, 4, 6, 7,]])

daftar =np.array(matrix).flatten().tolist()
#print('input(array/list)')
#print(daftar)
total= max(daftar)
kolom, baris = matrix.shape
#print('kolom')
#print(kolom)
#print('baris')
#print(baris)
luas = baris * kolom
#print('luas(baris*kolom)')
#print(luas) 
frewkwensi(daftar, len(daftar), total,luas,baris,kolom,matrix)
# This code is contributed by avanitrachhadiya2155
