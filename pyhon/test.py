from ProblemLinearnegaPrevoza import *

#print(main_GEN2(6,[[1,2,3,4],[5,6,7,8],[9,8,20,6],[30,8,9,5]],[17,5,23,15],[15,23,17,5],20,8, 0.5, 0.1,population_starting_GEN2,1,2))

print("--------------------------------  TEST 1   -------------------------")
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
#kot izgleda, je tu 355 kar optimalna rešitev - v večini primerov ziteriram do tega
#v enem primeru je našlo 353

def primerjavaAlgoritmov_testMojPrimer(st_poskusov):
    gen_1 = 0
    gen_2 = 0
    for i in range(st_poskusov):
        costGEN1, winnerGEN1, costGEN2, winnerGEN2 = testMojPrimer()
        if costGEN1 < costGEN2:
            gen_1 += 1
        elif costGEN2 < costGEN1:
            gen_2 +=1
    if gen_1 > gen_2:
        return "gen_1 zmagal za: " + str(gen_1) + ":" + str(gen_2)
    elif gen_1 > gen_2:
        return "gen_2 zmagal za: " + str(gen_2) + ":" + str(gen_1)
    else:
        return "gen_1 in gen_2 sta izenačena"

#print(primerjavaAlgoritmov_testMojPrimer(20))
# v tem primeru algoritem GEN1 zmagal za 6:2, v večkratnih poskusih vedno zmagal gen_1

#Optimalna resitev tega priemra: 4,525
def test1():
    size = 20
    cost = [[6,8,10],[7,11,11],[4,5,12]]
    sour = [150,175,275]
    dest = [200,100,300]
    t_max = 20
    T_max = 10
    p_mut = 0.5
    p_inv = 0.1
    old_population_GEN1 = create_starting_population_GEN1(size, sour, dest)
    old_population_GEN2 = create_starting_population_GEN2(size, sour, dest)
    number_of_couples = 8
    survive_next_generation = 5
    costGEN1, winnerGEN1 = main_GEN1(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN1, number_of_couples, survive_next_generation)
    costGEN2, winnerGEN2 = main_GEN2(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN2, number_of_couples, survive_next_generation)
    return costGEN1, winnerGEN1, costGEN2, winnerGEN2

print(test1())
