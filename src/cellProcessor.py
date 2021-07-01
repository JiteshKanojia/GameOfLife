import numpy as np


class cellProcessor:
    """ A Class For Processing the cells of numpy array
        For Conway's Game of Life

        For more info on Conway's Game of Life visit :
        https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

    """

    def __init__(self,arr):
        """ Parameters
            ----------
            arr : numpy.ndarray
        """
        self.arr = arr

    def check(self,coord):
        """ Takes a Tuple having co-ordinates and returns state of the cell

            Parameters
            ----------
            coord: Tuple

            returns
            ----------
            type => Int
        """
        x = coord[0]
        y = coord[1]
        return self.arr[x][y]

    def find_ones(self):
        """ Finds all coordinates of class object with value 1.

            Parameters
            ----------
            None

            returns
            ----------
            type => List
        """
        new_arr = np.where(self.arr==1)
        a = []
        for x in range(len(new_arr[0])):
            a.append(tuple((new_arr[0][x],new_arr[1][x])))
        return a


    def unique_sort(self,input_list):
        """ Takes a list and returns a list with sorted and unique elements

            Parameters
            ----------
            input_list: List

            returns
            ----------
            type => List
        """
        temp_list =[]
        for x in input_list:
            if x in temp_list:
                continue
            else:
                temp_list.append(tuple(x))
        temp_list.sort()
        return temp_list



    def find_neighbours(self,co_arr):
        """ Iterate through the 2d array and find  neighbour cells of co-ordinates
            For each tuple in list it gives a list of neighbour_coordinates

            Parameters
            ----------
            co_arr: List of Tuples

            Returns
            ----------
            type => List containing List of tuples -> [[(x1,y1),(x2,y2)],[(x3,y3),(x4,y4)]]
        """
        neighbour_list= []
        temp_list2 = []
        for coord in co_arr:
            for m in range(-1,2):
                for n in range(-1,2):
                    if((m==0 and n==0)):
                        continue
                    x=coord[0]
                    y=coord[1]
                    new_x = x+m
                    new_y = y+n
                    if((int(new_x) >=0 and int(new_y)>=0 ) and (new_x < np.size(self.arr,0) and new_y < np.size(self.arr,1))):
                        temp_list2.append((tuple((new_x,new_y))))
            neighbour_list.append(temp_list2)
            temp_list2 = []
        return neighbour_list

    def next_generation(self,neighbour_list):
        """ Takes neighbour list as parameter and returns the next
            generation of cells in Conway's Game of Life

            For more info on Conway's Game of Life visit :
            https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

            Parameters
            ----------
            neighbour_list: List

            returns
            ----------
            type => numpy.ndarray
        """
        new_arr = self.arr
        state_dict = {}
        uniq_neighbour_list = self.unique_sort(neighbour_list)


        for i in uniq_neighbour_list:
            state_dict.update({i : self.check(i)})

        for i in uniq_neighbour_list:
            count = 0
            new_list2 = []
            new_list2.append(i)
            new = self.find_neighbours(new_list2)
            new = sum(new,[]) #converts 2d list to 1d list

            for j in new:
                if j in state_dict:
                    count = count + state_dict[j]
                else:
                    continue
            if(count < 2 or count > 3):
                new_arr[i[0],i[1]] = 0
            elif(count == 3):
                new_arr[i[0],i[1]] = 1

        return new_arr



