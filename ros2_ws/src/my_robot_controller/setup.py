from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cagla',
    maintainer_email='cagla@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # "derleme ismi = paket_ismi.dosya_ismi:main" 
            'test_node = my_robot_controller.my_first_node:main',
            "draw_circle = my_robot_controller.draw_circle:main",
            "turtle_controller = my_robot_controller.turtle_controller:main",
            "pose_subscriber = my_robot_controller.pose_subscriber:main"
        ],
    },
)
