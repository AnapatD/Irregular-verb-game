import time
import os
import random
import sys

os.system('cls')
print('Verb ---> Irregular Verb Game!!!\n')
print('Please choose your game method\n		1 : Infinitive ---> Past Simple\n 		2 : Infinitive ---> Past Participle')
score = 0
lst = ['awake','be','beat','become','begin','bet','bite','blow','break','breed','bring','build','burn','buy','can','cast','catch','choose','come','cost','cut','deal','do','draw','dream','drink','drive','eat','fall','feed','feel','fight','find','flee','fly','forget','forgive','freeze','get','give','go','grow','hang','have','hear','hide','hit','hold','hurt','keep','know','lay','lead','learn','leave','lend','let','lie','light','lose','make','mean','meet','pay','prove','put','read','ride','ring','rise','run','say','see','seek','sell','send','set','shake','shoot','show','shut','sing','sink','sit','sleep','smell','speak','spell','spend','spill','spread','stand','steal','stick','strike','swim','swing','take','teach','tell','think','throw','understand','wake','wear','win','write']
methods = input('Your choice : ')
if methods == ('1'):
	os.system('cls')
	amount = int(input('How many numbers of problem you prefered to do : '))
	start = (time.time())
	for i in range(amount):
		problem = random.choice(lst)
		if problem == ('awake'):
			correct = ('awoke')
		elif problem == ('be'):
			correct = ('was/were')
		elif problem == ('beat'):
			correct = ('beat')
		elif problem == ('become'):
			correct = ('became')
		elif problem == ('begin'):
			correct = ('began')
		elif problem == ('bet'):
			correct = ('bet')
		elif problem == ('bite'):
			correct = ('bit')
		elif problem == ('blow'):
			correct = ('blew')
		elif problem == ('break'):
			correct = ('broke')
		elif problem == ('breed'):
			correct = ('bred')
		elif problem == ('bring'):
			correct = ('brought')
		elif problem == ('build'):
			correct = ('built')
		elif problem == ('burn'):
			correct = ('burnt')
		elif problem == ('buy'):
			correct = ('bought')
		elif problem == ('can'):
			correct = ('could')
		elif problem == ('cast'):
			correct = ('cast')
		elif problem == ('catch'):
			correct = ('caught')
		elif problem == ('choose'):
			correct = ('chose')
		elif problem == ('come'):
			correct = ('came')
		elif problem == ('cost'):
			correct = ('cost')
		elif problem == ('cut'):
			correct = ('cut')
		elif problem == ('deal'):
			correct = ('dealt')
		elif problem == ('do'):
			correct = ('did')
		elif problem == ('draw'):
			correct = ('drew')
		elif problem == ('dream'):
			correct = ('dreamt')
		elif problem == ('drink'):
			correct = ('drank')
		elif problem == ('drive'):
			correct = ('drove')
		elif problem == ('eat'):
			correct = ('ate')
		elif problem == ('fall'):
			correct = ('fell')
		elif problem == ('feed'):
			correct = ('fed')
		elif problem == ('feel'):
			correct = ('felt')
		elif problem == ('fight'):
			correct = ('fought')
		elif problem == ('find'):
			correct = ('found')
		elif problem == ('flee'):
			correct = ('fled')
		elif problem == ('fly'):
			correct = ('flew')
		elif problem == ('forget'):
			correct = ('forgot')
		elif problem == ('forgive'):
			correct = ('forgave')
		elif problem == ('freeze'):
			correct = ('froze')
		elif problem == ('get'):
			correct = ('got')
		elif problem == ('give'):
			correct = ('gave')
		elif problem == ('go'):
			correct = ('went')
		elif problem == ('grow'):
			correct = ('grew')
		elif problem == ('hang'):
			correct = ('hung')
		elif problem == ('have'):
			correct = ('had')
		elif problem == ('hear'):
			correct = ('heard')
		elif problem == ('hide'):
			correct = ('hid')
		elif problem == ('hit'):
			correct = ('hit')
		elif problem == ('hold'):
			correct = ('held')
		elif problem == ('hurt'):
			correct = ('hurt')
		elif problem == ('keep'):
			correct = ('kept')
		elif problem == ('know'):
			correct = ('knew')
		elif problem == ('lay'):
			correct = ('laid')
		elif problem == ('lead'):
			correct = ('led')
		elif problem == ('learn'):
			correct = ('learned/learnt')
		elif problem == ('leave'):
			correct = ('left')
		elif problem == ('lend'):
			correct = ('lent')
		elif problem == ('let'):
			correct = ('let')
		elif problem == ('lie'):
			correct = ('lied')
		elif problem == ('light'):
			correct = ('lit')
		elif problem == ('lose'):
			correct = ('lost')
		elif problem == ('make'):
			correct = ('made')
		elif problem == ('mean'):
			correct = ('meant')
		elif problem == ('meet'):
			correct = ('met')
		elif problem == ('pay'):
			correct = ('paid')
		elif problem == ('prove'):
			correct = ('proved')
		elif problem == ('put'):
			correct = ('put')
		elif problem == ('read'):
			correct = ('read')
		elif problem == ('ride'):
			correct = ('rode')
		elif problem == ('ring'):
			correct = ('rang')
		elif problem == ('rise'):
			correct = ('rose')
		elif problem == ('run'):
			correct = ('ran')
		elif problem == ('say'):
			problem = ('said')
		elif problem == ('see'):
			correct = ('saw')
		elif problem == ('seek'):
			correct = ('sought')
		elif problem == ('sell'):
			correct = ('sold')
		elif problem == ('send'):
			correct = ('sent')
		elif problem == ('set'):
			correct = ('set')
		elif problem == ('shake'):
			correct = ('shook')
		elif problem == ('shoot'):
			correct = ('shot')
		elif problem == ('show'):
			correct = ('showed')
		elif problem == ('shut'):
			correct = ('shut')
		elif problem == ('sing'):
			correct = ('sang')
		elif problem == ('sink'):
			correct = ('sank')
		elif problem == ('sit'):
			correct = ('sat')
		elif problem == ('sleep'):
			correct = ('slept')
		elif problem == ('smell'):
			correct = ('smelt')
		elif problem == ('speak'):
			correct = ('spoke')
		elif problem == ('spell'):
			correct = ('spelt')
		elif problem == ('spend'):
			correct = ('spent')
		elif problem == ('spill'):
			correct = ('spilled/split')
		elif problem == ('spread'):
			correct = ('spread')
		elif problem == ('stand'):
			correct = ('stood')
		elif problem == ('steal'):
			correct = ('stole')
		elif problem == ('stick'):
			correct = ('stuck')
		elif problem == ('strike'):
			correct = ('struck')
		elif problem == ('swim'):
			correct = ('swam')
		elif problem == ('swing'):
			correct = ('swung')
		elif problem == ('take'):
			correct = ('took')
		elif problem == ('teach'):
			correct = ('taught')
		elif problem == ('tell'):
			correct = ('told')
		elif problem == ('think'):
			correct = ('thought')
		elif problem == ('throw'):
			correct = ('threw')
		elif problem == ('understand'):
			correct = ('understood')
		elif problem == ('wake'):
			correct = ('woke')
		elif problem == ('wear'):
			correct = ('wore')
		elif problem == ('win'):
			correct = ('won')
		elif problem == ('write'):
			correct = ('wrote')
		answer = input(problem + ' : ')
		ans = answer.lower().replace(' ','')
		if ans == correct:
			print('Correct!')
			score += 1
		elif ans is not correct:
			print('Not correct The answer is : ' + correct)
	end = time.time()
	print('\n\nDone!\nYou got : ' + str(score) + '\nTime you used : ' + str(end - start))
	restart = input('Do you want to restart? [y/n]')
	res = restart.lower()
	if res == ('y'):
		os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
	elif res == ('n'):
		sys.exit(0)
	else:
		print('Please enter either "y" or "n"')
		os.sys('PAUSE')
elif methods == ('2'):
	os.system('cls')
	amount = int(input('How many numbers of problem you prefered to do : '))
	start = (time.time())
	for i in range(amount):
		problem = random.choice(lst)
		if problem == ('awake'):
			correct = ('awoken')
		elif problem == ('be'):
			correct = ('been')
		elif problem == ('beat'):
			correct = ('beaten')
		elif problem == ('become'):
			correct = ('become')
		elif problem == ('begin'):
			correct = ('begun')
		elif problem == ('bet'):
			correct = ('bet')
		elif problem == ('bite'):
			correct = ('bitten')
		elif problem == ('blow'):
			correct = ('blown')
		elif problem == ('break'):
			correct = ('broken')
		elif problem == ('breed'):
			correct = ('bred')
		elif problem == ('bring'):
			correct = ('brought')
		elif problem == ('build'):
			correct = ('built')
		elif problem == ('burn'):
			correct = ('burnt')
		elif problem == ('buy'):
			correct = ('bought')
		elif problem == ('can'):
			correct = ('-')
		elif problem == ('cast'):
			correct = ('cast')
		elif problem == ('catch'):
			correct = ('caught')
		elif problem == ('choose'):
			correct = ('chosen')
		elif problem == ('come'):
			correct = ('come')
		elif problem == ('cost'):
			correct = ('cost')
		elif problem == ('cut'):
			correct = ('cut')
		elif problem == ('deal'):
			correct = ('dealt')
		elif problem == ('do'):
			correct = ('done')
		elif problem == ('draw'):
			correct = ('drawn')
		elif problem == ('dream'):
			correct = ('dreamt')
		elif problem == ('drink'):
			correct = ('drunk')
		elif problem == ('drive'):
			correct = ('driven')
		elif problem == ('eat'):
			correct = ('eaten')
		elif problem == ('fall'):
			correct = ('fallen')
		elif problem == ('feed'):
			correct = ('fed')
		elif problem == ('feel'):
			correct = ('felt')
		elif problem == ('fight'):
			correct = ('fought')
		elif problem == ('find'):
			correct = ('found')
		elif problem == ('flee'):
			correct = ('fled')
		elif problem == ('fly'):
			correct = ('flown')
		elif problem == ('forget'):
			correct = ('forgotten')
		elif problem == ('forgive'):
			correct = ('forgiven')
		elif problem == ('freeze'):
			correct = ('frozen')
		elif problem == ('get'):
			correct = ('got')
		elif problem == ('give'):
			correct = ('given')
		elif problem == ('go'):
			correct = ('gone')
		elif problem == ('grow'):
			correct = ('grown')
		elif problem == ('hang'):
			correct = ('hung')
		elif problem == ('have'):
			correct = ('had')
		elif problem == ('hear'):
			correct = ('heard')
		elif problem == ('hide'):
			correct = ('hidden')
		elif problem == ('hit'):
			correct = ('hit')
		elif problem == ('hold'):
			correct = ('held')
		elif problem == ('hurt'):
			correct = ('hurt')
		elif problem == ('keep'):
			correct = ('kept')
		elif problem == ('know'):
			correct = ('known')
		elif problem == ('lay'):
			correct = ('laid')
		elif problem == ('lead'):
			correct = ('led')
		elif problem == ('learn'):
			correct = ('learned/learnt')
		elif problem == ('leave'):
			correct = ('left')
		elif problem == ('lend'):
			correct = ('lent')
		elif problem == ('let'):
			correct = ('let')
		elif problem == ('lie'):
			correct = ('lain')
		elif problem == ('light'):
			correct = ('lit')
		elif problem == ('lose'):
			correct = ('lost')
		elif problem == ('make'):
			correct = ('made')
		elif problem == ('mean'):
			correct = ('meant')
		elif problem == ('meet'):
			correct = ('met')
		elif problem == ('pay'):
			correct = ('paid')
		elif problem == ('prove'):
			correct = ('proved')
		elif problem == ('put'):
			correct = ('put')
		elif problem == ('read'):
			correct = ('read')
		elif problem == ('ride'):
			correct = ('ridden')
		elif problem == ('ring'):
			correct = ('rung')
		elif problem == ('rise'):
			correct = ('rose')
		elif problem == ('run'):
			correct = ('run')
		elif problem == ('say'):
			problem = ('said')
		elif problem == ('see'):
			correct = ('seen')
		elif problem == ('seek'):
			correct = ('sought')
		elif problem == ('sell'):
			correct = ('sold')
		elif problem == ('send'):
			correct = ('sent')
		elif problem == ('set'):
			correct = ('set')
		elif problem == ('shake'):
			correct = ('shaken')
		elif problem == ('shoot'):
			correct = ('shot')
		elif problem == ('show'):
			correct = ('shown')
		elif problem == ('shut'):
			correct = ('shut')
		elif problem == ('sing'):
			correct = ('sung')
		elif problem == ('sink'):
			correct = ('sunk')
		elif problem == ('sit'):
			correct = ('sat')
		elif problem == ('sleep'):
			correct = ('slept')
		elif problem == ('smell'):
			correct = ('smelt')
		elif problem == ('speak'):
			correct = ('spoken')
		elif problem == ('spell'):
			correct = ('spelt')
		elif problem == ('spend'):
			correct = ('spent')
		elif problem == ('spill'):
			correct = ('spiled/split')
		elif problem == ('spread'):
			correct = ('spread')
		elif problem == ('stand'):
			correct = ('stood')
		elif problem == ('steal'):
			correct = ('stolen')
		elif problem == ('stick'):
			correct = ('stuck')
		elif problem == ('strike'):
			correct = ('struck')
		elif problem == ('swim'):
			correct = ('swum')
		elif problem == ('swing'):
			correct = ('swung')
		elif problem == ('take'):
			correct = ('taken')
		elif problem == ('teach'):
			correct = ('taught')
		elif problem == ('tell'):
			correct = ('told')
		elif problem == ('think'):
			correct = ('thought')
		elif problem == ('throw'):
			correct = ('thrown')
		elif problem == ('understand'):
			correct = ('understood')
		elif problem == ('wake'):
			correct = ('waken')
		elif problem == ('wear'):
			correct = ('worn')
		elif problem == ('win'):
			correct = ('won')
		elif problem == ('write'):
			correct = ('written')
		answer = input(problem + ' : ')
		ans = answer.lower().replace(' ','')
		if ans == correct:
			print('Correct!')
			score += 1
		elif ans is not correct:
			print('Not correct The answer is : ' + correct)
	end = time.time()
	print('\n\nDone!\nYou got : ' + str(score) + '\nTime you used : ' + str(end - start))
	restart = input('Do you want to restart? [y/n]')
	res = restart.lower()
	if res == ('y'):
		os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
	elif res == ('n'):
		sys.exit(0)
	else:
		print('Please enter either "y" or "n"')
		os.sys('PAUSE')
else:
	print('Please enter either 1 or 2')
