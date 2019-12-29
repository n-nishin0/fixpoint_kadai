# プログラミング試験（フィックスポイント）

12月30日（月）10:00提出期限のプログラミング課題  
言語：python3系  
概要：Apache HTTPサーバのアクセスログを解析するプログラム

# Features

+ 問１　【アクセス件数の集計】　日付ごと、各時間単位で集計。リモートホスト毎（IP)にアクセスの件数を降順に集計する。
+ 問２　【複数ファイルの対応】　＊詳細はUsageへ。
+ 問３　【期限の指定】　＊詳細はUsageへ。
+ 問４　【大規模データへの対応】　アクセスログデータ一行毎に処理を行うようプログラムを記述。

# Requirement

* apache_log_parser
* ArgumentParser

# Installation

```bash
pip install apache_log_parser
pip install ArgumentParser
```

# Usage

+ １つのログファイルを解析する場合。-fオプションの後にファイル名を書く。パスはプログラム内で指定しているの書く必要なし。
```bash
python kadai.py -f hogehoge.log
```
+ 複数のログファイルを解析する場合。-fオプションの後にスペース区切りで複数ファイル名を書く。
```bash
python kadai.py -f hogehoge1.log hogehoge2.log hogehoge3.log ...
```
+ 期限を指定する場合。-pオプションの後に期限の開始日、終了日の順番に%y/%m/%dの書式で書く。
```bash
python kadai.py -p 2019/1/1 2020/1/1 -f hogehoge.log 
```
# DEMO

```bash
python kadai.py -f sample_log.log 
'2005/04/18 00'
[('10.2.3.4', 3)]
'2015/06/16 13'
[('104.33.70.151', 8),
 ('176.33.96.225', 3),
 ('32.129.29.109', 2),
 ('108.81.70.158', 1),
 ('192.75.60.93', 1),
 ('72.42.173.76', 1),
 ('168.180.150.153', 1),
 ('172.171.186.182', 1),
 ('212.147.150.123', 1),
 ('140.210.67.42', 1),
 ('152.90.29.208', 1)]
'2015/06/16 15'
[('32.129.29.109', 3)]
```

# Note

+ 結果は日付毎かつ時間毎の結果である。DEMOでの出力の、%y/%m/%dの後の数字は時間を表している。
+ 期限は開始日と終了日の両方が必要。
+ ファイル名を複数書いた場合、同じ日付（時間単位）で同じIPの場合は結果がマージされる。
+ ログファイルのパスはあらかじめプログラム内で指定している(/var/log/httpd/access_log)ため不要。

# Author

* 作成者：西野　直登
* 所属：北海道大学　情報科学院　修士1年
* E-mail：n-nishino@eis.hokudai.ac.jp / naoto8469@gmail.com

# License

"apache_log_parser" is © 2013-2015 Rory McCann, released under the terms of the GNU GPL v3 (or at your option a later version). If you'd like a different licence, please email rory@technomancy.org
