package main

import "fmt"
import "log"
import "os"
import "os/exec"

func main() {

	data_dir := os.Getenv("GETH_DATA_DIR")
	if data_dir == "" {
		log.Fatal("[ERROR] env [GETH_DATA_DIR] missing.")
		return
	}

	genesis_json := os.Getenv("GETH_GENESIS_JSON")
	if genesis_json == "" {
		log.Fatal("[ERROR] env [GETH_GENESIS_JSON] missing.")
		return
	}

	log.Printf("[INFO] starting geth\n\n    datadir: [%s]\n\n    init: [%s]\n\n", data_dir, genesis_json)

	command := exec.Command("geth", "--datadir", data_dir, "init", genesis_json)
	out, error := command.CombinedOutput()
	if error != nil {
		log.Fatal(error)
		return
	}
	fmt.Println(string(out))
}
