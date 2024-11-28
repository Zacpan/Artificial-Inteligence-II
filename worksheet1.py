import random
import copy

#Individual class defined
class Individual:
    def __init__(self, N):
        self.gene = [0] * N
        self.fitness = 0



#Population of individuals with random genes is generated
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
        
    
    print("DEBUG: Population of individuals created")
    
    return population





#Tournament selection
def tournament_selection(population, size):
    tournament_pool = []
    
    #Randomly selection individuals for tournemnt 
    for _ in range(size):
        random_id = random.randint(0, len(population) - 1)
        tournament_pool.append(population[random_id])
    
    #Return the fittested individuals from the tournement
    fittest = max(tournament_pool, key=lambda ind: ind.fitness)
    print("DEBUG. TOURNEMENT CONCLUDED")
    
    return copy.deepcopy(fittest)


#Returns the sum of the individual populations genes
def fitness_function(individual):
    print("DEBUG, FINTESSFUNCTION CALLED")
    return sum(individual.gene)

if __name__ == "__main__":
    #Paramenters
    N = 10  #Gnome length
    P = 50  #Population size
    T = 2   #Tournament size

    #Generate initial population
    population = generate_population(P, N)

    #Select parents using tournement selection
    #Each individual is put through the tournement and the best are selected
    selected_parents = []
    for _ in range(P):
        selected_parent = tournament_selection(population, T)
        selected_parents.append(selected_parent)




    #List to store fitness values
    initial_fitness = []
    for individual in population:
        initial_fitness.append(individual.fitness)

    #Find the best fitness in the population
    best_fitness = initial_fitness[0]
    for fitness in initial_fitness:
        if fitness > best_fitness:
            best_fitness = fitness

    #Calculate the average fitness of the population
    total_fitness = 0
    for fitness in initial_fitness:
        total_fitness += fitness
    average_fitness = total_fitness / len(initial_fitness)

    #Print results
    print("Initial Population:")
    print(f"Best Fitness: {best_fitness}")
    print(f"Average Fitness: {average_fitness}")
