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
print(testni_primer_iz_knjige_map())

###################################################################################################
##### 2. DEL - PRIPRAVA POPULACIJE ######
###################################################################################################

def create_starting_population(size, the_map):
    #this just creates a population of different routes of a fixed size.  Pretty straightforward.
    population = []
    
    #for i in range(0,size):
        #population.append(initialization(the_map))
    return population

###################################################################################################
##### GEN1 ######
###################################################################################################
def initialization_GEN1(sour,dest):
    # funcija initialization

    n = len(sour)
    k = len(dest)

    v = np.zeros((n,k))
    
    transport = np.zeros((1, n*k), dtype=int)
    not_visited = list(range(1,k*n+1))

    while len(not_visited) > 0:
        q = random.choice(not_visited) #izbere naključnega izmed not_visited q
        not_visited.remove(q)
        i = (q-1)//k + 1 #opomba - floor((q-1)/k+1)=floor((q-1)/k)+1
        j = (q-1)%k + 1
        val = min(sour[i-1], dest[j-1])
        v[i-1][j-1] = val
        sour[i-1] -= val
        dest[j-1] -= val
    return v

v1 = initialization_GEN1([1,2,3,5], [4,3,4])
v2 = initialization_GEN1([1,2,3,5], [4,3,4])
print(initialization_GEN1([15,25,5], [5,15,15,10]))

def evaluation_GEN1(v,cost):
    # izracuna ceno celotnega prevoza glede na podan nacrt prevoza v in ceno cost
    n = v.shape[0]
    k = v.shape[1]
    transport_cost = 0
    for i in range(n):
        for j in range(k):
            transport_cost += (v[i][j])*(cost[i][j])
    return transport_cost

print(evaluation_GEN1(v1, initialize_map(4,3)))


###################################################################################################
##### 3. DEL - GENETIC OPERATORS ######
###################################################################################################

def inversion_GEN1(vektor):
    #za podan seznam vector vrne njegovo obrnjeno razlicico
    return reversed(vektor)

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
    print(indeks1, indeks2)
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

def evaluation_GEN2(v,cost):
    return evaluation_GEN1(v,cost)

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
    print(sourW, destW)
    W = initialization_GEN1(sourW,destW) #pazi! od tu naprej se sourW in destW spremenita
    for i in range(p):
        for j in range(q):
            v[indeksiI[i]][indeksiJ[j]] = W[i][j]
    return v

def crossover_GEN2(v1, v2):
    n = v1.shape[0]
    k = v1.shape[1]
    div = np.zeros((n,k))
    rem = np.zeros((n,k))
    rem1 = np.zeros((n,k)) #samo zaradi preglednosti
    rem2 = np.zeros((n,k)) #samo zaradi preglednosti
    V3 = np.zeros((n,k))
    V4 = np.zeros((n,k))
##    sodo = True
    sourrem = np.zeros((n))
    destrem = np.zeros((k))
    sourrem1 = np.zeros((n))
    destrem1 = np.zeros((k))
##    sourrem2 = np.zeros((n))
##    destrem2 = np.zeros((k))
    for i in range(n):
        for j in range(k):
            div[i][j] = (v1[i][j] + v2[i][j])//2
            r = (v1[i][j] + v2[i][j])%2
            rem[i][j] = r
            if r==1:
                sourrem[i] += 1
                destrem[j] +=1
            #if rem[i][j] == 1:
##            r = (v1[i][j] + v2[i][j])%2
##            if r==1:
##                if sodo:
##                    rem1[i][j] = 1
##                else:
##                    rem2[i][j] = 1
##                sodo = not sodo
    for i in range(n):
        for j in range(k):
            if rem[i][j] == 1:
                if (sourrem1[i] < sourrem[i]/2) and (destrem1[j] < destrem[j]/2):
                    rem1[i][j] = 1 #samo zaradi preglednosti
                    sourrem1[i] += 1
                    destrem1[j] += 1
                    V3[i][j] = div[i][j] + 1
                    V4[i][j] = div[i][j]
                else:
                    rem2[i][j] = 1 #samo zaradi preglednosti
##                    sourrem1[i] += 1
##                    destrem1[j] += 1
                    V3[i][j] = div[i][j]
                    V4[i][j] = div[i][j] + 1
            else:
                V3[i][j] = div[i][j]
                V4[i][j] = div[i][j]
    return V3, V4

print("v1")
print(v1)
print("v2")
print(v2)

V3,V4 = crossover_GEN2(v1,v2)
print(V4)
print(V3)





###### PRINT POP ######
def print_pop(population):
    for i in population:
        print(i)

##### FITNESS #####
##def fitness(route, the_map):
##    
##    score = 0
##    
##    for i in range(1, len(route)):
##        if (the_map[route[i-1]][route[i]] == 0) and i != len(the_map)-1:
##            print("WARNING: INVALID ROUTE")
##            print(route)
##            print(the_map)
##        score = score + the_map[route[i-1]][route[i]]
##
##    return score



