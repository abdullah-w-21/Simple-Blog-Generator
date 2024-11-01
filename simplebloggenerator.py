import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import List

# api keys
os.environ["GOOGLE_API_KEY"] = "AIzaSyAoHZrkpzdA528x6DHMGdKgt1ur05_svaw"
os.environ["SERPER_API_KEY"] = "7ee17327c8ac81766519b8ef3de5fd236f84ce66"

llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.7)
search = GoogleSerperAPIWrapper()

# templates
RESEARCH_TEMPLATE = """
Summarize the most relevant information about:
{title}
{keywords}

Focus on factual information that would enhance a blog post about this topic.
"""

BLOG_TEMPLATE = """
Write a comprehensive blog post based on the following details:

Title: {title}
Keywords: {keywords}
Key Points: {points}

Additional Research Information:
{research_info}

Please write an engaging and informative blog post of 300-400 words that incorporates the keywords naturally,
covers all the key points, and integrates the research information smoothly. The tone should be professional 
yet conversational.

Structure the blog with:
1. An engaging introduction
2. Well-organized body paragraphs
3. A meaningful conclusion
"""


def get_research_info(title: str, keywords: str) -> str:

    research_prompt = PromptTemplate(
        input_variables=["title", "keywords"],
        template=RESEARCH_TEMPLATE
    )
    research_chain = LLMChain(llm=llm, prompt=research_prompt)

    # do web search
    search_results = search.run(f"{title} {keywords}")

    # gen research summary
    research_info = research_chain.run(title=title, keywords=keywords)

    return f"{research_info}\n\nAdditional web research:\n{search_results}"


def generate_blog(title: str, keywords: List[str], points: List[str]) -> str:

    # Convert lists to strings
    keywords_str = ", ".join(keywords)
    points_str = "\n- ".join(points)

    # Get research information
    research_info = get_research_info(title, keywords_str)

    # Create blog generation chain
    blog_prompt = PromptTemplate(
        input_variables=["title", "keywords", "points", "research_info"],
        template=BLOG_TEMPLATE
    )
    blog_chain = LLMChain(llm=llm, prompt=blog_prompt)

    # Generate blog post
    blog_post = blog_chain.run(
        title=title,
        keywords=keywords_str,
        points=points_str,
        research_info=research_info
    )

    return blog_post


def main():
    # test
    title = "Ai in education and its usecases"
    keywords = [
        "AI in education",
        "computer science",
        "learning",
        "generative ai",
        "education trends"
    ]
    points = [
        "Current applications of AI in education",
        "Benefits of AI-powered education",
        "Challenges and limitations",
        "Future predictions and developments",
        "Impact on teaching professionals"
    ]

    try:
        # Generate blog post
        blog_post = generate_blog(title, keywords, points)
        print("\nGenerated Blog Post:")
        print("-" * 50)
        print(blog_post)
        print("-" * 50)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()