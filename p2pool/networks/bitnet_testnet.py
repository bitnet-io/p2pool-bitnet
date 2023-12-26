from p2pool.bitcoin import networks


PARENT = networks.nets['bitnet_testnet']



SHARE_PERIOD = 90 # seconds
CHAIN_LENGTH = 60*60//10 # shares
REAL_CHAIN_LENGTH = 60*60//10 # shares
TARGET_LOOKBEHIND = 100 # shares
SPREAD = 10 # blocks

IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
P2P_PORT = 9334
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 9555
BOOTSTRAP_ADDRS = [
        ]
ANNOUNCE_CHANNEL = '#p2pool-bitnet'
VERSION_CHECK = lambda v: None if 100400 <= v else 'Litecoin version too old. Upgrade to 0.10.4 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit', 'taproot'])
MINIMUM_PROTOCOL_VERSION = 70030
SEGWIT_ACTIVATION_VERSION = 13
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
