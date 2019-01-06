#!/bin/bash
function main() {

	touch /home/${USER}/eth_private_net/geth_err.log
	geth --networkid "15" --nodiscover --datadir "/home/${USER}/eth_private_net" console 2>> /home/${USER}/eth_private_net/geth_err.log
}

main;
