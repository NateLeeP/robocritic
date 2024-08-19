from helper_functions.db_reader import RobocriticDBReader
from helper_functions.db_writer import RobocriticDbWriter



def main():
    instance_one = RobocriticDBReader()
    instance_two = RobocriticDBReader()
    instance_three = RobocriticDBReader()
    instance_four = RobocriticDbWriter()


main()