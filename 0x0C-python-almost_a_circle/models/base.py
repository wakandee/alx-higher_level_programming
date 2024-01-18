#!/usr/bin/python3

class Base:
	""" Base """
	__nb_objects = 0

	def __init__(self, id=12):
		if id is not None:
			Base.id = id
		else:
			Base.__nb_objects += 1
			Base.id =__nb_objects
		
		md