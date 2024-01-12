import subprocess
import time

def run_script(py_path, py_file):
    subprocess.run([py_path, py_file])

if __name__ == '__main__':
    python1_path = "C:\ProgramData\Anaconda3\python.exe"
    python2_path = "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"
    pyfile1 = "get_user.py"
    pyfile2 = "auto_update_email.py"
    while True:
        print("-------开始查询-{}-------".format(time.strftime("%Y-%m-%d %H:%M:%S")))
        run_script(python1_path, pyfile1)
        print("-------查询完毕-------")

        time.sleep(5)
        print("-------开始自动配置邮箱-------")
        run_script(python2_path, pyfile2)
        print("-------配置完毕-{}-------".format(time.strftime("%Y-%m-%d %H:%M:%S")))
        time.sleep(600)
        print("----------------------------")
        print("-------开始下一次循环-------")
