# 该指令是给车发个速度，车会一直按照最后收到的速度一直行驶，直到接收到新的速度指令
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "
linear:
  x: 0.24631578947368427
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: -0.1578947368421053" -1
