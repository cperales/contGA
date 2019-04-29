import numpy as np


def pop_fitness(pop, fun):
    len_pop = len(pop)
    fitness = np.ndarray(len_pop)
    for i, ind in zip(range(len_pop), pop):
        fitness[i] = fun(ind)
    return fitness


def select_parents(pop, fitness, num_parents):
    parents = np.empty((num_parents, pop.shape[1]))
    
    for parent_num in range(num_parents):
        idx_player_1 = np.random.randint(0, pop.shape[0])
        idx_player_2 = np.random.randint(0, pop.shape[0])
    
        idx_winner = idx_player_1
        if fitness[idx_player_1] > fitness[idx_player_2]:
            idx_winner = idx_player_2

        parents[parent_num, :] = pop[idx_winner, :]
    return parents


def select_elite(pop, fitness, num_ind):
    
    elite = np.empty((num_ind, pop.shape[1]))
    
    aux_fitness=fitness[:]
    
    for ind in range(num_ind):

        best_fitness_idx = np.where(aux_fitness == np.min(aux_fitness))
        best_fitness_idx = best_fitness_idx[0][0]
        aux_fitness[best_fitness_idx] = np.Inf
        
        elite[ind, :] = pop[best_fitness_idx, :]
    return elite


def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)
    
    for k in range(0, offspring_size[0],2):
        crossover_point = np.random.randint(low=1, high=offspring_size[0])
        parent1_idx = k
        parent2_idx = parent1_idx+1
        offspring[k, :crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]

        offspring[k+1, :crossover_point] = parents[parent2_idx, 0:crossover_point]
        offspring[k+1, crossover_point:] = parents[parent1_idx, crossover_point:]
    
    return offspring


def mutation(pop, mutation_rate, mutation_step):
    dim = pop.shape[1]
    for idx in range(pop.shape[0]):
        for w in range(dim):
            if np.random.uniform(0, 1.0) > mutation_rate:
                random_value = np.random.uniform(-mutation_step, mutation_step)
                pop[idx, w] = pop[idx, w] + random_value
    return pop


def continuous_genetic_algorithm(fitness_fun,
                                 dim,
                                 dom,
                                 sol_per_pop,
                                 num_parents,
                                 num_generations,
                                 mutation_rate,
                                 mutation_step):
    """
    :param fitness_fun: function with only one argument, the seed.
    :param seed: example of value.
    :param dom:
    :param sol_per_pop:
    :param num_parents:
    :param num_generations:
    :param mutation_rate:
    :param mutation_step:
    :return:
    """
    pop_size = (sol_per_pop, dim)
    new_population = np.random.uniform(low=dom[0], high=dom[1], size=pop_size)

    best_outputs = []
    for generation in range(num_generations):
    
        fitness = pop_fitness(new_population, fitness_fun)

        best_outputs.append(np.min(fitness))

        elite = select_elite(new_population, fitness, sol_per_pop-num_parents)

        parents = select_parents(new_population, fitness, num_parents)
     
        offspring_crossover = crossover(parents, offspring_size=(num_parents, dim))
        offspring_mutation = mutation(offspring_crossover, mutation_rate, mutation_step)

        new_population[0:elite.shape[0], :] = elite
        new_population[elite.shape[0]:, :] = offspring_mutation

    fitness = pop_fitness(new_population, fitness_fun)
    best_match_idx = np.where(fitness == np.min(fitness))
    best_match_idx=best_match_idx[0][0]

    return fitness[best_match_idx], new_population[best_match_idx]
