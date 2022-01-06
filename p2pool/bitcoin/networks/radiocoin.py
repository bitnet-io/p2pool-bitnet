import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

	      
P2P_PREFIX = 'd1d1d1d1'.decode('hex')
P2P_PORT = 8333
ADDRESS_VERSION = 60
ADDRESS_P2SH_VERSION = 22
HUMAN_READABLE_PART = 'radc'
RPC_PORT = 9332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
	    (yield helper.check_block_header(bitcoind, '000007ce46e6c59844c34fa7ba5b27c8dac0653a27fcfb7340cc0158849e4afd')) and # genesis block
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))		         
#SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//100000
#SUBSIDY_FUNC = lambda height: 50*100000000000 >> (height + 1)//100000
SUBSIDY_FUNC = lambda height: 6250000*1000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 90 # s
SYMBOL = 'RADC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'RadioCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/RadioCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.radiocoin'), 'radiocoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://radioblockchain.info/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://radioblockchain.info/block/'
TX_EXPLORER_URL_PREFIX = 'http://radioblockchain.info/tx/'

#SANE_TARGET_RANGE = (2**256//1000000000000000 - 1, 2*256//1000 - 1)
#SANE_TARGET_RANGE =  (2**256//100000000 - 1, 2**256//500000 - 1)




#last known working 125,000 coins
SANE_TARGET_RANGE = (2**256//10000000000 - 1, 2**256//16800000 - 1)


DUMB_SCRYPT_DIFF = 2**15
DUST_THRESHOLD = 0.03e8


