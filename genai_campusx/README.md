
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

Summary of the **Generative AI tutorial** , with all important pointers and basic examples for each concept.

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
10. Course will be **free on YouTube**, not paid (because he hasn’t mastered GenAI 100% yet).

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

summaries this genai tutorial transcript in simple words, make note of all important pointers and also explain each important concepts with basic code examples