from setuptools import setup

package_name = 'my_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=['my_bringup'],
    install_requires=['setuptools', 'launch', 'launch_ros'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='My custom bringup launch package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
