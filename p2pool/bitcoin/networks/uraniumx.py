import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9d9cdc3'.decode('hex')
P2P_PORT = 8334
ADDRESS_VERSION = 68
HUMAN_READABLE_PART = 'urx'
RPC_PORT = 8234
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_block_header(bitcoind, '6be1ade2619d1402571996e436b726c8b0bd72f10fdcae10cff5acd369118626')) and # genesis block
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))

SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//23500
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('yespowerurx').getHash(data, 80))
BLOCK_PERIOD = 150 # s
SYMBOL = 'URX'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'uraniumx') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/uraniumx/') if platform.system() == 'Darwin' else os.path.expanduser('~/.uraniumx'), 'uraniumx.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://explorer.uraniumx.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://explorer.uraniumx.org/address/'
TX_EXPLORER_URL_PREFIX = 'https://explorer.uraniumx.org/tx/'
SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 1e8
