## CEC-2008

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pygmo as pg
import pandas as pd
from opfunu.cec.cec2008.F1 import Model as m1
from opfunu.cec.cec2008.F2 import Model as m2
from opfunu.cec.cec2008.F3 import Model as m3
from opfunu.cec.cec2008.F4 import Model as m4
from opfunu.cec.cec2008.F5 import Model as m5
from opfunu.cec.cec2008.F6 import Model as m6
import tkinter as tk
from tkinter import simpledialog
import time

#Wrapping opfunu funcions into a class for PyGMO 
class functions:
    def __init__(self, f, dim):
        self.dim = dim
        if(f==1):
            self.f=m1()
            self.contour= np.loadtxt('F1_contour_solution.txt')
            self.bounds = ([-100] * self.dim, [100] * self.dim)
        elif(f==2):
           self.f=m2()
           self.contour= np.loadtxt('F2_contour_solution.txt')
           self.bounds = ([-100] * self.dim, [100] * self.dim)
        elif(f==3):
           self.f=m3()
           self.contour= np.loadtxt('F3_contour_solution.txt')
           self.bounds = ([-100] * self.dim, [100] * self.dim)
        elif(f==4):
           self.f=m4()
           self.contour= np.loadtxt('F4_contour_solution.txt')
           self.bounds = ([-5] * self.dim, [5] * self.dim)
        elif(f==5):
           self.f=m5()
           self.contour= np.loadtxt('F5_contour_solution.txt')
           self.bounds = ([-600] * self.dim, [600] * self.dim)
        elif(f==6):
           self.f=m6()
           self.contour= np.loadtxt('F6_contour_solution.txt')
           self.bounds = ([-32] * self.dim, [32] * self.dim)
        else:
            print("ERROR: Invalid function parameter") 
        
    
    def fitness(self, x):
        return [self.f._main__(x)]

    def get_bounds(self):
         return self.bounds

#driver code
def main(): 
    #Hyperparameters
    #---------------
    swarm= 20
    ind_best_weight= 1.2 #1.19314
    neigh_best_weight= 1.19314
    intertia_weigth= 0.72134

    #1 - gbest
    #2 - lbest
    #3 - Von Neumann
    #4 - Adaptive random
    neighb_topology= 1 
    neighb_param =4  # 3 # K informants

    #1 - Canonical (with inertia weight)
    #2 - Same social and cognitive rand.
    #3 - Same rand. for all components
    #4 - Only one rand.
    #5 - Canonical (with constriction fact.)
    #6 - Fully Informed (FIPS)
    pso_variant= 6
    swarm_size= 25
    generations=100

    #Select problem and dimensions
    application_window = tk.Tk()
    f_problem = simpledialog.askinteger("Input", "What problem (F) do you want to optimize? (1-6)", parent=application_window,  minvalue=1, maxvalue=6)
    dimensions = simpledialog.askinteger("Input", "For how many dimensions? (1-500)", parent=application_window, minvalue=1, maxvalue=500)

    swarm_size= 25
    #Solver
    #------
    print('\n----------------------------------------------')
    print('\nOptimization:')
    start = time.time()

    prob = pg.problem(functions(f=f_problem,dim=dimensions))
    pop = pg.population(prob, size=swarm_size)
    algo = pg.algorithm(pg.pso(gen=generations, omega=intertia_weigth, eta1=neigh_best_weight, eta2=ind_best_weight, max_vel=1, variant=pso_variant, neighb_type=neighb_topology, neighb_param= neighb_param, memory=False, seed=123))
    algo.set_verbosity(1)
    pop = algo.evolve(pop)
    log = algo.extract(pg.pso).get_log() 

    best_fitness = pop.get_f()[pop.best_idx()] # Getting the best individual in the population
    print('\n----------------------------------------------')
    print('\nResult:')
    print('\nBest fitness: ', best_fitness) # Get the best parameter set
    best_parameterset = pop.get_x()[pop.best_idx()]
    print('\nBest parameter set: ',best_parameterset)
    print('\nTime elapsed for optimization: ', time.time() - start, ' seconds\n')


    #Plot convergence curve (Iterations)
    x = [x[0] for x in log]
    y = [y[2] for y in log]
    z = [z[1] for z in log]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='lightblue', linewidth=1)
    ax.set_xlim(1, generations)
    plt.show()

    #For 2D
    if (dimensions==2):
        #Plot last swarm and best particle in contour plot
        f1= functions(f=f_problem,dim=dimensions)
        x = np.arange(f1.bounds[0][0], f1.bounds[1][1], 1)
        y = np.arange(f1.bounds[0][0], f1.bounds[1][1], 1)
        z= f1.contour
        #z=np.transpose(z)
        #h = plt.contourf(x[0:199],y[0:199],z[0:199,0:199])
        h = plt.contourf(x,y,z)
        plt.plot(pop.get_x()[:,0],pop.get_x()[:,1], 'b+')
        plt.plot(pop.get_x()[pop.best_idx()][0],pop.get_x()[pop.best_idx()][1], 'r+') 
        plt.show()


if __name__ == '__main__':
    main()