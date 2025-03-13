from flask import Flask, render_template, request, jsonify
import os
from groq import Groq

app = Flask(__name__)

# Set your Groq API key here
AI_KEY = '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'

if not AI_KEY:
    raise ValueError(
        "Masukan GROQ API KEY ke environment masing2 atau pake hardcoded version."
    )

client = Groq(
    api_key=AI_KEY,
)

# System Prompt
SYSTEM_PROMPT = {
    "role": "system",
    "content": "Act as a professional scriptwriter for a high-engagement content creator. Generate 5 different script that is concise, engaging, and optimized for [platform: TikTok, YouTube, Instagram, etc.]. The tone should be [fun, educational, emotional, authoritative, etc.] to resonate with the target audience. The script should include:"

"- A powerful hook in the first [X] seconds to capture attention"
"- Clear storytelling or step-by-step structure"
"- Emotional triggers or relatable elements"
"- A strong CTA (Call-to-Action) at the end to drive engagement"
"- Ensure the language is natural, easy to understand, and optimized for [platform algorithm: TikTok FYP, YouTube SEO, Instagram engagement, etc.]."
    "**Example Format:**"
    "🔥 *Content Scene #[number]:* [Title]"
    "- 🎯 **Script Scene [number of scene]:** [time, plot blackground, scr]"
    "- continuing the script scene if it has to be some script scene"
    "- 🎯 **Call to Action :** [time, plot blackground, scr]"
    "- 🎥 **Format:** [Short video, carousel, blog, livestream, etc.]"
    "- 🎯 **Best for:** [Platform & Target Audience]"
    "- 💡 **Bonus Tip:** [Optional extra insight]"
    "Respond in indonesia language. Always respond in this structured and engaging way. Do not include your thought process. Your goal is to maximize clarity, impact, and engagement."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    target = data.get('target', '')
    goal = data.get('goal', '')
    platform = data.get('platform', '')
    video_lenght = data.get('video_lenght', '')
    style = data.get('style', '')
    cta = data.get('cta', '')

    user_prompt = f"""
    Generate AI-powered content ideas based on the following criteria:
    - Target audience: {target}
    - Goal: {goal}
    - Platform : {platform}
    - Video Length: {video_lenght}
    - Tone & Style: {style}
    - Call to Action: {cta}
    """

    try:
        response = client.chat.completions.create(
            model="qwen-2.5-32b",  # Change to Groq-supported model if needed
            messages=[SYSTEM_PROMPT, {"role": "user", "content": user_prompt}]
        )

        ai_response = response.choices[0].message.content

    except Exception as e:
        ai_response = f"Error: {str(e)}"

    return jsonify({'content_ideas': ai_response})

if __name__ == '__main__':
    app.run(debug=True)
