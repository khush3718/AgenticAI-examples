import requests
import json
import argparse

SERVER_URL = "http://localhost:8000"

def main():
    parser = argparse.ArgumentParser(description="send query to Agentic RAG server")
    parser.add_argument("--query", type=str, required=True, help="The query to send to the server")

    args = parser.parse_args()
    payload = {"query": args.query}

    try:
        response = requests.post(f"{SERVER_URL}/predict", json=payload)
        result = response.json()['output']['raw']
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()