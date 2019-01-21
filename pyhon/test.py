from ProblemLinearnegaPrevoza import *

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
#print("--------------------------  TEST MOJ PRIMER   -------------------------")
#print(testMojPrimer())
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

#Optimalna resitev tega priemra: 4,525 (B-15 http://web.tecnico.ulisboa.pt/mcasquilho/compute/_linpro/TaylorB_module_b.pdf)
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
#print("--------------------------------  TEST 1   -------------------------")
#print(test1())

#verjetno je optimalna resitev 18650 (B-26 http://web.tecnico.ulisboa.pt/mcasquilho/compute/_linpro/TaylorB_module_b.pdf)
def test2():
    size = 20
    cost = [[200,750,300,450],[650,800,400,600],[400,700,500,550]]
    sour = [12,17,11]
    dest = [10,10,10,10]
    t_max = 30
    T_max = 10
    p_mut = 0.5
    p_inv = 0.1
    old_population_GEN1 = create_starting_population_GEN1(size, sour, dest)
    old_population_GEN2 = create_starting_population_GEN2(size, sour, dest)
    number_of_couples = 0
    survive_next_generation = 5
    costGEN1, winnerGEN1 = main_GEN1(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN1, number_of_couples, survive_next_generation)
    costGEN2, winnerGEN2 = main_GEN2(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN2, number_of_couples, survive_next_generation)
    return costGEN1, winnerGEN1, costGEN2, winnerGEN2
#print("--------------------------------  TEST 2   -------------------------")
#print(test2())

#verjetno je optimalna resitev 2350 (B-27 http://web.tecnico.ulisboa.pt/mcasquilho/compute/_linpro/TaylorB_module_b.pdf)
def test3():
    size = 20
    cost = [[6,7,4],[5,3,6],[8,5,7]]
    sour = [100,180,200]
    dest = [135,175,170]
    t_max = 30
    T_max = 10
    p_mut = 0.5
    p_inv = 0.1
    old_population_GEN1 = create_starting_population_GEN1(size, sour, dest)
    old_population_GEN2 = create_starting_population_GEN2(size, sour, dest)
    number_of_couples = 0
    survive_next_generation = 5
    costGEN1, winnerGEN1 = main_GEN1(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN1, number_of_couples, survive_next_generation)
    costGEN2, winnerGEN2 = main_GEN2(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN2, number_of_couples, survive_next_generation)
    return costGEN1, winnerGEN1, costGEN2, winnerGEN2
#print("--------------------------------  TEST 3   -------------------------")
#print(test3())

# priblizno 287
def test4():
    size = 20
    cost = [[3.7, 4.6, 4.9, 5.5, 4.3],[3.4, 5.1, 4.4, 5.9, 5.2],[3.3, 4.1, 3.7, 2.9, 2.6], [1.9, 4.2, 2.7, 5.4, 3.9], [6.1, 5.1, 3.8, 2.5, 4.1], [6.6, 4.8, 3.5, 3.6, 4.5]]
    sour = [18,15,10,12,20,15]
    dest = [20,15,15,15,20]
    t_max = 30
    T_max = 10
    p_mut = 0.5
    p_inv = 0.1
    old_population_GEN1 = create_starting_population_GEN1(size, sour, dest)
    old_population_GEN2 = create_starting_population_GEN2(size, sour, dest)
    number_of_couples = 0
    survive_next_generation = 5
    costGEN1, winnerGEN1 = main_GEN1(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN1, number_of_couples, survive_next_generation)
    costGEN2, winnerGEN2 = main_GEN2(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN2, number_of_couples, survive_next_generation)
    return costGEN1, winnerGEN1, costGEN2, winnerGEN2
#print("--------------------------------  TEST 4   -------------------------")
#print(test4())

# priblizno 2316.0 - glede na knjigo je to tudi optimalno https://econweb.ucsd.edu/~jsobel/172aw02/notes8.pdf stran 5
def test5():
    size = 20
    #cost = [[51,59,49],[62,68,56],[35,50,53],[45,39,51],[56,46,37]]
    cost = [[51, 62, 35, 45, 56],[59, 68, 50, 39, 46], [49, 56, 53, 51, 37]]
    sour = [15,20,15]
    dest = [11,12,9,10,8]
    t_max = 30
    T_max = 10
    p_mut = 0.5
    p_inv = 0.1
    old_population_GEN1 = create_starting_population_GEN1(size, sour, dest)
    old_population_GEN2 = create_starting_population_GEN2(size, sour, dest)
    number_of_couples = 0
    survive_next_generation = 5
    costGEN1, winnerGEN1 = main_GEN1(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN1, number_of_couples, survive_next_generation)
    costGEN2, winnerGEN2 = main_GEN2(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN2, number_of_couples, survive_next_generation)
    return costGEN1, winnerGEN1, costGEN2, winnerGEN2
#print("--------------------------------  TEST 5   -------------------------")
#print(test5())

# priblizno 615 - 640 v knjigi https://aetos.it.teithe.gr/~vkostogl/en/Epixeirisiaki/Transportation%20problems_en_29-5-2012.pdf stran 13
def test6():
    size = 20
    cost = [[3,2,3,4,1],[4,1,2,3,2], [1,0,5,3,2]]
    sour = [75,150,75]
    dest = [100,60,40,75,25]
    t_max = 30
    T_max = 10
    p_mut = 0.5
    p_inv = 0.1
    old_population_GEN1 = create_starting_population_GEN1(size, sour, dest)
    old_population_GEN2 = create_starting_population_GEN2(size, sour, dest)
    number_of_couples = 0
    survive_next_generation = 5
    costGEN1, winnerGEN1 = main_GEN1(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN1, number_of_couples, survive_next_generation)
    costGEN2, winnerGEN2 = main_GEN2(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN2, number_of_couples, survive_next_generation)
    return costGEN1, winnerGEN1, costGEN2, winnerGEN2
#print("--------------------------------  TEST 6   -------------------------")
#print(test6())

# priblizno 3900 - izracunana v knjigi = 3900 http://www.maths.unp.ac.za/coursework/MATH331/2012/transportation_assignment.pdf table 6
def test7():
    size = 10
    cost = [[5,4,3],[8,4,3], [9,7,5]]
    sour = [100,300,300]
    dest = [300,200,200]
    t_max = 30
    T_max = 10
    p_mut = 0.5
    p_inv = 0.1
    old_population_GEN1 = create_starting_population_GEN1(size, sour, dest)
    old_population_GEN2 = create_starting_population_GEN2(size, sour, dest)
    number_of_couples = 0
    survive_next_generation = 5
    costGEN1, winnerGEN1 = main_GEN1(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN1, number_of_couples, survive_next_generation)
    costGEN2, winnerGEN2 = main_GEN2(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN2, number_of_couples, survive_next_generation)
    return costGEN1, winnerGEN1, costGEN2, winnerGEN2
#print("--------------------------------  TEST 7   -------------------------")
#print(test7())

# priblizno 1065 - osnovna izracunana = 1265 http://www.maths.unp.ac.za/coursework/MATH331/2012/transportation_assignment.pdf table 6
def test8():
    size = 8
    cost = [[10,30,25,15],[20,15,20,10], [10,30,20,20],[30,40,35,45]]
    sour = [14,10,15,13]
    dest = [10,15,12,15]
    t_max = 30
    T_max = 10
    p_mut = 0.5
    p_inv = 0.1
    old_population_GEN1 = create_starting_population_GEN1(size, sour, dest)
    old_population_GEN2 = create_starting_population_GEN2(size, sour, dest)
    number_of_couples = 1
    survive_next_generation = 5
    costGEN1, winnerGEN1 = main_GEN1(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN1, number_of_couples, survive_next_generation)
    costGEN2, winnerGEN2 = main_GEN2(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population_GEN2, number_of_couples, survive_next_generation)
    return costGEN1, winnerGEN1, costGEN2, winnerGEN2
print("--------------------------------  TEST 8   -------------------------")
print(test8())


v_1 = np.array([[1,0,0,7,0],[0,4,0,0,0],[2,1,4,0,5],[0,0,6,0,0]])
v_2 = np.array([[0,0,5,0,3],[0,4,0,0,0],[0,0,5,7,0],[3,1,0,0,2]])
print(crossover_GEN2(v_1, v_2))

REM = np.array([[1., 0., 1., 1., 1.],[0., 0., 0., 0., 0.],[0., 1., 1., 1., 1.],[1., 1., 0., 0., 0.]])
sourrempol = [2,0,2,1]
destrempol = [1,1,1,1,1]
rem1 = np.zeros((4,5))
rem2 = np.zeros((4,5))

def najdi_enko(matrika):
    n = matrika.shape[0]
    k = matrika.shape[1]
    for i in range(n):
        for j in range(k):
            if matrika[i][j] == 1:
                return i,j
    return False


def razdeli_rem(rem, rem1, rem2,sourrempol,destrempol):
    print("sum od rem" + str(sum(sum(rem))))
    sourrem1 = np.sum(rem1, axis = 1)
    destrem1 = np.sum(rem1, axis = 0)
    #print("rem1:" + str(rem1) + "     rem2:" + str(rem2))
    if sum(sum(rem)) == 0:
        if np.array_equal(sourrem1,sourrempol) and np.array_equal(destrem1,destrempol):
            return rem1, rem2
        else:
            return False
    else:
        i,j = najdi_enko(rem)
        rem[i][j] = 0
        if (sourrem1[i] < sourrempol[i]) and (destrem1[j] < destrempol[j]):
            print("USPELO" + str(sourrem1) + "\n" + str(rem1) + "\n" + str(rem2))
            rem_copy = copy.deepcopy(rem)
            rem1_copy = copy.deepcopy(rem1)
            rem2_copy = copy.deepcopy(rem2)
            rem1_copy[i][j] = 1
            a = razdeli_rem(rem_copy,rem1_copy,rem2_copy,sourrempol,destrempol)
            if a != False:
                return a
            else:
                rem_copy2 = copy.deepcopy(rem)
                rem1_copy2 = copy.deepcopy(rem1)
                rem2_copy2 = copy.deepcopy(rem2)
                #rem1_copy2[i][j] = 0
                rem2_copy2[i][j] = 1
                return razdeli_rem(rem_copy2,rem1_copy2,rem2_copy2,sourrempol,destrempol)
        else:
            rem_copy3 = copy.deepcopy(rem)
            rem1_copy3 = copy.deepcopy(rem1)
            rem2_copy3 = copy.deepcopy(rem2)
            #rem1_copy3[i][j] = 0
            rem2_copy3[i][j] = 1
            return razdeli_rem(rem_copy3,rem1_copy3,rem2_copy3,sourrempol,destrempol)
            
            

#print(razdeli_rem(REM, rem1, rem2,sourrempol,destrempol))
