# Architecture, Design and guideline to run the script

## Architecture

We use 'Models' package to define all constant in terms of Enum class.
'Services' package provides data processing functionalities - Staging, filtering, transformation and writing to csv.
script file 'script_to_schedule.py' calls writing function from 'Services'. We can schedule this file to the scheduler to run.

## Design

Project folder 'Test' consist two packages 'Models' and 'Services'. 
It also consist a python client script file 'script_to_schedule.py' which we can configure in cron job script 'schedule_job.tab' using crontab scheduler.

I have scheduled cronjob at every first day of month at 12 am. (You can set the parameter and path according to your environment).
In the stdout.log file we can write the last processed date and automatically we can sink it to the parameter of functions into 'script_to_schedule.py' by reading from stdout.log on next run.


Here I am bound to provide last processed date mannually in the parameter of write_csv() function call of script 'script_to_schedule.py'.
Rest other parameters(these are static in nature) we read from a Enum class 'ProcessorParameter' in the 'Models' package.

So basically 'script_to_schedule.py' is responsible to call other functionalities from 'Services' package

'Services' is the main package here which contains a python file 'niit_usecase.py'. The code inside this file contains a service class 'DataProcessor' which contains a function called as 'parse_data()' is responsible for data staging.

The 'niit_usecase.py' contains two functions 'usecase1_filter_and_transform()' and 'usecase2_filter_and_transform()' which filter and transform the data on the top of staged data in terms of dataframe for two usecases respectively.And this function return the target dataframe.

The 'niit_usecase.py' also consist one more function 'write_csv()' to write the resultset in terms of csv file.

## Guideline to run the script

-- without cronjob 
Go to the path '/Test/'
python3.6 script_to_schedule.py

--with cron job
configure cronjob in crontab editor as schedule_job.tab (you can customize scheduled time as per requirement.)
edit 'script_to_schedule.py' to sink 'filter_condition' parameter from 'stdout.log' log file.



