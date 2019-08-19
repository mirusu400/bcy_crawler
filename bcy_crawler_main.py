# !/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
import argparse
import multiprocessing
from bcy_single_climber import bcy_single_climber
from bcy_user_climber import bcy_user_climber
def bcy_crawler():
    #if(len(sys.argv) == 1):
    #    print('usage : bcy_crawler_main.py ID [-j] [-d] Download images from bcy.net.\nOnly support like these form of links:\nbcy.net/item/detail/{Single_ID}\nbcy.net/u/{User_ID}')
    #    exit()
    parser = argparse.ArgumentParser(description="Download images from bcy.net.")
    parser.add_argument('Link', type=str,
                    metavar='Link',
                    help='Link of user or Link of post')
    parser.add_argument(
                    '-d', metavar='directory', dest='directory',default=os.getcwd() + '\\bcydownload',
                    help='Set path to save'
    )

    args = parser.parse_args()

    if("item" in args.Link): #Download if Post
        bcy = bcy_single_climber(str(args.Link))
        print("Success!") if bcy.start(args.directory) else print('Fail!')
        return
    elif("u" in args.Link): #Download if User
        UID=args.Link.split('/')[-1].split('?')[0]
        print("Begin crawing with UID {0}".format(UID))
        uitem = bcy_user_climber(UID)
        p = multiprocessing.Process(target=uitem.begin_download, args=(args.directory,))
        p.start()
        p.join()



if __name__=="__main__":
	bcy_crawler()