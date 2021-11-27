from cv_creator import CV_Creator

name = input('What is your name? ')
mobile_number = input('What is your mobile number? ')
email = input('What is your email? ')


my_cv = CV_Creator(name, mobile_number, email)

my_cv.create_header()
my_cv.create_experiences()
my_cv.create_education_entries()
my_cv.save_document()
