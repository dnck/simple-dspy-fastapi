# Simple DSPy Wrapper with FastAPI

This is a simple wrapper around the DSPy library using 
FastAPI to create a web service for generating text using 
large language models (LLMs). The service exposes an endpoint
that accepts a request payload specifying a repository your 
personal access token or api token to GitHub can read, 
and returns generated text for llm.txt file.

Requires env variable: GITHUB_ACCESS_TOKEN

Requires ollama running locally serving gpt-oss:latest.

See the example request in `example.sh`.