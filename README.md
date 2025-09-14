# Murder Mystery Detective Game

An interactive murder mystery detective game powered by AI agents, built with Streamlit and LangGraph. Step into the shoes of Sherlock Holmes and solve murders by interviewing AI-powered suspects and witnesses.

## Features

- **Dynamic Story Generation**: AI-generated murder scenarios with unique characters and crime scenes
- **Interactive Character Interviews**: Chat with AI-powered suspects and witnesses, each with distinct personalities
- **AI-Assisted Investigation**: Built-in Sherlock Holmes AI assistant to help generate investigative questions
- **Multiple Game Settings**: Customize the environment and number of characters
- **Real-time Conversation**: Contextual conversations with memory across interview sessions
- **Progressive Difficulty**: Limited guesses add challenge to the detective work

## Tech Stack

- **Frontend**: Streamlit with custom CSS styling
- **AI Framework**: LangGraph + LangChain for conversation workflows
- **LLM**: Databricks LLM integration
- **Data Validation**: Pydantic models for structured outputs
- **State Management**: Streamlit session state

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/murder-mystery-detective.git
cd murder-mystery-detective
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:

4. Run the application:
```bash
streamlit run app.py
```

## Usage

1. **Game Setup**: Choose your game environment and configure the number of characters and guesses
2. **Crime Scene Investigation**: Review the crime scene details, victim information, and initial clues
3. **Character Interviews**: Interview suspects and witnesses by asking questions or using AI suggestions
4. **Make Accusations**: Use your detective skills to identify the killer
5. **Case Resolution**: See the complete explanation of how the murder was committed

## Project Structure

```
murder-mystery-detective/
├── app.py                 # Main Streamlit application
├── src/
│   ├── models/           # Pydantic data models
│   ├── agents/           # AI agent implementations
│   ├── workflows/        # LangGraph workflow definitions
│   └── utils/           # Utility functions and configurations
├── ui/
│   ├── components/      # UI component modules
│   └── styles/         # CSS styling
└── config/             # Configuration files
```

## Configuration

The application requires the following environment variables:

```env
DATABRICKS_HOST=your_databricks_host
DATABRICKS_TOKEN=your_databricks_token
DATABRICKS_ENDPOINT=databricks-llama-4-maverick
```

## Game Mechanics

- **Character Generation**: AI creates 3-8 characters with one killer, one victim, and multiple suspects
- **Investigation Phase**: Interview characters to gather clues and evidence
- **Accusation Phase**: Make final accusations with limited attempts
- **Win/Lose Conditions**: Correctly identify the killer or run out of guesses

## Development

### Adding New Features

1. **New Character Types**: Extend the `Character` model in `src/models/character.py`
2. **Custom Prompts**: Modify prompts in `src/utils/prompts.py`
3. **UI Components**: Add new Streamlit components in `ui/components/`
4. **Workflow Changes**: Update LangGraph workflows in `src/workflows/`


## Acknowledgments

- Built with Streamlit for the web interface
- Powered by LangGraph for AI agent orchestration
- Uses Databricks LLMs for natural language processing