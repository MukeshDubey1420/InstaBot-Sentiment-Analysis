import requests, urllib                     # Importing Libraries..
from termcolor import colored
APP_ACCESS_TOKEN = '2949992764.95c80d8.47897e91a7f547e592decfde42b7cf94'  # Token of Mukesh Dubey....

#Sandbox Users :

BASE_URL = 'https://api.instagram.com/v1/'


#    Function declaration to get your own info ......

def self_info():                 # defining Function to ascess users information...
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print colored('Username: %s','blue') % (user_info['data']['username'])
            print colored('No. of followers: %s','blue') % (user_info['data']['counts']['followed_by'])
            print colored('No. of people you are following: %s','blue') % (user_info['data']['counts']['follows'])
            print colored('No. of posts: %s','blue') % (user_info['data']['counts']['media'])
        else:
            print colored('User does not exist!!','red')
    else:
        print colored('Status code other than 200 received!','red')



#    Function declaration to get the ID of a user by username


def get_user_id(insta_username):                  # Defining function to get User_ID by passing username ..
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print colored('Status code other than 200 received!','red')
        exit()



#       Function declaration to get the info of a user by username

def get_user_info(insta_username):      # Defining function to Get user information by passing username ...
    user_id = get_user_id(insta_username) # Calling Function of get user_Id  to further proceed..
    if user_id == None:
        print colored('Instauser Of This Username does not exist!','red')
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print colored('Username: %s','blue') % (user_info['data']['username'])
            print colored('No. of followers: %s','blue') % (user_info['data']['counts']['followed_by'])
            print colored('No. of people you are following: %s','blue') % (user_info['data']['counts']['follows'])
            print colored('No. of posts: %s','blue') % (user_info['data']['counts']['media'])
        else:
            print colored('There is no data exists for this user!','red')
    else:
        print colored('Status code other than 200 received!','red')



#   Function declaration to get your recent post



def get_own_post():                            #   Defining Function to get our recent post either picture or video..
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)    # using urllib library to download the post by passing link of recent media to it ..
            print colored('Your image From Your Recent Posts has been downloaded!','green')
        else:
            print colored('Post does not exist!','red')
    else:
        print colored('Status code other than 200 received!','red')



#          Function declaration to get the recent post of a user by username

def get_user_post(insta_username):   # Defining function to get recent posts of a user by passing username to function..
    user_id = get_user_id(insta_username)    # Calling get user id function to get user id by passing username ..
    if user_id == None:
        print colored('Instauser Of This Username does not exist!', 'red')
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print colored('GET request url : %s','blue') % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)  # Fetching users recent post by passing link to the function as parameter..
            print colored('The Image From users Recent Posts has been downloaded!','green')
        else:
            print colored('Post does not exist!', 'red')
    else:
        print colored('Status code other than 200 received!','red')


def start_bot():   # defining the Main function under which above sub-function works by calling ....
    while True:
        print colored('Hey! We Welcomes U to instaBot!','green')
        print colored('Select your menu options:','blue')
        print colored("Select Option:'A'  To Get your own details\n",'green')
        print colored("Select Option:'B'  To Get details of a user by username\n",'green')
        print colored("Select Option:'C'  To Get your own recent post\n",'green')
        print colored("Select Option:'D'  To Get the recent post of a user by username\n",'green')
        # print "e.Get a list of people who have liked the recent post of a user\n"
        # print "f.Like the recent post of a user\n"
        # print "g.Get a list of comments on the recent post of a user\n"
        # print "h.Make a comment on the recent post of a user\n"
        # print "i.Delete negative comments from the recent post of a user\n"
        print colored("Select Option:'J' For Exit",'red')

        choice = raw_input(colored("Enter you choice: ",'blue'))
        if choice.upper() == "A":
            self_info()
        elif choice.upper() == "B":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            get_user_info(insta_username)
        elif choice.upper() == "C":
            get_own_post()
        elif choice.upper() == "D":
            insta_username = raw_input(colored("Enter the username of the user: ",'blue'))
            get_user_post(insta_username)
        # elif choice=="e":
        #    insta_username = raw_input("Enter the username of the user: ")
        #    get_like_list(insta_username)
        # elif choice=="f":
        #    insta_username = raw_input("Enter the username of the user: ")
        #    like_a_post(insta_username)
        # elif choice=="g":
        #    insta_username = raw_input("Enter the username of the user: ")
        #    get_comment_list(insta_username)
        # elif choice=="h":
        #    insta_username = raw_input("Enter the username of the user: ")
        #    make_a_comment(insta_username)
        # elif choice=="i":
        #    insta_username = raw_input("Enter the username of the user: ")
        #    delete_negative_comment(insta_username)
        elif choice.upper() == "J":
            exit()
        else:
            print colored("Wrong Choice Selected By U",'red')


start_bot()             # Calling the main function ..........to start the application....