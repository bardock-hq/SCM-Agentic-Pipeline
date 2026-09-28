import os
from io import BytesIO
from dotenv import load_dotenv, find_dotenv
from google import genai
from PIL import Image
from atproto import Client, client_utils

# 1. Load environment variables from root .env
load_dotenv(find_dotenv())

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BLUESKY_HANDLE = os.getenv("BLUESKY_HANDLE")
BLUESKY_APP_PASSWORD = os.getenv("BLUESKY_APP_PASSWORD")

def generate_ai_image(prompt: str) -> str:
    """Generates an AI image using Imagen 3 and saves it to assets/."""
    print("🎨 Generating AI image via Imagen 3...")
    client = genai.Client(api_key=GEMINI_API_KEY)

    # Call Google Imagen 3 model
    result = client.models.generate_images(
        model='imagen-3.0-generate-002',
        prompt=prompt,
        config=dict(
            number_of_images=1,
            output_mime_type="image/jpeg",
            aspect_ratio="16:9",
        )
    )

    # Save generated image locally
    os.makedirs("assets", exist_ok=True)
    output_path = "assets/generated_briefing.jpg"

    for generated_image in result.generated_images:
        image = Image.open(BytesIO(generated_image.image.image_bytes))
        image.save(output_path)
        print(f"✅ Image saved locally at {output_path}")
        return output_path

    raise Exception("Image generation failed.")

def publish_to_bluesky():
    if not BLUESKY_HANDLE or not BLUESKY_APP_PASSWORD:
        print("❌ Error: BLUESKY_HANDLE or BLUESKY_APP_PASSWORD missing in .env")
        return

    # Short summary text prompt for image generation
    image_prompt = "A high-tech digital supply chain analytics network banner, futuristic global logistics, glowing nodes, 16:9 wallpaper."

    # A. Generate the image
    try:
        image_path = generate_ai_image(image_prompt)
    except Exception as e:
        print(f"⚠️ Image generation failed: {e}")
        image_path = None

    # B. Connect to Bluesky
    client = Client()
    print("Connecting to Bluesky...")
    client.login(BLUESKY_HANDLE, BLUESKY_APP_PASSWORD)

    # C. Build short hook post with website link
    tb = client_utils.TextBuilder()
    tb.text("📦 SCM Intelligence Briefing Updated!\n\n")
    tb.text("Read the full detailed report on our live platform: ")
    tb.link("View Dashboard", "https://scm-agentic-pipeline-z9tybikpc59chtafxjk8mk.streamlit.app/")

    # D. Publish post with generated image
    if image_path and os.path.exists(image_path):
        with open(image_path, "rb") as f:
            img_data = f.read()

        client.send_image(
            text=tb,
            image=img_data,
            image_alt="AI Generated Supply Chain Analytics Image"
        )
        print("🚀 Successfully posted short text, generated AI image, and link to Bluesky!")
    else:
        client.send_post(tb)
        print("🚀 Posted text update to Bluesky.")

if __name__ == "__main__":
    publish_to_bluesky()