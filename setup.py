import os
import shutil
import sys
import zipfile
import platform

from distutils.core import setup
from distutils.sysconfig import get_python_lib

version = __import__('p2pool').__version__
im64 = '64' in platform.architecture()[0]

extra_includes = []
import p2pool.networks
extra_includes.extend('p2pool.networks.' + x for x in p2pool.networks.nets)
import p2pool.bitcoin.networks
extra_includes.extend('p2pool.bitcoin.networks.' + x for x in p2pool.bitcoin.networks.nets)

if os.path.exists('INITBAK'):
    os.remove('INITBAK')
os.rename(os.path.join('p2pool', '__init__.py'), 'INITBAK')
try:
    open(os.path.join('p2pool', '__init__.py'), 'wb').write('__version__ = %r%s%sDEBUG = False%s' % (version, os.linesep, os.linesep, os.linesep))
    bundle = 1
    if im64:
        bundle = bundle + 2
    setup(name='p2pool',
        version=version,
        description='Peer-to-peer Bitcoin mining pool',
        author='Forrest Voight',
        author_email='forrest@forre.st',
        url='http://p2pool.forre.st/',
        data_files=[
            ('', ['README.md']),
            ('web-static', [
                'web-static/d3.v2.min.js',
                'web-static/index.html',
                'web-static/share.html',
            ]),
        ],

    )
finally:
    os.remove(os.path.join('p2pool', '__init__.py'))
    os.rename('INITBAK', os.path.join('p2pool', '__init__.py'))

win = '32'
if im64:
    win = '64'

dir_name = 'p2pool_win' + win + '_' + version

if os.path.exists(dir_name):
    shutil.rmtree(dir_name)

with zipfile.ZipFile(dir_name + '.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    for dirpath, dirnames, filenames in os.walk(dir_name):
        for filename in filenames:
            zf.write(os.path.join(dirpath, filename))

print dir_name
