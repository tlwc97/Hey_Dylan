#initial inquiry
def cs_service_bot():
    print("Hello! Welcome to DNS Calble Company's Servie Portal. \n [1] New Customer \n [2] Existing Customer")
    response = input("Please choose an option")
    pause
    if response == "1":
        new_customer_bot()
    elif response == "2" :
        existing_customer_bot()
    else:
        Print("Sorry, we did not understand your selection")
        customer_service_bot()

#for existing customers
def existing_customer_bot():
    print("[1] Television support \n [2] Internet support \n [3] Speak to a Support Representative")
    response = input("What kind of support do you need?")
    if response == "1":
        television_support():
    elif response == "2":
        internet_support()
    elif response == "3":
        live_rep()
    else:
        print("Sorry we did not understand your selection")
        existing_customer_bot()

#for new customers
def new_customer_bot():
    print("[1] Sign up for service \n [2] Schedule a home visit \n [3] Speak to a Support Representative")
    response = input("Please choose an option")
    if response == "1":
        sign_up()
    elif response == "2":
        home_visit()
    elif response == "3":
        live_rep()
    else:
        print("Sorry we did not understand your selection")
        existing_customer_bot()

#for option television_support
def television_support():
    print("What is the nature of your problem? \n [1] I can't  access certain channels. \n [2] My picture is blurry. \n [3] I keep losing service. \n [4] Other issues.")
    response = input("Please choose an issue")
    if response == "1":
        Print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    elif response == "2":
        print("Try adjusting the antenna above your television set.")
        did_that_help()
    elif response == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        did_that_help()
    elif response == "4":
        live_rep()
    else:
        print("Sorry, we did not understand your selection")
        television_support()

#option for internet Support
def internet_support():
    print("What is the nature of your problem? \n [1] I can't connect to my internet. \n [2] My connection is very slow. \n [3] I can't access certain sites. \n [4] Other issues")
    response = input("Please choose an issue")
    if response == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif response == "2":
        print("Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.'')
        did_that_help()
    elif response == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif response == "4":
        live_rep()
    else:
        print("Sorry, we did not understand your selection")
        internet_support()

#to see if issue is solved
def did_that_help():
    response = input("Did that resolve the issue?)
    if response == "Yes" or "Y" or "Yea" or "Hell Yea":
        print("We were glad to help! Thank you for using DNS!")
    elif response == "No" or "fuck you" or "Nope" or "N":
        response2 = input("Would you like to talk to a live representative or have a home visit?")
        if response2 == "Live rep":
            live_rep()
        elif response2 == "home visit":
            home_visit()
        else:
            print("Sorry we did not understand your selection")
            did_that_help()

#for signing up
def sign_up():
    print("Great choice friend! We are excited to have you jon the DNS family Please select the package you are interested in signing up for. \n [1]Bundle deal (Internet and Cable) \n [2] Internet \n [3] Cable")
    response = input("Please choose an option")
    if response == "1":
        print("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif response == "2":
        print("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif reponse == "3":
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    else:
        print("Sorry we could not understand your choice")
        sign_up()

#home visit function
def home_visit(purpose= "none"):
    if purpose == "none":
        print("What is the reason for your home visit? \n [1] New service installation? \n [2] Exisiting servive repair? \n [3]Service for unscouted region?")
        purpose2 = input("Which reason do you want?")
        if purpose2 == "1":
            home_visit("install")
        elif purpose2 == "2":
            home_visit("service")
        elif purpose2 == "3":
            home_visit("scouting")
        else:
            print("Sorry, we didn't understand your selection.")
            home_visit()
    if purpose == "new install":
        print("Please enter a date below when you are available for a technician to come to your home and install your new service.")
        visit_date = input("Date:")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm." )
        return visit_date
    if purpose == "service":
        print("Please enter a date below when you are available for a technician to come and inspect the problem:")
        visit_date = input("Date:")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm." )
        return visit_date
    if purpose == "scout":
        print("Please enter a date below when you are available for a technician to come scout your region for expansion:")
        visit_date = input("Date:")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm." )
        return visit_date

#live rep function
def live_rep(purpose):
    if purpose == "sales":
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
    if purpose == "support":
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
