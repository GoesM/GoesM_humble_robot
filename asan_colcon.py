import subprocess
import sys
# 用户输入包名
flag = None
pkgs_name = ''

def input_flag():
    global flag
    while flag==None:
        flag = input("指定包asan请输入Y，否则输入N,all输入A:")
        if flag=='Y':
            flag=True
        elif flag=='N':
            flag=False
        elif flag=='A':
            flag = 'A'
        else:
            flag=None

def add_pkg(pkg_name):
    global pkgs_name
    if(pkgs_name==''):
        pkgs_name = pkg_name
        return
    pkgs_name = pkgs_name + f" {pkg_name}"
    return 
def add_pkgs():
    global pkgs_name
    if flag==True:
        pkgs_name = input("请输入包名: ")
    elif flag=='A':
        return
    else:
        add_pkg("nav2_amcl")
        add_pkg("nav2_behaviors")
        # add_pkg("nav2_behavior_tree") #会使lifecycle不正常运行
        add_pkg("nav2_bringup")
        add_pkg("nav2_bt_navigator")
        add_pkg("nav2_collision_monitor")
        add_pkg("nav2_common")
        add_pkg("nav2_constrained_smoother")
        add_pkg("nav2_controller")
        add_pkg("nav2_core")
        # add_pkg("nav2_costmap_2d")  #rviz不显示cost界面，小车无法移动
        add_pkg("nav2_dwb_controller")
        # add_pkg("nav2_lifecycle_manager") #rviz界面中的“Amcl_Particle_Swarm”会被标记为红色。
        add_pkg("nav2_map_server")
        add_pkg("nav2_mppi_controller")
        # add_pkg("nav2_msgs")    # rviz界面中的“Amcl_Particle_Swarm”会被标记为红色。
        add_pkg("nav2_navfn_planner")
        add_pkg("nav2_planner")
        add_pkg("nav2_regulated_pure_pursuit_controller")
        add_pkg("nav2_rotation_shim_controller")
        #  add_pkg("nav2_rviz_plugins")   # rviz界面中的“Amcl_Particle_Swarm”会被标记为红色。
        add_pkg("nav2_simple_commander")
        add_pkg("nav2_smac_planner")
        add_pkg("nav2_smoother")
        add_pkg("nav2_theta_star_planner")
        # add_pkg("nav2_util") #rviz不加载地图
        add_pkg("nav2_velocity_smoother")
        add_pkg("nav2_voxel_grid")  
        add_pkg("nav2_waypoint_follower") 
    return 


def main():
    input_flag()
    add_pkgs()

    C_colcon = f'''
    export CC=/usr/bin/clang
    export CXX=/usr/bin/clang++
    colcon build \\
        --cmake-clean-cache \\
    '''
    
    if flag!='A':
        C_colcon += f'''    --packages-select {pkgs_name} \\
        '''  # 将包名替换到指令字符串中
    C_colcon += f'''    --cmake-args \\
            -DBUILD_TESTING=OFF \\
            -DCMAKE_CXX_FLAGS="${{CMAKE_CXX_FLAGS}} -w -Wno-error -Wno-everything -fsanitize=address --coverage -DCOVERAGE_RUN=1"  \\
            -DCMAKE_C_FLAGS="${{CMAKE_C_FLAGS}} -w -Wno-error -Wno-format-security -fsanitize=address --coverage -DCOVERAGE_RUN=1"
    '''    

    print(C_colcon)

    try:
        print("===================Wait!!===================")
        txt = subprocess.check_output(C_colcon,shell=True).decode()
        if 'failed' not in txt:
            print("===================Asan编译成功===================")
        else:
            print("===================Asan编译失败===================")
    except subprocess.CalledProcessError as e:
        print("====================Asan编译失败======================")
    return

if __name__ == "__main__":
    main()
