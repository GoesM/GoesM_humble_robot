import subprocess
# 用户输入包名
flag = None
pkgs_name = ''

def input_flag():
    global flag
    while flag==None:
        flag = input("指定包请输入Y，all输入A:")
        if flag=='Y':
            flag=True
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
    return 


def main():
    input_flag()
    add_pkgs()

    C_colcon = f'''export CC=/usr/bin/clang
    export CXX=/usr/bin/clang++
    colcon build \\
        --cmake-clean-cache \\
    '''
    
    if flag!='A':
        C_colcon += f'''    --packages-select {pkgs_name} \\
        '''  # 将包名替换到指令字符串中
    
    C_colcon += f'''    --cmake-args \\
            -DBUILD_TESTING=OFF \\
            -DCMAKE_CXX_FLAGS="${{CMAKE_CXX_FLAGS}} -w -Wno-error -Wno-everything"  \\
            -DCMAKE_C_FLAGS="${{CMAKE_C_FLAGS}} -w -Wno-error -Wno-format-security"
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
