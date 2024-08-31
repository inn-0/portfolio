# Contact: Jerome G

Contact Email: innoswit+we@pm.me

Contact LinkedIn: [linkedin.com/in/jg-0ch/](https://www.linkedin.com/in/jg-0ch/)

# Projects:

### Master's Thesis in Data Science (HSLU, 🇨🇭): Using LLMs to Extract Information from Sensitive Documents [Data Extraction Dashboard](https://embed-mt--e-dash-wide2rows1.replit.app) (hover over dots)

Tech & Skills: Python, GPT-4, PyMuPDF, OCR, OpenAI API, MongoDB, Beanie, Apify (web scraping), data extraction, CRM integration

Developed an automated system for extracting and analyzing data from VC pitch decks, cutting costs to 2.50 francs per document, achieving a processing cost of approximately 2.50 francs per document, well below the target of 5-8 francs.

This required multimodal LLM processing of documents, automated web scrape summarisation, integrated observability tooling, and outputting summaries aligned with the firm's internal CRM system, based on extensive client-facing requirements engineering.

Example of the costs dashboard created using the [Pydantic Logfire](https://docs.pydantic.dev/logfire/guides/) observability platform.

<img src="https://github.com/user-attachments/assets/77d59c65-1c35-41e8-8971-f662eb42afe0" alt="thesis costs dashboard" style="width: 100%;">

<hr>

### Conference Presentation: PyCon Lithuania 2024 - [Structured Outputs from LLMs Using the "Instructor" Package](https://www.linkedin.com/feed/update/urn:li:activity:7182057676166545408)

Tech & Skills: Instructor, Pydantic, GPT-4, structured prompts, technical communication.

Succinctly showcasing the "[Instructor](useinstructor.com/)" open-source project at Python Lithuania 2024, illustrating how it leverages Pydantic to neatly manage LLM system-prompts, and avoid unreliable LLM outputs.

My early advocacy for the value of this structured prompting approach was validated 4 months later OpenAI when themselves implemented analogous functionality in their API, directly crediting the Open-Source community project "Instructor" as inspiration.

<img src="https://github.com/user-attachments/assets/714b7476-df15-404b-9724-7c287564602b" alt="2024 PyCon Lithuania" style="width: 100%;">

<hr>

### Scrape & Visualisation of Swiss Gregorian Chant Manuscript Archive (MongoDB into Streamlit): [ecodices.replit.app/](https://ecodices.replit.app)

Tech & Skills: BeautifulSoup, MongoDB, Streamlit, Replit, web scraping, data analysis, multithreading, custom Plotly dashboards

Scraped metadata for 2,827 ancient manuscripts into MongoDB, creating an interactive data dashboard visualising their age, location, format etc.

The project sets the stage to create datasets for training multi-modal LLMs to transcribe and analyse ancient manuscripts. 

Using AI to transcribe everything will enable researchers to make definitive claims like "Document X is the only surviving example we have of technique Y", or, to track the variations in the melodies of the same song across cultures and centuries.

<img src="https://github.com/user-attachments/assets/f0efc9f2-f0b2-43a0-8bcb-ff1cd6d81b41" alt="Ecodices" style="width: 100%;">

<hr>

### Social Network Analysis of Indian Unicorn Startup Investments: [PDF](https://github.com/inn-0/portfolio/blob/main/The%20Business%20Social%20Networks%20of%20Indian%20Unicorn%20Startups.pdf)

Tech & Skills: Plotly in Dash, Networkx, Google Maps API, OpenAI API, APIFY API, PitchBook.com

A dataset on Indian Unicorn Startups was enriched with various web scraping (Google Maps API, Pitchdeck.com), and used to map the market, and how the the links between companies & co-investors were formed over time.

This revealed the importance of network positioning for investors, where those who got in early and stayed active in the market tended to preferentially accumulate more and connections, increasing their centrality & influence.

<img src="https://github.com/user-attachments/assets/b28d6769-987f-4488-a539-0769d4baea9c" alt="Investor Social Networks" style="width: 100%;">

<hr>

### Clean Tech Chatbot (RAG using DeepLake in Streamlit): [https://cleantech.replit.app](https://cleantech.replit.app)

Tech & Skills: small LLM fine-tuning on Google Collab, Replit, RAG (Retrieval-Augmented Generation), BERTTopic, UMAP, HDBSCAN, SentenceTransformers, HuggingFace.

Implemented a RAG-powered chatbot in a resource-limited Replit environment, using BERTTopic for topic modeling and Sentence Transformers for embeddings.

This makes a vast corpus of clean energy and technology articles accessible and usable, such as generating a synthetic QnA traning dataset to fine-tuning a small language model for improved query responses.

Successfully overcame the technical challenges from the sentence embedding model running out of micro-server memory, by re-routing low-frequency queries through HuggingFace's free 'trial' API.

<img src="https://github.com/user-attachments/assets/3c19ef34-7d2e-441f-aa9e-3d8a9beb0a3e" alt="cleantech" style="width: 100%;">

<hr>

### SmashCut - Tennis Without Time-Out = Computer Vision models to auto-generate highlight snippets from tennis matches (PyTorch, GPT4-vision, Dash): [https://is.gd/smashcut](https://is.gd/smashcut)

Tech & Skills: YOLOv8, PyTorch Lightning, CNNs, Autoencoders, GPT-4 vision, DVC, Azure Blob Storage, self-supervised learning.

Developed a system to automatically identify and remove non-action segments from tennis broadcasts, significantly enhancing the viewer experience by focusing on actual gameplay while maintaining match flow.

Compared the performance of CNNs, autoencoders, and GPT-4 vision (zero-shot) classifiers in categorizing tennis video content, finding that CNNs performed best with curated data while GPT-4 showed better generalization to new domains.

Investigated unsupervised learning techniques to overcome data scarcity, successfully creating a prototype for scalable training dataset generation from publicly available tennis match videos. This can be used for social-media content generation, or for automatic benchmarking and performance analysis for professional analysis.

<img src="https://github.com/user-attachments/assets/b0cd7038-00fb-4de7-98ad-fabd568e6b09" alt="SmashCut" style="width: 100%;">



