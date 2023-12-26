
import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import math, pack, jsonrpc



P2P_PREFIX = '0b110907'.decode('hex')
P2P_PORT = 9999
ADDRESS_VERSION = 111
ADDRESS_P2SH_VERSION = 196
HUMAN_READABLE_PART = 'tb'
RPC_PORT = 18332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'getreceivedbyaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'test'
        ))
#10,000 BIT subsidy
SUBSIDY_FUNC = lambda height: 10000*100000000 

POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('aurum_hash').getPoWHash(data))
BLOCK_PERIOD = 210 # s
SYMBOL = 'TB'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'bitnet') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/bitnet/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitnet'), 'bitnet.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/address/'
TX_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/tx/'


#SANE_TARGET_RANGE =  (2**256//2**32//1000000000 - 1, 2**256//2**32 - 1)  # TINY SHARES HERE
#SANE_TARGET_RANGE =  (2**256//2**4//1000000000 - 1, 2**256//1000 - 1)  # TINY SHARES HERE

#SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
#DUMB_SCRYPT_DIFF = 2**3
#DUST_THRESHOLD = 0.001e8



SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
#DUMB_SCRYPT_DIFF = 2**16
DUMB_SCRYPT_DIFF = 2**2
DUST_THRESHOLD = 0.001e8
