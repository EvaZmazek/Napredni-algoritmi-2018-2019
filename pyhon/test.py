from ProblemLinearnegaPrevoza import *

print("Eva")
#print(main_GEN2(6,[[1,2,3,4],[5,6,7,8],[9,8,20,6],[30,8,9,5]],[17,5,23,15],[15,23,17,5],20,8, 0.5, 0.1,population_starting_GEN2,1,2))

def testMojPrimer():
    size = 6
    cost = [[1,2,3,4],[5,6,7,8],[9,8,20,6],[30,8,9,5]]
    sour = [17,5,23,15]
    dest = [15,23,17,5]
    t_max = 20
    T_max = 8
    p_mut = 0.5
    p_inv = 0.1
    old_population_GEN1 = create_starting_population_GEN1(size, sour, dest)
    old_population_GEN2 = create_starting_population_GEN2(size, sour, dest)
    number_of_couples = 1
    survive_next_generation = 2
    costGEN1, winnerGEN1 = main_GEN1(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN1, number_of_couples, survive_next_generation)
    costGEN2, winnerGEN2 = main_GEN2(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN2, number_of_couples, survive_next_generation)
    return costGEN1, winnerGEN1, costGEN2, winnerGEN2

print(testMojPrimer())

def test1():
    return 
