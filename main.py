import requests
import random
import json
import argparse
import sys
import os
import time

def fileExists(path):
    return os.path.isfile(path)

def openJsonFile(path):
    data = open(path, "r")
    return json.load(data)

def tryToLogin(id, password, session=requests):
    url = "https://judgeapi.u-aizu.ac.jp/session"
    return session.post(url, json={"id": id, "password": password})

def requestJson(url, session=requests):
    data = session.get(url).text
    return json.loads(data)

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--exclude", action="store_true", help="Option to exclude the problems solved by the user")

args = parser.parse_args()
isExcluding = args.exclude

MAX_PROBLEMS = 10000
if isExcluding:
    filePath = "./data.json"
    if fileExists(filePath):
        passJson = openJsonFile(filePath)
        if "id" in passJson and "password" in passJson:
            id = passJson["id"]
            password = passJson["password"]

            session = requests.Session()
            post = tryToLogin(id, password, session)

            ERROR_CODE = 400
            if post.status_code == ERROR_CODE:
                isLogin = False
            else:
                isLogin = True
        else:
            isLogin = False
    else:
        isLogin = False

    if not isLogin:
        print(f"You are not yet logged in to AOJ. Please log in.")
        id = input("Your AOJ id: ");
        password = input("Password: ");

        session = requests.Session()
        post = tryToLogin(id, password, session)
        ERROR_CODE = 400
        if post.status_code == ERROR_CODE:
            print("Login failed")
            sys.exit()

        print("Login successful")

        with open(filePath, mode="wt") as file:
            json.dump({"id": id, "password": password}, file)

        username = id
    else:
        username = id

    apiUrl = f"https://judgeapi.u-aizu.ac.jp/problems?size={ MAX_PROBLEMS }"
    rawProblems = requestJson(apiUrl, session)

    problems = list(filter(lambda prob: prob["isSolved"] == False, rawProblems))
else:
    apiUrl = f"https://judgeapi.u-aizu.ac.jp/problems?size={ MAX_PROBLEMS }"
    problems = requestJson(apiUrl)

id = random.choice(problems)["id"]

print(f"https://onlinejudge.u-aizu.ac.jp/problems/{ id }")

# 参考: https://github.com/sugyan/aoj/blob/master/random.rb
