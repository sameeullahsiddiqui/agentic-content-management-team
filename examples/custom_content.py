import asyncio
import os
import sys
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv

# Add the parent directory (project root) to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root) + "/src")
from content_team import ContentCreationTeam

load_dotenv()


# Main execution
if __name__ == "__main__":
    print("AutoGen Content Creation Team - Indian Market Specialist")
    print("=" * 60)

    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print(
            """
        🔑 Setup Instructions:
        
        1. Get OpenAI API Key from: https://platform.openai.com/api-keys
        2. Set environment variable:
           
           # On Windows:
           set OPENAI_API_KEY=your-key-here
           
           # On Mac/Linux:
           export OPENAI_API_KEY=your-key-here
           
           # Or create a .env file:
           echo "OPENAI_API_KEY=your-key-here" > .env
        
        3. Install required packages:
           pip install pyautogen python-dotenv
        """
        )

    # Menu system for different examples
    print("\nChoose an example to run:")
    print("1. Custom Content (Enter your own brief)")
    print("2. Exit")

    try:
        choice = input("\nEnter your choice (1-2): ").strip()

        if choice == "1":
            print("\n  Custom Content Creation...")
            custom_brief = input("Enter your content brief: ").strip()
            if custom_brief:
                team = ContentCreationTeam()
                team.create_content(custom_brief)
            else:
                print(" No brief provided.")

        elif choice == "2":
            print(" Goodbye!")

        else:
            print(" Invalid choice. Please run the script again.")

    except KeyboardInterrupt:
        print("\n\n Script interrupted. Goodbye!")
    except Exception as e:
        print(f"\n Error: {e}")
        print("Please check your setup and try again.")
