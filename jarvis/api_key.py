import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Write the paragraph on car."}
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
print(response)

# Output

'''
{
  "id": "chatcmpl-7fBiIAtoMdf0rJ2o49yKYD2ga1eHG",
  "object": "chat.completion",
  "created": 1690050830,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "A car, also known as an automobile, is a wheeled motor vehicle used for transportation. It is typically propelled by an internal combustion engine or an electric motor. Cars are designed to accommodate passengers and also carry a certain amount of cargo. They have become an integral part of modern society, providing a convenient and efficient means of transportation. Cars come in various sizes and shapes, from small compact models to large SUVs and luxury vehicles. With advanced technological advancements, cars now offer numerous features such as air conditioning, power steering, and advanced safety systems. Despite the numerous benefits, cars also contribute to air pollution and traffic congestion. Overall, cars have revolutionized mobility and continue to evolve with advancements in technology."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 13,
    "completion_tokens": 141,
    "total_tokens": 154
  }
}
'''
