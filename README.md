# getting started with geth on Ubuntu 18 (2018-12-31)

### go-ethereum
* https://ethereum.github.io/go-ethereum/install/

### installation

```
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum
```

# initializing geth genesis block

```
geth --datadir /home/${USER}/eth_private_net init /home/${USER}/eth_private_net/myGenesis.json
```

# running geth

```
geth --networkid "15" --nodiscover --datadir "/home/${USER}/eth_private_net" console 2>> /home/${USER}/eth_private_net/geth_err.log
```

# web3.js

* Geth とやりとりを行うための JavaScript library
  https://web3js.readthedocs.io

