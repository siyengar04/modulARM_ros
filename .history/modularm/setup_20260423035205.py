import os
from setuptools import find_packages, setup
import glob
package_name = 'modularm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
                (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
                (os.path.join('share', package_name, 'description'), glob('description/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='samee',
    maintainer_email='sameeri2@illinois.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
