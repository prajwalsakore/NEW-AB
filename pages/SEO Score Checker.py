import streamlit as st
import re

def seo_score(text, keyword):
    score = 0
    feedback = []

    words = re.findall(r'\w+', text.lower())
    word_count = len(words)

    # 1. Length score
    if word_count >= 800:
        score += 30
        feedback.append("Great length! Your blog is over 800 words.")
    elif word_count >= 400:
        score += 15
        feedback.append("Good length, but consider making it longer for better SEO.")
    else:
        feedback.append("Too short. Aim for at least 800 words.")

    # 2. Keyword density (ideal 1-3%)
    if keyword:
        keyword_count = sum(1 for w in words if w == keyword.lower())
        density = (keyword_count / word_count) * 100 if word_count > 0 else 0

        if 1 <= density <= 3:
            score += 30
            feedback.append(f"Keyword density is good at {density:.2f}%.")
        elif density < 1:
            feedback.append(f"Keyword density is low ({density:.2f}%). Use the keyword more.")
        else:
            feedback.append(f"Keyword density is high ({density:.2f}%). Avoid keyword stuffing.")
    else:
        feedback.append("No keyword provided to check density.")

    # 3. Heading usage
    headings = re.findall(r'(^|\n)#{1,6} ', text)
    if len(headings) >= 3:
        score += 15
        feedback.append(f"Good use of headings ({len(headings)} found).")
    else:
        feedback.append("Add more headings to structure your content.")

    # 4. Links count
    links = re.findall(r'https?://\S+', text)
    if len(links) >= 2:
        score += 15
        feedback.append(f"Good number of links ({len(links)}) included.")
    else:
        feedback.append("Add more relevant links to boost SEO.")

    # 5. Readability (average sentence length)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    avg_sentence_length = word_count / len(sentences) if sentences else 0

    if 12 <= avg_sentence_length <= 20:
        score += 10
        feedback.append(f"Good readability with average sentence length {avg_sentence_length:.1f} words.")
    elif avg_sentence_length < 12:
        feedback.append(f"Sentences are short ({avg_sentence_length:.1f} words). Good for clarity.")
    else:
        feedback.append(f"Sentences are quite long ({avg_sentence_length:.1f} words). Try to shorten them.")

    return min(score, 100), feedback

# ----------- Streamlit UI for SEO Scorer --------------

st.header("📝 SEO Blog Scorer")

blog_text = st.text_area("Paste your blog content here:", height=300)
keyword = st.text_input("Enter your main keyword:")

if st.button("Analyze SEO Score"):
    if blog_text.strip() == "":
        st.warning("Please paste your blog content first.")
    else:
        score, feedback = seo_score(blog_text, keyword)
        st.metric(label="SEO Score", value=f"{score}/100")

        st.markdown("### Feedback:")
        for f in feedback:
            st.write("- " + f)
