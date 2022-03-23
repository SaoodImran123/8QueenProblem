package main

import (
	"fmt"
	"github.com/MaxHalford/eaopt"
	"math/rand"
)

// QUEEN_COUNT Number of queens on the board
const QUEEN_COUNT = 8

// Number of solutions for a given board size
const SOLUTION_COUNT = 92

// Number of mutation to apply
const MUTATION_COUNT = 1

// Positions is the location of queens on the board
type Positions []int

// Evaluate Fitness function
func (P Positions) Evaluate() (float64, error) {

	collisionCount := MyEval(P)

	return collisionCount, nil
}

func (P Positions) Mutate(rng *rand.Rand) {
	eaopt.MutPermuteInt(P, MUTATION_COUNT, rng)
}

func (P Positions) Crossover(Y eaopt.Genome, rng *rand.Rand) {
	//eaopt.CrossPMXInt(P, Y.(Positions), rng)
	eaopt.CrossOXInt(P, Y.(Positions), rng)
}

func (P Positions) Clone() eaopt.Genome {
	var clone = make(Positions, len(P))
	copy(clone, P)
	return clone
}

// GenerateBoard Make a board of size n
func GenerateBoard(rng *rand.Rand) eaopt.Genome {
	//Generate empty slice of size n
	var positions = make(Positions, QUEEN_COUNT)

	//Get a random permutation of slice 0....n
	locations := rng.Perm(QUEEN_COUNT)

	//Assign queen location on board
	for i := 0; i < QUEEN_COUNT; i++ {
		positions[i] = locations[i]
	}

	return eaopt.Genome(positions)
}

func main() {
	//GA Settings
	var conf = eaopt.NewDefaultGAConfig()
	conf.PopSize = 1000
	conf.NGenerations = 10e10
	conf.ParallelEval = false
	var ga, err = conf.NewGA()
	if err != nil {
		fmt.Println(err)
		return
	}

	//Save solutions
	var solutions [][]int
	ga.Callback = func(ga *eaopt.GA) {
		for i := 0; i < len(ga.Populations[0].Individuals); i++ {
			if ga.Populations[0].Individuals[i].Fitness == 0 {
				if ga.Populations[0].Individuals[i].Evaluated == true {
					var solution []int = ga.Populations[0].Individuals[i].Genome.(Positions)
					if MyEval(solution) == 0 { //For some reason fitness zero above does not always work
						if UniqueSlice(solution, solutions) {
							solutions = append(solutions, solution)
						}
					}
				}

			}
		}

		//Print stats every generation
		fmt.Println("Solution Count: ", len(solutions), " Generation: ", ga.Generations)
		fmt.Println("\n~~~~~~~~~~~~~NEW GENERATION~~~~~~~~~~~~~~~\n")
	}

	// Stop early if all solutions are found
	ga.EarlyStop = func(ga *eaopt.GA) bool {
		if len(solutions) == SOLUTION_COUNT {
			fmt.Printf("\nFound all solutions after %d generations in %s\n\n", ga.Generations, ga.Age)
			return true
		}
		return false
	}

	// Run the GA
	err = ga.Minimize(GenerateBoard)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Display result
	Print2D(solutions)

}
