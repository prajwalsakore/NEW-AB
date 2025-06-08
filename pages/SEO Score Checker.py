import streamlit as st
import openai

# Make sure to set your OpenAI API key as an environment variable or paste here securely
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Or set like: openai.api_key = "your_api_key_here"

st.title("📝 Blog SEO Scorer (Using OpenAI)")

blog_text = st.text_area("Paste your blog content here:", height=300)

if st.button("Get SEO Score"):
    if not blog_text.strip():
        st.warning("Please paste your blog content to analyze.")
    else:
        with st.spinner("Analyzing your blog..."):
            # Create a prompt to get SEO score and feedback
            prompt = f"""
You are an SEO expert. Please analyze the following blog content and:

1. Give it an SEO score out of 100.
2. Provide a brief rating summary.
3. List 3 suggestions to improve the blog's SEO.

Blog Content:
\"\"\"
{blog_text}
\"\"\"

Answer in this exact format:

SEO Score: <score out of 100>
Rating: <brief rating summary>
Suggestions:
1.
2.
3.
"""

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful SEO expert."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=300,
                    temperature=0.7,
                )
                answer = response.choices[0].message.content.strip()

                st.markdown("### SEO Analysis Result")
                st.markdown(answer)

            except Exception as e:
                st.error(f"Error communicating with OpenAI: {e}")
