from code import User
import sys

def run_test():
    # takes url when the code is initialised
    if(len(sys.argv)>1):
        initial_input_url_by_user = sys.argv[1]
    else:
        initial_input_url_by_user = None
    user = User(initial_input_url_by_user)

    # prompts user for new url and asks whether he wants to query the current saved url
    max_queries_cnt = 0
    while(max_queries_cnt<10):
        # Running Query
        is_run_query = str(input("Do you wish to run query on currently saved url: (Yes/No) "))
        if (is_run_query == "Yes"):
            user.run_query()

        # Prompting user for new target url
        is_new_target = str(input("Do you wish to enter new target url: (Yes/No) "))
        if(is_new_target=="Yes"):
            user.save_url()
        else:
            print("Exiting.") # exits when the user doesn't want to given new target url
            break
        max_queries_cnt += 1

if __name__== "__main__":
  run_test()