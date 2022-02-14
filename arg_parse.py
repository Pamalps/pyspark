import argparse

parser=argparse.ArgumentParser(description='Pamal test')
parse.add_argument('--date',type=str,default='current_date()')
parse.add_argument()
parse.add_argument()
parse.add_argument()
args=parser.parse_args()


print(args.date)