# revChatGPTAuth

Authenticate using your browser's cookies - no need to inconveniently copy and paste from your browser!

## Getting Started

### Prerequisites

- <= Python 3.9

### Installing

```bash
pip install revChatGPTAuth
```

### Usage

```python
from revChatGPTAuth import get_access_token
access_token = get_access_token('brave') # your browser
```

### With `revChatGPT`

The following example codes are from the `revChatGPT` README.

#### Basic example (streamed)

```python

from revChatGPT.V1 import Chatbot
from revChatGPTAuth import get_access_token

chatbot = Chatbot(config={
  "access_token": get_access_token('brave')
})

print("Chatbot: ")
prev_text = ""
for data in chatbot.ask(
    "Hello world",
):
    message = data["message"][len(prev_text) :]
    print(message, end="", flush=True)
    prev_text = data["message"]
print()
```

#### Basic example (single result)

```python
from revChatGPT.V1 import Chatbot
from revChatGPTAuth import get_access_token

chatbot = Chatbot(config={
  "access_token": get_access_token('brave')
})

prompt = "how many beaches does portugal have?"
response = ""

for data in chatbot.ask(
  prompt
):
    response = data["message"]

print(response)
```
