### Integrate local llama3 that is hosted in LMStudio - locally [🦙+ 🤗]
---
A very basic first hand python code that inetgrates your local llama model to python code to use as per your requirement.
[llama and higging face code integration]

The model we downloaded 'Llama-3.2-3B-Instruct-Q4_K_M.gguf' to be used offline

PreRequisites: 
  0. Env: Windows PC
  1. Open LMStudio
  2. Run the server
  3. Test in browser with Get 'http://127.0.0.1:1234/v1/models' to check if it is responding
  4. Try code in python

  --

```python
# pip install OpenAI
# ref: https://lmstudio.ai/docs/app/api/endpoints/openai
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  # model="model-identifier",
  model="Llama-3.2-3B-Instruct-GGUF/Llama-3.2-3B-Instruct-Q4_K_M.gguf",  
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "When should I wake up?"}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
```

- Answer:
  "ChatCompletionMessage(content="Listen up, don't be late,\nWaking up early is great.\nGet some rest, then rise with the sun's rays,\nAnd start your day in a happy way.", refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None)"


