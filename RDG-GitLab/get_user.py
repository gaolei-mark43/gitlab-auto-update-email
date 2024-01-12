import requests
from functools import wraps
import time

# 装饰器：计算函数的执行时间
def calculate_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("函数{}执行时间：".format(func.__name__), execution_time, "秒")
        return result
    return wrapper

@calculate_execution_time
def get_all_user_data():
    url = "https://gitlab.test.com/api/v4/users"
    params = {
        "per_page": 100,
        "page": 1
    }
    headers = {
      'PRIVATE-TOKEN': 'XXXXXXXXXXX' #超管Git-token
    }
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        total_users = int(response.headers.get("X-Total"))
        total_pages = int(response.headers.get("X-Total-Pages"))
        print("总用户数量:", total_users)
        print("总页数:", total_pages)

        all_users = []

        # 循环查询所有页面的数据
        for page in range(1, total_pages + 1):
            params["page"] = page
            response = requests.get(url, params=params, headers=headers)
            if response.status_code == 200:
                users = response.json()
                all_users.extend(users)
        # 数据循环写入文件
        print("总用户数量:", len(all_users))
        with open("user_data2.txt", "w") as f:
            for user in all_users:
                f.write(str(user) + "\n")

    else:
        print("返回错误:", response.status_code)


# 扫描email字段值为temp-email-for-oauth-开头、gitlab.localhost结尾的用户
def get_error_email_user():
    new_users = []
    with open("user_data2.txt", "r") as f:
        users = f.readlines()
        count = 0
        for user in users:
            user = eval(user)
            email = user["email"]
            if email.startswith("temp-email-for-oauth-") and email.endswith("gitlab.localhost"):
                count += 1
                new_users.append(user["name"])
        print("满足条件的用户数量:", count)
        # 返回用户列表name字段值
        return new_users


# 将get_error_email_user返回new_users写进文件保存
def write_new_users(new_users):
    with open("new_users.txt", "w") as f:
        for user in new_users:
            f.write(user + "\n")


if __name__ == '__main__':
    start_time = time.time()
    get_all_user_data()
    a = get_error_email_user()
    print(a)
    new_users = get_error_email_user()
    write_new_users(new_users)
    end_time = time.time()
    print("本次查询耗时：", end_time - start_time, "秒")