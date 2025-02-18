import ollama

CODE_COLOR = "\033[94m"  # Blue for code responses
DETAIL_COLOR = "\033[92m"  # Bright green for verbose details
RESET = "\033[0m"

prompt = "simple if else python code"

response_stream = ollama.generate(
    model="calista:latest",
    stream=True,
    prompt=prompt
)

for chunk in response_stream:
    response_text = chunk.get('response', '')
    print(f"{CODE_COLOR}{response_text}{RESET}", end='', flush=True)

    if chunk.get('done'):
        print(f"\n{DETAIL_COLOR}--- Verbose Details ---{RESET}")
        print(f"{DETAIL_COLOR}Total duration: {chunk.get('total_duration')/1e9:.2f} seconds{RESET}")
        print(f"{DETAIL_COLOR}Load duration: {chunk.get('load_duration')/1e9:.2f} seconds{RESET}")
        print(f"{DETAIL_COLOR}eval_duration: {chunk.get('eval_duration')/1e9:.2f} seconds{RESET}")
        print(f"{DETAIL_COLOR}prompt_eval_count: {chunk.get('prompt_eval_count')}/Tokens{RESET}")
        print(f"{DETAIL_COLOR}eval_count: {chunk.get('eval_count')}/Tokens{RESET}")
        print(f"{DETAIL_COLOR}Model: {chunk.get('model')}{RESET}")
