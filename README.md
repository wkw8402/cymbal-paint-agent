# Cymbal Paint Agent

The Cymbal Paint Agent is an AI-powered assistant designed to help customers of Cymbal Shops navigate their paint product catalog, select colors, calculate required paint quantities based on room dimensions, and provide pricing estimates.

This project demonstrates the use of **Google Cloud's Agent Development Kit (ADK)** to build, test, and deploy a multi-agent system grounded in enterprise data.

## Features

-   **Multi-Agent Architecture**: Orchestrates specialized agents for specific tasks:
    -   **Root Agent**: Manages the overall conversation flow.
    -   **Search Agent**: Retrieves product information using **Vertex AI Search** (RAG).
    -   **Room Planner Agent**: Collects room dimensions to calculate paint coverage.
    -   **Coverage Agent**: Performs the specific mathematical calculations for paint needs.
-   **Retrieval-Augmented Generation (RAG)**: Grounds responses in real product datasheets using Vertex AI Search.
-   **State Management**: maintains context across the conversation (e.g., selected paint, room dimensions) to provide accurate final estimates.
-   **Chainlit UI**: A modern, chat-based web interface for users to interact with the deployed agent.

## Demos

### 1. Final Deployed Agent
This video demonstrates the fully deployed agent running on **Vertex AI Agent Engine** and accessed via a **Chainlit** web application. The agent helps a user select paint, choose colors, and calculate costs for multiple rooms.

[![**🎥 Watch the Final Demo](https://img.youtube.com/vi/70m5CDpOnnw/hqdefault.jpg)](https://youtu.be/70m5CDpOnnw)

### 2. Development & State Management
This earlier demo shows the agent running locally during development. It highlights the agent's ability to maintain session state and debug context.

[![**🎥 Watch the Dev UI](https://img.youtube.com/vi/EFrXVBLe5Xs/hqdefault.jpg)](https://youtu.be/EFrXVBLe5Xs)

## Architecture

This project is built using:

-   **Runtime**: Python 3.x
-   **Framework**: [Google Cloud Agent Development Kit (ADK)](https://github.com/GoogleCloudPlatform/agent-development-kit)
-   **LLM**: Gemini Pro (via Vertex AI)
-   **Vector Search**: Vertex AI Search & Conversation
-   **Frontend**: [Chainlit](https://chainlit.io/)

### Directory Structure

-   `paint_agent/`: Contains the agent logic, tools, and sub-agent definitions.
-   `chainlit_ui/`: Contains the frontend application code connecting to the deployed agent.
-   `requirements.txt`: Python dependencies.

## Setup & Usage

### Prerequisites
-   Google Cloud Project with Vertex AI API enabled.
-   Python 3.8+ installed.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/cymbal-paint-agent.git
    cd cymbal-paint-agent
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Configure environment variables:
    Create a `.env` file in `chainlit_ui/` and `paint_agent/` with your Google Cloud details:
    ```env
    GOOGLE_CLOUD_PROJECT=your-project-id
    GOOGLE_CLOUD_LOCATION=us-central1
    MODEL=gemini-1.5-pro-001
    # ... other specific agent config
    ```

### Running the App
To run the Chainlit UI locally:

```bash
cd chainlit_ui
chainlit run app.py
```
