# -*- coding: utf-8 -*-
#コマンドライン引数にて2数を入力し、それらの最も簡単な比を出力	
import sys

def main():
	argv = sys.argv
	argc = len(argv)
	if (argc != 3):
		#引数がちゃんとあるかチェック
		#正しくなければメッセージを出力して終了
		print('関数 %s に引数が足りません' %argv[0])
        print('python %s path type のように実行してください' %argv[0])
		quit()
	path = argv[1]
	type = argv[2]
    print('%s をチェックします' %type)
    execute_type = check_type 
	gcd = ImageResize(path, type)
    print("処理を終了します")

def ImageResize(path, type):
	
    

	return x

if __name__ == '__main__':
	main()

from PIL import Image, ImageFilter

class ImageRisizer(object):

    def __init__(self, path):

        im = Image.open(path)

 
    def export_bg(self):

        im.