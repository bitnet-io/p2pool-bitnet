from p2pool.bitcoin import networks

PARENT=networks.nets['uraniumx']
SHARE_PERIOD = 600 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 100 # shares
SPREAD = 3 # blocks
#IDENTIFIER = 'ff37d5b8c6923410'.decode('hex')
#PREFIX = 'dd08c1a53ef629b0'.decode('hex')
IDENTIFIER='361586989049F628'.decode('hex')
PREFIX='149398244D9286B6'.decode('hex')
P2P_PORT = 9888
MAX_TARGET=2**256//2**32 - 1
MIN_TARGET = 0
PERSIST=False
WORKER_PORT = 9555
BOOTSTRAP_ADDRS = [
        '172.105.240.205'
        ]
#ANNOUNCE_CHANNEL = ''	
VERSION_CHECK = lambda v: None if 2000000 <= v else 'uraniumx version too old. Upgrade to 2.0.0 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip34', 'bip65', 'bip66', 'csv', 'segwit' ])
MINIMUM_PROTOCOL_VERSION = 80003
SEGWIT_ACTIVATION_VERSION = 20000000
BLOCK_MAX_SIZE = 10000000
BLOCK_MAX_WEIGHT = 40000000
ALGORITHM = 'Yescrypt'
from p2pool.bitcoin import networks
from p2pool.util import math
