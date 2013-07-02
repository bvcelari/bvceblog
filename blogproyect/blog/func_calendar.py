# -*- encoding: utf-8 -*-
def createCal(year,month,today,listdays):
        import re
        import calendar
	SUNDAY=0
	strHTMLCal= calendar.HTMLCalendar(firstweekday=SUNDAY)
	strHTMLCal= calendar.LocaleHTMLCalendar(firstweekday=SUNDAY)
        calendarHTML = strHTMLCal.formatmonth(year,month)
	calendarHTML = re.sub('Mon','L',calendarHTML)
	calendarHTML = re.sub('Tue','M',calendarHTML)
	calendarHTML = re.sub('Wed','X',calendarHTML)
	calendarHTML = re.sub('Thu','J',calendarHTML)
	calendarHTML = re.sub('Fri','V',calendarHTML)
	calendarHTML = re.sub('Sat','S',calendarHTML)
	calendarHTML = re.sub('Sun','D',calendarHTML)
	calendarHTML = re.sub('<td class="mon">','<td><span>',calendarHTML)
	calendarHTML = re.sub('<td class="tue">','<td><span>',calendarHTML)
	calendarHTML = re.sub('<td class="wed">','<td><span>',calendarHTML)
	calendarHTML = re.sub('<td class="thu">','<td><span>',calendarHTML)
	calendarHTML = re.sub('<td class="fri">','<td><span>',calendarHTML)
	calendarHTML = re.sub('<td class="sat">','<td><span>',calendarHTML)
	calendarHTML = re.sub('<td class="sun">','<td><span>',calendarHTML)
	calendarHTML = re.sub('</td>','</span></td>',calendarHTML)
	calendarHTML = re.sub('<td><span>'+str(today)+'<','<td class="today"><span>'+str(today)+'<',calendarHTML)
	for day in listdays:
	#should tune here the css.. bad bussiness... 
	#re implement, and/or change css...think it 

		calendarHTML = re.sub('<span>'+str(day)+'<','<span><a href="/monfth/day/postlist" >'+str(day)+'</a><',calendarHTML)
	return calendarHTML


