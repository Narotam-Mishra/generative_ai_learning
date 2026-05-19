
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

summaries this genai tutorial transcript in simple words, make note of all important pointers and also explain each important concepts with basic code examples

Imp Command - `pip install -r ../02_langchain_prompts/requirements.txt`