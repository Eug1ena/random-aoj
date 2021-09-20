# random-aoj

AOJ の問題からランダムに問題を選びます。

Solve した問題を除外することもできます。

## 導入方法

このライブラリを clone します。

```
$ git clone https://github.com/Eug1ena/random-aoj
```

## 使用方法

main.py を実行します。

```
$ cd random-aoj
$ python3 main.py
https://onlinejudge.u-aizu.ac.jp/problems/2918
```

-x オプションを付けると、既に解いた問題を除外することができます。<br>このオプションを付けて初めて実行するときには、AOJ の id と password が必要になります。

```
$ python3 main.py -x
You are not yet logged in to AOJ. Please log in.
Your AOJ id: hoge
Password: piyo
Login successful
https://onlinejudge.u-aizu.ac.jp/problems/1508
```