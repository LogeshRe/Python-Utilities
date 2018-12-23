# To find the number of business days between two dates
# Date is given as input in the indian date format separated by "/" (day/month/year).
# 23/12/2018

class Businessdays:
	 def __init__(self,date1,date2):
	 	date1t = date1.split('/')
	 	date2t = date2.split('/')
	 	self.date1day = int(date1t[0])
	 	self.date1month = int(date1t[1])
	 	self.date1year = int('20'+date1t[2])
	 	self.date2day = int(date2t[0])
	 	self.date2month = int(date2t[1])
	 	self.date2year = int('20'+date2t[2])

	 def datedifference(self):
	 	from datetime import date
	 	from datetime import timedelta
	 	date1 = date(self.date1year,self.date1month,self.date1day)
	 	date2 = date(self.date2year,self.date2month,self.date2day)
	 	d1 = date1.toordinal()
	 	d2 = (date2 + timedelta(days=1)).toordinal()
	 	count = 0
	 	for ordi in range(d1,d2):
	 		dayo = (date.fromordinal(ordi))
	 		if(dayo.weekday() == 6 or dayo.weekday() == 5):
	 			count = count + 1
	 	print(abs((date2 - date1).days) - count + 1)


def main():
	p1 = Businessdays('1/12/18','15/12/18')
	p1.datedifference()


if __name__ == "__main__":
	main()

