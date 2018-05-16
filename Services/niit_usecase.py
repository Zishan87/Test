import pandas as pd
import numpy as np
from datetime import datetime


class DataProcessing:
	def __init__(self):
		pass
	
	@staticmethod
	def parse_data(url):
		df = pd.read_excel(url,header=None)
		number_of_columns = df.shape[1]
		input_columns = []
		for i in range(1,number_of_columns+1):
			input_columns.append('column'+str(i))
		df.columns = input_columns
		return df

	@classmethod
	def usecase1_filter_and_transform(cls,url,filter_condition):
		df = cls.parse_data(url)
		year,month,day = filter_condition.split(' ')
		total_row = df.shape[0]
		ind1 = df.index[df['column1']==int(year)]
		df = df.iloc[ind1[0]:]

		i = 0
		while i<total_row-ind1[0]-1:
			temp = df.iloc[i]['column1']
			i+=1
			if df.iloc[i]['column1'] is np.nan:
				df.iloc[i]['column1'] = temp

		ind2 = df.index[df['column2']==month]
		df = df.iloc[(ind2[0]-ind1[0]):]

		i = 0
		repl = df.iloc[0]['column2']
		while i<total_row-ind2[0]-1:		
			if type(df.iloc[i]['column2']).__name__ == 'str':
				repl = df.iloc[i]['column2']
			elif type(df.iloc[i]['column2']).__name__ == 'int':
				df.iloc[i]['column2'] = repl+' '+str(df.iloc[i]['column2'])
			i+=1

		df['column1'] = df['column1'].astype(str) + ' ' + df['column2']
		del df['column2']

		df = df[df['column1'].notnull()]
		df = df[df.column1.str.split(' ').str.len().astype(int) == 3]

		df['column1'] = pd.to_datetime(df['column1'], format='%Y %b %d')
		conditional_date = datetime.strptime(filter_condition, '%Y %b %d')

		df = df[df['column1']>conditional_date]

		df['column1'] = df['column1'].dt.strftime('%m/%d/%Y')

		return df

	@classmethod
	def usecase2_filter_and_transform(cls,url,filter_condition):
		df = cls.parse_data(url)
		year,month = filter_condition.split(' ')
		total_row = df.shape[0]
		ind1 = df.index[df['column1']==int(year)]
		df = df.iloc[ind1[0]:]

		i = 0
		while i<total_row-ind1[0]-1:
			temp = df.iloc[i]['column1']
			i+=1
			if df.iloc[i]['column1'] is np.nan:
				df.iloc[i]['column1'] = temp

		ind2 = df.index[df['column2']==month]
		df = df.iloc[(ind2[0]-ind1[0]):]

		df['column1'] = df['column1'].astype(str) + ' ' + df['column2'] + ' 1'
		del df['column2']

		df['column1'] = pd.to_datetime(df['column1'], format='%Y %b %d')
		filter_condition = filter_condition + ' 1'
		conditional_date = datetime.strptime(filter_condition, '%Y %b %d')

		df = df[df['column1']>conditional_date]

		df['column1'] = df['column1'].dt.strftime('%m/%d/%Y')

		return df

	def write_csv(self,transform_function,output_columns,url,filter_condition,output_file_name):
		df = transform_function(url,filter_condition)
		df.columns = output_columns
		return df.to_csv(output_file_name)