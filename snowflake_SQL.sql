create database demo_db;

use database demo_db;

create schema demo_schema;
use schema demo_schema;

create table sales_details(Date date,Product string,Amount int);

create file format my_csv_format
type='csv'
skip_header=1;

create stage my_stage file_format=my_csv_format

copy into sales_details
from @my_stage 
file_format=my_csv_format;

SELECT * FROM sales_details;
SELECT COUNT(*) FROM sales_details;
