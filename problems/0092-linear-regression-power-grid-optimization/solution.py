import math

PI = 3.14159

def power_grid_forecast(consumption_data):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	detrended = [
        y - 10 * math.sin(2 * PI * i / 10)
        for i, y in enumerate(consumption_data)
    ]

	# 2) Perform linear regression on the detrended data.
	def linear_regression(points):
		n = len(points)
		sx = sum(i + 1 for i in range(n))
		sy = sum(points)
		sxy = sum((i + 1) * y for i, y in enumerate(points))
		sxx = sum((i + 1) ** 2 for i in range(n))

		m = (n * sxy - sx * sy) / (n * sxx - sx * sx)
		b = (sy - m * sx) / n
		return m, b
	
	m, b = linear_regression(detrended)

	# 3) Predict day 15's base consumption.
	day_15 = m * 15 + b

	# 4) Add the day 15 fluctuation back.
	day_15 = day_15 + (10 * math.sin(2 * PI * 15 / 10))

	# 5) Round, then add a 5% safety margin (rounded up).
	day_15 = math.ceil(1.05 * day_15)

	# 6) Return the final integer.
	return day_15