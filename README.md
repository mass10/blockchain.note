# Bitcoin Core

- オフィシャルクライアントソフトウェア
- C++

# Installing bitcoin core on Ubuntu

```bash
sudo apt-add-repository ppa:bitcoin/bitcoin
sudo apt-get update
sudo apt-get install bitcoind
```

# starting node

```bash
# by normal user
bitcoind -daemon
```

# getting started with geth on Ubuntu 18 (2018-12-31)

### go-ethereum

* https://ethereum.github.io/go-ethereum/install/

### installation

```bash
sudo add-apt-repository ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum
```

# initializing geth genesis block

```bash
geth --datadir /home/${USER}/eth_private_net init /home/${USER}/eth_private_net/myGenesis.json
```

# running geth

```bash
geth --networkid "15" --nodiscover --datadir "/home/${USER}/eth_private_net" console 2>> /home/${USER}/eth_private_net/geth_err.log
```

# attach geth

```bash
cd "/home/${USER}/eth_private_net"
geth attach geth.ipc
```

# アカウントを作成する

```bash
geth attach geth.ipc
```

```geth
> personal.newAccount("password")
```

# web3.js

* Geth とやりとりを行うための JavaScript library https://web3js.readthedocs.io

# パブリックネットワーク

* 不特定多数のノードが参加できる。
* 参加には制限なし。
* ブロックチェーンは共有されている。
* 一切の中央集権的機関がない。
* PoW などのコンセンサスアルゴリズムによってネットワークが維持されている。
* パブリックに運用されているチェーンのことを「パブリックチェーン」と言ったりもする。

# コンソーシアムネットワーク

* 複数のノードによって合意形成をして管理されている。
* チェーンへの参加者は制限されている。

# プライベートネットワーク

* ある閉鎖的な領域(個人、プロダクト、組織など)の内部で管理、運用されているネットワーク。何らかの中央集権的組織が台帳の記録、管理をしている。

# PoW

* 計算に大きな電力量が必要。
* 高コスト。
* Bitcoin では、ブロックの生成に10分かかっている。
* ファイナリティなし。
* ノードが51%の力を集めると、悪意のある改ざんが可能になる。
