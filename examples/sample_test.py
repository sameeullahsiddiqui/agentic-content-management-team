import os
from autogen import UserProxyAgent, AssistantAgent
import asyncio
import autogen
from dotenv import load_dotenv

load_dotenv()
azure_key = os.getenv('AZURE_OPENAI_API_KEY')
azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
model = os.getenv('AZURE_OPENAI_DEPLOYMENT_MODEL')
api_version = os.getenv('AZURE_OPENAI_API_VERSION')

# Make sure Ollama is running: ollama serve
lmstudio_config = {
    "model": "meta-llama-llama-3.1-8b-instruct",
    "base_url": "http://127.0.0.1:1234/v1",
    "api_key": "lm-studio",
    "api_type": "openai",
    "temperature": 0.7,
    "max_tokens": 2048,
    "price": [0.0, 0.0]
}

llm_config = {
                "config_list": [{
                    "model": model,
                    "api_key": azure_key,
                    "api_type": "azure",
                    "base_url": azure_endpoint,
                    "api_version": api_version
                }],
                "temperature": 0.7,
                "timeout": 120
            }
content_writer = AssistantAgent(name="ContentWriter",  llm_config=lmstudio_config)
project_manager = UserProxyAgent(
    name="ProjectManager",
    human_input_mode="NEVER",  # ask human for input at each step
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"), 
    system_message="You're an expert in project coordination in India.",
     code_execution_config={
        "last_n_messages": 1,
        "work_dir": "tasks",
        "use_docker": False,
    }, 
)

def _test_local_llm_connection(self):
        """Test if the local LLM is accessible"""
        try:
            test_agent = autogen.AssistantAgent(
                name="TestAgent",
                system_message="""You are a test agent.
                
                                STRICT RULES:
                                - Write ONLY creative marketing content
                                - NO code, NO programming, NO API calls, NO technical solutions
                                - NO mentions of "import", "requests", "API", "execute", or programming terms
                                - Focus on persuasive, engaging written content only
                                - Keep responses under 100 words unless specifically asked for longer content
                                - Always end with TERMINATE when you finish writing content
                        """,
                llm_config=self.llm_config
            )
            
            print("🔍 Testing local LLM connection...")
            # This will make a test call to the local LLM
            
        except Exception as e:
            print(f"❌ Local LLM connection failed: {e}")
            print("💡 Make sure your local LLM server is running!")
            raise

def main():
     project_manager.initiate_chat(
        content_writer,
        message="Please create content for mumbai restaurant in line with Indian standards."
    )

main()
