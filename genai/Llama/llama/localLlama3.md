### Integrate local llama3 that is hosted in LMStudio?
---
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
```

