aliens=[]

i=1

for alien_number in range(30):
	new_alien = { 'color':'green', 'points':i}
	aliens.append(new_alien)
	i+=1

for alien in aliens:
	print (alien)






'''
alien = {
	'color':'green',
	'points':5,
	'x_dimen': 10,
	'y_dimen': 25,
	'speed': 'fast',
	'velocity': 'fast'
}

for item in set(alien.values()):
	print (item)

print(alien)

print ("\nOriginal position : " + str(alien['x_dimen']) + " x " + str(alien['y_dimen']))

if (alien['speed']=='slow'):
	x_inc=1
elif (alien['speed']=='medium'):
	x_inc=2
else:
	x_inc=3

alien['x_dimen'] = alien['x_dimen'] + x_inc

print ("\nNew position : " + str(alien['x_dimen']) + " x " + str(alien['y_dimen']) + "\n")

del alien['color']

print(alien)
'''