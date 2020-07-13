"""
    作者：陈志安
    日期：19/3/21
    功能：AQI计算
    版本：v.1
"""


def cal_liner(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
	"""
		范围缩放
	"""
	iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
	return iaqi


def cal_pm_iaqi(pm_val):
	"""
		计算PM2.5的AQI
	"""
	if 0 <= pm_val < 36:
		iaqi = cal_liner(0, 50, 0, 35, pm_val)
	elif 36 <= pm_val < 76:
		iaqi = cal_liner(50, 100, 35, 75, pm_val)
	elif 76 <= pm_val < 116:
		iaqi = cal_liner(100, 150, 75, 115, pm_val)
	elif 116 <= pm_val < 151:
		iaqi = cal_liner(150, 200, 115, 150, pm_val)
	elif 151 <= pm_val < 251:
		iaqi = cal_liner(200, 300, 150, 250, pm_val)
	elif 251 <= pm_val < 351:
		iaqi = cal_liner(300, 400, 250, 350, pm_val)
	elif 351 <= pm_val < 501:
		iaqi = cal_liner(400, 500, 350, 500, pm_val)

	return iaqi


def cal_co_iaqi(co_val):
	"""
		计算CO的AQI
	"""
	if 0 <= co_val < 3:
		iaqi = cal_liner(0, 50, 0, 3, co_val)
	elif 2 <= co_val < 5:
		iaqi = cal_liner(50, 100, 2, 4, co_val)
	elif 4 <= co_val < 15:
		iaqi = cal_liner(100, 150, 4, 14, co_val)
	elif 14 <= co_val < 25:
		iaqi = cal_liner(150, 200, 14, 24, co_val)
	elif 24 <= co_val < 37:
		iaqi = cal_liner(200, 300, 24, 35, co_val)
	elif 36 <= co_val < 49:
		iaqi = cal_liner(300, 400, 36, 48, co_val)
	elif 48 <= co_val < 61:
		iaqi = cal_liner(400, 500, 48, 60, co_val)

	return iaqi


def cal_aqi(parpm_list):
	"""
		AQI计算
	"""
	pm_val = parpm_list[0]
	co_val = parpm_list[1]

	pm_iaqi = cal_pm_iaqi(pm_val)
	co_iqai = cal_co_iaqi(co_val)

	iaqi_list = []
	iaqi_list.append(pm_iaqi)
	iaqi_list.append(co_iqai)

	aqi = max(iaqi_list)
	return aqi


def main():
	"""
		主函数
	"""
	print('请输入以下信息，用空格分割')
	input_str = input('(1)PM2.5 (2)CO:')
	str_list = input_str.split(' ')
	pm_val = float(str_list[0])
	co_val = float(str_list[1])

	parpm_list = []
	parpm_list.append(pm_val)
	parpm_list.append(co_val)

	# 调用AQI函数
	aqi_val = cal_aqi(parpm_list)

	print('空气质量指数为：{}'.format(aqi_val))


if __name__ == '__main__':
	main()
