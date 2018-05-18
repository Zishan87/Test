from enum import Enum

# class which defines all the constant values across the project.
class ProcessorParameter(Enum):
	url1 = 'http://www.bcb.gov.br/pec/Indeco/Ingl/ie5-24i.xlsx'
	url2 = 'http://www.bcb.gov.br/pec/Indeco/Ingl/ie5-26i.xlsx'
	usecase1_output_columns = ['Date','BCB_Commercial_Exports_Total',
	'BCB_Commercial_Exports_Advances_on_Contracts','BCB_Commercial_Exports_Payment_Advance',
	'BCB_Commercial_Exports_Others','BCB_Commercial_Imports','BCB_Commercial_Balance',
	'BCB_Financial_Purchases','BCB_Financial_Sales','BCB_Financial_Balance','BCB_Balance']
	usecase2_output_columns = ['Date','BCB_FX_Position']
	output_file1 = 'bcb_output_1.csv'
	output_file2 = 'bcb_output_2.csv'