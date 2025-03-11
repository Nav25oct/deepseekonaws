import boto3
import json

# Initialize AWS session (Ensure credentials are correctly configured)
session = boto3.Session(profile_name="bedrock")

# Create the Bedrock Runtime client
bedrock_runtime = session.client("bedrock-runtime", region_name="us-east-1")

# ✅ Replace this with your actual Inference Profile ARN
inference_profile_arn = "arn:aws:bedrock:us-east-1:307698253033:inference-profile/us.deepseek.r1-v1:0"

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
    # Invoke DeepSeek-R1 using the inference profile
    response = bedrock_runtime.invoke_model(modelId=inference_profile_arn, body=request_body)

    # Parse the response body
    model_response = json.loads(response["body"].read())

    # Extract generated text from choices
    choices = model_response.get("choices", [])

    # Print response text
    for index, choice in enumerate(choices):
        print(f"Response {index + 1}:\n{choice['text']}\n")
        print(f"Stop reason: {choice['stop_reason']}\n")

except Exception as e:
    print(f"ERROR: Unable to invoke model '{inference_profile_arn}'. Reason: {e}")