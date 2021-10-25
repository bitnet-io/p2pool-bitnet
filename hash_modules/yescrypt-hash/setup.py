from distutils.core import setup, Extension

yescrypt_hash_module = Extension('yescrypt_hash', sources = ['yescryptmodule.c'], extra_compile_args=['-march=native'],
                               include_dirs=['.'])

#ltc_scrypt_module = Extension('ltc_scrypt',
 #                              sources = ['scryptmodule.c',
  #                                        'scrypt.c'],
   #                            include_dirs=['.'])


setup (name = 'yescrypt_hash',
       version = '1.0',
       ext_modules = [yescrypt_hash_module])
