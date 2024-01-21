import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'd1e1d1e1'.decode('hex')
P2P_PORT = 9999
ADDRESS_VERSION = 25
ADDRESS_P2SH_VERSION = 22
HUMAN_READABLE_PART = 'bit'
RPC_PORT = 18332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'getreceivedbyaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))

#10,000 BIT per block here until height 125,000
SUBSIDY_FUNC = lambda height: 10000*100000000 >> (height + 1)//6000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('aurum_hash').getPoWHash(data))
BLOCK_PERIOD = 220 # s
SYMBOL = 'BIT'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'bitnet') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/bitnet/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitnet'), 'bitnet.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://bitexplorer.io/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://bitexplorer.io/address/'
TX_EXPLORER_URL_PREFIX = 'https://bitexplorer.io/tx/'

#SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
#DUMB_SCRYPT_DIFF = 1
#DUST_THRESHOLD = 0.001e8

SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)

								#DUMB_SCRYPT_DIFF = 2**14
								# last working with hashrate #DUMB_SCRYPT_DIFF = 4096
								#DUMB_SCRYPT_DIFF = 2**6

DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
