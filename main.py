# imports
# (here we imports all the modules)
import app_functions
import cv_bot
from email_module import Email
from app_classes_v2 import Candidate, Adviser_Bot, Recruiter, Job
import cover_letter_bot

def main():
    # 1) "Candidate info"
    # (which collects all the inputs for the personal info and the job.
    # Please use the "input_..." functions in app_functions file to restrict and verify user inputs.)

    print("---------------------------------------")
    Candidate.data["user_language"] = input("Which language do you choose for your documents? ")
    Candidate.data["name"] = input("Name: ")
    Candidate.data["surname"] = input("Surname: ")
    Candidate.data["birthday"] = app_functions.input_date("Birthday (dd.mm.yyyy): ")
    Candidate.data["sex"] = app_functions.input_strict("Sex (male/female): ", ["male", "female"])
    Candidate.data["phone"] = input("Phone: ")
    Candidate.data["email"] = app_functions.input_email("Email: ")
    Candidate.data["address"] = input("Address: ")
    print("---------------------------------------")
    print()
    print("Input some previous working experience.")
    print("---------------------------------------")
    Candidate.data["experience"] = [] # clear experience list in dictionary
    loop = True
    while loop:
        new_experience = {
            "title": input("Position: "),
            "description": input("Description: "),
            "company": input("Company: "),
            "date_start": app_functions.input_date("Starting date (dd.mm.yyyy): "),
            "date_end": app_functions.input_date("Ending date (dd.mm.yyyy): ")     
        }
        Candidate.add_experience(new_experience)
        answer = app_functions.input_strict("Do you want to add a new experience? (Y/N) ", ["Y", "N"])
        print("---------------------------------------")
        if answer == "n":
            loop = False
    
    print()
    print("Input some previous education.")
    print("---------------------------------------")
    Candidate.data["education"] = [] # clear education list in dictionary
    loop = True
    while loop:
        new_education = {
            "title": input("Position: "),
            "description": input("Description: "),
            "school": input("Institution: "),
            "date_start": app_functions.input_date("Starting date (dd.mm.yyyy): "),
            "date_end": app_functions.input_date("Ending date (dd.mm.yyyy): ")     
        }
        Candidate.add_experience(new_education)
        answer = app_functions.input_strict("Do you want to add a new education? (Y/N) ", ["Y", "N"])
        print("---------------------------------------")
        if answer == "n":
            loop = False
    
    print()
    print("Input some hobbies. Ex: I play guitar with true passion.")
    print("---------------------------------------")
    Candidate.data["hobbies"] = [] # clear hobbies list in dictionary
    loop = True
    while loop:
        new_hobby = {
            "hobby": input("Hobby: "),
        }
        Candidate.add_hobbies(new_hobby)
        answer = app_functions.input_strict("Do you want to add a new hobby? (Y/N) ", ["Y", "N"])
        print("---------------------------------------")
        if answer == "n":
            loop = False
    
    
    print()
    print("Input some skills. Ex: Python - expert level.")
    print("---------------------------------------")
    Candidate.data["skills"] = [] # clear skills list in dictionary
    loop = True
    while loop:
        new_skill = {
            "skill": input("Skill: "),
        }
        Candidate.add_skills(new_skill)
        answer = app_functions.input_strict("Do you want to add a new skill? (Y/N) ", ["Y", "N"])
        print("---------------------------------------")
        if answer == "n":
            loop = False
    
    print()
    print("Input some languages. Ex: German - native.")
    print("---------------------------------------")
    Candidate.data["languages"] = [] # clear languages list in dictionary
    loop = True
    while loop:
        new_language = {
            "language": input("Language: "),
        }
        Candidate.add_languages(new_language)
        answer = app_functions.input_strict("Do you want to add a new language? (Y/N) ", ["Y", "N"])
        print("---------------------------------------")
        if answer == "n":
            loop = False
    
    Candidate.save_infos()   
    

    # 2) "Job"
    # Collect the information about the job description and the name of the Recruiter in HR
    print()
    print("Input some informations about the job.")
    print("---------------------------------------")
    Recruiter.data["name"] = input("Recriuter name: ")
    Recruiter.data["surname"] = input("Recriuter surname: ")
    Recruiter.data["sex"] = app_functions.input_strict("Sex (male/female): ", ["male", "female"])
    Recruiter.data["attitude"] = input("Recriuter attitude (for interview): ")
    Recruiter.data["email"] = app_functions.input_email("Recriuter email: ")
    Recruiter.data["position"] = input("Recriuter position: ")
    Recruiter.data["company"] = input("Company name: ")
    Recruiter.data["company_address"] = input("Company address: ")
    Recruiter.save_infos()
    
    Job.data["position"] = input("Job position: ")
    Job.data["description"] = input("""Job description: """)
    Job.data["source"] = input("Job anouncement source: ")
    Job.save_infos()

    # cv_description = Adviser_Bot.generate_cv_short_description()

    # 3) "CV"
    # Create the CV
    print("Please, upload a picture for the CV.")
    resume = cv_bot.Resume('json/candidate.json', cv_bot.HexColor("#D4AF37"), cv_bot.HexColor("#404040"), cv_bot.HexColor("#FFFFFF"))
    resume.generate()
    
    # 4) "Cover letter
    # Writes the cover letter
    Adviser_Bot.generate_letter()
    # cover_letter_bot.generate()

    # 5) "Email"
    # Send the email, attaching cover letter and CV
    email = Email(
        f"{Candidate.data['email']}",  # sender
        [f"{Recruiter.data['email']}"],  # list of receivers
        f"Applying for the position of {Job.data['position']}",
    )  # object

    password = email.password("email_pass.txt")  # app password

    body = Adviser_Bot.generate_letter()  # text of the email

    attachments = email.attachments(
        [
            f"{Candidate.data['name']}_{Candidate.data['surname']}_CV.pdf"
        ]
    )  # cv and cover letter

    email.send(password, body, attachments)  # Send the email

    # 6) "Interview"
    # Prepare for the job interview

    # 7) "Interview analyse"
    # Give a feedback about the interview

    # Testing if this file is running properly


if __name__ == "__main__":
    main()
