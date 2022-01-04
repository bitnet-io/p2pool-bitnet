from distutils.core import setup, Extension

ltc_scrypt_module = Extension('yespowerurx',
                               sources = ['yespowerurxmodule.c',
                                          'yespowerurx.c'],
                               include_dirs=['.'])

setup (name = 'yespowerurx',
       version = '1.0',
       description = 'Bindings for yespowerurx proof of work used by UraniumX',
       ext_modules = [ltc_scrypt_module])
