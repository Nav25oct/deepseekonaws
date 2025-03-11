# DeepSeek-R1 on Amazon Bedrock (Fully Managed)

## Overview

This repository demonstrates how to interact with **DeepSeek-R1**, a powerful text-to-text model, using **Amazon Bedrock**. The example includes invoking the model via both **AWS Console** and **API (boto3)**.

## Features

- **Serverless & Fully Managed**: No infrastructure management required.
- **Seamless API Access**: Use `boto3` to interact with DeepSeek-R1.
- **Flexible Configuration**: Adjust parameters like `temperature`, `top_p`, and `max_tokens`.

## Prerequisites

Ensure you have the following set up:

1. **AWS Account** with access to Amazon Bedrock.
2. **AWS CLI** installed and configured with necessary permissions.
3. **Python 3.x** installed.
4. **boto3** library installed (`pip install boto3`).

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/deepseek-bedrock.git
   cd deepseek-bedrock
   ```

2. Configure AWS credentials:
   ```bash
   aws configure
   ```

3. Install dependencies:
   ```bash
   pip install boto3
   ```

## Usage

### Invoke DeepSeek-R1 via API

Run the script to invoke the DeepSeek-R1 model:

```bash
python deepseek.py
```

### Sample Python Script

```python
import boto3
import json

# Initialize AWS session
session = boto3.Session(profile_name="bedrock")

# Create the Bedrock Runtime client
bedrock_runtime = session.client("bedrock-runtime", region_name="us-east-1")

# Inference Profile ARN for DeepSeek-R1 ( Repace with your Inference ARN )
inference_profile_arn = "arn:aws:bedrock:us-east-1:<awsaccount>:inference-profile/us.deepseek.r1-v1:0"

# Define the prompt
prompt = "Describe the purpose of a 'hello world' program in one line."

# Define the request body
request_body = json.dumps({
    "prompt": prompt,
    "temperature": 0.7,
    "top_p": 0.9,
    "max_tokens": 512,
    "stop": []
})

try:
    # Invoke DeepSeek-R1
    response = bedrock_runtime.invoke_model(modelId=inference_profile_arn, body=request_body)
    model_response = json.loads(response["body"].read())
    
    # Extract response text
    for index, choice in enumerate(model_response.get("choices", [])):
        print(f"Response {index + 1}:
{choice['text']}
")
        print(f"Stop reason: {choice['stop_reason']}
")

except Exception as e:
    print(f"ERROR: Unable to invoke model '{inference_profile_arn}'. Reason: {e}")
```

## Troubleshooting

- If you encounter `UnrecognizedClientException`, ensure AWS credentials are correctly configured.
- If you get `ValidationException`, check if your Bedrock model requires an inference profile.

## License

This project is licensed under the **MIT License**.

---

Happy experimenting with **DeepSeek-R1 on Amazon Bedrock**! 🚀
