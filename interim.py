def tourlength(tour, locations):
    
    total_distance = 0.0
    
    #returns length 0.0 if there is only 0 or 1 location provided
    if len(tour)<2:
        return total_distance
    
    else:
        for j in range(len(tour)-1):
            #setting up value for place and place 2
            for i in range(len(locations)):
                if tour[j]==locations[i][0]:
                    place=tuple([locations[i][1],locations[i][2]])
                if tour[j+1]==locations[i][0]:
                    place2=tuple([locations[i][1],locations[i][2]])
            #calculate distance between two locations and adds to total
            distance = (((place2[0]-place[0])**2+
                        (place2[1]-place[1])**2)**0.5)
            total_distance += distance
    
    #returns calculated total distance
    return total_distance