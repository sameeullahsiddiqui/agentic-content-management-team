import asyncio
import os
import sys
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv

# Add the parent directory (project root) to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root)+"/src")
from content_team import ContentCreationTeam

load_dotenv()

# Main execution
if __name__ == "__main__":    

    """Example: Creating content for a Bangalore tech startup"""
    team = ContentCreationTeam()
    
    brief = """
                Create a blog article for 'EduTech Solutions', a Bangalore-based startup that provides 
                AI-powered learning platforms for rural Indian schools.
                
                Article topic: "How AI is Revolutionizing Education in Rural India: Real Success Stories"
                
                Target audience: 
                - Education policymakers
                - School administrators in Tier-2/3 cities
                - Ed-tech investors
                - Government officials in education sector
                
                Key points to cover:
                - Current challenges in rural education
                - How AI is solving these problems
                - Real case studies from Karnataka and Rajasthan
                - Cost-effectiveness for government schools
                - Future roadmap
                
                Goal: Establish thought leadership and generate leads for government contracts
            """
    
    team.create_blog_article(brief)
        