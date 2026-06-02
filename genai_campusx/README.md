
# Generative AI using LangChain

## 01. Intro to GenAI (50:14)

### Generative AI is a type of artificial intelligence that creates new content - such as text, images, music or code - by learning patterns from existing data, mimicking human creativity.

### GenAI Impact Areas
1. Customer Support
2. Content Creation
3. Education
4. Software Development

### Is GenAI successful?
- Does it solve real world problems?
- Is it useful on a daily basis?
- Is it impacting the world economics?
- Is it creating new jobs?
- Is it accessible?

---

## ✅ Important Pointers (Key Takeaways)

1. **GenAI is evolving extremely fast** – new models, tools, research papers every day.
2. **Traditional AI** (Machine Learning) was good at prediction, **not creation**.
3. **GenAI’s superpower** – it can create new text, images, videos, music, and code.
4. **GenAI is already successful** – solving real-world problems, creating jobs, impacting economies.
5. **Central concept of GenAI** = **Foundation Models** (like LLMs).
6. **Two main activities in GenAI**:
   - **Use** existing Foundation Models
   - **Build** new Foundation Models
7. **Builder side** = harder, needs ML/DL knowledge.
8. **User side** = easier, needs basic software dev skills.
9. **Best to learn both sides** to become an AI Engineer.

---

## 📚 Important Concepts Explained (with Basic Examples)

### 1. What is Generative AI?
> **Definition:** A type of AI that creates **new content** (text, images, music, code) by learning patterns from existing data.

**Simple Example:**  
You show an AI 1000 cat photos. Later, you ask it – *“Draw a cat wearing a hat”*. It creates a **new image** that never existed before. That’s Generative AI.

---

### 2. Traditional AI (Machine Learning) vs Generative AI

| Traditional ML | Generative AI |
|----------------|----------------|
| Predicts numbers or categories | Creates new content |
| Example: Predict tomorrow’s stock price | Example: Write a poem about stock market |
| Example: Is this a cat or dog? | Example: Generate a new cat image |

---

### 3. Foundation Models
> **Definition:** Very large AI models trained on **massive amounts of data** (almost entire internet). They are **generalized**, not specialized.

**Example:**  
- **GPT-4**, **Llama**, **Gemini** are foundation models.
- A foundation model can: write an essay, summarize a book, answer questions, translate languages – **all with one model**.

**Comparison:**  
- Old ML model: trained only to detect spam emails → can’t write poetry.  
- Foundation model: trained on everything → can do many tasks.

---

### 4. Builder’s Perspective (Making Foundation Models)
> **Who does this?** Research scientists, data scientists, big companies (OpenAI, Google, Meta).

**Steps to build a foundation model:**
1. **Transformer Architecture** – the brain behind modern GenAI.
2. **Types of Transformers** – Encoder-only, Decoder-only, Encoder-Decoder.
3. **Pre-training** – Train model on huge data (internet scale).
4. **Optimization** – Make model smaller/faster (quantization, distillation).
5. **Fine-tuning** – Adapt model for specific tasks.
6. **Evaluation** – Test performance.
7. **Deployment** – Put model online for others to use.

**Simple Example:**  
Building a foundation model = Building a **car engine from scratch**. You need advanced engineering, materials, tools.

---

### 5. User’s Perspective (Using Foundation Models)
> **Who does this?** Software developers, AI engineers, app builders.

**Steps to use foundation models:**
1. **Basic Apps** – Call model via API or run locally.
2. **Prompt Engineering** – Write better inputs to get better outputs.
3. **RAG (Retrieval-Augmented Generation)** – Give private data to model for Q&A.
4. **Fine-tuning** – Lightweight adaptation of existing model.
5. **AI Agents** – Model that can take actions (book tickets, send emails).
6. **LLMOps** – Deploy and monitor LLM-based apps.
7. **Multimodal** – Handle images, audio, video.

**Simple Example:**  
Using a foundation model = **Driving a car**. You don’t need to know how the engine works. Just learn steering, brakes, accelerator.

---

### 6. Prompt Engineering
> **Definition:** The art of writing better inputs (prompts) to get better answers from an LLM.

**Bad prompt:** *“Tell me about India”*  
→ Answer: too broad, long, unfocused.

**Good prompt:** *“List top 5 tourist places in India with one-line description each.”*  
→ Answer: precise, short, useful.

---

### 7. RAG (Retrieval-Augmented Generation)
> **Definition:** Give private/external documents to an LLM so it can answer questions based on **your data**.

**Example:**  
You have 100 company policy PDFs. You ask ChatGPT: *“How many paid leaves do I get?”*  
Without RAG → ChatGPT doesn’t know.  
With RAG → It first searches your PDFs, finds the answer, then replies correctly.

---

### 8. AI Agents
> **Definition:** An LLM that can not only chat but also **take actions** (use tools, call APIs).

**Example:**  
You say: *“Book a hotel in Goa for next Friday.”*  
- Normal chatbot: suggests hotels.  
- AI Agent: actually books the hotel for you.

---

### 9. Fine-tuning
> **Definition:** Taking a pre-trained foundation model and training it a **little more** on specific data to improve performance on a specific task.

**Example:**  
General GPT-4 is okay at legal advice. You fine-tune it with 10,000 legal documents → now it’s excellent at legal Q&A.

---

### 10. Transformer Architecture (Simplified)
> **Definition:** The neural network design that made modern GenAI possible. It uses **self-attention** to understand relationships between words.

**Super simple example:**  
Sentence: *“She gave him her book”*  
Transformer understands that “her” refers to “She”, not someone else. It pays **attention** to relevant words.

---

## 02. Intro to GenAI (contd..) (15:18)

## Important Pointers (Key Takeaways)

1. **LangChain** is the first topic in the **User Side** of GenAI curriculum.
2. **User Side** = using existing Foundation Models (like GPT, Llama) to build applications.
3. **Builder Side** = building Foundation Models from scratch (will be covered later).
4. LangChain is an **open-source framework** to build LLM-powered applications.
5. LangChain supports **almost all LLMs** (OpenAI, Anthropic, Google, open-source models).
6. LangChain simplifies building **chatbots, RAG apps, AI agents, and more**.
7. It provides **modular components** and **integrations** with databases, APIs, deployment tools.
8. LangChain is **free** and actively developed (already 3 major versions).

---

## 📚 Important Concepts Explained (with Basic Examples)

### 1. What is LangChain?
> **Definition:** An open-source framework that helps developers build applications powered by Large Language Models (LLMs).

**Simple Example:**  
You want to build a chatbot that answers questions about your company’s policies.  
- Without LangChain: You write hundreds of lines of code to connect to GPT, manage memory, handle file uploads, etc.  
- With LangChain: You use pre-built components like `DocumentLoader`, `ChatModel`, `ConversationBufferMemory` – and build it in **minutes**.

---

### 2. Why is LangChain So Popular? (5 Key Features)

| Feature | What it means | Simple Example |
|---------|---------------|----------------|
| **Supports all major LLMs** | Works with OpenAI, Anthropic, Google, open-source models | You can switch from GPT-4 to Llama 3 by changing **one line of code** |
| **Simplifies development** | Provides ready-made components (Chains, Prompts, Output Parsers) | Building a multi-step reasoning app becomes easy |
| **Many integrations** | Connects to databases, APIs, vector stores, deployment tools | Connect to Pinecone (vector DB) in 3 lines of code |
| **Free & open-source** | No cost, actively maintained | You can use it commercially without paying |
| **Supports all use cases** | Chatbots, RAG, Agents, Summarization, Q&A | One framework for almost any LLM app |

---

### 3. LangChain Components (High-Level)

LangChain has modular building blocks. Think of them like **LEGO bricks**:

| Component | Purpose | Example |
|-----------|---------|---------|
| **Models** | Interface to LLMs | `ChatOpenAI(model="gpt-4")` |
| **Prompts** | Templates for inputs | “Summarize this: {text}” |
| **Chains** | Sequence of steps | Load doc → Split → Embed → Search → Answer |
| **Memory** | Remember conversation history | Chatbot remembers what you said 5 messages ago |
| **Retrievers** | Fetch relevant documents | Search vector database for similar content |
| **Tools** | Let LLM take actions | Search web, send email, book calendar |
| **Agents** | LLM that decides which tools to use | User: “Book a flight” → Agent calls flight API |

---

### 4. RAG (Retrieval-Augmented Generation) with LangChain

> **Definition:** Giving private data to an LLM so it can answer questions based on **your documents**.

**Simple Example without RAG:**  
You ask ChatGPT: *“What is our company’s leave policy?”*  
→ ChatGPT: “I don’t know, I wasn’t trained on your company data.”

**Simple Example with RAG (using LangChain):**  
1. Load your HR policy PDF  
2. Split into chunks  
3. Create embeddings (numerical representations)  
4. Store in vector database  
5. User asks question → LangChain retrieves relevant chunks → Sends to LLM with context → LLM answers correctly  

**LangChain makes this easy with:** `DocumentLoaders` → `TextSplitters` → `Embeddings` → `VectorStores` → `Retrievers`

---

### 5. AI Agents with LangChain

> **Definition:** An LLM that can not only chat but also **take actions** using tools.

**Simple Example:**  
You say: *“What’s the weather in Mumbai? If it’s sunny, book a hotel for me.”*  
- Normal chatbot: Only tells weather.  
- **AI Agent**: Calls weather API → reads result → calls hotel booking API → confirms booking.

**LangChain provides:** `Tools`, `ToolKits`, `AgentExecutor`

---

### 6. Chains in LangChain

> **Definition:** A sequence of steps where output of one step becomes input to the next.

**Simple Example Chain:**  
Step 1: Translate English to Hindi  
Step 2: Summarize the Hindi text  
Step 3: Check sentiment of summary  

**Without LangChain:** You write separate API calls and glue code.  
**With LangChain:** Use `LLMChain`, `SimpleSequentialChain`, or `RouterChain`.

---

### 7. Prompt Engineering (within LangChain)

> **Definition:** Writing better inputs (prompts) to get better outputs from LLMs.

**Without Prompt Engineering:**  
Prompt: *“Tell me about AI”* → Answer is too broad.

**With Prompt Engineering (LangChain `PromptTemplate`):**  
```python
template = "Explain {concept} to a 5-year-old in 2 sentences."
prompt = PromptTemplate(template=template, input_variables=["concept"])
```
Call with: `prompt.format(concept="Generative AI")`  
→ Output is focused, simple, and useful.

---

### 8. Why LangChain FIRST in the User Side?

| Benefit | Explanation |
|---------|-------------|
| **Holistic view** | LangChain touches almost every User Side topic (prompts, RAG, agents, memory, output parsing) |
| **Learn by doing** | You build real apps while learning concepts |
| **Smooth transition** | After LangChain, deep-diving into individual topics (pure Prompt Engineering, advanced RAG) becomes easier |
| **Conceptual clarity** | LangChain’s abstractions (Runnable, Chain, etc.) help you understand LLM app architecture |

**Think of it like this:**  
Learning LangChain first = learning to drive a car before learning how the engine works. You get practical skills fast, then go deeper later.

---

## 📅 LangChain Playlist Curriculum (3 Parts)

### Part 1: Fundamentals (~7 videos)
- What is LangChain & why needed
- All components overview
- Working with Models (GPT, Llama, etc.)
- Prompts & PromptTemplates
- Output Parsing
- Runnable & LCEL (LangChain Expression Language)
- Chains
- Memory in chatbots

### Part 2: RAG Applications
- Document Loaders (PDF, websites, YouTube, etc.)
- Text Splitters (how to chunk documents)
- Embeddings & Vector Databases
- Retrievers
- **Build a complete RAG app from scratch**

### Part 3: AI Agents
- Tools & ToolKits
- Tool Calling
- **Build an AI Agent from scratch**

**Total videos:** ~17  
**Total time to complete:** ~2 months (2 videos/week)

---

## 🙌 Final Takeaway

> LangChain is the **best starting point** for the User Side of Generative AI.  
> It gives you a **holistic view**, lets you **build real apps quickly**, and makes learning other topics (prompt engineering, RAG, agents) much easier.  
> The playlist is **free, practical, and concept-focused** – not just code copying.

**Start with LangChain → Build real LLM apps → Then go deeper into each topic.**

---

## 03. Introduction to LangChain (37:43)

## ✅ Important Pointers (Key Takeaways)

1. **LangChain** = framework to build apps powered by LLMs (chatbots, agents, RAG, etc.)
2. **Main problem it solves** – orchestrating many moving parts (document loading, splitting, embeddings, vector DB, LLM calls)
3. **Without LangChain** – you’d write hundreds of lines of glue code, handle integrations manually
4. **With LangChain** – plug-and-play components, easy switching between models, built-in memory and chains
5. **Core architecture explained** – PDF → load → split → embed → store → retrieve similar chunks → LLM answers
6. **Two big challenges** (solved by LLMs + APIs):
   - Natural language understanding & generation → solved by LLM (GPT, Llama)
   - Running heavy models → solved by LLM APIs (OpenAI, Anthropic)
7. **Third challenge (orchestration)** – solved by **LangChain**
8. **Key benefits**:
   - **Chains** – pipeline tasks automatically
   - **Model-agnostic** – switch between GPT, Claude, Llama with 1 line change
   - **Full ecosystem** – 50+ document loaders, text splitters, vector stores
   - **Memory** – conversation history management
9. **Popular use cases**:
   - Conversational chatbots (customer support)
   - AI knowledge assistants (chat with your docs)
   - AI agents (take actions – book flights, send emails)
   - Summarization & research helpers
10. **Alternatives** – LlamaIndex, Haystack

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. What is LangChain?
> **Definition:** An open-source framework that helps you build applications powered by LLMs.

**Basic Code Example – Creating a simple LLM call:**
```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model="gpt-3.5-turbo")
response = llm.invoke([HumanMessage(content="Explain AI in one sentence")])
print(response.content)
# Output: "AI is the simulation of human intelligence in machines."
```

---

### 2. Why Need LangChain? (The Orchestration Problem)

**Problem:** Building a PDF Q&A app requires:
- Load PDF
- Split text into chunks
- Generate embeddings
- Store in vector database
- Retrieve relevant chunks for a query
- Send chunks + query to LLM
- Return answer

**Without LangChain** – you manually write code for each step, handle API differences, manage state.

**With LangChain** – you chain components together.

**Code Example – Simple chain (pseudo):**
```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Load PDF
loader = PyPDFLoader("book.pdf")
documents = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
docs = text_splitter.split_documents(documents)

# Create embeddings & store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

# Create retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever()
)

# Ask question
answer = qa_chain.invoke("What are the advantages of linear regression?")
print(answer)
```

---

### 3. Semantic Search vs Keyword Search

| Keyword Search | Semantic Search |
|----------------|------------------|
| Matches exact words | Matches meaning |
| Example: search "advantages" → returns every page with "advantages" | Understands "advantages" = "benefits", "pros" |
| Less relevant results | More relevant results |

**How it works (embeddings + similarity):**
```python
# Conceptual code
from langchain.embeddings import OpenAIEmbeddings

embedder = OpenAIEmbeddings()
query = "What are the advantages of linear regression?"
query_embedding = embedder.embed_query(query)

# Compare with document embeddings (vector DB)
similar_docs = vectorstore.similarity_search(query_embedding, k=3)
# returns top 3 most similar text chunks
```

---

### 4. Embeddings & Vector Databases

**Embedding** = converting text into a list of numbers (vector) that captures its meaning.

**Vector Database** = stores these vectors for fast similarity search.

**Code Example:**
```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

embeddings = OpenAIEmbeddings()
texts = ["Linear regression predicts numbers.", "Logistic regression classifies categories."]

# Create vector store
vectorstore = FAISS.from_texts(texts, embeddings)

# Search
results = vectorstore.similarity_search("prediction model")
# Returns first text (about linear regression)
```

---

### 5. RAG (Retrieval-Augmented Generation)

**Definition:** Retrieve relevant documents from a knowledge base, then ask the LLM to answer based on those documents.

**Why needed:** LLMs don't know your private data. RAG gives them that context.

**Code Example (complete RAG pipeline with LangChain):**
```python
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# 1. Load
loader = TextLoader("company_policy.txt")
documents = loader.load()

# 2. Split
splitter = CharacterTextSplitter(chunk_size=500)
docs = splitter.split_documents(documents)

# 3. Embed & store
embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(docs, embeddings)

# 4. Retrieve & answer
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectordb.as_retriever()
)
answer = qa.invoke("How many paid leaves do I get?")
# LLM answers based on the retrieved policy chunks
```

---

### 6. LangChain Chains

**Definition:** Sequence components where output of one becomes input of the next.

**Code Example – Simple Sequential Chain:**
```python
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI()

# Chain 1: Translate to Hindi
prompt1 = PromptTemplate(input_variables=["text"], template="Translate to Hindi: {text}")
chain1 = LLMChain(llm=llm, prompt=prompt1)

# Chain 2: Summarize
prompt2 = PromptTemplate(input_variables=["hindi_text"], template="Summarize in 2 lines: {hindi_text}")
chain2 = LLMChain(llm=llm, prompt=prompt2)

# Combine
overall_chain = SimpleSequentialChain(chains=[chain1, chain2])
result = overall_chain.invoke("Artificial intelligence is changing the world.")
# Output: Hindi translation → then summary of that Hindi text
```

---

### 7. Model-Agnostic Development

**Definition:** Switch between LLM providers without changing your core logic.

**Code Example:**
```python
# Same code, different models
from langchain.chat_models import ChatOpenAI, ChatAnthropic

# Using OpenAI
llm_openai = ChatOpenAI(model="gpt-4")
response1 = llm_openai.invoke("Hello")

# Switch to Anthropic's Claude – just change the import/instance
llm_claude = ChatAnthropic(model="claude-3")
response2 = llm_claude.invoke("Hello")

# Your chain logic remains identical
```

---

### 8. Memory in LangChain

**Definition:** Keep conversation history so the LLM remembers what was said earlier.

**Code Example:**
```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=ChatOpenAI(),
    memory=memory
)

# First turn
conversation.invoke("What are the advantages of linear regression?")
# LLM answers

# Second turn – no need to repeat topic
response = conversation.invoke("Also give me interview questions on this algorithm")
# LLM understands "this algorithm" = linear regression
```

---

### 9. AI Agents (Chatbots on Steroids)

**Definition:** LLM that not only chats but also **takes actions** using tools (APIs, databases, web search).

**Code Example (conceptual):**
```python
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

# Define tools
def search_web(query):
    return f"Search results for {query}"

def book_hotel(destination):
    return f"Hotel booked in {destination}"

tools = [
    Tool(name="WebSearch", func=search_web, description="Search the internet"),
    Tool(name="HotelBooking", func=book_hotel, description="Book a hotel")
]

agent = initialize_agent(tools, ChatOpenAI(), agent="zero-shot-react-description")

# User says: "Book a hotel in Goa"
response = agent.invoke("Book a hotel in Goa")
# Agent decides: needs to call HotelBooking tool with "Goa"
```

---

### 10. What You Can Build with LangChain

| Use Case | Example | Why LangChain? |
|----------|---------|----------------|
| **Chatbots** | Customer support bot | Memory, easy LLM switching |
| **Knowledge Assistant** | Chat with your PDFs | RAG pipelines, document loaders |
| **AI Agents** | Travel booking agent | Tools, toolkits, decision making |
| **Summarization** | Research paper summarizer | Chain long docs, handle context limits |

---

## 🔁 Alternatives to LangChain

| Framework | Key Feature |
|-----------|-------------|
| **LangChain** | Most popular, huge ecosystem |
| **LlamaIndex** | Specialized for RAG & data indexing |
| **Haystack** | Production-focused NLP pipelines |

---

> **Final takeaway:** LangChain saves you from writing boilerplate orchestration code. You focus on your idea, not on gluing APIs together.

### Different components in GenAI ecosystem
- Cloud Service (AWS / Azure / GCP)
- Text Splittters
- Embedding models
- Vector DB
- LLM

### Different tasks performed in GenAI ecosystem
- Document loading,
- Text splitting
- Creating embeddings
- Managing vector db,
- Retrieval

### How Semantic Search Work? Explain with basic examples

### First, The Problem with Old-School "Keyword Search"

To understand semantic search, you first need to see what it improves upon.

**Keyword Search** (like `Ctrl+F` or a basic database search) works by **literally matching characters**.
- You type `"how to fix a car"`.
- The search engine looks for documents containing the exact words `"how"`, `"to"`, `"fix"`, `"a"`, `"car"`.

**It fails when:**
- **Synonyms are used:** A document says *"repair an automobile"* (no match).
- **Different phrasing:** A document says *"car fixing guide"* (partial match, but low score).
- **Context matters:** The word "apple" (fruit vs. company).

**Result:** Keyword search is brittle. It speaks only **word-for-word**, not **meaning-for-meaning**.

### The Solution: How Semantic Search Works

Semantic search aims to understand **the intent** and **contextual meaning** behind your query, not just the letters.

The core magic trick is **Converting words into numbers (Vectors/Embeddings).**

Imagine you have a giant 3D map. Every word, sentence, or document gets plotted as a **point** on this map. The key rule is:

> **Words with similar meanings are placed close together.**

- `"Happy"`, `"Joyful"`, `"Cheerful"` are all neighbors in one cluster.
- `"Car"`, `"Automobile"`, `"Vehicle"` are neighbors in another cluster.
- `"Sad"` and `"Depressed"` are in a third cluster, far from the "Happy" cluster.

When you search, the engine:
1.  Turns your query into a point on this map.
2.  Finds **all other points (documents)** that are closest to your query's point.
3.  Returns those documents, even if they use **zero** of your original keywords.

---

### Basic Example 1: The Synonym Problem

**Your Search Query:** `"How to fix a car?"`

| Document | Keyword Search (Old) | Semantic Search (New) |
| :--- | :--- | :--- |
| Doc A: "Steps to **fix a car**" | ✅ Perfect match (100%) | ✅ Great match (100%) |
| Doc B: "Guide to **repair an automobile**" | ❌ Zero matches (0%) - No `fix`, no `car`. | ✅ Excellent match (95%) - Understands `repair` = `fix` and `automobile` = `car`. |

**How it works:** Semantic search has learned that the vector for `"fix"` is very close to the vector for `"repair"`, and `"car"` is close to `"automobile"`. So Doc B is "geographically" near your query on the meaning-map.

### Basic Example 2: The Context & Intent Problem

**Your Search Query:** `"How does learning multiple languages affect a child's brain?"`

A keyword search will hunt for those exact words. It might miss a fantastic article that is phrased differently.

**A perfect semantic match (no keywords matched!):**
> *"This study explores the **cognitive impact** of **bilingualism** on **young minds**, specifically looking at **memory retention and problem-solving skills**."*

**Why semantic search finds it:**
- It understands `"multiple languages"` = `"bilingualism"`
- `"child"` = `"young mind"`
- `"affect the brain"` = `"cognitive impact"`

The search engine doesn't see different words. It sees **the same meaning** expressed differently.

### Simple Example 3: Beyond Single Words (Sentence Meaning)

Consider this classic example:

**Query:** `"A tall man who eats a lot of pasta."`

**A potential match:** *"The skinny teenager loves Italian food, especially spaghetti and meatballs."*

At a word level, there are almost no matches (`"pasta"` vs `"spaghetti"`). But semantically:
- The system understands that `"tall"` and `"skinny"` are both physical descriptions.
- `"eats a lot of"` = `"loves food"`
- `"pasta"` = `"Italian food" / "spaghetti"`
- The *topic* of the sentence is the same: *describing a person's physical trait and their eating habits.*

### Summary Table: Keyword vs. Semantic

| Feature | Keyword Search | Semantic Search |
| :--- | :--- | :--- |
| **Matching Logic** | Exact text strings | Meaning, intent, and concepts |
| **Handles Synonyms?** | ❌ No | ✅ Yes |
| **Handles Typos?** | Only if identical | Often yes (via vector proximity) |
| **Needs exact phrasing?** | Yes, rigid | No, flexible |
| **Example** | `Ctrl+F` in a PDF | Google. Ask "best car" and get results for "top automobiles" |

### How Does It Learn This "Meaning"?

Semantic search is powered by **Machine Learning models** (like BERT, SBERT, or GPT).
- You feed the model millions of sentences and their contexts.
- It learns to predict which words replace which (synonyms).
- It learns that words appearing together frequently (`"peanut butter"` and `"jelly"`) are related.
- The final output is a **vector** (a long list of numbers, e.g., `[0.23, -0.45, 0.81, ...]`) that uniquely represents the *meaning* of that sentence.

**In short: Semantic search translates human language into math (vectors) and then finds the closest matches mathematically.**

---

## 04. LangChain Components (53:23)

## 🧑‍🏫 What This Video Covers

Nitesh explains the **six core components** of LangChain:
1. **Models** – Standardized interface to AI models (LLMs & Embedding models)
2. **Prompts** – Dynamic, reusable, and role-based input templates
3. **Chains** – Pipelines where output of one step auto-becomes input of next
4. **Indexes** – Connect LLM to external knowledge (PDFs, websites, databases)
5. **Memory** – Give conversation memory to stateful LLM apps
6. **Agents** – LLM with reasoning + tools to take actions

---

## ✅ Important Pointers (Key Takeaways)

1. **Problem #1 (Solved by Models component)** – Different LLM providers have different APIs. Switching from OpenAI to Claude requires rewriting code. LangChain gives a **standard interface** – change just 1-2 lines to switch models.
2. **Problem #2 (Solved by Prompts)** – LLM outputs are very sensitive to input phrasing. LangChain provides **dynamic templates, role-based prompts, and few-shot examples**.
3. **Problem #3 (Solved by Chains)** – Building multi-step pipelines manually is tedious. Chains auto-pipe outputs to next steps.
4. **Problem #4 (Solved by Indexes)** – LLMs don’t know your private data. Indexes help load, split, embed, store, and retrieve from external sources (RAG).
5. **Problem #5 (Solved by Memory)** – LLM API calls are **stateless** – each request is independent. Memory adds conversation history.
6. **Problem #6 (Solved by Agents)** – Chatbots can’t take actions. Agents have **reasoning** + **tools** (APIs, calculators) to act.
7. LangChain supports **two model types**: Language models (text↔text) and Embedding models (text→vector).
8. **Chains** can be sequential, parallel, or conditional.
9. **Indexes** internally use: Document Loaders → Text Splitters → Vector Stores → Retrievers.
10. **Memory types**: ConversationBuffer (full history), BufferWindow (last N turns), Summary-based, Custom.

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. Models Component

**Why needed?** Each LLM provider has its own API. LangChain standardizes interaction.

**Code Example – Switching from OpenAI to Claude with minimal changes:**
```python
# Using OpenAI
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo")
response = llm.invoke("Explain AI")

# Switch to Anthropic's Claude – only 2 lines change
from langchain.chat_models import ChatAnthropic
llm = ChatAnthropic(model="claude-3-sonnet-20240229")
response = llm.invoke("Explain AI")   # Same invocation!
```

**Two types of models in LangChain:**
- **Language models** (text in → text out) – for chatbots, agents, summarization
- **Embedding models** (text in → vector out) – for semantic search

---

### 2. Prompts Component

**Why needed?** LLM outputs are sensitive to wording. Prompts should be dynamic, reusable, and structured.

**Example 1 – Dynamic prompt with placeholders:**
```python
from langchain.prompts import PromptTemplate

template = "Summarize the topic '{topic}' in a {tone} tone."
dynamic_prompt = PromptTemplate(
    input_variables=["topic", "tone"],
    template=template
)

# User says: topic = "cricket", tone = "fun"
final_prompt = dynamic_prompt.format(topic="cricket", tone="fun")
# Output: "Summarize the topic 'cricket' in a fun tone."
```

**Example 2 – Role-based (system + user) prompt:**
```python
from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are an experienced {profession}."),
    ("user", "Tell me about {topic}.")
])

prompt = template.format_messages(profession="doctor", topic="viral fever")
```

**Example 3 – Few-shot prompt (give examples before asking):**
```python
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {"query": "I was charged twice", "category": "Billing Issue"},
    {"query": "App crashes on login", "category": "Technical Problem"},
]

example_template = PromptTemplate(
    input_variables=["query", "category"],
    template="Query: {query}\nCategory: {category}"
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_template,
    prefix="Classify the following customer ticket:",
    suffix="Query: {input}\nCategory:",
    input_variables=["input"]
)
```

---

### 3. Chains Component

**Why needed?** Automatically connect multiple steps – output of step 1 becomes input of step 2.

**Example – Sequential chain (translate English → Hindi → summarize in <100 words):**
```python
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI()

# Step 1: Translate to Hindi
translate_prompt = PromptTemplate(
    input_variables=["text"],
    template="Translate to Hindi: {text}"
)
translate_chain = LLMChain(llm=llm, prompt=translate_prompt)

# Step 2: Summarize Hindi text
summarize_prompt = PromptTemplate(
    input_variables=["hindi_text"],
    template="Summarize in under 100 words in Hindi: {hindi_text}"
)
summarize_chain = LLMChain(llm=llm, prompt=summarize_prompt)

# Combine into one chain
pipeline = SimpleSequentialChain(chains=[translate_chain, summarize_chain])
result = pipeline.run("Artificial intelligence is changing the world.")
# Behind the scenes: translate → output becomes input of summarizer → final result
```

**Parallel chain example (multiple reports combined):**
```python
from langchain.chains import ParallelChain

# Two chains processing same input simultaneously
chain1 = LLMChain(...)  # generates report from perspective A
chain2 = LLMChain(...)  # generates report from perspective B
combine_chain = LLMChain(...)  # combines both reports

parallel = ParallelChain(chains=[chain1, chain2], combine_chain=combine_chain)
```

**Conditional chain (decide based on sentiment):**
```python
# If feedback positive → thank you; if negative → email support
# (Conceptual – uses RouterChain)
```

---

### 4. Indexes Component

**Why needed?** LLMs don’t know your private company data. Indexes connect LLM to external knowledge (PDFs, websites, DBs).

**Four sub-components of Indexes:**

| Component | Purpose | Example |
|-----------|---------|---------|
| **Document Loader** | Load data from source | `PyPDFLoader`, `WebBaseLoader` |
| **Text Splitter** | Chunk into small pieces | `RecursiveCharacterTextSplitter` |
| **Vector Store** | Store embeddings (vectors) | `FAISS`, `Chroma`, `Pinecone` |
| **Retriever** | Search similar chunks | `vectorstore.as_retriever()` |

**Complete RAG (Retrieval-Augmented Generation) example with Indexes:**
```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# 1. Load external PDF
loader = PyPDFLoader("company_leave_policy.pdf")
documents = loader.load()

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# 3. Create embeddings & store in vector DB
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 4. Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 5. QA chain with external knowledge
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=retriever
)

answer = qa.invoke("What is the notice period policy?")
# LLM answers based on your private PDF, not just internet data
```

---

### 5. Memory Component

**Why needed?** LLM API calls are **stateless** – they don't remember previous questions.

**Problem without memory:**
```python
# First call
llm.invoke("Who is Narendra Modi?")  # Gets answer

# Second call – no memory of previous question
llm.invoke("How old is he?")  # Error: "I don't know who 'he' is"
```

**Solution – ConversationBufferMemory (stores full history):**
```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=ChatOpenAI(), memory=memory)

conversation.invoke("Who is Narendra Modi?")   # LLM answers
conversation.invoke("How old is he?")          # LLM remembers "he" = Modi
```

**Other memory types:**

| Memory Type | What it stores | When to use |
|-------------|----------------|--------------|
| `ConversationBufferMemory` | Full chat history | Short conversations |
| `ConversationBufferWindowMemory` | Last K messages | Long chats (saves cost) |
| `ConversationSummaryMemory` | Summarized history | Very long conversations |
| Custom memory | User preferences, facts | Specialized needs |

```python
# Buffer window memory – keep only last 5 exchanges
from langchain.memory import ConversationBufferWindowMemory
memory = ConversationBufferWindowMemory(k=5)
```

---

### 6. Agents Component

**Why needed?** Chatbots can only talk. Agents can **take actions** using tools (APIs, calculators, databases).

**Key differences:**
- **Chatbot**: "What's the best hill station?" → Answers "Shimla, Manali"
- **Agent**: Same question + "Book the cheapest flight from Delhi to Shimla on 24 Jan" → Calls flight API → books ticket

**How agents work:** Reasoning (break down problem) + Tools access

**Example – Agent with calculator and weather API tools:**
```python
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

# Define tools (simplified)
def weather_api(city):
    return f"Temperature in {city} is 25°C"

def calculator(expression):
    return str(eval(expression))   # unsafe, just for demo

tools = [
    Tool(name="Weather", func=weather_api, description="Get temperature of a city"),
    Tool(name="Calculator", func=calculator, description="Do math operations")
]

agent = initialize_agent(
    tools,
    ChatOpenAI(),
    agent="zero-shot-react-description",  # reasoning agent
    verbose=True
)

# User query: "Multiply today's Delhi temperature by 3"
response = agent.invoke("Multiply today's Delhi temperature by 3")
# Agent reasoning steps:
# 1. Need temperature of Delhi → calls Weather tool → gets 25
# 2. Need to multiply 25 * 3 → calls Calculator tool → gets 75
# 3. Returns 75
```

**Popular agent reasoning technique – Chain of Thought (CoT):**
- Breaks complex queries into step-by-step reasoning
- Example query: *"What is the average of highest temperature in Mumbai and lowest in Shimla?"*
- Agent internally: "Step1: get Mumbai highest temp; Step2: get Shimla lowest; Step3: calculate average"

---

## 🔁 Summary Table of Components

| Component | Core Problem Solved | Key Feature |
|-----------|---------------------|--------------|
| **Models** | Different LLM APIs | Standardized interface, model-agnostic |
| **Prompts** | Input sensitivity | Dynamic, reusable, few-shot templates |
| **Chains** | Manual pipeline coding | Auto output→input, complex flows |
| **Indexes** | LLM doesn't know private data | Document loading, splitting, embedding, retrieval |
| **Memory** | Stateless API calls | Conversation history, summaries |
| **Agents** | Chatbots can't act | Reasoning + tools access |

---

## 🗓️ Next Steps

- Future videos will deep-dive into each component with **practical projects**
- Start with **Models & Prompts** (easiest), then Chains, then Indexes (RAG), then Memory, then Agents

> **Final takeaway:** LangChain’s six components work together to let you build production-ready LLM applications without writing hundreds of lines of glue code. Learn them in order – Models → Prompts → Chains → Indexes → Memory → Agents.

---

### Different components of Langchain

1. Model

- [LangChain Model](https://docs.langchain.com/oss/python/langchain/models)

- [Chat Model](https://docs.langchain.com/oss/python/integrations/chat)

- [Embedding Model](https://docs.langchain.com/oss/python/integrations/embeddings)

2. Prompts

3. Chains

4. Indexes
- Document loaders
- Text splitters
- vector store
- Retrievers

5. Memory

6. Agents
- Reasoning capabilities
- Tool calling

---

## 05. LangChain Models (01:42:02)

## 🧑‍🏫 What This Video Covers

This lecture deep into the **Models component** of LangChain – the most important component. He explains:
- What are Models in LangChain (interface to AI models)
- Two types: **Language Models** (text ↔ text) and **Embedding Models** (text → vector)
- Language models further split into **LLMs** (older, general-purpose) and **Chat Models** (newer, conversation-focused)
- How to use **closed-source models** (OpenAI, Anthropic, Google)
- How to use **open-source models** (via Hugging Face API or locally)
- How to use **embedding models** for semantic search
- Build a **document similarity search app** from scratch

---

## ✅ Important Pointers (Key Takeaways)

1. **Models component** = a standardized interface to talk to any AI model (LLM or embedding model)
2. **Two model types:**
   - **Language models** – text in → text out (chatbots, agents, summarization)
   - **Embedding models** – text in → vector (numbers) out (semantic search, RAG)
3. **Language models → two sub-types:**
   - **LLMs** (e.g., `gpt-3.5-turbo-instruct`) – old, general purpose, being deprecated
   - **Chat Models** (e.g., `gpt-4`, `claude`, `gemini`) – newer, support conversation history, roles, recommended
4. **Key parameters for chat models:**
   - `temperature` – controls creativity (0 = deterministic, 1.5 = creative)
   - `max_tokens` – limits output length (saves cost)
5. **Closed-source models** – paid APIs (OpenAI, Anthropic, Google). LangChain gives a consistent interface – swap models with minimal code changes.
6. **Open-source models** – free, downloadable from Hugging Face. You can run them locally (need good GPU/CPU) or via Hugging Face Inference API (free tier available).
7. **Embedding models** convert text to vectors. Use `embed_query()` for a single text, `embed_documents()` for multiple.
8. **Cosine similarity** measures how similar two vectors are – used to find which document best matches a query.
9. **Setup:** create virtual env, install `langchain`, `langchain-openai`, `langchain-anthropic`, `langchain-google-genai`, `langchain-huggingface`, `python-dotenv`, `scikit-learn`, `numpy`.
10. **Always store API keys in `.env` file** (never hardcode).

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. What Are Models in LangChain?

> **Definition:** The Models component is an interface that lets you interact with different AI models (language or embedding) in a standardized way – same code pattern for OpenAI, Anthropic, or open-source models.

**Why needed?** Each LLM provider has a different API. LangChain standardizes it.

---

### 2. Language Models: LLMs vs Chat Models

| Feature | LLM (Old) | Chat Model (New) |
|---------|-----------|------------------|
| Input | Single string | List of messages (system, user, AI) |
| Output | Single string | Message object with content + metadata |
| Memory | No | Supports conversation history |
| Roles | No | Yes (system, user, assistant) |
| Recommendation | Deprecated | Use this |

**LLM example (not recommended for new projects):**
```python
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(model="gpt-3.5-turbo-instruct")
result = llm.invoke("What is the capital of India?")
print(result)  # "New Delhi"
```

**Chat Model example (recommended):**
```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4")
response = model.invoke("What is the capital of India?")
print(response.content)  # "The capital of India is New Delhi."
```

---

### 3. Chat Model Parameters: Temperature & Max Tokens

**Temperature** – controls randomness/creativity:
- 0.0 – deterministic, factual answers (good for code, math)
- 0.5–0.7 – balanced
- 1.0–1.5 – creative, varied (good for stories, jokes)

**Max tokens** – limits output length (saves money).

```python
model = ChatOpenAI(
    model="gpt-4",
    temperature=0.0,      # factual
    max_tokens=50          # short answer
)
```

---

### 4. Using Different Closed-Source Models (OpenAI, Anthropic, Google)

**OpenAI (GPT-4):**
```python
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4")
```

**Anthropic (Claude):** (need `ANTHROPIC_API_KEY` in `.env`)
```python
from langchain_anthropic import ChatAnthropic
model = ChatAnthropic(model="claude-3-sonnet-20240229")
```

**Google (Gemini):** (need `GOOGLE_API_KEY` in `.env`)
```python
from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
```

**Notice:** The `invoke()` method and response structure are the same across all – only the import and model name change.

---

### 5. Open-Source Models via Hugging Face

**Two ways to use open-source models:**

#### A. Via Hugging Face Inference API (free tier, runs on HF servers)
```python
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()  # needs HUGGINGFACEHUB_ACCESS_TOKEN

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
response = model.invoke("What is the capital of India?")
print(response.content)
```

#### B. Locally downloaded (runs on your machine – needs good hardware)
```python
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100, "temperature": 0.5}
)
model = ChatHuggingFace(llm=llm)
response = model.invoke("What is the capital of India?")
print(response.content)
```

**Note:** First run downloads the model (~500MB). Local inference is slower on CPU.

---

### 6. Embedding Models

**What they do:** Convert text into a vector (list of numbers) that captures meaning.

**Why useful:** To perform semantic search – find text that is *similar in meaning*, not just keywords.

**Using OpenAI Embeddings (closed-source):**
```python
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=300       # vector size (can be up to 3072)
)

# Single text
vector = embeddings.embed_query("Delhi is the capital of India")
print(len(vector))      # 300

# Multiple documents
docs = [
    "Delhi is capital of India",
    "Kolkata is capital of West Bengal",
    "Paris is capital of France"
]
vectors = embeddings.embed_documents(docs)
print(len(vectors))     # 3
print(len(vectors[0]))  # 300
```

**Using open-source embeddings (HuggingFace, locally):**
```python
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"  # 384-dim vectors
)
vector = embeddings.embed_query("Delhi is the capital of India")
print(len(vector))  # 384
```

---

### 7. Document Similarity Search (Complete Example)

**Goal:** Given a set of documents and a user query, find which document is most semantically similar to the query.

**How it works:**
1. Generate embeddings for all documents (vectors)
2. Generate embedding for the query
3. Compute cosine similarity between query vector and each document vector
4. Return the document with highest similarity score

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Step 1: Documents
documents = [
    "Virat Kohli is an Indian cricketer known for aggressive batting.",
    "Jasprit Bumrah is an Indian fast bowler with a unique action.",
    "Rohit Sharma holds the record for highest ODI score of 264.",
    "MS Dhoni is famous for his captaincy and finishing skills.",
    "Sachin Tendulkar is the highest run-scorer in Test cricket."
]

# Step 2: User query
query = "Tell me about Virat Kohli"

# Step 3: Create embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)
doc_embeddings = embeddings.embed_documents(documents)   # list of 5 vectors
query_embedding = embeddings.embed_query(query)          # 1 vector

# Step 4: Compute cosine similarity (convert to 2D for sklearn)
query_2d = np.array(query_embedding).reshape(1, -1)
doc_2d = np.array(doc_embeddings)
scores = cosine_similarity(query_2d, doc_2d)[0]  # array of 5 similarity scores

# Step 5: Find best match
best_index = np.argmax(scores)
best_score = scores[best_index]
best_doc = documents[best_index]

print(f"Query: {query}")
print(f"Best match: {best_doc}")
print(f"Similarity score: {best_score:.2f}")
```

**Output:**
```
Query: Tell me about Virat Kohli
Best match: Virat Kohli is an Indian cricketer known for aggressive batting.
Similarity score: 0.66
```

> This is the core idea behind **RAG (Retrieval-Augmented Generation)** – you’d then feed the retrieved document to an LLM to answer the query.

---

## 🔁 Summary Table

| Concept | What it does | Code snippet |
|---------|--------------|---------------|
| **LLM (old)** | Text in → text out | `OpenAI(model="gpt-3.5-turbo-instruct")` |
| **Chat Model** | Messages in → message out | `ChatOpenAI(model="gpt-4")` |
| **Temperature** | Controls creativity | `temperature=0.7` |
| **Max tokens** | Limits output length | `max_tokens=100` |
| **Open-source (API)** | Free, runs on HF servers | `HuggingFaceEndpoint(repo_id="...")` |
| **Open-source (local)** | Runs on your machine | `HuggingFacePipeline.from_model_id(...)` |
| **Embeddings (closed)** | Text → vector | `OpenAIEmbeddings().embed_query("text")` |
| **Embeddings (open)** | Text → vector | `HuggingFaceEmbeddings(model_name="...")` |
| **Cosine similarity** | Measure vector similarity | `cosine_similarity(query_vec, doc_vecs)` |

---

> **Final takeaway:** The Models component is your gateway to all AI models in LangChain. Master the difference between LLMs and Chat Models, learn to switch between providers, and understand embeddings – they are the foundation of semantic search and RAG.

- [Hugging Face Models](https://huggingface.co/models)

---

## 06. Prompts in LangChain (01:18:32)

## 🧑‍🏫 What This Covers

It covers the **Prompts component** in LangChain – the second most important component after Models whcih contains:
- What prompts are (text input to LLM)
- **Static vs Dynamic prompts** – why dynamic is better
- **PromptTemplate** – creating reusable, dynamic single-message prompts
- **Saving & loading prompts** to JSON files for reusability
- Building a simple **chat bot** with conversation history
- **Message types** – SystemMessage, HumanMessage, AIMessage
- **ChatPromptTemplate** – dynamic prompts for multi-message conversations
- **MessagePlaceholder** – inserting chat history dynamically

---

## ✅ Important Pointers (Key Takeaways)

1. **Prompt** = the input message/text you send to an LLM. LLM outputs are very sensitive to prompts.
2. **Static prompts** – user types full prompt every time. Problem: inconsistent output, user can make mistakes, no control.
3. **Dynamic prompts** – you create a template with placeholders, user only provides values (e.g., paper name, style, length). Gives consistent experience.
4. **PromptTemplate** – LangChain class for dynamic single-message prompts. Provides validation, reusability, and integration with Chains.
5. **Why not just use f-strings?** PromptTemplate gives: (a) automatic validation of placeholders, (b) ability to save/load templates as JSON, (c) seamless integration with LangChain Chains.
6. **Chat bot with memory** – need to maintain chat history and send it back to LLM for context.
7. **Message types in LangChain:**
   - `SystemMessage` – sets assistant's role/behavior (start of conversation)
   - `HumanMessage` – user's input
   - `AIMessage` – assistant's response
8. **ChatPromptTemplate** – used when you need dynamic placeholders inside a list of messages (multi-turn conversations).
9. **MessagePlaceholder** – a special placeholder that injects an entire list of messages (e.g., previous chat history) at runtime.
10. **Temperature correction:** Temperature 0 = deterministic (same input → same output). Higher values = more creative/random outputs.

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. What is a Prompt?

> **Definition:** The text message you send to an LLM. It can be a simple question, a complex instruction, or include examples.

**Simple example (hardcoded static prompt):**
```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI()
response = model.invoke("What is the capital of India?")
print(response.content)
```

---

### 2. Static vs Dynamic Prompts

**Problem with static prompts:** User writes the whole prompt. If they misspell or write unclearly, output is bad. Also, you can't guarantee consistent style.

**Dynamic prompt approach:** Create a template with placeholders; user only fills specific values.

**Example – Research summarizer tool (conceptual UI):**
```python
# Template (pre-defined by developer)
template = """
Please summarize the research paper titled {paper_name} with the following specifications:
- Explanation style: {style}
- Explanation length: {length}
Include mathematical details if present. Use simple analogies.
"""

# User selects: paper_name = "Attention Is All You Need", style = "simple", length = "short"
```

---

### 3. PromptTemplate Class

**Why use PromptTemplate instead of f-strings?**
- Automatic validation of placeholders
- Save/load templates as JSON (reusability)
- Works seamlessly with LangChain Chains

**Basic usage:**
```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic", "tone"],
    template="Explain {topic} in a {tone} tone."
)

# Fill placeholders
final_prompt = template.format(topic="cricket", tone="funny")
print(final_prompt)
# Output: "Explain cricket in a funny tone."
```

**Validation example – missing placeholder:**
```python
template = PromptTemplate(
    input_variables=["topic", "tone"],
    template="Explain {topic} in a {tone} tone."
)
# This will raise an error because "tone" is missing
final_prompt = template.format(topic="cricket")  # KeyError
```

---

### 4. Saving and Loading PromptTemplates

**Save template to JSON:**
```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["paper_name", "style", "length"],
    template="Summarize {paper_name} in {style} style, length: {length}."
)
template.save("my_template.json")
```

**Load template from JSON:**
```python
from langchain_core.prompts import load_prompt

template = load_prompt("my_template.json")
final_prompt = template.format(paper_name="Attention Paper", style="simple", length="short")
```

---

### 5. Simple Chat Bot with Manual History (Without Message Types)

**Problem:** LLM has no memory of previous messages.

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI()
chat_history = []  # list of strings

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    chat_history.append(user_input)  # missing role info!
    response = model.invoke("\n".join(chat_history))
    print(f"AI: {response.content}")
    chat_history.append(response.content)
```

**Issue:** The LLM doesn't know who said what (user vs AI) – leads to confusion.

---

### 6. Message Types in LangChain

LangChain provides three message classes to label who said what:

| Message Type | Purpose | Example |
|--------------|---------|---------|
| `SystemMessage` | Set assistant's behavior (start of conversation) | `"You are a helpful AI assistant."` |
| `HumanMessage` | User's input | `"Tell me about LangChain."` |
| `AIMessage` | Assistant's response | `"LangChain is a framework..."` |

**Example – using message classes:**
```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="Tell me about LangChain."),
]

response = model.invoke(messages)
print(response.content)  # AIMessage

# Add AI response to history
messages.append(AIMessage(content=response.content))
```

---

### 7. ChatPromptTemplate (Dynamic Multi-Message Prompts)

Use when you need dynamic placeholders inside a list of messages.

**Example – dynamic system role and user topic:**
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# Create template with placeholders
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful {domain} expert."),
    HumanMessage(content="Explain in simple terms: What is {topic}?")
])

# Fill placeholders (using dictionary in invoke)
final_messages = chat_template.invoke({
    "domain": "cricket",
    "topic": "LBW rule"
})

print(final_messages)
# Output: [SystemMessage(content="You are a helpful cricket expert."),
#          HumanMessage(content="Explain in simple terms: What is LBW rule?")]
```

**Note:** In LangChain v3, use `.invoke()` with a dict, not `.format()`.

---

### 8. MessagePlaceholder (Insert Chat History)

**Problem:** You have previous conversation history stored in a database. You want to inject it into the prompt at runtime.

**Solution:** `MessagePlaceholder` – a placeholder that gets replaced by a list of messages.

**Example – Customer support with history:**
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Previous chat history (loaded from DB)
chat_history = [
    HumanMessage(content="I want a refund for order #12345"),
    AIMessage(content="Your refund request has been initiated. It will take 3-5 business days.")
]

# Current user query
current_query = HumanMessage(content="Where is my refund?")

# Create template with a placeholder for history
template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),   # history will be injected here
    HumanMessage(content="{current_query}")
])

# Fill the template
final_messages = template.invoke({
    "chat_history": chat_history,
    "current_query": "Where is my refund?"
})

print(final_messages)
# Output: SystemMessage + [previous history] + current query
# Now LLM understands context of the refund request
```

---

### 9. Temperature Correction

**Correction from previous video:** Temperature does not directly control creativity vs determinism in a linear way. Instead:

- **Temperature = 0** – same input always gives the same output (deterministic)
- **Higher temperature** – more random/creative, same input can give different outputs

```python
from langchain_openai import ChatOpenAI

# Deterministic – same output every time
model = ChatOpenAI(temperature=0.0)
for _ in range(3):
    response = model.invoke("Write a 5-line poem on cricket")
    print(response.content)
    print("---")

# Creative – each run different
model = ChatOpenAI(temperature=1.5)
for _ in range(3):
    response = model.invoke("Write a 5-line poem on cricket")
    print(response.content)
    print("---")
```

---

## 🔁 Summary Table

| Concept | When to use | Key code |
|---------|-------------|-----------|
| **PromptTemplate** | Single dynamic message | `PromptTemplate(input_variables=[...], template=...)` |
| **ChatPromptTemplate** | Multiple dynamic messages (conversation) | `ChatPromptTemplate.from_messages([...])` |
| **SystemMessage** | Set assistant role/behavior | `SystemMessage(content="...")` |
| **HumanMessage** | User input | `HumanMessage(content="...")` |
| **AIMessage** | Assistant response | `AIMessage(content="...")` |
| **MessagesPlaceholder** | Insert previous chat history | `MessagesPlaceholder(variable_name="history")` |
| **save/load_prompt** | Reuse templates across files | `template.save("file.json")`, `load_prompt("file.json")` |

---

> **Final takeaway:** Prompts are the most sensitive part of LLM apps. Use PromptTemplate for single queries, ChatPromptTemplate for multi-turn conversations, and MessagesPlaceholder to inject history. Never use raw f-strings – you lose validation and reusability.

---

## 07. Structured Output in LangChain (01:08:12)

## 🧑‍🏫 What This Video Covers

This lecture explains how to get **structured output** from LLMs using LangChain – instead of plain text, you get data in a defined format (like JSON). This allows LLMs to integrate with databases, APIs, and other systems. He covers:
- What is structured vs unstructured output
- Why structured output is needed (data extraction, API building, agent tools)
- Three ways to define the output schema: **TypedDict**, **Pydantic**, **JSON Schema**
- The `with_structured_output` function
- When to use each approach
- Models that don't support structured output (will be covered in next video)

---

## ✅ Important Pointers (Key Takeaways)

1. **Unstructured output** = plain text (e.g., "New Delhi is the capital of India"). Hard to use programmatically.
2. **Structured output** = well-defined data format like JSON. Easy to parse and integrate with other systems.
3. **Why needed?** Three main use cases:
   - Data extraction from resumes, invoices, reviews → store in database
   - Build APIs that return structured data
   - Agents need structured output to call tools (e.g., extract numbers for calculator)
4. **LangChain's solution:** `with_structured_output(schema)` – attach a schema to your model.
5. **Three ways to define schema:**
   - **TypedDict** – lightweight, only type hints (no runtime validation)
   - **Pydantic** – full validation, default values, type coercion, constraints (recommended)
   - **JSON Schema** – language-agnostic, good for multi-language projects
6. **Method parameter:** `method="json_mode"` (for Gemini, Claude) or `method="function_calling"` (default for OpenAI).
7. **Not all models support structured output** – open-source models like TinyLlama will need output parsers 

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. Structured vs Unstructured Output

**Unstructured (plain text):**
```python
response = model.invoke("Give me a one-day itinerary for Paris")
print(response.content)
# Output: "Morning: Visit Eiffel Tower. Afternoon: Louvre Museum. Evening: Dinner cruise."
```

**Structured (JSON):**
```json
[
  {"time": "Morning", "activity": "Visit Eiffel Tower"},
  {"time": "Afternoon", "activity": "Louvre Museum"},
  {"time": "Evening", "activity": "Dinner cruise"}
]
```

---

### 2. Basic `with_structured_output` with TypedDict

**Step 1 – Define schema using TypedDict:**
```python
from typing import TypedDict

class Review(TypedDict):
    summary: str
    sentiment: str   # "positive", "negative", or "neutral"
```

**Step 2 – Use it with a model:**
```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")
structured_model = model.with_structured_output(Review)

review_text = "The battery life is amazing, but the camera is average."

result = structured_model.invoke(review_text)
print(result)        # {'summary': '...', 'sentiment': 'positive'}
print(result["summary"])   # access like a dict
print(result["sentiment"])
```

> **Note:** TypedDict provides **type hints only** – no runtime validation. If the LLM returns wrong data type, it won't raise an error.

---

### 3. Adding Descriptions (Annotations) to TypedDict

Help the LLM understand each field better:
```python
from typing import Annotated, TypedDict

class Review(TypedDict):
    summary: Annotated[str, "A brief overview of the main points"]
    sentiment: Annotated[str, "Overall tone: positive, negative, or neutral"]
```

---

### 4. Pydantic – Full Validation & Power

Pydantic gives runtime validation, default values, type coercion, and constraints.

**Basic Pydantic model:**
```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

# Valid
s1 = Student(name="Nitesh", age=25)

# Invalid – will raise validation error
s2 = Student(name="Nitesh", age="twenty")  # Error!
```

**Optional fields & defaults:**
```python
from typing import Optional
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: Optional[int] = None   # can be missing, defaults to None

s = Student(name="Nitesh")
print(s.age)   # None
```

**Default values:**
```python
class Student(BaseModel):
    name: str = "Unknown"
    age: int = 18

s = Student()  # no arguments needed
print(s.name)  # "Unknown"
```

**Type coercion (auto-conversion):**
```python
class Student(BaseModel):
    age: int

# Even if you pass string "25", Pydantic converts to int 25
s = Student(age="25")
print(s.age)        # 25
print(type(s.age))  # <class 'int'>
```

**Field validations (constraints):**
```python
from pydantic import BaseModel, Field

class Student(BaseModel):
    cgpa: float = Field(ge=0, le=10, description="Decimal value representing CGPA")

# Valid
s = Student(cgpa=8.5)

# Invalid
s = Student(cgpa=12)   # ValidationError: ensure value ≤ 10
```

**Email validation (built-in):**
```python
from pydantic import BaseModel, EmailStr

class Student(BaseModel):
    email: EmailStr

s = Student(email="abc")              # Error!
s = Student(email="abc@gmail.com")    # Valid
```

**Convert Pydantic object to dict or JSON:**
```python
s = Student(name="Nitesh", age=25)
print(s.dict())      # {'name': 'Nitesh', 'age': 25}
print(s.json())      # '{"name": "Nitesh", "age": 25}'
```

**Using Pydantic with `with_structured_output`:**
```python
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class Review(BaseModel):
    summary: str = Field(description="Brief summary of the review")
    sentiment: str = Field(description="Positive, negative, or neutral")

model = ChatOpenAI(model="gpt-4")
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("Great phone, amazing battery!")
print(result.summary)    # access as attribute (Pydantic object)
print(result.sentiment)
```

---

### 5. JSON Schema (Language-Agnostic)

Use when your project uses multiple languages (Python backend + JavaScript frontend).

**Example JSON Schema:**
```json
{
  "title": "Review",
  "type": "object",
  "properties": {
    "summary": {"type": "string", "description": "Brief summary"},
    "sentiment": {"type": "string", "enum": ["positive", "negative"]}
  },
  "required": ["summary", "sentiment"]
}
```

**Using JSON Schema with LangChain:**
```python
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "sentiment": {"type": "string", "enum": ["positive", "negative"]}
    },
    "required": ["summary", "sentiment"]
}

structured_model = model.with_structured_output(json_schema)
result = structured_model.invoke(review_text)
print(result)  # returns a Python dict
```

---

### 6. Complete Example – Smartphone Review Analysis

**Goal:** Extract themes, summary, sentiment, pros, cons, and reviewer name (optional).

**Pydantic schema:**
```python
from typing import List, Optional
from pydantic import BaseModel, Field

class ReviewAnalysis(BaseModel):
    themes: List[str] = Field(description="Main topics discussed")
    summary: str = Field(description="Brief overview")
    sentiment: str = Field(description="positive or negative")
    pros: Optional[List[str]] = Field(default=None, description="List of pros")
    cons: Optional[List[str]] = Field(default=None, description="List of cons")
    reviewer_name: Optional[str] = Field(default=None, description="Name if mentioned")

# Use with model
structured_model = model.with_structured_output(ReviewAnalysis)
review = "The Snapdragon processor is blazing fast. 5000mAh battery lasts 2 days. Only downside is the price."
result = structured_model.invoke(review)

print(result.themes)     # ['Snapdragon', 'battery']
print(result.sentiment)  # positive
print(result.pros)       # ['fast processor', 'long battery']
```

---

### 7. Method Parameter: JSON Mode vs Function Calling

```python
# For OpenAI (default function_calling)
structured_model = model.with_structured_output(Review, method="function_calling")

# For Gemini or Claude (use json_mode)
structured_model = model.with_structured_output(Review, method="json_mode")
```

> If your model doesn't support structured output at all (e.g., TinyLlama), you'll need **output parsers** – covered in the next video.

---

## 🔁 Summary Table – When to Use Which Schema

| Schema | Validation | Defaults | Type Coercion | Cross-language | Best for |
|--------|-----------|----------|---------------|----------------|-----------|
| **TypedDict** | ❌ No | ❌ No | ❌ No | ❌ No | Quick prototypes, pure Python |
| **Pydantic** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No | **Most Python projects** (recommended) |
| **JSON Schema** | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes | Multi-language projects |

---

> **Final takeaway:** Use `with_structured_output` with a Pydantic model for most Python projects. It gives you validation, defaults, and clean object access. Save JSON Schema for when you need to share the schema with non-Python code.

---

## 08. Output Parsers in LangChain (53:12)

## 🧑‍🏫 What This Video Covers

This lecture explains **Output Parsers** in LangChain – tools that convert raw LLM responses (unstructured text) into structured formats like strings, JSON, or Pydantic objects. This is essential for models that **don't** natively support structured output (e.g., open-source models like TinyLlama). He covers:
- Why output parsers are needed
- Four most important parsers: **StringOutputParser**, **JsonOutputParser**, **StructuredOutputParser**, **PydanticOutputParser**
- How to use them with **Chains** (pipelines)
- When to use which parser

---

## ✅ Important Pointers (Key Takeaways)

1. **Output Parsers** = LangChain classes that convert raw LLM text responses into structured data.
2. **Why needed?** Many LLMs (especially open-source) cannot produce structured output natively. Parsers force/extract structure from plain text.
3. **Two types of LLMs:**
   - Models that support structured output natively (GPT-4, Claude) → use `with_structured_output`
   - Models that don't (TinyLlama, many open-source) → use **Output Parsers**
4. **StringOutputParser** – extracts plain text from LLM response (removes metadata). Best used inside chains.
5. **JsonOutputParser** – forces LLM to return JSON, but **does not enforce a schema** (structure can vary).
6. **StructuredOutputParser** – enforces a specific JSON schema (field names and types), but **no data validation** (e.g., can't enforce age > 18).
7. **PydanticOutputParser** – enforces schema + full data validation (types, constraints, defaults). Most powerful and recommended.
8. **Always prefer using parsers inside Chains** – cleaner code, automatic piping.
9. LangChain has many other parsers (CSV, list, datetime, etc.) – check documentation.

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. The Problem – Raw LLM Response Contains Metadata

```python
response = model.invoke("Tell me about black holes")
print(response)  
# Output: content='Black holes are...' , response_metadata={'token_usage': {...}} etc.
```

To get just the text: `response.content` – annoying when chaining steps.

---

### 2. StringOutputParser

**Purpose:** Extract plain string content from LLM response. Most useful inside **Chains**.

**Without parser (manual):**
```python
result1 = model.invoke("Write a detailed report on black holes")
text1 = result1.content
result2 = model.invoke(f"Summarize this: {text1}")
print(result2.content)
```

**With StringOutputParser inside a Chain:**
```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI()
parser = StrOutputParser()

template1 = PromptTemplate(input_variables=["topic"], template="Write a detailed report on {topic}")
template2 = PromptTemplate(input_variables=["text"], template="Summarize in 5 lines: {text}")

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({"topic": "black holes"})
print(result)  # Directly prints the final summary string
```

> **When to use:** When you only need plain text output, especially in multi-step chains.

---

### 3. JsonOutputParser

**Purpose:** Force LLM to return JSON. But **no schema enforcement** – LLM decides the JSON structure.

**Example:**
```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me name, age, and city of a fictional person.\n{format_instructions}\n",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({})
print(result)  # {'name': 'John', 'age': 30, 'city': 'New York'}
```

**Problem:** If you ask for 5 facts, the LLM might return `{"facts": [...]}` instead of `{"fact1": "...", "fact2": "..."}`. No control.

> **When to use:** Quick JSON extraction when exact schema doesn't matter.

---

### 4. StructuredOutputParser

**Purpose:** Enforce a **specific JSON schema** – field names and types are fixed.

**Example – forcing a fact1, fact2, fact3 structure:**
```python
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

response_schemas = [
    ResponseSchema(name="fact1", description="First fact about the topic"),
    ResponseSchema(name="fact2", description="Second fact about the topic"),
    ResponseSchema(name="fact3", description="Third fact about the topic"),
]
parser = StructuredOutputParser.from_response_schemas(response_schemas)

template = PromptTemplate(
    template="Give 3 facts about {topic}.\n{format_instructions}\n",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({"topic": "black holes"})
print(result)  # {'fact1': '...', 'fact2': '...', 'fact3': '...'}
```

**Limitation:** No data validation. If the LLM returns `fact2: 42` (number instead of string), it won't raise an error.

> **When to use:** When you need a fixed field structure but don't need type/range validation.

---

### 5. PydanticOutputParser (Most Powerful)

**Purpose:** Enforce schema + **full data validation** (types, constraints, default values, custom validators).

**Example – Person with age constraint (must be > 18):**
```python
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(ge=18, description="Age of the person (must be > 18)")
    city: str = Field(description="City where person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate name, age, and city of a {nationality} person.\n{format_instructions}\n",
    input_variables=["nationality"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

model = ChatOpenAI()
chain = template | model | parser
result = chain.invoke({"nationality": "Indian"})
print(result.name)   # Access as Pydantic object attribute
print(result.age)    # Will be int; if LLM returns "25 years", Pydantic coerces to 25
```

**If LLM returns age = 15, Pydantic raises validation error – you can catch and handle it.**

> **When to use:** Most Python projects. You get schema enforcement + validation + type coercion.

---

## 🔁 Summary Table – Four Output Parsers

| Parser | Schema Enforcement | Data Validation | Best for |
|--------|-------------------|-----------------|----------|
| **StringOutputParser** | ❌ (just string) | ❌ | Plain text, multi-step chains |
| **JsonOutputParser** | ❌ (freeform JSON) | ❌ | Quick JSON, structure not critical |
| **StructuredOutputParser** | ✅ (field names fixed) | ❌ | Fixed schema, no validation needed |
| **PydanticOutputParser** | ✅ (fields + types) | ✅ (constraints, defaults, coercion) | **Most Python projects (recommended)** |

---

## 🔁 Using Parsers in Chains – General Pattern

All parsers follow the same pattern:

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI()
parser = SomeOutputParser()  # e.g., PydanticOutputParser(pydantic_object=MyModel)

template = PromptTemplate(
    template="Your prompt here...\n{format_instructions}\n",
    input_variables=["your_variable"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({"your_variable": "some value"})
```

> The `|` operator chains components together. `get_format_instructions()` injects parsing instructions into the prompt.

---

## 🗓️ Next Steps

- Next video will likely cover **Chains** in depth (already used here, but more details coming)
- You can explore other parsers: `CommaSeparatedListOutputParser`, `DatetimeOutputParser`, `EnumOutputParser`, etc.

> **Final takeaway:** Use **PydanticOutputParser** for most projects – it gives you the best of both worlds: structured output + validation. Only fallback to simpler parsers if you need something very basic or are working with non-Python systems.

### Different Output Parsers
- StrOutput Parser
- JSON Output Parser
- Structured Output Parser
- Pydantic Output Parser

---

## 09. Chains in LangChain (54:00)

## 🧑‍🏫 What This Video Covers

This lecture explains **Chains** – the most important component in LangChain (the library is named after it). Chains let you build **pipelines** where the output of one step automatically becomes the input of the next. He covers:
- Why chains are needed (avoid manual step-by-step coding)
- **Simple Chain** – one prompt → one LLM → one parser
- **Sequential Chain** – multiple steps in sequence (e.g., detailed report → summary)
- **Parallel Chain** – run multiple chains simultaneously and combine results
- **Conditional Chain** – choose which chain to execute based on a condition (if/else)

---

## ✅ Important Pointers (Key Takeaways)

1. **Chain** = a pipeline that connects multiple components (prompts, models, parsers) so data flows automatically.
2. **Without chains:** You manually call `prompt.format()`, then `model.invoke()`, then extract `response.content` – very tedious for multi-step apps.
3. **With chains (LCEL – LangChain Expression Language):** Use the **pipe operator `|`** to connect components: `prompt | model | parser`
4. **StringOutputParser** is commonly used at the end of a chain to extract plain text from LLM responses.
5. **Sequential chains** run steps one after another. Use multiple `|` operators.
6. **Parallel chains** run independent tasks simultaneously using `RunnableParallel`. Great for when you need multiple outputs from the same input (e.g., notes + quiz from a document).
7. **Conditional chains** use `RunnableBranch` – like an if-else statement for chains. Based on a condition (e.g., sentiment = positive or negative), execute different chains.
8. **RunnableLambda** converts a simple Python function into a runnable (usable in a chain).
9. You can **visualize** any chain with `chain.get_graph().print_ascii()`.

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. Simple Chain (One LLM Call)

**Goal:** User gives a topic → LLM generates 5 interesting facts → output as string.

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Generate 5 interesting facts about {topic}."
)

# Build chain using pipe operator
chain = prompt | model | parser

# Run
result = chain.invoke({"topic": "cricket"})
print(result)

# Visualize
print(chain.get_graph().print_ascii())
```

**Why useful:** No need to manually call `prompt.format()`, then `model.invoke()`, then extract `.content`. All automatic.

---

### 2. Sequential Chain (Multiple Steps in Sequence)

**Goal:** First generate a detailed report on a topic, then summarize that report into 5 key points.

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI()
parser = StrOutputParser()

# Step 1: Generate detailed report
prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Generate a detailed report on {topic}."
)

# Step 2: Summarize the report
prompt2 = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text into 5 key points:\n{text}"
)

# Chain: prompt1 → model → parser → prompt2 → model → parser
chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "unemployment in India"})
print(result)
```

**What happens automatically:** The output of step 1 (detailed report) is fed as input `{text}` into step 2.

---

### 3. Parallel Chain (Running Multiple Tasks Simultaneously)

**Goal:** Given a technical document (e.g., about Linear Regression), generate **notes** and a **quiz** in parallel, then combine them.

**Architecture:**
- Input text goes to two separate chains (one for notes, one for quiz)
- Both run in parallel (using `RunnableParallel`)
- Their outputs are combined by a third chain

```python
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

model1 = ChatOpenAI()        # for notes
model2 = ChatAnthropic(model="claude-3")  # for quiz
model3 = ChatOpenAI()        # for merging
parser = StrOutputParser()

# Prompt for notes
prompt_notes = PromptTemplate(
    input_variables=["text"],
    template="Generate simple notes from the following text:\n{text}"
)

# Prompt for quiz
prompt_quiz = PromptTemplate(
    input_variables=["text"],
    template="Generate 5 short Q&A from the following text:\n{text}"
)

# Prompt for merging
prompt_merge = PromptTemplate(
    input_variables=["notes", "quiz"],
    template="Merge the following notes and quiz into one document:\nNotes:\n{notes}\n\nQuiz:\n{quiz}"
)

# Define the two parallel chains
chain_notes = prompt_notes | model1 | parser
chain_quiz = prompt_quiz | model2 | parser

# Run them in parallel
parallel = RunnableParallel(notes=chain_notes, quiz=chain_quiz)

# Merge chain
merge_chain = prompt_merge | model3 | parser

# Final chain: parallel then merge
final_chain = parallel | merge_chain

result = final_chain.invoke({"text": "Your long document text here..."})
print(result)
```

> **Note:** `RunnableParallel` takes a dictionary. It runs each value (chain) with the same input and outputs a dict with same keys.

---

### 4. Conditional Chain (If/Else Based on Condition)

**Goal:** Classify customer feedback as positive or negative, then generate an appropriate response.

**How it works:**
1. First chain classifies sentiment (returns "positive" or "negative" using a Pydantic parser for consistency)
2. Then `RunnableBranch` checks the sentiment:
   - If "positive" → run a chain that thanks the customer
   - If "negative" → run a chain that apologizes
   - Else → run a default chain

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

model = ChatOpenAI()
parser = StrOutputParser()

# Define schema for consistent sentiment output
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Sentiment of feedback")

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

# Step 1: Classify sentiment
prompt_classify = PromptTemplate(
    input_variables=["feedback"],
    template="Classify the sentiment of the following feedback as positive or negative.\n{format_instructions}\nFeedback: {feedback}",
    partial_variables={"format_instructions": pydantic_parser.get_format_instructions()}
)
classify_chain = prompt_classify | model | pydantic_parser

# Step 2: Branch based on sentiment
# Define positive response chain
prompt_positive = PromptTemplate(
    input_variables=["feedback"],
    template="Write a thank you reply for this positive feedback: {feedback}"
)
positive_chain = prompt_positive | model | parser

# Define negative response chain
prompt_negative = PromptTemplate(
    input_variables=["feedback"],
    template="Write an apology reply for this negative feedback: {feedback}"
)
negative_chain = prompt_negative | model | parser

# Default chain (if sentiment not recognized)
def default_func(x):
    return "Could not determine sentiment."

default_chain = RunnableLambda(default_func)

# Build the branch
branch = RunnableBranch(
    (lambda x: x.sentiment == "positive", positive_chain),
    (lambda x: x.sentiment == "negative", negative_chain),
    default_chain
)

# Final chain: classify → branch
final_chain = classify_chain | branch

# Test with negative feedback
result = final_chain.invoke({"feedback": "This is a terrible smartphone."})
print(result)  # Apology message

# Test with positive feedback
result = final_chain.invoke({"feedback": "This is a wonderful smartphone!"})
print(result)  # Thank you message
```

> **Important:** The condition function receives the output of the previous step (the `Feedback` object). We use `RunnableLambda` to wrap a simple function into a runnable for the default branch.

---

## 🔁 Summary Table – Types of Chains

| Chain Type | When to use | Key component | Data flow |
|------------|-------------|---------------|------------|
| **Simple** | One LLM call | `prompt \| model \| parser` | Single path |
| **Sequential** | Multiple steps in order | `step1 \| step2 \| step3` | Output of step N → input of step N+1 |
| **Parallel** | Independent tasks from same input | `RunnableParallel(dict of chains)` | Same input to all → outputs combined as dict |
| **Conditional** | Choose path based on condition | `RunnableBranch(conditions + chains)` | Only one branch executes |

---

> **Final takeaway:** Chains are the backbone of any LLM application in LangChain. Use `|` to build pipelines, `RunnableParallel` for parallel processing, and `RunnableBranch` for conditional logic. Always end with a parser like `StrOutputParser` to get clean text.

---

## 10. What are Runnables in LangChain (01:16:21)

## 🧑‍🏫 What This Video Covers

This lecture explains the **Runnable** interface – the foundation of LangChain that makes Chains work. He covers:
- Why Runnables exist (the problems LangChain faced)
- What Runnables are (unit of work with common interface)
- The four key properties of Runnables
- How Runnables enable flexible chain building (like Lego blocks)
- Building custom Runnables from scratch (code demo)
- How LangChain's actual code implements Runnables

---

## ✅ Important Pointers (Key Takeaways)

1. **The problem LangChain solved first:** Standardized interface to different LLM providers (OpenAI, Anthropic, Google).
2. **The next problem:** LLM apps need many components (loaders, splitters, embeddings, vector stores, retrievers, parsers). Each component had its own methods (`predict`, `format`, `get_relevant_documents`, `parse`) – not compatible.
3. **LangChain's solution:** Create many **pre-built Chains** (LLMChain, RetrievalQA, etc.) to glue components together.
4. **The new problem:** Too many chains → bloated codebase, steep learning curve.
5. **Root cause:** Components were not standardized. Each had different interfaces.
6. **The fix:** **Runnable interface** – a common standard for ALL components.
7. **A Runnable is:** a **unit of work** that takes input, processes it, returns output.
8. **Four properties of Runnables:**
   - Each does one specific job
   - All follow the same interface (same methods: `invoke`, `batch`, `stream`)
   - Runnables can be **composed** (chained together using `|`)
   - A chain of Runnables is **itself a Runnable**
9. **Analogy:** Runnables = Lego blocks. Same connectors, can build anything.
10. **Key methods:** `invoke` (single input → output), `batch` (multiple inputs), `stream` (stream output).

---

## 📚 Important Concepts Explained (with Basic Code Examples)

### 1. The Problem – Incompatible Components

Different LangChain components had different methods:

| Component | Method to call |
|-----------|----------------|
| LLM | `predict(prompt)` |
| PromptTemplate | `format(**kwargs)` |
| Retriever | `get_relevant_documents(query)` |
| OutputParser | `parse(text)` |

You couldn't simply chain them. LangChain had to write custom chain classes for every combination.

---

### 2. What is a Runnable?

> **Definition:** A Runnable is a unit of work with a common interface. It takes an input, processes it, and returns an output.

**Basic example (conceptual):**
```python
class MyRunnable:
    def invoke(self, input_data):
        # process input
        return output
```

**Four key properties (Lego block analogy):**

| Property | Meaning | Lego analogy |
|----------|---------|--------------|
| **Unit of work** | Each Runnable does one specific job | Each Lego block has a shape/function |
| **Common interface** | All Runnables have same methods (`invoke`, `batch`, `stream`) | All Lego blocks have same connector studs |
| **Composable** | You can connect Runnables with `\|` | You can connect Lego blocks |
| **Result is also Runnable** | A chain of Runnables is itself a Runnable | A built structure is itself a Lego block (can connect to others) |

---

### 3. Building a Custom Runnable (Simplified)

Here's how you'd implement a Runnable interface from scratch:

**Step 1 – Define an abstract Runnable class:**
```python
from abc import ABC, abstractmethod

class Runnable(ABC):
    @abstractmethod
    def invoke(self, input_data):
        """Process single input and return output"""
        pass
    
    def batch(self, inputs_list):
        """Process multiple inputs (default implementation)"""
        return [self.invoke(inp) for inp in inputs_list]
    
    def stream(self, input_data):
        """Stream output (simplified)"""
        yield self.invoke(input_data)
```

**Step 2 – Create a component that implements Runnable (e.g., dummy LLM):**
```python
import random

class DummyLLM(Runnable):
    def __init__(self):
        self.responses = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]
    
    def invoke(self, prompt):
        # In real LLM, this would call an API
        return random.choice(self.responses)
```

**Step 3 – Create a PromptTemplate as Runnable:**
```python
class DummyPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
    
    def invoke(self, inputs):
        # Format the template with inputs (like f-string)
        result = self.template
        for key, value in inputs.items():
            result = result.replace(f"{{{key}}}", str(value))
        return result
```

**Step 4 – Create a RunnableConnector to chain Runnables:**
```python
class RunnableConnector(Runnable):
    def __init__(self, *runnables):
        self.runnables = runnables
    
    def invoke(self, input_data):
        current_input = input_data
        for runnable in self.runnables:
            current_input = runnable.invoke(current_input)
        return current_input
```

**Step 5 – Use the connector to build a chain:**
```python
# Create components
prompt = DummyPromptTemplate(
    template="Write a short poem about {topic}",
    input_variables=["topic"]
)
llm = DummyLLM()

# Create chain
chain = RunnableConnector(prompt, llm)

# Run
result = chain.invoke({"topic": "cricket"})
print(result)  # Random response from dummy LLM
```

---

### 4. The Pipe Operator (`|`) as Syntactic Sugar

LangChain allows you to use `|` instead of manual connector:

```python
# Instead of this:
chain = RunnableConnector(prompt, llm, parser)

# You can write:
chain = prompt | llm | parser
```

The `|` operator does the same thing – passes output of left to input of right.

---

### 5. Real LangChain Runnable Hierarchy

In actual LangChain code:

```
Runnable (abstract base class)
    ↑
RunnableSerializable
    ↑
BaseLanguageModel
    ↑
BaseChatModel
    ↑
ChatOpenAI
```

Every model (ChatOpenAI, ChatAnthropic, etc.) implements the `invoke` method.

---

### 6. Using Runnables in Practice (Simple Example)

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Each of these is a Runnable
model = ChatOpenAI()
prompt = PromptTemplate.from_template("Tell me a joke about {topic}")
parser = StrOutputParser()

# Chain them (works because all are Runnables)
chain = prompt | model | parser

# Invoke the chain (which is itself a Runnable)
result = chain.invoke({"topic": "cats"})
print(result)
```

---

## 🔁 Summary – Why Runnables Matter

| Before Runnables | After Runnables |
|------------------|-----------------|
| Components had different methods (`predict`, `format`, `parse`) | All components have `invoke` |
| Each new use case needed a custom Chain class | Use `\|` to compose any components |
| Codebase bloated with many chain classes | Minimal, flexible, Lego-like building |
| Steep learning curve | Uniform interface, easy to learn |

---

## 🧠 Key Takeaway

> **Runnables are the secret sauce that makes LangChain chains work.** By giving every component the same interface (`invoke`), LangChain allows you to connect them like Lego blocks – and the resulting chain is itself a Runnable, so you can build arbitrarily complex pipelines without writing custom glue code.

---

### Additional Notes

- [chains](https://reference.langchain.com/python/langchain-classic/chains)

### Runnable - A unit of work that can be invoked, batched, streamed, transformed and composed

### Working of **Retrieval QA chain** using LangChain Expression Language, or LCEL.

```python
qa_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
```

Think of it as a pipeline:

```text
user question
   ↓
retrieve relevant docs + keep original question
   ↓
fill prompt template
   ↓
send to LLM
   ↓
convert model response to plain string
```

Step by step:

**1. User input enters the chain**

Later in your file, you call:

```python
answer = qa_chain.invoke(query)
```

where:

```python
query = "What are the key takeaways from the document?"
```

So the input to `qa_chain` is just a string question.

---

**2. This dictionary creates the prompt inputs**

```python
{"context": retriever | format_docs, "question": RunnablePassthrough()}
```

Your prompt needs two variables:

```python
{context}
{question}
```

So this dictionary creates those two values.

It means:

```text
context  = run the question through retriever, then format the retrieved docs
question = pass the original question as-is
```

---

**3. `"context": retriever | format_docs`**

This part is itself a mini-chain:

```python
retriever | format_docs
```

The `retriever` receives the user question and searches the FAISS vector database for relevant document chunks.

For example:

```python
retriever.invoke("What are the key takeaways from the document?")
```

returns a list of `Document` objects.

Then `format_docs` runs:

```python
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
```

So it converts retrieved documents into one big text string.

Example result:

```text
Chunk 1 text...

Chunk 2 text...

Chunk 3 text...
```

That final string becomes the value of `{context}`.

---

**4. `"question": RunnablePassthrough()`**

This keeps the original input unchanged.

If the user asks:

```python
"What are the key takeaways from the document?"
```

then:

```python
RunnablePassthrough()
```

passes that same string forward as the value of `{question}`.

So after the dictionary runs, LangChain has something like:

```python
{
    "context": "Relevant document chunk 1...\n\nRelevant document chunk 2...",
    "question": "What are the key takeaways from the document?"
}
```

---

**5. `| prompt`**

Now this dictionary is sent into your prompt template:

```python
prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the following context:
{context}

Question: {question}
""")
```

LangChain fills in `{context}` and `{question}`.

So the LLM receives a prompt like:

```text
Answer the question based only on the following context:
Relevant document chunk 1...

Relevant document chunk 2...

Question: What are the key takeaways from the document?
```

---

**6. `| llm`**

This sends the completed prompt to the chat model:

```python
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)
```

The model reads the retrieved context and generates an answer.

---

**7. `| StrOutputParser()`**

Chat models usually return a structured message object, not just plain text.

`StrOutputParser()` extracts the text content from the model response.

So instead of getting a LangChain message object, you get a normal Python string:

```python
"The key takeaways from the document are..."
```

---

In short, this line:

```python
qa_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
```

means:

> Take the user’s question, retrieve relevant document chunks for context, keep the original question, insert both into the prompt, send the prompt to the LLM, and return the answer as a plain string.

The most important part is this:

```python
{"context": retriever | format_docs, "question": RunnablePassthrough()}
```

because it prepares the two inputs your prompt needs: retrieved `context` and original `question`.

---

## 11. Langchain Runnables - Part 2 (54:25)

## 🧑‍🏫 What This Video Covers

This lecture continues the **Runnables** topic, focusing on **Runnable Primitives** – special runnables that help you combine task‑specific runnables (like PromptTemplate, ChatOpenAI, StrOutputParser) to build flexible workflows. He covers:
- **RunnableSequence** – chain runnables in order (sequential)
- **RunnableParallel** – run multiple runnables in parallel with same input
- **RunnablePassthrough** – pass input through unchanged (like a bypass)
- **RunnableLambda** – turn any Python function into a runnable
- **RunnableBranch** – conditional logic (if/else) for runnables
- **LCEL (LangChain Expression Language)** – the `|` pipe operator for cleaner sequential chains

---

## ✅ Important Pointers (Key Takeaways)

1. **Task‑specific runnables** = LangChain components (PromptTemplate, ChatOpenAI, Retriever, etc.) converted to runnables. They do one specific job.
2. **Runnable primitives** = tools to combine task‑specific runnables into workflows (sequential, parallel, conditional, etc.)
3. **RunnableSequence** = connects runnables in a sequence. Output of one becomes input of next.
4. **RunnableParallel** = runs multiple runnables on the same input, returns a dict of outputs.
5. **RunnablePassthrough** = returns the input unchanged. Useful when you need to pass data forward without processing.
6. **RunnableLambda** = wraps any Python function as a runnable, allowing custom logic inside chains.
7. **RunnableBranch** = like an if‑else statement – chooses which runnable to execute based on a condition.
8. **LCEL (pipe operator `|`)** = syntactic sugar for `RunnableSequence`. Most common way to build sequential chains.
9. You can mix primitives: a `RunnableParallel` can contain `RunnableSequence`s inside it.
10. Future LangChain versions may add declarative syntax for parallel and conditional chains as well.

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. RunnableSequence (Sequential Chain)

**Purpose:** Chain multiple runnables one after another. Output of first → input of second, etc.

**Without LCEL (explicit):**
```python
from langchain.schema.runnable import RunnableSequence

chain = RunnableSequence(first_runnable, second_runnable, third_runnable)
result = chain.invoke(input_data)
```

**With LCEL (recommended):**
```python
chain = first_runnable | second_runnable | third_runnable
result = chain.invoke(input_data)
```

**Complete example – generate a joke and then explain it:**
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

model = ChatOpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate.from_template("Tell a joke about {topic}")
prompt2 = PromptTemplate.from_template("Explain this joke: {text}")

# Sequential chain
chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({"topic": "AI"})
print(result)
```

---

### 2. RunnableParallel (Parallel Execution)

**Purpose:** Run multiple runnables independently on the **same input**, return results as a dictionary.

**Use case:** Generate a tweet **and** a LinkedIn post from the same topic.

```python
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI()
parser = StrOutputParser()

prompt_tweet = PromptTemplate.from_template("Write a tweet about {topic}")
prompt_linkedin = PromptTemplate.from_template("Write a LinkedIn post about {topic}")

# Each is a sequential chain
tweet_chain = prompt_tweet | model | parser
linkedin_chain = prompt_linkedin | model | parser

# Run them in parallel
parallel = RunnableParallel(
    tweet=tweet_chain,
    linkedin=linkedin_chain
)

result = parallel.invoke({"topic": "artificial intelligence"})
print(result["tweet"])
print(result["linkedin"])
```

> **Important:** Both chains receive the same input `{"topic": "..."}`. Output is a dict with keys `"tweet"` and `"linkedin"`.

---

### 3. RunnablePassthrough (Bypass)

**Purpose:** Returns the input unchanged. Useful when you want to keep the original data flowing while also doing other processing.

**Example – generate a joke and also count its words:**

```python
from langchain.schema.runnable import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate.from_template("Tell a joke about {topic}")
joke_chain = prompt | model | parser

# Word counter function
def word_count(text):
    return len(text.split())

word_counter = RunnableLambda(word_count)  # convert function to runnable

# Parallel: one branch passes joke through, other branch counts words
parallel = RunnableParallel(
    joke=RunnablePassthrough(),      # just pass the joke unchanged
    word_count=word_counter          # count words
)

# Final chain: generate joke → parallel processing
final_chain = joke_chain | parallel
result = final_chain.invoke({"topic": "cats"})
print(f"Joke: {result['joke']}")
print(f"Word count: {result['word_count']}")
```

> Without `RunnablePassthrough`, the word counter would receive the joke, but the original joke wouldn't be available in the output.

---

### 4. RunnableLambda (Custom Function as Runnable)

**Purpose:** Convert any Python function into a runnable so you can use it inside chains.

**Example – clean text before sending to LLM:**

```python
from langchain.schema.runnable import RunnableLambda
import re

def clean_text(text):
    # Remove HTML tags, extra spaces, special characters
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().strip()

cleaner = RunnableLambda(clean_text)

# Now you can use it in a chain
chain = cleaner | model | parser
result = chain.invoke(dirty_text)
```

**Shorter syntax using lambda directly:**
```python
word_counter = RunnableLambda(lambda x: len(x.split()))
```

---

### 5. RunnableBranch (Conditional Chains)

**Purpose:** Like an if‑else statement for runnables. Choose which runnable to execute based on a condition.

**Example – summarize only if report is longer than 500 words, otherwise return as‑is:**

```python
from langchain.schema.runnable import RunnableBranch, RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI()
parser = StrOutputParser()

# Report generation
prompt_report = PromptTemplate.from_template("Write a detailed report on {topic}")
report_chain = prompt_report | model | parser

# Summarizer (for long reports)
prompt_summary = PromptTemplate.from_template("Summarize this text: {text}")
summarize_chain = prompt_summary | model | parser

# Condition: check word count
def is_long(text):
    return len(text.split()) > 500

# RunnableBranch: (condition, runnable_if_true), (default_runnable)
branch = RunnableBranch(
    (RunnableLambda(is_long), summarize_chain),   # if long → summarize
    RunnablePassthrough()                         # else → pass through
)

final_chain = report_chain | branch
result = final_chain.invoke({"topic": "climate change"})
print(result)
```

> **Syntax:** `RunnableBranch( (condition, runnable_for_true), default_runnable )`. Condition can be any runnable that returns a boolean (e.g., `RunnableLambda`).

---

### 6. LCEL (LangChain Expression Language)

**Definition:** A declarative way to build sequential chains using the `|` pipe operator. It is syntactic sugar for `RunnableSequence`.

**Instead of:**
```python
from langchain.schema.runnable import RunnableSequence
chain = RunnableSequence(prompt, model, parser)
```

**You write:**
```python
chain = prompt | model | parser
```

> The pipe operator works because each component (`prompt`, `model`, `parser`) is a **Runnable** that implements the `__or__` method.

**You can also combine primitives with `|`:**
```python
# RunnableParallel inside a sequence
chain = prompt | model | parser | RunnableParallel(
    original=RunnablePassthrough(),
    word_count=RunnableLambda(lambda x: len(x.split()))
)
```

---

## 🔁 Summary Table – Runnable Primitives

| Primitive | Purpose | When to use |
|-----------|---------|--------------|
| `RunnableSequence` (or `\|`) | Sequential execution | Most common – chain steps one after another |
| `RunnableParallel` | Parallel execution | Same input → multiple independent outputs |
| `RunnablePassthrough` | Pass input unchanged | Keep original data while doing extra processing |
| `RunnableLambda` | Custom Python function | Add preprocessing, validation, counting, etc. |
| `RunnableBranch` | Conditional logic | If/else based on intermediate result |

---

## 📌 Final Takeaway

> **Runnable primitives are the Lego blocks for building LLM workflows in LangChain.** Learn them well – `|` for sequences, `RunnableParallel` for parallel tasks, `RunnableLambda` for custom logic, and `RunnableBranch` for decisions. Almost all complex chains are combinations of these five primitives.

---

## 12. Document Loaders in LangChain (56:43)

## 🧑‍🏫 What This Video Covers

This lecture introduces **RAG (Retrieval-Augmented Generation)** and the first component needed to build RAG apps – **Document Loaders** in LangChain. He covers:
- What RAG is and why it's needed (LLMs don't know your private/current data)
- The four main components of a RAG system (Document Loaders, Text Splitters, Vector Stores, Retrievers)
- **Document Loaders** – load data from various sources into a standardized `Document` object
- Five practical loaders: **TextLoader**, **PyPDFLoader**, **DirectoryLoader**, **WebBaseLoader**, **CSVLoader**
- **Load vs Lazy Load** – memory and performance considerations
- How to find other loaders and even build custom ones

---

## ✅ Important Pointers (Key Takeaways)

1. **RAG (Retrieval-Augmented Generation)** = give LLM access to external knowledge (PDFs, websites, databases) so it can answer questions about your private or up‑to‑date data.
2. **Four main components of RAG:**
   - Document Loaders – bring data into LangChain
   - Text Splitters – break documents into chunks
   - Vector Stores – store embeddings for semantic search
   - Retrievers – fetch relevant chunks for a query
3. **Document Loader** = a LangChain component that loads data from any source and converts it into a **standardized `Document` object**.
4. A `Document` object has two parts:
   - `page_content` – the actual text
   - `metadata` – source, page number, author, etc.
5. Every loader returns a **list of `Document` objects**. For PDFs, each page becomes one `Document`.
6. **Load method** (`loader.load()`) – eager loading: loads **everything into memory at once**, returns a list. Use for small datasets.
7. **Lazy load method** (`loader.lazy_load()`) – returns a generator; loads **one document at a time** on demand. Use for large datasets to save memory.
8. LangChain has **100+ document loaders** for PDFs, web pages, cloud storage (S3, Google Drive), social media, YouTube transcripts, etc.
9. Most loaders are in `langchain_community.document_loaders`.
10. You can **create custom document loaders** by inheriting from `BaseLoader` if your data source isn't supported.

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. What is RAG?

**Problem:** LLMs like ChatGPT don't know your private company data or current events (their training data is outdated).  
**Solution:** RAG – retrieve relevant information from your own knowledge base and feed it to the LLM as context.

**Simple RAG flow:**
1. User asks a question.
2. System searches your documents (PDFs, websites, DB) for relevant chunks.
3. LLM answers based on those chunks + its own knowledge.

---

### 2. Document Loader – Standardized Document Object

Every loader returns a **list of `Document` objects**. Each `Document` has:
- `page_content` – the extracted text
- `metadata` – source, page number, etc.

```python
# Example Document object (conceptual)
Document(
    page_content="This is the actual text from the file...",
    metadata={"source": "cricket.txt", "page": 1}
)
```

---

### 3. TextLoader – Load a `.txt` File

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("cricket.txt", encoding="utf-8")
docs = loader.load()  # returns list of Document objects

print(len(docs))               # 1
print(docs[0].page_content)    # the poem text
print(docs[0].metadata)        # {'source': 'cricket.txt'}
```

> **Use when:** You have plain text files (logs, transcripts, code snippets).

---

### 4. PyPDFLoader – Load a PDF (One Document per Page)

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("deep_learning_curriculum.pdf")
docs = loader.load()

print(len(docs))               # number of pages (e.g., 23)
print(docs[0].page_content)    # text of first page
print(docs[0].metadata)        # includes page number, source, etc.
```

> **Note:** PyPDFLoader works well for text‑based PDFs. For scanned PDFs or complex layouts, use other loaders like `UnstructuredPDFLoader`, `PDFPlumberLoader`, etc.

---

### 5. DirectoryLoader – Load All PDFs in a Folder

```python
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books/",                    # folder path
    glob="*.pdf",                     # pattern: all PDFs
    loader_cls=PyPDFLoader           # loader to use for each file
)

docs = loader.load()
print(len(docs))  # total pages across all PDFs
```

**Other glob patterns:**
- `"*.txt"` – all text files
- `"**/*.pdf"` – PDFs in all subfolders
- `"data/*.csv"` – CSV files in data folder

---

### 6. Load vs Lazy Load – Memory Management

| Method | Behavior | Returns | When to use |
|--------|----------|---------|--------------|
| `loader.load()` | Eager – loads all documents at once | List of Documents | Small datasets |
| `loader.lazy_load()` | Lazy – loads one by one on demand | Generator of Documents | Large datasets (saves memory) |

**Example – lazy loading:**
```python
loader = DirectoryLoader("books/", glob="*.pdf", loader_cls=PyPDFLoader)

# Lazy load – returns a generator
for doc in loader.lazy_load():
    print(doc.metadata)   # processes one page at a time, memory efficient
```

> When you have hundreds of large PDFs, **always prefer `lazy_load()`** to avoid running out of RAM.

---

### 7. WebBaseLoader – Load Text from a Web Page

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.flipkart.com/macbook-air-m2/product")
docs = loader.load()   # single Document for the whole page

print(docs[0].page_content)  # extracted text (HTML tags removed)
```

> **Limitation:** Works best with static web pages (blogs, news articles). For JavaScript‑heavy pages, use `SeleniumURLLoader`.

**You can load multiple URLs at once:**
```python
loader = WebBaseLoader(["url1", "url2", "url3"])
docs = loader.load()   # returns list of Documents (one per URL)
```

---

### 8. CSVLoader – Load a CSV File (One Document per Row)

```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("social_network_ads.csv")
docs = loader.load()

print(len(docs))              # number of rows (e.g., 400)
print(docs[0].page_content)   # string like: "User ID: 1001, Gender: Male, Age: 32..."
print(docs[0].metadata)       # {'source': 'social_network_ads.csv', 'row': 0}
```

> Each row becomes a separate `Document`. Useful for querying tabular data with LLMs.

---

### 9. Other Useful Document Loaders (Quick Overview)

| Category | Examples |
|----------|----------|
| **Web** | `SeleniumURLLoader`, `UnstructuredURLLoader`, `AsyncHtmlLoader` |
| **Cloud** | `S3FileLoader`, `GoogleDriveLoader`, `AzureBlobStorageLoader` |
| **Social** | `TwitterTweetLoader`, `RedditPostsLoader` |
| **Productivity** | `NotionDirectoryLoader`, `SlackLoader`, `GmailLoader` |
| **Other formats** | `JSONLoader`, `MarkdownLoader`, `UnstructuredWordDocumentLoader` |
| **Media** | `YoutubeTranscriptLoader` |

> **Full list:** https://python.langchain.com/docs/integrations/document_loaders/

---

### 10. Custom Document Loader (Concept)

If your data source isn't supported, create a custom loader by inheriting from `BaseLoader`:

```python
from langchain_community.document_loaders import BaseLoader
from langchain_core.documents import Document

class MyCustomLoader(BaseLoader):
    def __init__(self, source):
        self.source = source
    
    def lazy_load(self):
        # Fetch data from your custom source
        # Yield Document objects one by one
        yield Document(page_content="...", metadata={"source": self.source})
    
    # Or implement .load() using .lazy_load()
```

> Most community loaders are built this way – you can contribute your own!

---

## 🔁 Summary Table – Loaders Covered

| Loader | Source | Output | Key method |
|--------|--------|--------|-------------|
| `TextLoader` | .txt file | 1 Document per file | `.load()` |
| `PyPDFLoader` | PDF file | 1 Document per page | `.load()` |
| `DirectoryLoader` | Folder | Multiple Documents (all files) | `.load()` / `.lazy_load()` |
| `WebBaseLoader` | Web page URL | 1 Document per URL | `.load()` |
| `CSVLoader` | CSV file | 1 Document per row | `.load()` |

---

## 📌 Final Takeaway

> **Document Loaders are the first step in any RAG pipeline.** They bring external data (PDFs, websites, CSVs, etc.) into LangChain as standardized `Document` objects. Use `lazy_load()` for large datasets to save memory. There are 100+ loaders – learn the basic pattern (import → create loader object → call load/lazy_load) and you can use any of them.

### Imp Links

- [Langchain Document Loaders](https://reference.langchain.com/python/langchain-community/document-loaders)

---

## 13. Text Splitters in LangChain (59:00)

## 🧑‍🏫 What This lecture Covers

This lecture explains why text splitting is essential for RAG applications and then dives into **four text splitting techniques** in LangChain:
1. **Length‑based** (fixed character/token count)
2. **Text‑structure based** (recursive – paragraphs → sentences → words → characters)
3. **Document‑structure based** (for code, Markdown, HTML)
4. **Semantic meaning based** (experimental – uses embeddings to detect topic changes)

---

## ✅ Important Pointers (Key Takeaways)

1. **Why split text?**
   - LLMs have **context length limits** (e.g., 50k tokens). Large documents won't fit.
   - **Better embeddings** – small chunks capture semantic meaning more accurately.
   - **Better semantic search** – focused chunks give more relevant results.
   - **Better summarization** – LLMs perform worse on very long texts (drift, hallucination).
   - **Computational efficiency** – smaller chunks use less memory and allow parallel processing.

2. **Length‑based splitting** (`CharacterTextSplitter`):
   - Simplest and fastest. Splits at exact character count.
   - **Pros:** simple, fast. **Cons:** ignores grammar; can cut words/sentences in half.

3. **Text‑structure based splitting** (`RecursiveCharacterTextSplitter`):
   - Tries to split on **paragraphs first**, then **sentences**, then **words**, then **characters**.
   - **Most recommended** – preserves natural language boundaries.
   - Uses a list of separators: `["\n\n", "\n", " ", ""]`

4. **Chunk overlap**:
   - Number of characters shared between consecutive chunks.
   - Helps retain context lost at the cut.
   - Recommended overlap: **10–20% of chunk size** (e.g., 100‑char chunks → 10‑20 overlap).

5. **Document‑structure based splitting**:
   - Extension of recursive splitting for **code** (Python, JS, Java, etc.), **Markdown**, **HTML**.
   - Uses language‑specific separators (e.g., `class`, `def`, `function` for Python).

6. **Semantic meaning based splitting** (`SemanticChunker` – experimental):
   - Uses embeddings and similarity to detect where topic changes.
   - Not yet production‑ready; performance can be inconsistent.

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. Length‑Based Splitting – `CharacterTextSplitter`

```python
from langchain.text_splitter import CharacterTextSplitter

text = "Machine learning is amazing. It helps computers learn without being explicitly programmed."

splitter = CharacterTextSplitter(
    chunk_size=50,      # max characters per chunk
    chunk_overlap=0,    # no overlap
    separator=""        # split at exact count
)

chunks = splitter.split_text(text)
print(chunks)
# Output: ['Machine learning is amazing. It he', 'lps computers learn without be', 'ing explicitly programmed.']
# Notice words are cut in the middle.
```

**Add overlap to retain context:**
```python
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20, separator="")
chunks = splitter.split_text(long_text)
```

---

### 2. Text‑Structure Based – `RecursiveCharacterTextSplitter` (Recommended)

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""]   # try paragraphs, then lines, then words, then chars
)

chunks = splitter.split_text(long_text)
print(len(chunks))
```

**Why better?** It tries to split at paragraph breaks first, so you don't cut sentences in the middle unless absolutely necessary.

**Combine with document loader:**
```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("document.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)   # list of Document objects
```

---

### 3. Document‑Structure Based – For Code and Markdown

**For Python code – use language‑specific splitter:**
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import Language

python_code = """
class MyClass:
    def __init__(self):
        pass
    def my_method(self):
        return True
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_text(python_code)
print(len(chunks))   # Each class/method may become its own chunk
```

**Supported languages:** `PYTHON`, `JAVASCRIPT`, `JAVA`, `RUST`, `MARKDOWN`, `HTML`, `CPP`, `GO`, etc.

**For Markdown:**
```python
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=200,
    chunk_overlap=20
)
chunks = splitter.split_text(markdown_text)
```

---

### 4. Semantic Meaning Based – `SemanticChunker` (Experimental)

```python
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

# Use standard deviation as threshold
splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1.0   # 1 standard deviation
)

text = "Agriculture is important for farmers. The IPL is a cricket league. Terrorism is a global issue."
chunks = splitter.split_text(text)
print(len(chunks))   # Ideally 3 chunks, but may be inconsistent
```

**Other threshold types:** `"percentile"`, `"interquartile"`, `"gradient"`.

> **Note:** This is experimental – results may not be perfect. Use with caution.

---

## 🔁 Summary Table – Four Text Splitting Techniques

| Technique | LangChain Class | Best for | Pros | Cons |
|-----------|----------------|----------|------|------|
| **Length‑based** | `CharacterTextSplitter` | Quick prototyping | Very fast, simple | Cuts words/sentences, loses context |
| **Text‑structure (recursive)** | `RecursiveCharacterTextSplitter` | General RAG (most recommended) | Respects paragraphs/sentences | Slightly slower |
| **Document‑structure** | `RecursiveCharacterTextSplitter.from_language()` | Code, Markdown, HTML | Preserves code structure | Requires language specification |
| **Semantic** | `SemanticChunker` (experimental) | Topic‑based splitting | Understands meaning | Inconsistent, experimental |

---

## 📌 Final Takeaway

> **Use `RecursiveCharacterTextSplitter` for most RAG applications.** It balances speed and linguistic structure. Add `chunk_overlap` (10‑20% of `chunk_size`) to retain context. Only use `CharacterTextSplitter` for very simple tasks, and semantic splitting only for experimentation.

- [ChunkViz v0.1](https://chunkviz.up.railway.app/)

## How `RecursiveCharacterTextSplitter` Works ? 

The `RecursiveCharacterTextSplitter` is the most recommended text splitter in LangChain for RAG applications. It tries to split text **naturally** – at paragraph boundaries, then sentence boundaries, then word boundaries – before falling back to character‑level splitting. This preserves meaning and avoids cutting words or sentences in half.

---

### 🧠 Core Idea

Instead of cutting at a fixed character count no matter what (like `CharacterTextSplitter`), it **recursively** tries a list of **separators** (e.g., `"\n\n"`, `"\n"`, `" "`, `""`). For each separator, it attempts to split the text into chunks that fit within the `chunk_size`. If a chunk is still too large, it moves to the next separator in the list and splits that chunk further.

After splitting, it also **merges** small neighbouring chunks to get as close to `chunk_size` as possible (without exceeding it). This yields chunks that are both size‑controlled and semantically coherent.

---

### ⚙️ Step‑by‑Step Algorithm

Let’s use a concrete example:

**Text:**
```
First paragraph. It has two sentences. Here is the second sentence.
Second paragraph. This is another sentence.
```

**Settings:**
- `chunk_size = 25` characters (small for illustration)
- `chunk_overlap = 0` (for simplicity)
- `separators = ["\n\n", "\n", ".", " ", ""]`

#### Step 1 – Try the first separator `"\n\n"`
The text contains **one** `"\n\n"` (between the two paragraphs). Splitting on it gives:
- Chunk A: `"First paragraph. It has two sentences. Here is the second sentence."` (length ≈ 65 characters → too big)
- Chunk B: `"Second paragraph. This is another sentence."` (length ≈ 45 characters → too big)

Both exceed `chunk_size = 25`. So we move to the **next separator**.

#### Step 2 – Try separator `"\n"`
There is no `"\n"` inside either chunk (the original `\n\n` has been consumed). No split occurs.

#### Step 3 – Try separator `"."` (sentence boundary)
Split Chunk A on periods (`.`). Keep the period at the end of each sentence.

Chunk A becomes:
- `"First paragraph. "` (length 18) – fits
- `"It has two sentences. "` (length 23) – fits
- `"Here is the second sentence."` (length 27) – still too big

Chunk B becomes:
- `"Second paragraph. "` (length 18) – fits
- `"This is another sentence."` (length 24) – fits

Now we have sentences. But `"Here is the second sentence."` is still 27 characters > 25. So we go deeper.

#### Step 4 – Try separator `" "` (word boundary)
Take the oversized sentence `"Here is the second sentence."` and split on spaces:
- `"Here"` (4)
- `"is"` (2)
- `"the"` (3)
- `"second"` (6)
- `"sentence."` (9)

Now we have very small chunks (words). None exceed `chunk_size`. The splitter then **merges** neighbouring words to create larger chunks without exceeding `chunk_size`.

For example, merge `"Here"` + `"is"` + `"the"` → `"Here is the"` (11 chars). Add `"second"` → `"Here is the second"` (17 chars). Add `"sentence."` would make 26 > 25, so stop. New chunk: `"Here is the second"`. Remaining `"sentence."` becomes its own chunk.

#### Step 5 – Final chunks (without overlap)
After merging, you get something like:
1. `"First paragraph. "`
2. `"It has two sentences. "`
3. `"Here is the second"`
4. `"sentence."`
5. `"Second paragraph. "`
6. `"This is another sentence."`

> Notice no chunk exceeds 25 characters, and most are **full sentences** or **fragments of a sentence** – still much better than cutting inside a word.

---

### 🔁 What if `chunk_overlap > 0`?

If `chunk_overlap = 10`, the splitter will make sure that the last 10 characters of chunk N become the first 10 characters of chunk N+1. This helps retain context that would otherwise be lost at the cut.

Example (simplified):
- Chunk 1: characters 0‑100
- Chunk 2: characters 90‑190 (overlap of last 10 chars of chunk 1)

---

### 💻 Basic Code Example

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Sample text
text = """First paragraph. It has two sentences. Here is the second sentence.
Second paragraph. This is another sentence."""

# Create splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=25,
    chunk_overlap=0,
    separators=["\n\n", "\n", ".", " ", ""]
)

# Split
chunks = splitter.split_text(text)

# Print results
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk}")
```

**Output (will be similar to the steps above):**
```
Chunk 0: First paragraph.
Chunk 1: It has two sentences.
Chunk 2: Here is the second
Chunk 3: sentence.
Chunk 4: Second paragraph.
Chunk 5: This is another sentence.
```

---

### ✅ Why It’s Better Than `CharacterTextSplitter`

| Feature | `CharacterTextSplitter` | `RecursiveCharacterTextSplitter` |
|---------|------------------------|----------------------------------|
| Splitting logic | Exact character count | Tries natural boundaries first |
| Word cutting | Yes, can cut inside a word | Avoids unless forced |
| Sentence integrity | No | Tries to keep sentences whole |
| Custom separators | Only one | List of separators (recursive) |
| Output quality | Poor for semantic search | Much better |

---

### 🧠 Key Takeaways

- **RecursiveCharacterTextSplitter** is the go‑to splitter for RAG.
- It works by **trying separators in order** (paragraph → sentence → word → character).
- If a chunk is too large, it goes **one level deeper** (recursively) for that chunk.
- After splitting, it **merges** small adjacent chunks to optimize size.
- Use `chunk_overlap` (10‑20% of chunk size) to prevent context loss at boundaries.

> **Rule of thumb:** Start with `chunk_size = 500` and `chunk_overlap = 50`, adjust based on your document type and embedding model requirements.

---

## 14. Vector Stores in LangChain (50:30)

## 🧑‍🏫 What This lecture Covers

This lecture explains **Vector Stores** – the third core component of a RAG pipeline. It starts with a real‑world problem (movie recommendation) to show why keyword matching fails and why we need **semantic similarity** using embeddings. Then it defines vector stores, their four key features, the difference between a vector store and a vector database, and how LangChain provides a **unified interface** for many vector stores (Chroma, FAISS, Pinecone, Qdrant, etc.). A hands‑on demo with **Chroma DB** shows how to create a vector store, add/update/delete documents, perform similarity search, and filter by metadata. Finally, an assignment asks to reimplement the same workflow with another vector store (FAISS or Pinecone). Below we complete the assignment using **FAISS**.

---

## ✅ Important Pointers (Key Takeaways)

1. **Keyword matching** is too simplistic for recommendation systems – two movies can have the same director/actor but completely different stories (e.g., *My Name Is Khan* vs *Kabhi Alvida Na Kehna*). Conversely, movies with similar themes but no common keywords (e.g., *Taare Zameen Par* and *A Beautiful Mind*) are never matched.
2. **Better approach:** Compare the semantic meaning of movie plots using **embeddings** – numerical vectors that capture meaning. Embeddings are generated by an embedding model (e.g., OpenAI’s `text-embedding-3-large`).
3. **Three main challenges** when working with embeddings:
   - Generating embeddings for millions of items.
   - Storing them efficiently (relational DBs are poor at vector operations).
   - Performing fast similarity search (comparing one vector against all stored vectors is too slow).
4. **Vector Store** = a system designed to store vectors and enable fast similarity search using indexing (e.g., clustering, HNSW). It provides:
   - **Storage** (in‑memory or on disk, with optional metadata)
   - **Similarity search** (find vectors closest to a query)
   - **Indexing** (speed up searches, e.g., approximate nearest neighbour)
   - **CRUD operations** (add, update, delete)
5. **Vector Store vs Vector Database:**
   - **Vector Store** (e.g., FAISS) – lightweight, good for prototyping, lacks full database features (transactions, authentication, distributed architecture).
   - **Vector Database** (e.g., Pinecone, Chroma) – full‑fledged with persistence, auth, backups, etc.  
     *Every vector database is a vector store, but not every vector store is a vector database.*
6. **LangChain’s unified interface** – all major vector stores share the same method names:  
   `from_documents`, `add_documents`, `similarity_search`, `similarity_search_with_score`, `delete`, `update_document` (where supported). This makes switching between stores easy.
7. **Chroma** is a lightweight, open‑source vector database that sits between a pure store and a full database – great for local development and small/medium production.

---

## 📚 Important Concepts Explained (with Basic Code Examples)

### 1. Generating Embeddings (Using OpenAI)

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector = embeddings.embed_query("A movie about a genius mathematician struggling with mental illness.")
print(len(vector))   # e.g., 3072 dimensions
```

### 2. Creating a Vector Store from Documents (Chroma)

```python
from langchain_chroma import Chroma
from langchain_core.documents import Document

docs = [
    Document(page_content="Virat Kohli is a batsman.", metadata={"team": "RCB"}),
    Document(page_content="Jasprit Bumrah is a bowler.", metadata={"team": "MI"}),
]

vector_store = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db")
```

### 3. Similarity Search

```python
results = vector_store.similarity_search("Who is a bowler?", k=1)
print(results[0].page_content)   # Jasprit Bumrah is a bowler.

# With distance scores (lower = closer)
results_with_scores = vector_store.similarity_search_with_score("Who is a bowler?", k=2)
for doc, score in results_with_scores:
    print(f"Score: {score:.4f} | {doc.page_content}")
```

### 4. Metadata Filtering

```python
# Only return documents where team == "CSK"
filtered = vector_store.similarity_search("Captain", k=2, filter={"team": "CSK"})
```

### 5. Adding, Updating, Deleting

```python
# Add
new_doc = Document(page_content="MS Dhoni is a captain.", metadata={"team": "CSK"})
vector_store.add_documents([new_doc])

# Update (requires document ID – get it from .get() or when adding)
vector_store.update_document(doc_id, updated_doc)

# Delete
vector_store.delete(ids=[doc_id])
```

---

## 📌 Assignment: Reimplement the Chroma Demo with FAISS

### Setup

```bash
pip install langchain langchain-community langchain-openai faiss-cpu
```

Below is the complete FAISS implementation that mirrors all the operations shown in the Chroma demo (create, add, view, search, filter, update, delete). The LangChain interface remains almost identical – only the import and a few details (like saving/loading) differ.

```python
import os
import shutil
import uuid
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# ---------- 1. Clean previous data (for demonstration) ----------
PERSIST_DIR = "./faiss_db"
if os.path.exists(PERSIST_DIR):
    shutil.rmtree(PERSIST_DIR)

# ---------- 2. Create embedding model ----------
embeddings = OpenAIEmbeddings()

# ---------- 3. Create cricket player documents ----------
documents = [
    Document(page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history.",
             metadata={"team": "RCB"}),
    Document(page_content="Rohit Sharma is known for his elegant batting and record 5 IPL titles as captain.",
             metadata={"team": "MI"}),
    Document(page_content="MS Dhoni is famous for his calm captaincy and finishing skills. He led CSK to multiple titles.",
             metadata={"team": "CSK"}),
    Document(page_content="Jasprit Bumrah is a fast bowler with a unique action. He is a key wicket‑taker for MI.",
             metadata={"team": "MI"}),
    Document(page_content="Ravindra Jadeja is an exceptional all‑rounder, great with both bat and ball. He plays for CSK.",
             metadata={"team": "CSK"}),
]

# ---------- 4. Create vector store from documents ----------
vector_store = FAISS.from_documents(documents, embeddings)
vector_store.save_local(PERSIST_DIR)   # persist to disk

print("Documents added successfully.")

# ---------- 5. View all documents (similar to Chroma's .get()) ----------
all_data = vector_store.get()
print(f"\nTotal documents: {len(all_data['ids'])}")
print("Document IDs:", all_data['ids'])
print("Metadatas:", all_data['metadatas'])

# ---------- 6. Similarity search (without scores) ----------
query = "Who among these is a bowler?"
print("\n=== Similarity Search (k=2) ===")
results = vector_store.similarity_search(query, k=2)
for doc in results:
    print(f"- {doc.page_content}")

# ---------- 7. Similarity search with scores (lower = better) ----------
print("\n=== Similarity Search with Scores ===")
results_with_score = vector_store.similarity_search_with_score(query, k=2)
for doc, score in results_with_score:
    print(f"Score: {score:.4f} | {doc.page_content}")

# ---------- 8. Metadata filtering ----------
print("\n=== Filtered Search (team = CSK) ===")
filtered_results = vector_store.similarity_search(
    query="Who is a great all‑rounder?",
    k=2,
    filter={"team": "CSK"}
)
for doc in filtered_results:
    print(f"- {doc.page_content}")

# ---------- 9. Add a new document ----------
new_doc = Document(page_content="Hardik Pandya is a dynamic all‑rounder and captain of Gujarat Titans.",
                   metadata={"team": "GT"})
new_id = str(uuid.uuid4())                 # generate a custom ID
vector_store.add_documents([new_doc], ids=[new_id])
vector_store.save_local(PERSIST_DIR)       # persist after addition

print("\nNew document added.")

# ---------- 10. Update an existing document (FAISS has no native update – delete + add) ----------
# Find the ID of the document we want to update (Virat Kohli)
target_id = None
for i, meta in enumerate(all_data["metadatas"]):
    if meta.get("team") == "RCB":
        target_id = all_data["ids"][i]
        break

if target_id:
    # Delete the old document
    vector_store.delete(ids=[target_id])
    # Add the updated version using the same ID
    updated_doc = Document(
        page_content="Virat Kohli, the former captain of RCB, is renowned for his aggressive leadership and batting consistency.",
        metadata={"team": "RCB"}
    )
    vector_store.add_documents([updated_doc], ids=[target_id])
    vector_store.save_local(PERSIST_DIR)
    print(f"\nDocument with ID {target_id} updated successfully.")
else:
    print("\nCould not find document with team='RCB' to update.")

# ---------- 11. Delete a document (example: delete the newly added Hardik Pandya) ----------
# We can delete by ID (we already have `new_id` from earlier)
vector_store.delete(ids=[new_id])
vector_store.save_local(PERSIST_DIR)
print(f"\nDocument with ID {new_id} deleted.")

# ---------- 12. Verify final state ----------
final_data = vector_store.get()
print(f"\nFinal document count: {len(final_data['ids'])}")
print("Remaining IDs:", final_data['ids'])
```

### Differences Between Chroma and FAISS in This Implementation

| Operation               | Chroma                                      | FAISS                                                  |
|-------------------------|---------------------------------------------|--------------------------------------------------------|
| **Import**              | `from langchain_chroma import Chroma`       | `from langchain_community.vectorstores import FAISS` |
| **Create from docs**    | `Chroma.from_documents(...)`                | `FAISS.from_documents(...)`                           |
| **Persistence**         | Optional (`persist_directory`) – SQLite     | Manual `.save_local()` and `.load_local()`            |
| **View all documents**  | `.get()` returns ids, docs, metadatas       | ✅ Same                                                |
| **Update document**     | `.update_document(id, doc)`                 | ❌ Not available – must delete + add with same ID     |
| **Delete**              | `.delete(ids=[...])`                        | ✅ Same                                                |
| **Similarity search**   | `.similarity_search()`                      | ✅ Same                                                |
| **Scores**              | `.similarity_search_with_score()` returns distance (lower = better) | ✅ Same (L2 distance)                     |
| **Metadata filtering**  | `filter={"team": "CSK"}`                    | ✅ Same                                                |

> **Note:** FAISS does not natively support `update_document()`. The code above demonstrates the recommended workaround: delete the old document and add the updated one using the same ID.

---

> **Final takeaway:** Vector stores are the heart of semantic search. LangChain’s unified interface lets you switch between Chroma, FAISS, Pinecone, etc. with minimal code changes – focus on your application logic, not the underlying database.

---

## 15. Retrievers in LangChain (51:09)

## 🧑‍🏫 What This lecture Covers

This lecture explains **Retrievers** – the component that fetches relevant documents from a data source in response to a user query. He covers:
- What retrievers are and why they are essential in RAG
- Types of retrievers based on **data source** (Wikipedia, Vector Store)
- Types based on **retrieval strategy** (MMR, Multi-Query, Contextual Compression)
- How to implement them in LangChain with code examples

---

## ✅ Important Pointers (Key Takeaways)

1. **Retriever** = a component that takes a user query and returns a list of relevant LangChain `Document` objects from a data source (vector store, API, database, etc.).
2. **Retrievers are Runnables** – they have an `invoke()` method, so you can use them inside chains.
3. **Two ways to categorize retrievers:**
   - By **data source** (Wikipedia, Vector Store, Arxiv, etc.)
   - By **retrieval strategy** (MMR, Multi‑Query, Contextual Compression, etc.)
4. **Wikipedia Retriever** – queries Wikipedia API (keyword matching, not semantic). Returns Wikipedia articles as Documents.
5. **Vector Store Retriever** – the most common. Wraps a vector store (Chroma, FAISS, Pinecone) and performs semantic similarity search.
6. **MMR (Maximum Marginal Relevance)** – reduces redundancy in results by balancing relevance and diversity. Returns documents that are relevant but also different from each other.
7. **Multi‑Query Retriever** – uses an LLM to generate multiple alternative queries from the original ambiguous query, fetches results for each, then combines and deduplicates. Improves retrieval for vague questions.
8. **Contextual Compression Retriever** – after fetching documents, uses an LLM to compress each document, keeping only the parts relevant to the query. Reduces noise and improves answer accuracy.
9. LangChain has **many other retrievers** (Parent Document, Time‑Weighted, Self‑Query, Ensemble, etc.) – you can explore them in the documentation.

---

## 📚 Important Concepts Explained (with Code Examples)

### 1. What is a Retriever?

**Definition:** A component that takes a user query and returns relevant documents from a data source.

```python
# A retriever is a Runnable – you can invoke it like a model
docs = retriever.invoke("What is climate change?")
# Returns list of Document objects (page_content + metadata)
```

---

### 2. Wikipedia Retriever (Data Source: Wikipedia API)

```python
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2, lang="en")

query = "The geopolitical history of India and Pakistan from a Chinese perspective"
docs = retriever.invoke(query)

for doc in docs:
    print(doc.page_content[:200])   # first 200 chars
```

> **Note:** Uses **keyword matching**, not semantic search. Good for quick fact‑retrieval from Wikipedia.

---

### 3. Vector Store Retriever (Most Common)

Wrap any vector store (Chroma, FAISS, Pinecone) into a retriever.

```python
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

# Create sample documents
docs = [
    Document(page_content="LangChain is a framework for building LLM apps.", metadata={"topic": "langchain"}),
    Document(page_content="Chroma is a vector database.", metadata={"topic": "chroma"}),
    Document(page_content="Embeddings convert text to vectors.", metadata={"topic": "embeddings"}),
]

# Create vector store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)

# Create retriever from vector store
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# Retrieve
query = "What is Chroma used for?"
docs = retriever.invoke(query)
for doc in docs:
    print(doc.page_content)
```

> You can also use `similarity_search` directly on the vector store, but the retriever is a **Runnable** – easier to chain.

---

### 4. MMR Retriever (Maximum Marginal Relevance)

MMR balances **relevance** and **diversity** – avoids returning very similar documents.

```python
# Create retriever with MMR
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.5}
)
# lambda_mult = 1 → pure similarity (no diversity)
# lambda_mult = 0 → maximum diversity (less relevance)
# 0.5 is a good balance

docs = retriever.invoke("What is LangChain?")
for doc in docs:
    print(doc.page_content)
```

> Use when your query could return many redundant documents (e.g., multiple paragraphs saying the same thing).

---

### 5. Multi‑Query Retriever

For ambiguous queries, generate multiple alternative queries using an LLM, retrieve for each, then combine results.

```python
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI

# Base retriever (e.g., similarity search)
base_retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# Multi‑Query retriever
llm = ChatOpenAI(model="gpt-3.5-turbo")
retriever = MultiQueryRetriever.from_llm(
    retriever=base_retriever,
    llm=llm
)

# Query with ambiguity
docs = retriever.invoke("How to improve energy levels and maintain balance?")
for doc in docs:
    print(doc.page_content)
```

> **How it works:** The LLM generates different phrasings of the query, runs each through the base retriever, merges all results, and removes duplicates.

---

### 6. Contextual Compression Retriever

Retrieves documents using a base retriever, then **compresses** each document (keeping only query‑relevant parts) using an LLM.

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import ChatOpenAI

# Base retriever (e.g., similarity)
base_retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# Compressor (LLM that extracts relevant parts)
llm = ChatOpenAI(model="gpt-3.5-turbo")
compressor = LLMChainExtractor.from_llm(llm)

# Contextual compression retriever
retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

# Query
docs = retriever.invoke("What is photosynthesis?")
for doc in docs:
    print(doc.page_content)   # Only the sentence(s) about photosynthesis
```

> **Use case:** When your documents contain multiple topics or extra information. The compressor removes irrelevant parts, giving the LLM cleaner context.

---

## 🔁 Summary Table – Retrievers Covered

| Retriever | Strategy | Best for |
|-----------|----------|----------|
| **WikipediaRetriever** | Keyword matching on Wikipedia | Quick facts from Wikipedia |
| **VectorStoreRetriever** | Semantic similarity (embeddings) | Most RAG applications |
| **MMR Retriever** | Relevance + Diversity | Avoiding redundant results |
| **MultiQueryRetriever** | Generate multiple query variants | Ambiguous / broad queries |
| **ContextualCompressionRetriever** | Extract only relevant parts from long documents | Noisy or mixed‑content documents |

---

## 📌 Final Takeaway

> **Retrievers are the bridge between your data and the LLM.** Start with a simple `VectorStoreRetriever`. When your RAG system needs improvement, experiment with advanced retrievers like MMR (for diversity), Multi‑Query (for ambiguous queries), or Contextual Compression (for long/noisy documents).


### Types of Retrievers 
1. Data Source Retrievers
2. Search Strategies Retrievers

#### Data Source Retrievers
- Wikipedia Retriever
- Vector Store Retriever
- Archive Retrievers

#### Search Strategies Retrievers (different search strategies used in Retrievers) :-
- Maximum Marginal Relevance (MMR)
- Multi Query Retriever 
- Contextual Compression Retriever 

#### Useful Links

- [Retrievers](https://reference.langchain.com/python/langchain-community/retrievers)

- [Retrievers Integration](https://docs.langchain.com/oss/python/integrations/retrievers/)

---

## 16. Retrieval Augmented Generation (59:23)

## 🧑‍🏫 What This lecture Covers

This lecture explains **RAG** – why it’s needed, how it works step by step, and how it compares to fine‑tuning. He covers:
- Three major problems with LLMs (private data, recent data, hallucination)
- Fine‑tuning as a solution – but it has drawbacks (expensive, requires expertise, frequent re‑training)
- **In‑context learning** – LLMs can learn from examples given in the prompt (few‑shot prompting)
- **RAG** = retrieve relevant context from an external knowledge base and inject it into the prompt
- The four stages of a RAG system: **Indexing**, **Retrieval**, **Augmentation**, **Generation**
- How RAG solves the three problems better than fine‑tuning
- Next video: build a RAG system with LangChain

---

## ✅ Important Pointers (Key Takeaways)

1. **Three problems of plain LLMs (no external data):**
   - ❌ **Private data** – LLM wasn’t trained on your company’s internal documents.
   - ❌ **Recent data** – LLM has a knowledge cutoff date; can’t answer about current events.
   - ❌ **Hallucination** – LLM may confidently generate false information.

2. **Fine‑tuning** – retrain a pre‑trained LLM on a small, domain‑specific dataset.  
   - It can solve the three problems, but has major downsides:
     - 🧠 **Computationally expensive** – needs GPUs, time, money.
     - 👨‍🔧 **Requires ML expertise** – not for everyone.
     - 🔁 **Frequent updates** – each new document requires re‑training.

3. **In‑context learning** – LLMs can learn from examples provided *inside the prompt* (few‑shot prompting).  
   - This is an **emergent property** of large models (GPT‑3 and above).  
   - No weight updates – just examples in the prompt.

4. **RAG** = give the LLM **relevant context** (retrieved from your own documents) together with the user’s query.  
   - The LLM answers based on that context, not just its internal knowledge.

5. **Four stages of RAG:**
   - **Indexing** (offline) – prepare the external knowledge base.
   - **Retrieval** (real‑time) – find relevant context for the query.
   - **Augmentation** – combine query + context into a prompt.
   - **Generation** – LLM produces the final answer.

6. **RAG vs fine‑tuning – RAG wins for dynamic, cost‑sensitive, and non‑expert setups:**
   - No re‑training needed – just add/remove documents from the vector store.
   - Cheaper and simpler.
   - Works with any LLM (no need to modify model weights).

---

## 📚 Detailed Explanation of RAG Stages (with Basic Code Concepts)

### Stage 1: Indexing – Building the External Knowledge Base

> **Goal:** Convert your documents into a searchable vector store.

**Sub‑steps:**

1. **Document Ingestion** – Load documents from any source (PDF, website, database, etc.)  
   *LangChain provides many document loaders.*

   ```python
   from langchain_community.document_loaders import PyPDFLoader
   loader = PyPDFLoader("company_policy.pdf")
   docs = loader.load()   # list of Document objects
   ```

2. **Text Chunking** – Split large documents into smaller, semantically meaningful chunks.  
   *Using `RecursiveCharacterTextSplitter` (recommended).*

   ```python
   from langchain.text_splitter import RecursiveCharacterTextSplitter
   splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
   chunks = splitter.split_documents(docs)
   ```

3. **Embedding** – Convert each chunk into a vector (embedding) that captures its meaning.  
   *Use an embedding model (OpenAI, HuggingFace, etc.)*

   ```python
   from langchain_openai import OpenAIEmbeddings
   embeddings = OpenAIEmbeddings()
   # Each chunk will be converted to a vector
   ```

4. **Store in Vector Store** – Save the vectors together with the original text and metadata.  
   *Options: FAISS (local), Chroma, Pinecone, etc.*

   ```python
   from langchain_community.vectorstores import FAISS
   vector_store = FAISS.from_documents(chunks, embeddings)
   vector_store.save_local("./faiss_index")
   ```

> After indexing, you have a **searchable external knowledge base**.

---

### Stage 2: Retrieval – Finding Relevant Context for a Query

> **Goal:** Given a user query, fetch the most relevant chunks from the vector store.

**Steps:**

1. **Convert query to vector** using the same embedding model used during indexing.
2. **Perform similarity search** (e.g., cosine similarity) to find the closest vectors in the store.
3. **Rank and return** the top‑k chunks (these become the **context**).

```python
# Load the vector store (if previously saved)
vector_store = FAISS.load_local("./faiss_index", embeddings)

# Create a retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# User query
query = "What is the leave policy for new employees?"
context_docs = retriever.invoke(query)   # list of Document objects
context = "\n".join([doc.page_content for doc in context_docs])
```

> LangChain provides advanced retrievers (MMR, Multi‑Query, Contextual Compression) for better results.

---

### Stage 3: Augmentation – Building the Prompt with Context

> **Goal:** Combine the user’s query and the retrieved context into a single prompt that instructs the LLM to answer **only from the context**.

**Example prompt template:**

```
You are a helpful assistant. Answer the question based ONLY on the provided context.
If the context does not contain the answer, say "I don't know".

Context:
{context}

Question: {question}
Answer:
```

```python
from langchain_core.prompts import PromptTemplate

template = """
You are a helpful assistant. Answer the question based ONLY on the provided context.
If the context does not contain the answer, say "I don't know".

Context:
{context}

Question: {question}
Answer:
"""

prompt = PromptTemplate(template=template, input_variables=["context", "question"])
```

---

### Stage 4: Generation – Producing the Final Answer

> **Goal:** Send the augmented prompt to an LLM and get the answer.

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")

# Create a chain that combines prompt, model, and a simple output parser
from langchain_core.output_parsers import StrOutputParser

chain = prompt | model | StrOutputParser()

answer = chain.invoke({"context": context, "question": query})
print(answer)
```

> The LLM uses both its own parametric knowledge and the provided context, but the prompt forces it to **ground** the answer in the context, reducing hallucination.

---

## 🔁 Complete RAG Pipeline (Conceptual Code)

```python
# 1. Indexing (one‑time setup)
loader = PyPDFLoader("doc.pdf")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(chunks, embeddings)

# 2. Retrieval (per query)
retriever = vector_store.as_retriever(k=3)
query = "What is the refund policy?"
context_docs = retriever.invoke(query)
context = "\n".join([d.page_content for d in context_docs])

# 3. Augmentation + 4. Generation
prompt = PromptTemplate.from_template(
    "Context: {context}\nQuestion: {question}\nAnswer based only on context:"
)
chain = prompt | ChatOpenAI() | StrOutputParser()
answer = chain.invoke({"context": context, "question": query})
print(answer)
```

---

## 🆚 RAG vs Fine‑Tuning – Summary

| Aspect                | Fine‑Tuning                                    | RAG                                             |
|-----------------------|------------------------------------------------|-------------------------------------------------|
| **Updates**           | Re‑train the model for each new document       | Just add/remove documents from vector store    |
| **Cost**              | High (GPUs, time, expertise)                   | Low (embedding + vector search)                |
| **Knowledge source**  | Becomes part of model weights (parametric)     | External (non‑parametric) – easily inspectable |
| **Hallucination**     | Can still happen if training data is noisy     | Greatly reduced – forced to use context        |
| **Freshness**         | Requires re‑training to stay current           | Add latest docs instantly                       |
| **Explainability**    | Hard – you don’t know which training example was used | Easy – you can show the retrieved context |

---

## 🔍 How RAG Solves the Three Problems

| Problem                | How RAG fixes it                                              |
|------------------------|---------------------------------------------------------------|
| **Private data**       | Context comes from your own vector store (your documents).    |
| **Recent data**        | Add new documents to the vector store – no re‑training.       |
| **Hallucination**      | Prompt forces LLM to answer *only* from provided context – if context lacks info, LLM says “I don’t know”. |

---

## 📌 Final Takeaway

> **RAG = retrieve relevant context + augment the prompt + generate grounded answers.**  
> It’s cheaper, simpler, and more flexible than fine‑tuning for most real‑world applications where data changes frequently or you don’t have ML engineering resources.  
> **Next video:** Build a complete RAG system using LangChain – combining all four components (loaders, splitters, vector stores, retrievers, LLMs).

---

## More Readings

## 🧠 Parametric Knowledge of an LLM – Explained Simply

### What is Parametric Knowledge?

> **Parametric knowledge** is all the information that an LLM (Large Language Model) learns during its **pre‑training** phase and stores inside its **parameters** (weights and biases of the neural network).

When an LLM is trained on massive amounts of text (like the entire internet, books, articles), it doesn’t memorize sentences word‑for‑word. Instead, it learns patterns, facts, relationships, and structures, and encodes them as **numerical values** in its billions of parameters. Those numbers **are** the model’s knowledge.

After training, the model no longer has access to the original training data. It only has the parameters – hence the knowledge is called **parametric**.

---

### Why is Parametric Knowledge Useful (and Powerful)?

1. **Compact storage**  
   Billions of facts are compressed into a few gigabytes of numbers. No need to keep a huge database.

2. **Fast inference**  
   Answering a question requires only a forward pass through the network – no searching external databases.

3. **Generalisation**  
   The model can answer questions about topics it never saw exactly in training, because it has learned underlying patterns.

4. **Zero‑shot and few‑shot ability**  
   Even without fine‑tuning, a large LLM can perform new tasks just by reading the prompt – because its parametric knowledge provides a rich foundation.

---

### Basic Examples

#### Example 1 – Factual knowledge

**Question:** *“What is the capital of France?”*  
**LLM’s answer:** *“The capital of France is Paris.”*

- The LLM never saw a line saying “capital of France is Paris” for every possible phrasing.  
- During pre‑training, it saw the word “Paris” associated with “France” many times, in contexts like “Paris is the capital”, “France’s capital Paris”, etc.  
- It encoded that relationship into its parameters.  
- When you ask, it uses those parameters to generate the correct answer.

#### Example 2 – Reasoning without explicit training data

**Question:** *“If a train travels at 60 km/h for 2.5 hours, how far does it go?”*  
**LLM’s answer:** *“Distance = speed × time = 60 × 2.5 = 150 km.”*

- The LLM was never explicitly trained on that exact math problem.  
- Its parametric knowledge includes the mathematical relationship `distance = speed × time` and how to multiply.  
- It applies that knowledge to solve the problem on the fly.

#### Example 3 – Language understanding

**Prompt:** *“Translate ‘Good morning’ to Hindi.”*  
**LLM’s answer:** *“शुभ प्रभात”*

- The mapping between English and Hindi phrases is not stored as a lookup table.  
- The model learned patterns of translation from bilingual text during training.  
- That knowledge is distributed across millions of parameters.

---

### Where Parametric Knowledge Falls Short – Why We Need RAG

Parametric knowledge has limits:

| Limitation | Example |
|------------|---------|
| **Private data** | Your company’s internal policies – never seen during training. |
| **Recent events** | “Who won the latest IPL match?” – training data is outdated. |
| **Hallucination** | The model may invent plausible but false facts because it “knows” patterns, not truth. |

That’s why **RAG (Retrieval‑Augmented Generation)** adds **non‑parametric knowledge** – external documents – to supplement the model’s parametric memory.

---

### Final Analogy

> **Parametric knowledge** = what you learned in school and still remember without looking up.  
> **RAG** = looking up an encyclopedia while answering a question – you still use your brain, but you also refer to fresh, specific information.

--- 

## How LLM Parameters Actually Store Knowledge – A Deeper Look

This is a fascinating (and complex) topic. Let’s break it down without heavy math.

---

## 1. What Are Parameters?

In a neural network, **parameters** are the **weights** and **biases** of all the connections between neurons.  
For an LLM like GPT‑3, there are about **175 billion parameters**.

Think of parameters as **knobs** or **dials** inside a giant machine.  
Initially, these knobs are set randomly. During training, the machine adjusts them little by little so that given an input (e.g., “The capital of France is”), it turns the knobs to produce the correct output (“Paris”).

After training, the final positions of all knobs **store** everything the model has learned.

---

## 2. Knowledge is Not Stored in One Place – It’s Distributed

Unlike a database where “Paris” is linked to “France” in one row, LLM knowledge is **distributed across millions of parameters**. No single parameter knows “Paris”. Instead, patterns emerge from the **combination** of many parameters.

**Example analogy:**  
A symphony orchestra playing a melody. No single musician plays the whole tune; the melody exists in the collective interaction. Similarly, the fact “capital of France is Paris” is encoded in the collective activation patterns of thousands of neurons.

---

## 3. How Training Shapes Parameters

### Step 1 – Predict next word (pre‑training objective)
LLMs are trained to predict the next word given previous words.  
Example: *“The capital of France is ___”* → the correct next word is “Paris”.

Every time the model predicts correctly, the parameters are slightly adjusted to reinforce that pattern. Over billions of sentences, the parameters learn:
- Word meanings (semantics)
- Grammar (syntax)
- Relationships (e.g., “is capital of”)
- Common sense and reasoning

### Step 2 – Backpropagation and gradient descent
The model calculates an error (difference between its prediction and the true next word). Then it uses an algorithm called **backpropagation** to figure out which knobs (parameters) contributed to the error and how much to turn them to reduce the error next time. This is repeated trillions of times.

Over time, the parameters settle into a configuration that produces correct predictions for a vast range of inputs.

---

## 4. Where Is “Paris” Stored? – A Concrete Example

Consider a very simplified 2‑layer network that maps words to concepts.  
In reality, LLMs have many more layers (e.g., 96 layers in GPT‑3), each with many “attention heads”.

**Word embeddings:** Each word is first converted into a vector (list of numbers). For example, “Paris” might be represented as `[0.2, 0.7, -0.3, …]`. These embeddings are also learned parameters (the “embedding matrix”).

**Attention weights:** When the model reads “The capital of France is”, attention mechanisms assign high weight to the words “capital” and “France” and learn that the next word should be a city that is associated with “capital” and “France”. The attention weights are parameters that encode *relationships*.

**Feed‑forward weights:** After attention, the information passes through dense layers. These layers combine and transform the information. The ability to retrieve “Paris” as the answer is the result of many such transformations.

So “Paris” is not stored as a string. Instead, there is a **path** through the network that, when triggered by the context “capital of France”, leads to the vector for “Paris” being generated.

---

## 5. Emergent Properties – Why Large Models Work Better

When the model has only a few parameters (e.g., 10 million), it can’t capture fine‑grained relationships; it may store only simple word co‑occurrence statistics.

With billions of parameters, the model can learn:
- **Multi‑hop reasoning** (e.g., “A is taller than B, B is taller than C → A is taller than C”)
- **Abstract concepts** (e.g., “justice”, “humour”)
- **Few‑shot learning** – the model can infer a new task from just a few examples in the prompt, because its parameters have learned the *meta‑pattern* of learning from examples.

These **emergent abilities** appear only at large scale. That’s why bigger models (more parameters) are generally more capable.

---

## 6. Limitations – Why Parameters Aren’t Perfect

- **Static knowledge** – Once training is finished, the parameters don’t change. New events (e.g., “2025 election results”) are not known.
- **Hallucination** – Because knowledge is distributed, the model can sometimes combine patterns in plausible‑sounding but incorrect ways. It doesn’t “know” that it doesn’t know.
- **No source attribution** – You can’t ask the model “which training document said that?”.

That’s why **RAG (Retrieval‑Augmented Generation)** combines parametric knowledge (the model) with non‑parametric knowledge (external documents). The model still uses its parameters for language understanding, reasoning, and generation, but it also refers to retrieved text to ensure accuracy and freshness.

---

## 7. Simple Code Intuition (Not Real LLM Code)

Imagine a tiny “parametric knowledge” as a Python dictionary, but in reality it’s billions of numbers:

```python
# This is a metaphor – real parameters are not explicit key‑value pairs.
parametric_knowledge = {
    "capital_of_France": "Paris",
    "speed×time": "distance",
    # ... billions of such patterns encoded in numbers
}
```

The LLM’s parameters are like a **very high‑dimensional, fuzzy, overlapping dictionary**. When you ask a question, the model runs a computation that essentially “looks up” the answer by activating the relevant combination of parameters.

---

## Final Takeaway

> **LLM parameters store knowledge as numerical patterns that, when activated together, produce correct words and reasoning.**  
> This compression is incredibly powerful – it allows generalisation, reasoning, and language fluency – but it is static and can produce errors.  
> That’s why we augment parametric knowledge with external, non‑parametric data in systems like RAG.

---

## Everything about **Fine Tuning**

### 🎯 What is Fine-Tuning & Why Do It?

Fine-tuning is the process of taking a pre-trained Large Language Model (LLM) and continuing its training on a smaller, task-specific dataset. Think of the pre-trained model as a well-educated generalist who has read much of the internet. Fine-tuning makes that generalist a specialist in your domain—whether that's answering medical questions, handling legal documents, or writing code in your company’s style.

This process modifies the model's internal parameters, allowing it to learn new patterns and adapt to your specific task.

#### **Key Advantages**

*   **Domain Specialization**: Adapts general-purpose models to excel in a particular field.
*   **Performance Gains**: Models learn industry-specific terminology and problem-solving patterns, leading to higher accuracy on focused tasks.
*   **Cost & Privacy**: It's dramatically cheaper than training a model from scratch and can be performed on your own infrastructure, keeping data private.
*   **Model Compression & Speed**: Combined with quantization, fine-tuned models can be compressed to a fraction of their size, enabling faster inference on everyday hardware.

#### **💡 When to Fine-Tune (and When Not To)**

Before committing to fine-tuning, consider simpler, less resource-intensive options.

*   **Use Prompt Engineering for simple tasks**: Well-crafted prompts can often steer a general LLM effectively without any training.
*   **Use RAG when you need up-to-date or specific information**: RAG lets the model look up external information, making it ideal for private documents or content that changes frequently. It also allows you to cite sources.
*   **Fine-Tune when you need to permanently change the model’s behavior**: This is best for:
    *   Mastering a consistent **style or tone** (e.g., a brand voice).
    *   Learning complex, domain-specific **rules and formats**.
    *   Reliably **following specific instructions** for a task like summarization.
    *   Developing complex **reasoning abilities** that are hard to capture with a prompt or RAG.

### 🛠️ The Main Approaches to Fine-Tuning

Fine-tuning methods are broadly divided into full parameter updates and efficient techniques that train only a fraction of the parameters.

#### **Full Fine-Tuning**

This traditional method updates **all** the model's weights during training, providing the highest degree of customization.

*   **Advantages**: Maximum adaptability to new domains, often yielding the best theoretical performance for complex tasks.
*   **Disadvantages**: Very demanding—training a 7B model can require over 100GB of VRAM and is extremely expensive. It’s also prone to **catastrophic forgetting**, where the model loses its general knowledge while specializing.

#### **⛓️ PEFT: The Efficient Revolution**

**PEFT** techniques have made fine-tuning accessible by drastically reducing memory and time requirements. They work by freezing the original model and training only a tiny number of additional parameters. This approach can slash memory use by **10 to 20 times** while preserving **90-95% of the performance** of full fine-tuning.

Let’s look at the key PEFT methods:

**LoRA (Low-Rank Adaptation)**
* **Core Idea**: Adds small "adapter" matrices alongside frozen model weights.
* **Key Characteristics**: Very efficient; adapters can be merged into the base weights for **zero inference latency**.
* **Resource Needs & Performance**:
  * Memory: ~28GB (for a 7B model)
  * Performance: **90-95% of full fine-tuning**
* **Best For**: General fine-tuning on limited but capable hardware (e.g., 24GB GPU).

**QLoRA (Quantized LoRA)**
* **Core Idea**: Takes LoRA further by quantizing the base model to 4-bit precision.
* **Key Characteristics**: The most memory-efficient technique, enabling fine-tuning of large models on consumer GPUs.
* **Resource Needs & Performance**:
  * Memory: Enables 33B+ models on a 24GB GPU
  * Performance: **80-90% of full fine-tuning**
* **Best For**: Resource-constrained environments where you need to fine-tune very large models.

**Other PEFT Variants**

*   **Prefix Tuning**: Trains small, continuous "virtual tokens" that are prepended to the input. It uses very few parameters (usually <1%).
*   **Adapter Tuning**: Inserts small adapter modules between the layers of a frozen Transformer model.
*   **BitFit**: An ultra-lightweight method that only fine-tunes the bias terms of the model, less than 0.1% of parameters.

### 🧠 Alignment Fine-Tuning: Shaping Model Behavior

While PEFT adapts *knowledge*, alignment techniques adapt the model's *behavior*, teaching it to follow instructions and align with human values.

*   **Supervised Fine-Tuning (SFT)**: Uses a dataset of explicit **input-output pairs** to teach the model how to behave. For instance, training it with examples of how a customer support agent should answer questions.
*   **Reinforcement Learning from Human Feedback (RLHF)**: This three-stage pipeline creates a highly aligned conversational AI:
    1.  **Supervised Fine-Tuning (SFT)**: Gives the model a baseline in the desired task.
    2.  **Reward Modeling**: Humans rank different model outputs to train a "reward model" that learns human preferences.
    3.  **Reinforcement Learning (RL)**: The model is fine-tuned using the reward model as a guide, learning to generate responses that achieve higher scores.
*   **Direct Preference Optimization (DPO)**: A simpler and more stable alternative to RLHF. It bypasses the need for a separate reward model by using preference data to directly optimize the policy.

### 💻 Putting It Into Practice: Code Examples

The easiest way to get started with fine-tuning is using the **Hugging Face `transformers`** and **`peft`** libraries.

#### **1. Basic Full Fine-Tuning with Hugging Face Trainer**

This example shows the workflow for full fine-tuning using the `Trainer` API.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer

model_name = "meta-llama/Llama-2-7b-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
# Add padding token if missing
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name)

# Assume you've created a 'dataset' object with your training data
# ...

training_args = TrainingArguments(
    output_dir="./llama_finetuned",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    learning_rate=3e-5,
    fp16=True,                     # Enable mixed precision
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,         # Your Hugging Face Dataset object
)

trainer.train()
model.save_pretrained("./llama_finetuned")
```

#### **2. Efficient LoRA Fine-Tuning with PEFT**

Here's how to use LoRA to achieve similar results with far fewer resources.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset

model_name = "meta-llama/Llama-2-7b-hf"

# --- 1. Load and optionally quantize model (for QLoRA) ---
# This uses 4-bit quantization to drastically reduce memory.
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,  # Comment this line to run without quantization
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

# Prepare the model for k-bit training (for QLoRA)
model = prepare_model_for_kbit_training(model)

# --- 2. Configure LoRA ---
lora_config = LoraConfig(
    r=16,                        # Rank
    lora_alpha=32,               # Scaling factor
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"], # Modules to adapt
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters() # Should show <1% of parameters trainable

# --- 3. Load a sample dataset and preprocess ---
# Replace with your own dataset
dataset = load_dataset("gururise/AlpacaDataCleaned", split="train")
dataset = dataset.select(range(500)) # Select first 500 samples for demo

def format_prompt(example):
    """Formats the instruction dataset for causal LM."""
    text = f"### Instruction:\n{example['instruction']}\n\n### Response:\n{example['output']}"
    return tokenizer(text, truncation=True, max_length=512, padding="max_length")

tokenized_dataset = dataset.map(format_prompt, remove_columns=dataset.column_names)

# --- 4. Train ---
training_args = TrainingArguments(
    output_dir="./lora_llama2",
    per_device_train_batch_size=4,
    num_train_epochs=1,
    learning_rate=2e-4,
    fp16=True,
    report_to="none",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()

# --- 5. Save the adapter weights ---
model.save_pretrained("./my_lora_adapter")
```

### 💎 Summary & Final Recommendations

Fine-tuning is a powerful way to turn a general LLM into an expert on your specific task. The table below summarizes the key trade-offs to help you choose the right approach.

| Method | Trainable Parameters | Hardware Needs (for 7B model) | Performance vs. Full FT | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Full Fine-Tuning** | 100% (7B params) | 100-120GB VRAM | 100% (baseline) | Maximum performance, complex domain shifts, abundant compute |
| **LoRA** | ~0.1-1% | ~28GB VRAM | 90-95% | General fine-tuning on limited hardware |
| **QLoRA** | ~0.1-1% | Can run 70B+ models on 24GB | 80-90% | Extreme resource constraints, fine-tuning very large models |

---

### Different ways to fine tune LLM :-
1. **Supervised Fine Tuning** - provide labelled dataset (prompt with desired output, usually thousand to lakh dataset are provided)

2. **Continued Pretraining** - this is unsupervised fine tuning technique where unlabelled dataset are provided to LLM.

3. **Reinforcement Learning From Human Feedback** (RLHF) - RLHF is a technique used to align Large Language Models (LLMs) with human preferences – teaching the model what kind of responses humans find helpful, honest, and harmless.

---

## 17. YouTube Chatbot using LangChain | Building a RAG system in LangChain (46:14)

## 🧑‍🏫 What This lecture Covers

User builds a **real RAG (Retrieval-Augmented Generation) system** from scratch using LangChain. The goal: allow users to chat with any YouTube video – ask questions, get summaries, find specific topics – without watching the whole video.

He covers:
- Problem statement (long videos, hard to find information)
- Step‑by‑step implementation (indexing, retrieval, augmentation, generation)
- Building a LangChain **chain** to automate the entire pipeline
- Possible improvements (UI, evaluation, advanced techniques)

---

## ✅ Important Pointers (Key Takeaways)

1. **Problem**: YouTube videos (especially podcasts or lectures) are long. You want to ask specific questions without watching everything.
2. **Solution**: RAG system that:
   - Loads the video transcript
   - Splits it into chunks
   - Creates embeddings and stores in a vector store
   - For a user query, retrieves relevant chunks
   - Augments the query with those chunks
   - Generates an answer using an LLM
3. **Tech stack**: YouTube Transcript API, `RecursiveCharacterTextSplitter`, `FAISS` vector store, `OpenAIEmbeddings`, `ChatOpenAI`, LangChain chains (`RunnableParallel`, `RunnableLambda`, `RunnablePassthrough`).
4. **The system is built in four stages**:
   - **Indexing** (offline): load transcript → split → embed → store.
   - **Retrieval** (real‑time): convert query to embedding → semantic search → get relevant chunks.
   - **Augmentation**: combine query + retrieved chunks into a prompt.
   - **Generation**: LLM answers based on the prompt.
5. **Final implementation uses a LangChain chain** – a single `invoke()` call triggers the whole pipeline.
6. **Possible improvements** (advanced RAG): UI (Streamlit or Chrome extension), evaluation (RAGAS, LangSmith), better indexing (semantic chunking, translation), advanced retrieval (MMR, multi‑query, hybrid search), post‑retrieval (contextual compression), generation (citation, guardrails), and even multi‑modal or agentic RAG.

---

## 📚 Detailed Explanation with Code Examples

### 1. Problem & Plan of Action

**Goal**: Build a system where a user can ask questions about a YouTube video.

**High‑level plan** (same as standard RAG architecture):

| Stage | Step |
|-------|------|
| Indexing | Load transcript → split into chunks → embed → store in vector store |
| Retrieval | User query → embed → similarity search → get relevant chunks |
| Augmentation | Combine query + chunks into a prompt |
| Generation | LLM generates answer |

---

### 2. Indexing – Building the Knowledge Base

**Step 1 – Get YouTube transcript**

```python
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "VIDEO_ID_HERE"   # e.g., "dQw4w9WgXcQ"
transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])

# Combine all text segments into one string
transcript_text = " ".join([item["text"] for item in transcript_list])
```

> You can also specify `languages=["hi"]` for Hindi transcripts.

**Step 2 – Split into chunks**

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_text(transcript_text)   # list of strings
```

**Step 3 – Create embeddings and store in vector store (FAISS)**

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_texts(chunks, embeddings)
```

> Now you have a searchable index of the video content.

---

### 3. Retrieval – Finding Relevant Chunks for a Query

```python
# Create a retriever from the vector store
retriever = vector_store.as_retriever(search_kwargs={"k": 4})

# User query
query = "What is DeepMind?"

# Retrieve relevant documents
docs = retriever.invoke(query)   # list of Document objects
```

**Combine retrieved chunks into a single context string**

```python
def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

context = format_docs(docs)
```

---

### 4. Augmentation – Building the Prompt with Context

```python
from langchain_core.prompts import PromptTemplate

template = """
You are a helpful assistant. Answer the question based ONLY on the provided transcript context.
If the context does not contain the answer, say "I don't know".

Context:
{context}

Question: {question}
Answer:
"""

prompt = PromptTemplate(template=template, input_variables=["context", "question"])
```

---

### 5. Generation – LLM Produces the Answer

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

# Combine prompt, model, parser into a chain
generation_chain = prompt | model | parser

# Generate answer
answer = generation_chain.invoke({"context": context, "question": query})
print(answer)
```

---

### 6. Putting It All Together – A Single LangChain Chain

The video builds a **complete chain** using `RunnableParallel`, `RunnableLambda`, and `RunnablePassthrough` so that one `invoke()` call does everything.

**Step A – Parallel chain to get both context and question**

```python
from langchain.schema.runnable import RunnableParallel, RunnableLambda, RunnablePassthrough

# Retriever chain: query → retriever → format_docs → context string
retrieve_chain = retriever | RunnableLambda(format_docs)

# Parallel chain: produces a dict with "context" and "question"
parallel_chain = RunnableParallel(
    context=retrieve_chain,
    question=RunnablePassthrough()   # passes the original query unchanged
)
```

**Step B – Main chain: parallel_chain → generation_chain**

```python
final_chain = parallel_chain | generation_chain

# Now you can ask any question in one line
answer = final_chain.invoke("Is the topic of aliens discussed in this video?")
print(answer)
```

> This single chain handles retrieval, augmentation, and generation automatically.

---

## 🧠 Understanding the Final Chain (Visual)

```
User query
    │
    ▼
┌─────────────────────────────────────┐
│         RunnableParallel            │
│  ┌──────────────┐  ┌──────────────┐ │
│  │  context     │  │  question    │ │
│  │ retriever →  │  │ Passthrough  │ │
│  │ format_docs  │  │              │ │
│  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────┘
    │                      │
    └──────────┬───────────┘
               ▼
    ┌─────────────────────┐
    │  PromptTemplate     │
    │  (context, question)│
    └─────────────────────┘
               │
               ▼
    ┌─────────────────────┐
    │  ChatOpenAI (LLM)   │
    └─────────────────────┘
               │
               ▼
    ┌─────────────────────┐
    │  StrOutputParser    │
    └─────────────────────┘
               │
               ▼
           Final answer
```

---

## 💡 Improvements & Next Steps (Advanced RAG)

The video ends with a long list of possible improvements – these are **not implemented** but suggested for future videos:

| Area | Improvements |
|------|--------------|
| **UI** | Streamlit web app or Chrome extension |
| **Evaluation** | RAGAS library (faithfulness, relevance, context precision, context recall) |
| **Indexing** | Clean transcripts, translate to English, use semantic chunking instead of fixed‑size |
| **Retrieval (pre)** | Query rewriting, multi‑query generation, domain‑aware routing |
| **Retrieval (during)** | MMR (diversity), hybrid search (keyword + semantic), re‑ranking |
| **Retrieval (post)** | Contextual compression (keep only relevant parts) |
| **Augmentation** | Better prompt templates, answer grounding, context window optimisation |
| **Generation** | Answer with citations, guardrails (prevent harmful output) |
| **System architecture** | Multi‑modal RAG (images, video), agentic RAG (takes actions), memory‑based RAG (personalised) |

---

## 📌 Final Takeaway

> **You’ve built a working RAG system that lets you chat with any YouTube video.**  
> The core is simple: transcript → chunks → embeddings → vector store → retriever → prompt → LLM.  
> LangChain chains make the whole pipeline clean and reusable.  
> Real‑world RAG systems add many optimisations, but this is the foundation.

---

## 18. Tools in LangChain (45:15)

- [Tools](https://docs.langchain.com/oss/python/langchain/tools)

- [Tool Integrations](https://docs.langchain.com/oss/python/integrations/tools)

summaries this genai tutorial transcript in simple words with all detail, make note of all important pointers and also explain each important concepts with basic code examples

Imp Command - `pip install -r ../09_youtube_chatbot_using_rag/requirements.txt`
