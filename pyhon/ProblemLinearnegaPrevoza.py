import numpy as np
import random
import copy
import math
import matplotlib.pyplot as plt

###################################################################################################
##### 1. DEL - PRIPRAVA PRIMEROV ######
###################################################################################################


###### INITIALIZE_MAP ######
def initialize_map(n,m):
    # ta funkcija nam zgenerira problem, ki vsebuje m skladisc in m trgovin
    # vhodni podatki:
    #     n ... stevilo skladisc
    #     m ... stevilo trgovin
    # izhodni podatki:
    #     cost ... matrika, ki na (i,j)-tem mestu predstavlja ceno prevoza enega izdelka
    #             iz skladiscnega mesta i v trgovino j
    #     sour ... seznam, ki na i-tem mestu pove, koliko zaloge ima skladisce i
    #     dest ... seznam, ki na j-tem mestu pove, koliksna je zahteva trgovine j
    #
    # matrika cost je zastavljena tako, da vsebuje vrednosti med 1 in 6
    
    cost = np.zeros((n,m))
    
    for i in range(0, n):
        for j in range(0, m):
                cost[i][j] = int(((random.random()*10)+1)/2)+1
    return cost

###### TESTNI_PRIMER_IZ_KNJIGE_MAP #####
def testni_primer_iz_knjige_map():
    cost = np.zeros((3,4))
    cost[0][0] = 10
    cost[0][1] = 0
    cost[0][2] = 20
    cost[0][3] = 11
    cost[1][0] = 12
    cost[1][1] = 7
    cost[1][2] = 9
    cost[1][3] = 20
    cost[2][0] = 0
    cost[2][1] = 14
    cost[2][2] = 16
    cost[2][3] = 18
    return cost

testni_primer_iz_knjige_sour = np.array([15, 25, 5])
testni_primer_iz_knjige_dest = np.array([5,15,14,10])
##print(testni_primer_iz_knjige_map())


###################################################################################################
##### 2. DEL - PRIPRAVA ZAČETNE POPULACIJE ######
###################################################################################################
def initialization_GEN1(sour,dest):
    n = len(sour)
    k = len(dest)
    
    p = random.sample(list(range(n*k)),n*k)

    return p

def initialization_GEN2(sour,dest):
    # funcija initialization

    n = len(sour)
    k = len(dest)

    v = np.zeros((n,k))
    
    not_visited = list(range(1,k*n+1))

    sour_copy = copy.deepcopy(sour)
    dest_copy = copy.deepcopy(dest)

    while len(not_visited) > 0:
        q = random.choice(not_visited) #izbere naključnega izmed not_visited q
        not_visited.remove(q)
        i = (q-1)//k + 1 #opomba - floor((q-1)/k+1)=floor((q-1)/k)+1
        j = (q-1)%k + 1
        val = min(sour_copy[i-1], dest_copy[j-1])
        v[i-1][j-1] = val
        sour_copy[i-1] -= val
        dest_copy[j-1] -= val
    return v

v1 = initialization_GEN2([1,2,3,5], [4,3,4])
v2 = initialization_GEN2([1,2,3,5], [4,3,4])
##print(initialization_GEN2([15,25,5], [5,15,15,10]))


def create_starting_population_GEN1(size, sour, dest):
    population = []

    for i in range(0,size):
        population.append(initialization_GEN1(sour,dest))
    return population

population_starting_GEN1 = create_starting_population_GEN1(5,[1,2,3], [3,2,1])
##print("starting population GEN1: " + str(population_starting_GEN1))

def create_starting_population_GEN2(size, sour, dest):
    population = []
    
    for i in range(0,size):
        population.append(initialization_GEN2(sour,dest))
    return population

population_starting_GEN2 = create_starting_population_GEN2(5,[1,2,3], [3,2,1])
##print("starting population GEN2: " + str(population_starting_GEN2))

###################################################################################################
##### GEN1 ######
###################################################################################################
def evaluation_GEN2(v,cost):
    # izracuna ceno celotnega prevoza glede na podan nacrt prevoza v in ceno cost
    n = v.shape[0]
    k = v.shape[1]
    transport_cost = 0
    for i in range(n):
        for j in range(k):
            transport_cost += (v[i][j])*(cost[i][j])
    return transport_cost

def evaluation_GEN1(p,cost,sour,dest):
    n = len(sour)
    k = len(dest)

    all_cost = 0
    sour_copy = copy.deepcopy(sour)
    dest_copy = copy.deepcopy(dest)

    v = np.zeros((n,k)) #za test

    for indeks in range(n*k):
        q = p[indeks]
        i = (q-1)//k + 1 #opomba - floor((q-1)/k+1)=floor((q-1)/k)+1
        j = (q-1)%k + 1
        val = min(sour_copy[i-1], dest_copy[j-1])
        v[i-1][j-1] = val #za test
        sour_copy[i-1] -= val
        dest_copy[j-1] -= val
        all_cost = all_cost + val*cost[i-1][j-1]
##    print("test v: " + str(v))
##    print("test cost: " + str(cost))
    return all_cost
    
##print(evaluation_GEN1([1,2,3,4,7,9,5,8,6],initialize_map(3,3),[1,2,3], [3,2,1]))

###################################################################################################
##### 3. DEL - GENETIC OPERATORS ######
###################################################################################################

def inversion_GEN1(vektor):
    #za podan seznam vector vrne njegovo obrnjeno razlicico
    return list(reversed(vektor))

def mutation_GEN1(vektor):
    #za podan seznam vector vrne isti vektor, ki ima zamenjani dve vrednosti
    q = len(vektor)
    [indeks1,indeks2] = random.sample(range(q),2)
    element1 = vektor[indeks1]
    element2 = vektor[indeks2]
    vektor[indeks1] = element2
    vektor[indeks2] = element1
    return vektor

def crossover_GEN1(vektor1, vektor2):
    q = len(vektor1)
    [indeks1,indeks2] = random.sample(range(q+1),2)
##    print(indeks1, indeks2)
    if indeks1 > indeks2:
        indeks1, indeks2 = indeks2, indeks1
    part2 = vektor1[indeks1:indeks2]
    part1 = []
    while len(part1) < indeks1:
        a = vektor2[0]
        if a not in part2:
            part1 += [a]
        vektor2 = vektor2[1:]
    part3 = []
    while len(vektor2)>0:
        a = vektor2[0]
        if a not in part2:
            part3 += [a]
        vektor2 = vektor2[1:]
    return part1 + part2 + part3


###################################################################################################
##### GEN2 ######
###################################################################################################

###################################################################################################
##### 3. DEL - GENETIC OPERATORS ######
###################################################################################################

def mutation_GEN2(v):
    n = v.shape[0]
    k = v.shape[1]
    p = random.choice(range(2,n+1))
    q = random.choice(range(2,k+1))
    indeksiI = sorted(random.sample(range(n),p))
    indeksiJ = sorted(random.sample(range(k),q))
    sourW = np.zeros((p))
    destW = np.zeros((q))
    for i in range(p):
        for j in range(q):
            v_ij = v[indeksiI[i],indeksiJ[j]]
            sourW[i] = sourW[i] + v_ij
            destW[j] = destW[j] + v_ij
    ##print(sourW, destW)
    W = initialization_GEN2(sourW,destW) #pazi! od tu naprej se sourW in destW spremenita
    ##print(W)
    for i in range(p):
        for j in range(q):
            v[indeksiI[i]][indeksiJ[j]] = W[i][j]
    return v

def najdi_enko(matrika):
    n = matrika.shape[0]
    k = matrika.shape[1]
    for i in range(n):
        for j in range(k):
            if matrika[i][j] == 1:
                return i,j
    return False


def razdeli_rem(rem, rem1, rem2,sourrempol,destrempol):
    #print("sum od rem" + str(sum(sum(rem))))
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
            #print("USPELO" + str(sourrem1) + "\n" + str(rem1) + "\n" + str(rem2))
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

def crossover_GEN2(v1, v2):
    n = v1.shape[0]
    k = v1.shape[1]
    div = np.zeros((n,k))
    rem = np.zeros((n,k))
    rem1 = np.zeros((n,k))
    rem2 = np.zeros((n,k))
    V3 = np.zeros((n,k))
    V4 = np.zeros((n,k))
    sourrem = np.zeros((n))
    destrem = np.zeros((k))
    sourrem1 = np.zeros((n))
    destrem1 = np.zeros((k))
    for i in range(n):
        for j in range(k):
            div[i][j] = (v1[i][j] + v2[i][j])//2
            r = (v1[i][j] + v2[i][j])%2
            rem[i][j] = r
            if r==1:
                sourrem[i] += 1
                destrem[j] +=1
    sourrempol = np.zeros((n))
    destrempol = np.zeros((k))
    for i in range(n):
        sourrempol[i] = sourrem[i]/2
    for j in range(k):
        destrempol[j] = destrem[j]/2

    rem1, rem2 = razdeli_rem(rem, rem1, rem2,sourrempol,destrempol)
    for i in range(n):
        for j in range(k):
            V3[i][j] = div[i][j] + rem1[i][j]
            V4[i][j] = div[i][j] + rem2[i][j]
    return V3, V4

#print(razdeli_rem(REM, rem1, rem2,sourrempol,destrempol))


##print("v1")
##print(v1)
##print("v2")
##print(v2)
##
##V3,V4 = crossover_GEN2(v1,v2)
##print(V4)
##print(V3)

###################################################################################################
##### 4. DEL - CENE PREVOZOV ######
###################################################################################################
def cene_prevozov_GEN1(population, cost, sour, dest):
    cene = []
    for i in range(len(population)):
        cene += [evaluation_GEN1(population[i],cost,sour,dest)]
    return cene

##print(cene_prevozov_GEN1(population_starting_GEN1, initialize_map(3,3),[1,2,3], [3,2,1]))

def cene_prevozov_GEN2(population, cost):
    cene = []
    for i in range(len(population)):
        cene += [evaluation_GEN2(population[i],cost)]
    return cene

cost_starting_population_GEN2 = initialize_map(3,3)
##print(cost_starting_population_GEN2)
##print(cene_prevozov_GEN2(population_starting_GEN2, cost_starting_population_GEN2))

###################################################################################################
##### 5. DEL - SELECT MEMBER (RWS-priblizno) ######
###################################################################################################

def select_person(population, cost,sour,dest,T_max,GEN):
    size = len(population)
    if GEN == 1:
        vse_cene = cene_prevozov_GEN1(population,cost,sour,dest)
    if GEN == 2:
        vse_cene = cene_prevozov_GEN2(population,cost)
    S = sum(vse_cene)

    selected = False
    t = 0
    
    while ((not selected) and (t < T_max)):
        t +=1
        random_index = random.choice(range(size))
        p_mogoce_izbrani = population[random_index]
        verjetnost_da_izbrani = (vse_cene[random_index])/S
        r = random.random()
        if r > verjetnost_da_izbrani: #vecja, kot bo cena, manjsa je verjetnost, da bo izbran
            return p_mogoce_izbrani
    return population[random.choice(range(size))]

##print()
##print("test za select_person_GEN1")
##print("...")
##print(population_starting_GEN1)
##costtestni1 = initialize_map(3,3)
##print(cene_prevozov_GEN1(population_starting_GEN1,costtestni1,[1,2,3],[3,2,1]))
##print(select_person(population_starting_GEN1,costtestni1,[1,2,3],[3,2,1],5,1))
##print()

    

def main_GEN1(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population, number_of_couples, survive_next_generation):

    population = create_starting_population_GEN1(size, sour, dest)
    vse_cene = cene_prevozov_GEN1(population,cost,sour,dest)
    cena_najcenejsa = vse_cene[np.argmin(vse_cene)]
    best = cena_najcenejsa
    print(cena_najcenejsa)

    print("Starting iteration: Best so far is cost %i, winner is \n %s" % (best, str(population[np.argmin(vse_cene)])))
    
    for i in range(t_max):
        ##print("t=" + str(i))
        new_population = []
        
        if best != cena_najcenejsa:
            print("Iteration %i: Best so far is cost %i, winner is \n %s" % (i, best, str(population[np.argmin(vse_cene)])))
            cena_najcenejsa = best

        #naredi otroke
        for j in range(number_of_couples):
            parent_1 = select_person(population,cost,sour,dest,T_max,1)
            parent_2 = select_person(population,cost,sour,dest,T_max,1)
            child_1 = crossover_GEN1(parent_1,parent_2)
            child_2 = crossover_GEN1(parent_2,parent_1)
            new_population += [child_1, child_2]
        #mutriaj
        for j in range(len(new_population)):
            if random.random() < p_mut:
                person = new_population[j]
                new_population[j] = mutation_GEN1(person)
        #inverz
        for j in range(len(new_population)):
            if random.random() < p_inv:
                person = new_population[j]
                new_population[j] = inversion_GEN1(person)
        #ohranimo del generacije
        new_population += [population[np.argmin(vse_cene)]]
        for j in range(1, survive_next_generation):
            #keeper = population[np.argsort(vse_cene)[j]]
            keeper = select_person(population,cost,sour,dest,T_max,1)
            new_population += [keeper]
        #dodaj preostanek
        while len(new_population) < size:
            new_population += [initialization_GEN1(sour,dest)]
        population = copy.deepcopy(new_population)

        vse_cene = cene_prevozov_GEN1(population,cost,sour,dest)
        ##print(vse_cene)
        best = vse_cene[np.argmin(vse_cene)]
    return cena_najcenejsa, population[np.argmin(vse_cene)]

def main_GEN2(size,cost,sour,dest,t_max,T_max, p_mut, p_inv, old_population, number_of_couples, survive_next_generation):

    population = create_starting_population_GEN2(size, sour, dest)
    vse_cene = cene_prevozov_GEN2(population,cost)
    cena_najcenejsa = vse_cene[np.argmin(vse_cene)]
    best = cena_najcenejsa
    print(cena_najcenejsa)

    print("Starting iteration: Best so far is cost %i, winner is \n %s" % (best, str(population[np.argmin(vse_cene)])))
    
    for i in range(t_max):
        ##print("t=" + str(i))
        new_population = []
        
        if best != cena_najcenejsa:
            print("Iteration %i: Best so far is cost %i, winner is \n %s" % (i, best, str(population[np.argmin(vse_cene)])))
            cena_najcenejsa = best

        #naredi otroke
        for j in range(number_of_couples):
            parent_1 = select_person(population,cost,sour,dest,T_max,2)
            parent_2 = select_person(population,cost,sour,dest,T_max,2)
            child_1, child_2 = crossover_GEN2(parent_1,parent_2)
            new_population += [child_1, child_2]
        #mutriaj
        for j in range(len(new_population)):
            if random.random() < p_mut:
                person = new_population[j]
                new_population[j] = mutation_GEN2(person)
        #ohranimo del generacije
        new_population += [population[np.argmin(vse_cene)]]
        for j in range(1, survive_next_generation):
            #keeper = population[np.argsort(vse_cene)[j]]
            keeper = select_person(population,cost,sour,dest,T_max,2)
            new_population += [keeper]
        #dodaj preostanek
        while len(new_population) < size:
            new_population += [initialization_GEN2(sour,dest)]
        population = copy.deepcopy(new_population)

        vse_cene = cene_prevozov_GEN2(population,cost)
        ##print(vse_cene)
        best = vse_cene[np.argmin(vse_cene)]
    return cena_najcenejsa, population[np.argmin(vse_cene)]


###### PRINT POP ######
def print_pop(population):
    for i in population:
        print(i)



##print(main_GEN1(6,[[1,2,3,4],[5,6,7,8],[9,8,20,6],[30,8,9,5]],[17,5,23,15],[15,23,17,5],20,8, 0.5, 0.1,population_starting_GEN1,1,2))
##print(main_GEN2(6,[[1,2,3,4],[5,6,7,8],[9,8,20,6],[30,8,9,5]],[17,5,23,15],[15,23,17,5],20,8, 0.5, 0.1,population_starting_GEN2,1,2))
