import numpy as np
import cellProcessor as cp

#Rules of the game for each cell
#Underpopulation - live cell dies if it has fewer than 2 neighbours.
#existence - live cell with 2 or 3 live neighbours lives on.
#Overpopulation - live cell with more than 3 live neighbours dies.
#Reproduction - Cell with exactly 3 live neighbours becomes a live cell.

#arr = np.array([[1,0,0,1,1],[1,0,0,1,1],[1,0,0,0,1]])
#arr = np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
arr = np.array([[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,1,1,1,0],[0,1,1,1,1,1,0],[0,0,0,0,0,0,0]])

print(arr)
arr2 = cp.cellProcessor(arr)
new_arr = arr2.find_neighbours(arr2.find_ones())
#arr2.iterate(new_arr)
new_arr = sum(new_arr,[]) #Converts 2d list to 1d list
print("--"*50)
arr3 = arr2.next_generation(new_arr)
print(arr3)
