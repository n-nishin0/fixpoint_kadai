#-*-coding:utf-8-*-
import apache_log_parser
import sys
from pprint import pprint
from argparse import ArgumentParser
import datetime

log_path = '/var/log/httpd/access_log/'
line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

###プログラムのオプション引数を定義する関数（ファイル名と期間）
def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('-f', '--filename', type=str, nargs='+')
    argparser.add_argument('-p', '--period', type=str, nargs=2, default=False, help='Whether a period is specified')
    return argparser.parse_args()

###日付の時間単位でリモートホスト別のアクセス件数を辞書型に集計する関数
def Number_of_accesses_per_hour(dict, line, start_date=None, end_date=None):
    key_date = 0
    key_IP = 0
    log_line_data = line_parser(line)
    time = log_line_data['time_received_datetimeobj']

    ###期間の指定がある場合の条件分岐
    if start_date and end_date:#期間の指定がある場合
        if start_date <= time <= end_date:
            key_date = time.strftime("%Y/%m/%d %H")
            key_IP = log_line_data['remote_host']
    else:#期間の指定がない場合
        key_date = time.strftime("%Y/%m/%d %H")
        key_IP = log_line_data['remote_host']
    
    if key_date == 0:#要素がない場合、処理を抜ける
        return 0
    dict.setdefault(key_date,{})
    dict[key_date].setdefault(key_IP, 0) 
    dict[key_date][key_IP] += 1

        
if __name__ == "__main__":
    args = get_option()
    dict = {}

    for i in range(0,len(args.filename)):
        filename = args.filename[i]
        with open(log_path + filename, "r") as f:
            line = f.readline()
            while line:
                ###期間の指定がある場合の条件分岐
                if args.period:#期間の指定がある場合
                    start_date = datetime.datetime.strptime(args.period[0], "%Y/%m/%d")
                    end_date = datetime.datetime.strptime(args.period[1], "%Y/%m/%d")
                    Number_of_accesses_per_hour(dict, line, start_date, end_date)
                else:#期間の指定がない場合
                    Number_of_accesses_per_hour(dict, line)
                line = f.readline()

    ###以下時間帯ごとにアクセス件数の多いリモートホスト順を標準出力
    for key in dict.keys():
        pprint(key)
        pprint(sorted(dict[key].items(), key = lambda x : x[1], reverse=True))
