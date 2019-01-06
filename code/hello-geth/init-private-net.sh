#!/bin/bash

function main {

	export GETH_DATA_DIR=/home/${USER}/eth_private_net
	export GETH_GENESIS_JSON=/home/${USER}/eth_private_net/myGenesis.json
	go run init-private-net.go
}

main;
