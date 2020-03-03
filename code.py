import re


class User:
    # take input url from command line and saves it if valid
    def __init__(self, initial_input_url_by_user=None):
        self.cur_url_saved = ""
        self.save_url(initial_input_url_by_user)

    # function to check whether the given url is valid
    def chk_url(self, url):
        regex_pattern = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return regex_pattern.match(url) is not None

    # function takes input url from prompt, saves the url returns true if it valid
    def each_attempt_save_url(self, input_url=None):
        if input_url is None:
            new_target_url = str(input("Please enter a valid url:"))
        else:
            new_target_url = input_url
        if self.chk_url(new_target_url):
            self.cur_url_saved = new_target_url
            print("Your new target url %s is valid and saved" % new_target_url)
            return True
        else:
            print("You have entered an invalid url")
            return False

    # function to prompt user for url to be given as input and saves if valid
    # input_url is not None when a url is given when initializing the code
    def save_url(self, input_url=None):
        num_attempts = 0
        max_attempts = 3
        while num_attempts < max_attempts:
            if(num_attempts!=0):
                input_url = None
            if self.each_attempt_save_url(input_url):
                return
            num_attempts += 1
        print("You have reached maximum no. of attempts")
        print("Session terminated.")

    # Runs query on the saved url, prints error message when no url is saved
    def run_query(self):
        if self.cur_url_saved == "":
            print("Error: No URL is saved")
            return
        print("Query ran on stored url: %s" % self.cur_url_saved)
