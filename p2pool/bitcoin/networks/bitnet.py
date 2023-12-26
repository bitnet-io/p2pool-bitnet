import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fabfb5da'.decode('hex')
P2P_PORT = 9999
ADDRESS_VERSION = 111
ADDRESS_P2SH_VERSION = 196
HUMAN_READABLE_PART = 'bcrt'
RPC_PORT = 18332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
#            'litecoin' in (yield bitcoind.rpc_help()) and # new versions have "litecoinprivkey" but no "litecoinaddress"
            (yield helper.check_block_header(bitcoind, '11e712e923c7e29b16e1e5970ebe78bc2c7a8ac44283bc446278ae7a23ef4ad1')) and
                          (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 10000*100000000 
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('aurum_hash').getPoWHash(data))
BLOCK_PERIOD = 220 # s
SYMBOL = 'BCRT'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'bitnet') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/bitnet/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitnet'), 'bitnet.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/address/'
TX_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/tx/'

SANE_TARGET_RANGE = (2**256//1000000000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8

