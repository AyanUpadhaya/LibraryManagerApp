from datetime import datetime
class Date:
	def __init__(self):
		self.current=datetime.date(datetime.now())
		self.data=str(self.current).split('-')
		self.year=self.data[0]
		self.date=self.data[2]
		self.month=self.data[1]
		self.date_int=int(self.data[2])
		self.submission_days=self.date_int+6 #6 days for submission
		self.submission_date=str(self.submission_days)+'/'+self.month+'/'+self.year
		
	def current_date(self):
		currentDate=self.date+'/'+self.month+'/'+self.year
		return currentDate