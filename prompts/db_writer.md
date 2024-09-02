# DB Writer creation instructions

## Objective
Create a 'RobocriticDBWriter' python class that can be used to insert data into the database.

The database schema can be found in the db_scripts/initial_schema.sql file. 

The class should have methods for: 

Writing a 'game' to the database.
Writing a 'reviewer' to the database.
Writing a 'review' to the database.
Writing a 'platform_game' to the database.
Writing a 'review_pro' to the database.
Writing a 'review_con' to the database.

The 'RoboCriticDBWriter' class should accept a 'mysql.connector.connection.MySQLConnection' instantiation argument. 
Each method should accept as an argument a dictionary containing the data to be inserted. 

Write the class to the python file 'etl/helper_functions/robo_db_writer.py'
