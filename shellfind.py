#!/usr/bin/env python
'''
Author : Aziz Ezzaher
Email : shakorlaxx@gmail.com
Description : shellfind.py is a Python command line utility which lets you look for shells on a site that the hacker must have uploaded. It considers all the shells available and tries all possibilities via dictionary match.
'''
import socket
import sys
import httplib
from urlparse import urlparse
import time as t
import urllib2
from urllib2 import Request, urlopen, URLError


negative = '\033[91m'
positive = '\033[32m'
wait = '\033[95m'
final = '\033[93m'
total_scanned_global=0
found_scanned_global=0

def OpenLog(log_file_name): 
	try:
		f = open(log_file_name, 'r')
		return f.read()
		f.close()
	except IOError:
		return "File" + log_file_name + "does not exist."

def main():
socket.setdefaulttimeout(10)
print wait+"\n## ------ Welcome to Shell Finder Developed by Aziz Ezzaher |welcome To site fake pages|
(http://fakescams.us) | Hacked By Ezzaher)------ ##"
	website_url = raw_input("\n\nEnter URL to scan ([eg, http://sitename.com or https://sitename.com/subdir ] | Do not add slash at the end of URL) : ")
	parse_url=urlparse(website_url)
	log_file_name = ""+parse_url.netloc+".log"
	global total_scanned_global
	global found_scanned_global
	try:
		try:
			create=open(log_file_name,"w")
		except:
			print negative+"\nError generating log file. Please check directory access permissions."
		print wait+"\nCreating a persistent connection to site "+website_url
		conn = urllib2.Request(website_url)
		urllib2.urlopen(website_url)
		print positive+"Connected! Begining to scan for shells.."
	except (urllib2.HTTPError) as Exit:
		print negative+"\nEither the server is down or you are not connected to the internet."
		exit()
	try:
		dictionary = open("dictionary","r")
	except(IOError):
		print negative+"Dictionary file not found_scanned_global. Please download the latest dictionary from github link"
		exit()
	keywords = dictionary.readlines()
	for keys in keywords:
		keys=keys.replace("\n","") #To replace newline with empty
		New_URL = website_url+"/"+keys
		print wait+">────► "+New_URL
		req=Request(New_URL)
		try:
			response = urlopen(req)
		except URLError, e:
			if hasattr(e,'reason'):
				print negative+"Not found"
				total_scanned_global = total_scanned_global+1
			elif hasattr(e,'code'):
				print negative+"Not found "
				total_scanned_global = total_scanned_global+1
		else:
			try:
				log_file=open(log_file_name,"a+") #Appending to it
			except(IOError):
				print negative+"Failed to create log file. Check dir permissions."
			found_scanned_url=New_URL
			print positive+"Possible shell found at ",found_scanned_url
			log_file.writelines(found_scanned_url+"\n")
			found_scanned_global=found_scanned_global+1
			total_scanned_global=total_scanned_global+1
			log_file.close()
	print "\nTotal tries : ", total_scanned_global
	print positive+"\nPossible shells: ",found_scanned_global
	print final+"\nFollowing are the links to possible shells "
	print OpenLog(log_file_name)

if __name__ == '__main__':
    main()  
