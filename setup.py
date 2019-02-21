# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup

setup(
    name='troy_platform',     # 包名字
    version='0.1',   # 包版本
    description='This is a test of the prompt_toolkit',   # 简单描述
    author='niekl',  # 作者
    author_email='niekl@126.com',  # 作者邮箱
    url='',      # 包的主页
    packages=['troy_platform'],                 # 包
    install_requires=[
        'prompt_toolkit', 'terminaltables'],
    entry_points={
        'console_scripts': [
            'ptp=troy_platform.__main__:main',
        ],
    }
)
