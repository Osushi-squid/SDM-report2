#!/usr/bin/python3

import re
                
def calc(ai, bi):
    # 型チェック（int 以外は即 NG）
    if not isinstance(ai, int) or not isinstance(bi, int):
        return -1

    # 範囲チェック
    if ai < 1 or ai > 999 or bi < 1 or bi > 999:
        return -1

    return ai * bi

        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
