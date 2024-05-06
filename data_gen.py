import pandas as pd
import openai
import os


# Load the DataFrame from CSV
# df = pd.read_csv('synthetic_data.csv')
def events_gen(user1,user2):
    
    """
    events generation from a csv
    """
    # Define the column names
    columns = ['name', 'dob', 'gender', 'address', 'city', 'state', 'email', 'phone_number', 'occupation', 'education', 'relationship', 'parent', 'preferred_location', 'hobbies', 'friends', 'username', 'password']
    data_1 = pd.DataFrame([user1], columns=columns)
    data_2 = pd.DataFrame([user2], columns=columns)
    
    # # Randomly select two rows from the DataFrame
    # #random_rows = df.sample(n=2)
    # data_1=user1
    # data_2=user2

    city=data_1['city']
    # Extract hobbies/interests from the selected rows
    # hobbies_1 = set(",".join(list(data_1['hobbies'])).split(','))
    # hobbies_2 = set(",".join(list(data_2['hobbies'])).split(','))
    hobbies_1=set(data_1['hobbies'].iloc[0])
    hobbies_2=set(data_2['hobbies'].iloc[0])
    # Find common hobbies/interests between the two rows
    common_activities = hobbies_1.intersection(hobbies_2)

    # Convert the set of common activities to a list
    common_activities_list = list(common_activities)

    # Combine the common activities with tuples of values from both rows for each column
    combined_data = {'Combined Activities': ', '.join(common_activities_list)}
    for column in columns:
        if column != 'Name':
            combined_data[column] = (data_1[column], data_2[column])

    # Set up OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')
    if combined_data:
    # Generate text indicating the combined activities along with other columns
        prompt = "the two people's individual information in tuple and combined activities:\n"
        for key, value in combined_data.items():
            prompt += f"- {key}: {value}\n"


        # Use the OpenAI API to generate text

        question = f"Now, please give exactly 5 events based on the information in the {prompt}"
        context="You are a event planner to make their date memorable."
        message = [
            {"role": "system", "content": context},
            {"role": "user", "content": question},
            {"role": "function","name":"example_func", "content": "date: Go to an avengers movie tonight at AMC metreon, San Francisco"},
        ]

        model_use = "gpt-3.5-turbo"
        response = openai.chat.completions.create(
        messages=message,
        model=model_use,
        temperature=0.5,
        frequency_penalty=0.0,
        max_tokens=500
        )

        # Extract the generated text
        generated_text = response.choices[0].message.content
    else:
        generated_text=None
    return generated_text,city
