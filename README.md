# Cymbal Paint Agent

![paint](https://github.com/user-attachments/assets/dd0754fc-28c6-45aa-ae11-74b8ea39b214)

## Multi-Agent System Built with Google ADK + Vertex AI Search + Agent Engine

An end-to-end multi-agent AI assistant built and deployed on Google Cloud using the **Agent Development Kit (ADK)**.

This system simulates an enterprise retail workflow for Cymbal Shops' Paint Department — helping customers:

- Discover paint products grounded in real datasheets  
- Select product lines and colors  
- Calculate paint quantity based on room geometry  
- Estimate final cost with multi-room, multi-coat support  

The agent is fully deployed to **Vertex AI Agent Engine** and accessed through a **Chainlit web frontend**.

---

## Architecture

### Multi-Agent Design

| Component | Responsibility |
|------------|----------------|
| **Root Agent (`product_selector`)** | Conversation orchestration and tool routing |
| **Search Agent** | Retrieval via `VertexAiSearchTool` (RAG) |
| **Room Planner Agent** | Structured collection of room metadata |
| **Coverage Calculator Agent** | Paint volume and pricing computation |

To comply with ADK tool constraints, the search agent is wrapped using `AgentTool(...)`, isolating search functionality while enabling other tools within the root agent.

---

### System Flow

1. User requests paint information.
2. Root agent invokes Search Agent via `AgentTool`.
3. Search Agent retrieves grounded data from Vertex AI Search.
4. Selected paint metadata is stored in session state.
5. Room planner collects geometry and constraints.
6. Coverage agent computes required paint volume and total price.

---

## Key Technical Features

### Retrieval-Augmented Generation (RAG)
- Grounded responses from enterprise PDF datasheets
- Structured retrieval of price and coverage rate

### Session State Management
Persistent conversational state across turns:
- `SELECTED_PAINT`
- `COVERAGE_RATE`
- `PRICE`
- Room dimensions
- Coat count

### Tool Composition
- Resolved ADK multi-tool constraint using `AgentTool`
- Clean separation between retrieval logic and orchestration logic

### Cloud Deployment
- Deployed to Vertex AI Agent Engine
- IAM configuration for:
  - Vertex AI User
  - Discovery Engine User

---

## Demo

### Deployed Agent Engine + Chainlit Frontend
Click the thumbnail to play:

[![Watch Final Demo](https://img.youtube.com/vi/70m5CDpOnnw/hqdefault.jpg)](https://youtu.be/70m5CDpOnnw)

---

### Local Dev UI (State + Tooling working)
Click the thumbnail to play:

[![Watch Dev Demo](https://img.youtube.com/vi/EFrXVBLe5Xs/hqdefault.jpg)](https://youtu.be/EFrXVBLe5Xs)

---

## Tech Stack

- **Language:** Python 3.10+
- **Framework:** Google Agent Development Kit (ADK)
- **LLM:** Gemini (Vertex AI)
- **Retrieval:** Vertex AI Search (Discovery Engine)
- **Deployment:** Vertex AI Agent Engine
- **Frontend:** Chainlit

---

## Repository Structure

```

cymbal-paint-agent/
├── paint_agent/
│   ├── agent.py
│   ├── tools.py
│   ├── callback_logging.py
│   └── sub_agents/
│       ├── search_agent/
│       │   └── agent.py
│       └── room_planner/
│           ├── agent.py
│           └── sub_agents/
│               └── coverage_calculator/
│                   ├── agent.py
│                   └── tools.py
├── chainlit_ui/
│   ├── app.py
│   └── public/
│       ├── swatches.svg
│       └── theme.json
├── requirements.txt
└── README.md

````

---

## Setup

### Prerequisites

Before running this project, the following Google Cloud resources must be provisioned:

- Vertex AI enabled
- Discovery Engine Data Store (Layout Parser + table annotation)
- Search App connected to the Data Store
- Indexed paint datasheet (PDF) for grounding
- IAM roles granted to Vertex AI Reasoning Engine Service Agent:
  - Vertex AI User
  - Discovery Engine User

Local requirements:

- Python 3.10+
- Google Cloud CLI authenticated
- `google-adk` installed

---

### Installation

```bash
git clone https://github.com/your-username/cymbal-paint-agent.git
cd cymbal-paint-agent

python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
````

---

### Environment Configuration

Create a `.env` file:

* `paint_agent/.env`

```env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
MODEL=gemini-2.0-flash
SEARCH_ENGINE_ID=your-search-engine-id
```

Authenticate:

```bash
gcloud auth application-default login
gcloud config set project your-project-id
```

---

## Local Development

### Run via CLI

```bash
adk run paint_agent
```

### Run Dev Web UI

```bash
adk web
```

---

## Deployment

Deploy to Vertex AI Agent Engine:

```bash
adk deploy agent_engine paint_agent \
  --display_name "Paint Agent" \
  --staging_bucket gs://your-staging-bucket
```

Grant required IAM roles to the **Vertex AI Reasoning Engine Service Agent**:

* Vertex AI User
* Discovery Engine User

---

## Run Frontend Against Deployed Agent

Update `chainlit_ui/app.py`:

```python
agent = agent_engines.get("projects/PROJECT_ID/locations/us-central1/reasoningEngines/ENGINE_ID")
```

Then run:

```bash
cd chainlit_ui
chainlit run app.py
```

Visit:

```
http://localhost:8000
```

---

## License

MIT
