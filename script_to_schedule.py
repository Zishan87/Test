from Services.niit_usecase import DataProcessing
from Models.processor_parameter import ProcessorParameter

obj = DataProcessing()

obj.write_csv(obj.usecase1_filter_and_transform,
	ProcessorParameter.usecase1_output_columns.value,
	ProcessorParameter.url1.value,
	'2017 Dec 22',
	ProcessorParameter.output_file1.value
	)

obj.write_csv(obj.usecase2_filter_and_transform,
	ProcessorParameter.usecase2_output_columns.value,
	ProcessorParameter.url2.value,
	'2017 Nov',
	ProcessorParameter.output_file2.value
	)