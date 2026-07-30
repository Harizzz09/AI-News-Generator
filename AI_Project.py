from openai import OpenAI
from dotenv import dotenv_values, find_dotenv

#It's an AI tool dedicated to find news response regarding of anything 
env_path = find_dotenv("APIL.env") 
config = dotenv_values(env_path)

client = OpenAI(api_key=config["API_KEY"])

def generate_blog(topic):
    response = client.responses.create(
        model="gpt-5",
        input=f"Write a news response about {topic}."
    )

    print(response.output_text)

topic = input("Please enter the topic of interest: \n")
print('Please wait for our AI to response.... \n')
generate_blog(topic)

keep_writing = True

print('\n')

while keep_writing:
    answer = input('Write another news response? Y for yes, anything else for no.').lower() #.lower() is placed to ensure that even if user put 'y' it'll still work 
    if answer == 'y':
        paragraph_topic = input('What should this paragraph talk about? \n')
        print('Please wait for our AI to response.... \n')
        generate_blog(paragraph_topic)
    else:
        keep_writing = False 
        print('\n')
        print('Thank for using our service')
