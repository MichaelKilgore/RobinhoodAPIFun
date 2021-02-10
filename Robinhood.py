#!/usr/bin/env python3

import os
import robin_stocks as rs
import stockHistory

def login():
        rs.login(username=os.environ.get("robinhood_username"),
		password=os.environ.get("robinhood_password"),
		expiresIn=86400,
		by_sms=True)

if __name__ == '__main__':
	login()
	#stockHistory.stockStats("TSLA", "5minute", "week")
	stockHistory.trendLinesGraph("TSLA", "5minute", "week")
