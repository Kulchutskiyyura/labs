from constant import list_of_coordinates
def create_coordinate_list(number_of_level):
    for i in range(number_of_level):
        for j in range(2**i):
            list_of_coordinates.append([i,j])
    



