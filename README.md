# Simple-Blog-Generator
Simple blog generator made using Langchain, Gemini LLM &amp; Serper API

# AI-Powered Blog Generator 🤖✍️

An intelligent blog post generator that leverages the power of Google's Gemini AI and web search capabilities to create well-researched, engaging blog content automatically.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🚀 Features

- Automated blog post generation with customizable topics
- AI-powered content creation using Google's Gemini API
- Web research integration using Serper API
- Keyword-focused content generation
- Structured output with introduction, body, and conclusion
- 300-400 word articles perfect for SEO
- Natural integration of researched information

## 📋 Prerequisites

Before running the project, make sure you have:

- Python 3.8 or higher
- Google Gemini API key
- Serper API key

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/abdullah-w-21/Simple-Blog-Generator.git
cd Simple-Blog-Generator
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
export GOOGLE_API_KEY="your-gemini-api-key"
export SERPER_API_KEY="your-serper-api-key"
```

## 📝 Usage

Here's a simple example of how to use the blog generator:

```python
from blog_generator import generate_blog

# Define your blog parameters
title = "The Future of Artificial Intelligence in Healthcare"
keywords = [
    "AI in healthcare",
    "medical diagnosis",
    "healthcare automation",
    "patient care",
    "medical technology"
]
points = [
    "Current applications of AI in healthcare",
    "Benefits of AI-powered medical diagnosis",
    "Challenges and limitations",
    "Future predictions and developments",
    "Impact on healthcare professionals"
]

# Generate the blog post
blog_post = generate_blog(title, keywords, points)
print(blog_post)
```

## 🔧 Configuration

The generator can be configured by modifying the following parameters:

- `temperature`: Controls creativity (default: 0.7)
- Blog post length: Adjustable in the `BLOG_TEMPLATE`
- Research depth: Modifiable in the `get_research_info` function

## 📚 API Reference

### `generate_blog(title: str, keywords: List[str], points: List[str]) -> str`

Generates a complete blog post based on the provided parameters.

**Parameters:**
- `title`: The main topic of the blog post
- `keywords`: List of relevant keywords for SEO
- `points`: Key points to be covered in the blog

**Returns:**
- A formatted blog post as a string

### `get_research_info(title: str, keywords: str) -> str`

Performs web research on the given topic.

**Parameters:**
- `title`: Topic to research
- `keywords`: Related keywords for search refinement

**Returns:**
- Compiled research information as a string


## 📄 Dependencies

- `langchain-google-genai`: Interface with Gemini AI
- `google-generativeai`: Google's Generative AI tools
- `langchain`: LLM chain operations
- Additional requirements in `requirements.txt`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 🙏 Acknowledgments

- Google Gemini AI for the powerful language model
- Serper API for web search capabilities
- LangChain for the excellent framework

## 📧 Contact

Abdullah Wasim - (https://pk.linkedin.com/in/abdullah-wasim-436a39253)

Project Link: (https://github.com/abdullah-w-21/Simple-Blog-Generator)

## ⚠️ Disclaimer

This tool uses AI to generate content. Always review and edit the generated content before publishing. The quality and accuracy of the output depend on the input parameters and available research data.
