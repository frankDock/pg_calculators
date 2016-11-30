from django.core.management.base import BaseCommand, CommandError
from glazing.models import *
import csv
import os
from django.conf import settings

class Command(BaseCommand):

	help = "Import Glass_Frame_Join"

	def handle(self, *args, **options):

		Glass_Frame_Join.objects.all().delete()

		with open(os.path.join(settings.ROOT_PATH, 'glazing/data/import.csv'), 'rb') as file:
			rows = csv.reader(file, delimiter=",", quotechar='"')

			for row in rows:

				if rows.line_num == 1:
					continue

				#import pdb; pdb.set_trace()
				glass = Glass.objects.get(description=row[0])
				frame = Frame.objects.get(description=row[1])
				

				db_row = Glass_Frame_Join(glass=glass,frame=frame,SHGC=row[2],U_Value=row[3])
				db_row.save()

			# dump entire table
			for glass_frame_join in Glass_Frame_Join.objects.all():
				print glass_frame_join


