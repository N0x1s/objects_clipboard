from distutils.core import setup
setup(
    name='objects_clipboard',
    packages=['objects_clipboard'],
    version='0.1',
    license='MIT',
    description='objects clipboard',
    author='n0x1s',
    author_email='n0x1s0x01@gmail.com',
    url='https://github.com/n0x1s/objects_clipboard',
    download_url='https://github.com/N0x1s/objects_clipboard/archive/0.1.tar.gz',
    keywords=['objects clipboard', 'share objects', 'pickle',
              'clipboard'],
    install_requires=[
          'pyperclip',
      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
