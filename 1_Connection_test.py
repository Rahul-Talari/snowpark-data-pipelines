import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

connection_parameters = {"account":"AQKUTJW-GN70912",
"user": "RAHULTALARI",
"password": "Lenovothinkpad@1",
"role":"ACCOUNTADMIN",
"warehouse":"SNOWPARK_WH",
"database":"SNOWPARK_DB",
"schema":"SNOWPARK_SCHEMA"
}

test_session = Session.builder.configs(connection_parameters).create()

print(test_session.sql("select current_warehouse(), current_database(), current_schema()").collect())

session = Session.builder.configs(connection_parameters).create()