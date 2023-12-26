from distutils.core import setup, Extension

aurum_hash_module = Extension('aurum_hash',
                               sources = ['aurum-module.c',
                                          'aurum.c'],
                               include_dirs=['.'])

setup (name = 'aurum_hash',
       version = '1.0',
       description = 'Bindings for aurum proof of work used by Bitnet IO',
       ext_modules = [aurum_hash_module])
