# Simple DSPy Wrapper with FastAPI

This is a simple wrapper around the DSPy library using 
FastAPI to create a web service for generating text using 
large language models (LLMs). The service exposes an endpoint
that accepts a request payload specifying a repository your 
personal access token or api token to GitHub can read, 
and returns generated text for llm.txt file.

Requires env variable: GITHUB_ACCESS_TOKEN

Requires ollama running locally serving gpt-oss:latest.

Alternatively, you can set the env variable OPENAI_API_KEY to use the closed source gpt-4-mini model. 

Usage:

```base
git clone https://github.com/dnck/simple-dspy-fastapi.git
cd simple-dspy-fastapi
python -m venv .simple-dspy-fastapi 
source .simple-dspy-fastapi/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
python main.py
```


See the example request in `example.sh`.