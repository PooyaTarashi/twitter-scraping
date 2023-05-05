from twitterScraping import *
from getpass import getpass

username = input("Enter your twitter account username: ")
password = getpass("Enter your twitter account password: ")
target = input("Enter the username of target account (without @ or anything else): ")
main_app(username, password, target)