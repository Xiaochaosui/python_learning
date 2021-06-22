import argparse
'''
argparse 
python自带的命令行参数解析包，方便的读取命令行参数
'''
def main():
    parser = argparse.ArgumentParser(description='Demo of argparse')
    parser.add_argument('-n','--name',default='Li')
    parser.add_argument('-y','--year',default='20')
    args = parser.parse_args()
    print(args)
    name = args.name
    year = args.year
    print(name,year)

if __name__ == '__main__':
    main()