



running local
```
python2 get-pip.py
python2 -m pip install .
python2 -m pip install twisted
python2 -m pip install wheel
python2 -m pip install zope

cd aurum-hash
python2 setup.py install


place bitnet.conf into /root/.bitnet/
bitnetd -testnet
bitnet-cli -testnet createwallet "default"
bitnet-cli -testnet unloadwallet "default"
bitnet-cli -testnet loadwallet "default" true
bitnet-cli -testnet getnewaddress "testing" "legacy"


adjust run-testnet.sh or run the command below

python2 run_p2pool.py --allow-obsolete-bitcoind --testnet --net bitnet-a YOUR-RECEIVING_ADDR -f 1 --give-author 0 --worker-port 80 --bitcoind-p2p-port 9999 --bitcoind-rpc-port 18332 testuser testpassword
 ```


# cpuminer
cpuminer-avx2 -a aurum --url stratum+tcp://127.0.0.1:80 --userpass your-testnet-receving-address:x -t 20 
