import os
import time

# 设置提交的时间间隔（秒）
interval = 60 * 60 * 24 # 每天提交一次

while True:
    # 设置提交的文件路径和提交信息
    file_path = "./commit_file"
    commit_message = "Daily commit"

    with open(file_path, "a") as f:
        f.write("\n# Add a new line")

    # 提交更改到 GitHub
    os.system("git add " + file_path)
    os.system("git commit -m \"" + commit_message + "\"")
    os.system("git push")

    # 等待下一次提交
    time.sleep(interval)
