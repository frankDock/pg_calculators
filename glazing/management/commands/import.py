from django.core.management.base import BaseCommand, CommandError
from glazing.models import *
import csv
import os
from django.conf import settings

class Command(BaseCommand):

	help = "Import Solar_Exposure_Factor"

	def handle(self, *args, **options):

		Solar_Exposure_Factor.objects.all().delete()

		with open(os.path.join(settings.ROOT_PATH, 'glazing/data/import.csv'), 'rb') as file:
			rows = csv.reader(file, delimiter=",", quotechar='"')

			for row in rows:

				if rows.line_num == 1:
					continue

				#import pdb; pdb.set_trace()
				zone = Climate_Zone.objects.get(description=row[0])
				orientation = Orientation.objects.get(symbol=row[1])

				db_row = Solar_Exposure_Factor(zone=zone,orientation=orientation, e=row[2], ph=row[3])
				db_row.save()

			# dump entire table
			for solar_exposure_factor in Solar_Exposure_Factor.objects.all():
				print solar_exposure_factor


