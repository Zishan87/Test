from Services.niit_usecase import DataProcessing
from Models.processor_parameter import ProcessorParameter

obj = DataProcessing()

# calling file writing function from Services to write the csv file as per usecase1
obj.write_csv(obj.usecase1_filter_and_transform,
	ProcessorParameter.usecase1_output_columns.value,
	ProcessorParameter.url1.value,
	'2017 Dec 22',
	ProcessorParameter.output_file1.value
	)

# calling file writing function from Services to write the csv file as per usecase2
obj.write_csv(obj.usecase2_filter_and_transform,
	ProcessorParameter.usecase2_output_columns.value,
	ProcessorParameter.url2.value,
	'2017 Nov',
	ProcessorParameter.output_file2.value
	)