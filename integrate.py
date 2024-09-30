import openai

# Copy and paste our API key on the line below
openai.api_key = 'sk-proj-PeU7ubp-ru8emy4elbzpyOJfOoBhtWXieVhvo_BPFOR-sB0KGDkCwqkEML1nbCLeDI9xx|2X033B|bkFJFyUyNUQwknacEgiW31sclkXjYsYgOM4xvXcqAUNXVbpBdw-CXuyAF9DLJ-aX2ZZBqwkq1yMMA'
messages = [ {"role": "system", "content": 
              "You are an intelligent assistant."} ]

# Create an infinite loop so we can have a continuous conversation with the AI
while True:
      # Access the correct model of GPT for the code and correctly syntax it for Python (TYPE EXTRA HERE)
      message = input("User: ")
      if message:
        message.append( {"role": "system", "content": message},
                      )
        chat = openai.ChatCompletion.create(
          model ="gpt-3.5-turbo", messages= messages
         )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
  # print whatever reply the AI comes up with into the terminal (TYPE EXTRA HERE)
    reply = chat.choices[0].message.content
    print(f"ChatGPT:{reply}")
    messages.append({"role": "assistant", "content": reply})
