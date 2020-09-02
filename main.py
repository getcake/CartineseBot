import praw
import cartibot
import time

reddit = cartibot.authenticate()

while True:
	try:

		cartibot.run(reddit)
	except Exception as e:
		print(e)
		continue

	time.sleep(30)