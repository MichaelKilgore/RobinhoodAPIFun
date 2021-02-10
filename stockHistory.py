#!/usr/bin/env python3

import os
import robin_stocks as rs
import matplotlib.pyplot as plt
import numpy as np

def stockStats(stock, loopTime, timeSpan):
	#price = rs.stocks.get_latest_price('TSLA', includeExtendedHours=True)

	#print('the price of tesla is: ', price)
	
	data = rs.stocks.get_stock_historicals(stock, interval=loopTime, span=timeSpan)
	
	#growth
	start = data[0]['open_price']
	end = data[-1]['close_price']

	#high / low / best day / growth on best day / worst day / growth on worst day
	high, low, bestDay, growthOnBestDay, worstDay, growthOnWorstDay = 0.0, 1000000.0, "", 0.0, "", 0.0
	#Closing Price / Open Price / Previous Open Price / Previous Close Price
	CP, OP, POP, PCP = 0.0, 0.0, 0.0, 0.0
	for i in data:
					
		#calculates the high, low, best day of growth, and worst day of growth
		CP = float(i['close_price'])
		OP = float(i['open_price'])	
		if (CP > high):
			high = CP
		if (CP < low):
			low = CP
		if (((CP - OP) / OP) * 100 > growthOnBestDay):
			growthOnBestDay = ((CP - OP) / OP) * 100
			bestDay = i['begins_at']
		if (((OP - CP) / OP) * 100 > growthOnWorstDay):
			growthOnWorstDay = ((OP - CP) / OP) * 100
			worstDay = i['begins_at']
		
		i['growth'] = ((CP - OP) / OP) * 100

	#TODO: does more consecutive positive days or more consecutive negative days increase chance
	#of stock price going up or down
	print("price 5 years ago: " + str(start))
	print("price today:       " + str(end))
	print("highest day:       " + str(high))
	print("lowest day:        " + str(low))
	print("Date of best day:  " + str(bestDay))
	print("percent increase:  " + str(growthOnBestDay) + "%")
	print("Date of worst day: " + str(worstDay))
	print("percent decrease:  " + str(growthOnWorstDay) + "%")




def trendLinesGraph(stock, loopTime, timeSpan): 	
	data = rs.stocks.get_stock_historicals(stock, interval=loopTime, span=timeSpan)	
	#dates = [i['begins_at'] for i in data]
	dates = [i for i in range(len(data))]
	price = [float(i['close_price']) for i in data]

	#plotting points
	plt.plot(dates, price, marker=".", markersize=3)

	#naming the axis
	plt.xlabel('date')
	plt.ylabel('price')

	#plot title
	plt.title('price over date graph')	

	change = 100
	finished = 0
	#calculate the trendline
	for i in dates:
		if (i%change == 0 and i>=change):
			z = np.polyfit(dates[i-change:i], price[i-change:i], 1)
			p = np.poly1d(z)
			plt.plot(dates[i-change:i], p(dates[i-change:i]), "-")
			finished = 1
		if (dates[-1] - dates[i] <= change and finished == 1):
			z = np.polyfit(dates[i:], price[i:], 1)
			p = np.poly1d(z)
			plt.plot(dates[i:], p(dates[i:]), "-")
			break	
		finished = 0
	
	#the line equation
	#print("y=%.6fx+(%.6f)", z[0], z[1])
	

	#display plot
	plt.show()




