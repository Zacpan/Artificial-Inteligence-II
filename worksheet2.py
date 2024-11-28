import random
import copy


class Individual:
    def __init__(self, N):
        self.gene = [0] * N
        self.fitness = 0



def generate_population(size, N):
    population = []

    for i in range(size):
        individual = Individual(N)
        individual.gene = []
        for _ in range(N):
            random_gene = random.randint(0, 1)
            individual.gene.append(random_gene)

        individual.fitness = fitness_function(individual)
        population.append(individual)

    return population



def tournament_selection(population, size):
    tournament_pool = []


    for _ in range(size):
        random_id = random.randint(0, len(population) - 1)
        tournament_pool.append(population[random_id])

    
    fittest = max(tournament_pool, key=lambda ind: ind.fitness)

    return copy.deepcopy(fittest)


def single_point_crossover(parent1, parent2):
    cross_point = random.randint(1, len(parent1.gene) - 1)
    child1 = Individual(len(parent1.gene))
    child2 = Individual(len(parent2.gene))

   
    child1.gene = parent1.gene[:cross_point] + parent2.gene[cross_point:]
    child2.gene = parent2.gene[:cross_point] + parent1.gene[cross_point:]

    return child1, child2



def mutate(individual, mutation_rate):
    for i in range(len(individual.gene)):
        if random.random() < mutation_rate:
            individual.gene[i] = 1 - individual.gene[i]


def fitness_function(individual):
    return sum(individual.gene)


if __name__ == "__main__":
    N = 10  #Genome length
    P = 50  #Population size
    T = 2   #Tournament size
    MUTRATE = 0.01  #Mutation rate


    population = generate_population(P, N)


    selected_parents = []
    for _ in range(P):
        selected_parent = tournament_selection(population, T)
        selected_parents.append(selected_parent)


    offspring = []
    for i in range(0, len(selected_parents), 2):
        if i + 1 < len(selected_parents):
            parent1 = selected_parents[i]
            parent2 = selected_parents[i + 1]
            child1, child2 = single_point_crossover(parent1, parent2)
            offspring.append(child1)
            offspring.append(child2)


    for individual in offspring:
        mutate(individual, MUTRATE)


    for individual in offspring:
        individual.fitness = fitness_function(individual)


    new_fitness = []
    for individual in offspring:
        new_fitness.append(individual.fitness)


    best_fitness = new_fitness[0]
    for fitness in new_fitness:
        if fitness > best_fitness:
            best_fitness = fitness


    total_fitness = 0
    for fitness in new_fitness:
        total_fitness += fitness
    average_fitness = total_fitness / len(new_fitness)

    #Print results
    print("New Population After Crossover and Mutation:")
    print(f"Best Fitness: {best_fitness}")
    print(f"Average Fitness: {average_fitness}")
