\# LangChain Prompt Practice \& Research Tool



A Streamlit-based AI research and prompt experimentation tool built using \*\*LangChain\*\*, \*\*Hugging Face models\*\*, and \*\*Python\*\*. This project focuses on practicing prompt engineering, understanding LLM integrations, and building simple AI-powered web applications.



---



\## 🚀 Features



\* Interactive \*\*Streamlit UI\*\*

\* Prompt experimentation with LangChain

\* Text summarization using Hugging Face models

\* Secure handling of API keys using `.env`

\* Beginner-friendly and easy to extend



---



\## 🛠️ Tech Stack



\* \*\*Python 3.10+\*\*

\* \*\*LangChain\*\*

\* \*\*Hugging Face (transformers / inference)\*\*

\* \*\*Streamlit\*\*

\* \*\*Git \& GitHub\*\*



---



\## 📁 Project Structure



```

langchain\_prompt\_practice/

│

├── practice.py           # Core LangChain practice code

├── prompt\_ui.py          # Streamlit UI for prompt input

├── 1\_prompt\_ui.py        # Alternate UI experiment

├── hugging.py            # Hugging Face model testing

├── .gitignore            # Ignored files (env, venv, cache)

├── .env.example          # Environment variable template

└── README.md             # Project documentation

```



---



\## 🔐 Environment Variables



This project uses environment variables to keep API keys secure.



Create a `.env` file in the root directory:



```env

HUGGINGFACEHUB\_API\_TOKEN=your\_huggingface\_token\_here

```



⚠️ \*\*Important:\*\* Never upload your `.env` file to GitHub.



---



\## ▶️ How to Run the Project



\### 1️⃣ Clone the repository



```bash

git clone https://github.com/<your-username>/langchain\_prompt\_practice.git

cd langchain\_prompt\_practice

```



\### 2️⃣ Create virtual environment (recommended)



```bash

python -m venv venv

source venv/bin/activate   # On Windows: venv\\Scripts\\activate

```



\### 3️⃣ Install dependencies



```bash

pip install -r requirements.txt

```



\### 4️⃣ Run Streamlit app



```bash

streamlit run prompt\_ui.py

```



---



\## 📌 Learning Outcomes



\* Understanding LangChain prompt workflows

\* Difference between Hugging Face local models vs hosted inference

\* Handling API keys securely in real projects

\* Debugging common LLM \& API errors (403, StopIteration)



---



\## 🧠 Author



\*\*Anshan Singh\*\*

B.Com Graduate | Python Full Stack | AI \& LangChain Learner



---



\## ⭐ Future Improvements



\* Add chat-style interface

\* Support multiple models

\* Deploy on Streamlit Cloud

\* Add logging and error handling



---



⭐ If you found this project useful, give it a star on GitHub!



