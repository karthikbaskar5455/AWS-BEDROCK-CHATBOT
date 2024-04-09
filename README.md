
---

# Amazon Bedrock Chatbot Streamlit App

This repository hosts a Streamlit-based web application that leverages Amazon Bedrock for implementing a chatbot powered by AI. Users can interact with the chatbot by asking questions, and the AI model responds with helpful answers. The project uses the AWS Bedrock service to deploy and manage the chatbot's language models.

## Usage

To use the application:

1. **Clone the Repository**: 
   
    ```bash
    git clone https://github.com/karthikbaskar5455/AWS-BEDROCK-CHATBOT.git
    ```

2. **Install Dependencies**:
   
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up AWS Credentials**:
   
   Ensure you have an AWS account and the AWS CLI (Command Line Interface) installed and configured with proper credentials. Make sure to set up an AWS profile and configure it with the necessary permissions. You'll need to provide AWS access key ID and AWS secret access key.

4. **Enable Language Models on AWS Bedrock**:
   
   In the AWS Bedrock service, enable the necessary language models. For this project, the AI model "amazon.titan-text-express-v1" is used with a maximum token count of 700. Note that there may be minimal costs associated with API token-based usage of chatbots for prompts and responses.

5. **Run the Streamlit App**:
   
    ```bash
    streamlit run app2.py
    ```

6. **Interact with the Chatbot**:
   
   Access the app in your web browser and interact with the chatbot by typing questions in the input field.

## Project Structure

- **`app2.py`**: Main Streamlit application file.
  
- **`bedrock.py`**: Contains functions for initializing the chatbot chain, handling user input, and rendering chat messages.
  
- **`requirements.txt`**: List of Python dependencies.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
##Output 
![output1](https://github.com/karthikbaskar5455/AWS-BEDROCK-CHATBOT/assets/164629495/341caedf-b4e0-44f1-840f-8996a1def7a8)
![output2](https://github.com/karthikbaskar5455/AWS-BEDROCK-CHATBOT/assets/164629495/8a12a79b-36a8-4000-a579-74bd30725687)
![output3](https://github.com/karthikbaskar5455/AWS-BEDROCK-CHATBOT/assets/164629495/1f5c36b4-d700-48cb-8d1f-292ad44b4b5e)
![output4](https://github.com/karthikbaskar5455/AWS-BEDROCK-CHATBOT/assets/164629495/59c4ec01-17ef-4f05-af28-d38884402164)
![output5](https://github.com/karthikbaskar5455/AWS-BEDROCK-CHATBOT/assets/164629495/ab9508d1-31d5-40fb-bd7b-bf525a37d7ac)

