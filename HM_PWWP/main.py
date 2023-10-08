import application.salary
import application.db.people
import datetime

current_date = datetime.datetime.now().strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(current_date)
    print()
    application.salary.calculate_salary()
    print()
    application.db.people.get_employees()
