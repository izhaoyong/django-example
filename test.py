latest_question_list = [
	{
		'id': 1,
		'question_text': "hahah"
	}
]



def test():
	import ipdb
	ipdb.set_trace()

	print(latest_question_list)


# test()


def main():
	DATABASE_APPS_MAPPING = {'app1': 'db1', 'app2': 'db2'}
	label = 'app1'
	if label in DATABASE_APPS_MAPPING:
		print(DATABASE_APPS_MAPPING[label])

main()
