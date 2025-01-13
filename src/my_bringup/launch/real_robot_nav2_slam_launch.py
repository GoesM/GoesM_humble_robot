from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
import os
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    slam_toolbox_dir = get_package_share_directory('slam_toolbox')
    slam_toolbox_launch_dir = os.path.join(slam_toolbox_dir, 'launch')

    nav2_dir = get_package_share_directory('nav2_bringup')
    nav2_launch_dir = os.path.join(nav2_dir, 'launch')
    
    return LaunchDescription([
        # 启动 nav2_bringup rviz_launch
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_launch_dir, 'nav2_bringup', 'rviz_launch.py')
            ),
        ),
        # 启动 nav2_bringup navigation_launch
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_launch_dir, 'nav2_bringup', 'navigation_launch.py')
            ),
        ),
    ])
