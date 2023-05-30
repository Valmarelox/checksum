from distutils.core import setup, Extension

def build():
    checksum_module = Extension('checksum', 
            sources = ['checksum.c'],
            extra_compile_args=['-Wall', '-Wextra',
                '-Wno-missing-field-initializers', '-Werror'],
            extra_link_args=['-Wl,--build-id=none', '-s'])

    setup(name='checksum',
            version='1.0',
            description='Native checksum implementation for python',
            author='Efi Weiss',
            author_email='valmarelox@gmail.com',
            ext_modules = [checksum_module])


if __name__ == '__main__':
    build()
