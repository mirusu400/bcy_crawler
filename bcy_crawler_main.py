# !/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
import argparse
import multiprocessing
from bcy_single_climber import bcy_single_climber
from bcy_user_climber import bcy_user_climber
def bcy_crawler():
    parser = argparse.ArgumentParser(description="Download images from bcy.net.")
    parser.add_argument('Link', type=str,
                    metavar='Link',
                    help='Link of user or Link of post')
    parser.add_argument(
                    '-n', metavar='directory', dest='directory',default=os.getcwd() + '\\bcydownload',
                    help='Set path to save'
    )
    parser.add_argument(
                    '-d','--date', required=False, action='store_true', help='Use it if you need download with date.'
    )
    args = parser.parse_args()
    if("item" in args.Link): #Download if Post
        bcy = bcy_single_climber(str(args.Link))
        print("Success!") if bcy.start(args.directory, args.date) else print('Fail!')
        return
    elif("u" in args.Link): #Download if User
        UID=args.Link.split('/')[-1].split('?')[0]
        print("Begin crawling with UID {0}".format(UID))
        uitem = bcy_user_climber(UID)
        p = multiprocessing.Process(target=uitem.begin_download, args=(args.directory,args.date,))
        p.start()
        p.join()



if __name__=="__main__":
	bcy_crawler()