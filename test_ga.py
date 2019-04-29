import numpy as np
from contGA.ga import continuous_genetic_algorithm


def test_x_2():
    real_fitness = 0.0
    real_solution = np.zeros(4)

    def fitness_fun(ind):
        """
        Return i_1**2 + i_2**2 + ... + i_n**2 for i in ind.

        :param ind:
        :return:
        """
        return np.power(ind, 2).sum()

    # Calling genetic solver
    fitness, solution = continuous_genetic_algorithm(fitness_fun=fitness_fun,
                                                     dim=4,
                                                     dom=(-10, 10),
                                                     sol_per_pop=100,
                                                     num_parents=98,
                                                     num_generations=800,
                                                     mutation_rate=0.95,
                                                     mutation_step=1.0)
    np.testing.assert_almost_equal(fitness, real_fitness, 4)
    np.testing.assert_almost_equal(solution, real_solution, 2)
    print('fitness',fitness)
    print('solution', solution)


if __name__ == '__main__':
    test_x_2()
