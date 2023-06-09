# Steam Chatbot

This repository offers an API to bridge from Steam Chat to ChatGPT with custom knowledge/prompt. The chatbot is powered by OpenAI's GPT-3.5 architecture and can provide personalized responses to users.

## Installation

1. Clone the project:

   ```bash
   git clone https://github.com/toosyou/steam-chatbot.git
   ```

2. Fill in `secret.cfg` with your OpenAI API key:

   ```
   api-key = <your_api_key>
   ```
   Here are the instructions to get an OpenAI API key:

    1. Go to OpenAI’s Platform website at platform.openai.com and sign in with an OpenAI account.
    2. Click your profile icon at the top-right corner of the page and select “View API Keys.”
    3. Click “Create New Secret Key” to generate a new API key.
   
    For more information, you can check out this [link](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/).

3. Fill in `system_prompt.txt` with custom knowledge about the stream. This can include information about the game being played, the streamer's personality, and any inside jokes or recurring themes.

4. Fill in `example_in.txt` and `example_response.txt` with example input/output to better guide the bot. This will help the chatbot learn to provide more relevant responses.

## Docker

You can also use Docker to build and run the chatbot. 

1. Build the Docker image:

   ```bash
   docker build -t steam-chatbot .
   ```

2. Run the Docker container:

   ```bash
   docker run -it -p 8080:8080 steam-chatbot
   ```

   This will start the chatbot on port 8080. You can test the chatbot by sending GET requests to `http://localhost:8080/ai?&message=<message>`.

## Google Cloud (Optional)

You can also deploy the Docker container to Google Cloud Run to serve the chatbot.

1. Build the Docker image:

   ```bash
   docker build -t gcr.io/[PROJECT-ID]/[IMAGE]:[TAG] .
   ```

2. Push the Docker image to Google Container Registry:

   ```bash
   docker push gcr.io/[PROJECT-ID]/[IMAGE]:[TAG]
   ```

3. Deploy the container to Google Cloud Run:

   ```bash
   gcloud run deploy --image gcr.io/[PROJECT-ID]/[IMAGE]:[TAG] --platform managed --region [REGION] --allow-unauthenticated [SERVICE-NAME]
   ```

Replace `[PROJECT-ID]`, `[IMAGE]`, `[TAG]`, `[REGION]`, and `[SERVICE-NAME]` with your own values.  
For more information, you can check out this [link](https://cloud.google.com/run/docs/deploying).

## Nightbot

To use the chatbot with Nightbot, you can create two custom commands to send a GET request to the chatbot URL with the `message` query parameters. For example, if your chatbot is running on Google Cloud Run, you can create a command with the following URL:

* First command: `!ai` whose alise is set to `_ai`
   ```
   $(twitch $(user) "{{displayName}}"): $(query)
   ```
* Second command: `_ai`
   ```
   MrDestructoid < $(urlfetch <url-to-api>/ai?message=$(querystring))
   ```

Replace `<url-to-api>` with the URL to your chatbot API.