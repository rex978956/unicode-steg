from setuptools import find_packages, setup

setup(
    name='unicode_steg',
    version=__import__('unicode_steg').__version__,
    description='Unicode Steganography with Zero-Width Characters',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rex Weng',
    author_email='me@rexweng.tw',
    url='https://github.com/rex978956/unicode_steg',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3 :: Only',
    ],
)
