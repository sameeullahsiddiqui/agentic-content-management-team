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


if __name__ == "__main__":    
    """Example: Creating content for an e-commerce platform"""
    team = ContentCreationTeam()
    
    brief = """
                Create content for 'DesiCart', an e-commerce platform specializing in Indian ethnic wear.
                
                Campaign: Diwali Festival Sale 2024
                
                Target audience: Indian women aged 22-45 across metro and Tier-2 cities
                
                Content needed:
                1. Instagram carousel posts showcasing festival collections
                2. WhatsApp marketing messages for existing customers
                3. Email newsletter content
                4. Facebook ads copy for different age groups
                
                Key messages:
                - Up to 70% off on ethnic wear
                - Free shipping across India
                - Easy returns and exchanges
                - Authentic traditional designs
                - Size guide for perfect fit
                
                Cultural considerations: Emphasize tradition, family values, and festival celebrations
            """
    
    team.create_social_media_campaign(brief)
