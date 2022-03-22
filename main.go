// go get github.com/MaxHalford/eaopt
package main

import (
	"fmt"
	"github.com/MaxHalford/eaopt"
)

func main() {

	// Instantiate a GA with a GAConfig
	var ga, err = eaopt.NewDefaultGAConfig().NewGA()
	if err != nil {
		fmt.Println(err)
		return
	}

	// Set the number of generations to run for
	ga.NGenerations = 10

}
