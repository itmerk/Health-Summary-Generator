import streamlit as st  # Importing Streamlit for building interactive web apps
import google.generativeai as genai  # Importing Google Gemini for generative AI
import os  # Importing os module for environment variable access

# Configure Google Gemini API with the API key from environment variable
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Streamlit page configuration: setting layout to wide and defining the page title
st.set_page_config(layout="wide")
st.title(':rainbow[Health Summary Generator]')  # Title for the web app with a rainbow-colored effect

# Model configuration settings for text generation
generation_config = {
  "temperature": 0.2,  # Controls the randomness of the model's output (lower value = more predictable)
  "top_p": 0.95,       # Nucleus sampling parameter; considers only tokens whose cumulative probability is within this value
  "top_k": 40,         # Limits the model to consider only the top k tokens for generation
  "max_output_tokens": 8192,  # Max tokens for the output response
  "response_mime_type": "text/plain",  # Specifies the format of the response as plain text
}

# Initialize the generative model with the specified configuration and instruction for system behavior
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",  # Model version to use
    generation_config=generation_config,  # Pass in the model's configuration
    system_instruction="Answer Question for the PDF Attachment only"  # Instruction for the model's behavior during the chat
)

# Streamlit file uploader for accepting multiple PDF files from the user
uploaded_files = st.file_uploader("Upload one or more PDF files", type="pdf", accept_multiple_files=True)

# Text input for custom prompt to summarize the PDFs
user_prompt = st.text_input("Enter your prompt for summarizing the PDF(s)", "Give me a summary of this PDF file in 20 words.")

# Create a submit button that triggers the PDF processing and content generation
if st.button("Generate Summary") and uploaded_files:
    summaries = {}  # Dictionary to store summaries for each uploaded file
    
    # Loop through each uploaded file and process them
    for uploaded_file in uploaded_files:
        # Save each uploaded file temporarily to the local system
        temp_file_path = f"temp_{uploaded_file.name}"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Upload the saved file to Google Gemini for processing
        sample_file = genai.upload_file(temp_file_path)
        
        # Generate content (summary) for each file based on the user’s prompt
        response = model.generate_content([user_prompt, sample_file])
        
        # Store the generated summary in the dictionary, using the filename as the key
        summaries[uploaded_file.name] = response.text
    
    # Display the generated summaries for each uploaded file
    st.write("### Summaries:")
    for filename, summary in summaries.items():
        st.write(f"**{filename}:** {summary}")  # Display the summary for each file
