import ollama
response = ollama.chat(model='llama3.2-vision:latest', messages=[
  {
    'role': 'user',
    'content': r'''Explain what is love'''
  },
])
print(response['message']['content'])
