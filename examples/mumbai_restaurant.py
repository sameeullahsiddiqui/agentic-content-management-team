#!/usr/bin/env python3
"""
Mumbai Restaurant Content Creation Example
Demonstrates creating social media content for a South Indian restaurant in Mumbai

Author: Samee Ullah Siddiqui
Repository: https://github.com/sameeullahsiddiqui/agentic-content-management-team
"""
import asyncio
import os
import sys
from pathlib import Path
from typing import Dict, Any


# Add the parent directory (project root) to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root)+"/src")
from content_team import ContentCreationTeam


async def create_restaurant_content() -> Dict[str, Any]:

    team = ContentCreationTeam()

    # Detailed restaurant brief
    restaurant_brief = """
                RESTAURANT SOCIAL MEDIA CAMPAIGN
                
                BUSINESS DETAILS:
                Restaurant Name: Spice Route
                Location: Bandra West, Mumbai (Near BKC)
                Cuisine: Authentic South Indian (Kerala & Tamil specialties)
                Target Audience: Young professionals aged 25-35 working in BKC
                Price Range: ₹200-400 per meal
                
                UNIQUE SELLING POINTS:
                - Authentic recipes from Kerala and Tamil Nadu
                - Home-style cooking by chefs from Kerala and Chennai
                - Quick lunch service (15-minute delivery to BKC offices)
                - Healthy options with traditional ingredients
                - Affordable pricing for premium quality
                - Family recipes passed down through generations
                - Fresh coconut milk and spices ground daily
                - Vegetarian and non-vegetarian options
                
                BUSINESS GOALS:
                - Drive foot traffic during lunch hours (12 PM - 3 PM)
                - Increase weekend dinner bookings
                - Build brand awareness in Bandra-BKC corridor
                - Compete with nearby restaurants and food courts
                - Establish reputation for authentic South Indian cuisine
                
                TARGET DEMOGRAPHICS:
                - Primary: IT professionals, consultants, finance executives in BKC
                - Secondary: Bandra residents who appreciate authentic South Indian food
                - Tertiary: South Indian community in Mumbai missing home food
                
                PLATFORM STRATEGY:
                - Instagram: Food photography, behind-the-scenes content, chef stories
                - Facebook: Community engagement, customer reviews, event announcements
                - LinkedIn: Corporate lunch packages, office catering services
                - WhatsApp Business: Direct orders, daily menu updates, customer service
                
                CONTENT REQUIREMENTS:
                - 5 Instagram posts with captions and hashtags
                - 3 Facebook posts for community engagement
                - 2 LinkedIn posts for corporate audience
                - WhatsApp Business message templates
                - Email newsletter for weekend dinner promotions
                
                CULTURAL CONTEXT:
                - Emphasize authentic South Indian flavors and traditions
                - Connect with professionals missing home-cooked meals
                - Address fast-paced Mumbai lifestyle with quick service
                - Highlight value for money in expensive Mumbai market
                - Build trust through chef credentials and family recipes
                
                SEASONAL CONSIDERATIONS:
                - Upcoming festivals: Onam, Pongal, South Indian new year celebrations
                - Monsoon comfort food messaging
                - Summer refreshing drinks and lighter meals
                
                COMPETITION ANALYSIS:
                - Nearby competitors: Saravana Bhavan, Café Madras, local food courts
                - Differentiation: Faster service, authentic Kerala dishes, affordable pricing
                - Positioning: "Authentic South Indian food, BKC-fast, home-made taste"
                
                SUCCESS METRICS:
                - Increase lunch orders by 40% in next 2 months
                - Build Instagram following to 5,000 followers
                - Generate 100+ weekend dinner reservations monthly
                - Establish 20+ corporate lunch partnerships
                """
    
    # Create social media campaign
    print("\n   Creating Mumbai Restaurant Social Media Campaign...")
    print("         Target: Young professionals in BKC area")
    print("         Location: Bandra West, Mumbai")
    print("         Cuisine: Authentic South Indian")
    
    results = team.create_social_media_campaign(restaurant_brief)
    
    # Add restaurant-specific metadata
    results.update({
        "business_type": "restaurant",
        "location": "mumbai_bandra",
        "cuisine_type": "south_indian",
        "target_demographic": "young_professionals_bkc",
        "campaign_type": "social_media_comprehensive"
    })
    
    return results

def create_additional_restaurant_content() -> Dict[str, Any]:
    
    team = ContentCreationTeam()
    
    # Menu description content
    menu_brief = """
                MENU CONTENT CREATION - SPICE ROUTE RESTAURANT
                
                Create engaging menu descriptions that sell the experience, not just the food:
                
                SIGNATURE DISHES TO HIGHLIGHT:
                - Kerala Fish Curry - Traditional recipe with coconut milk and curry leaves
                - Malabar Biryani - Aromatic basmati rice with spices and tender meat
                - Appam with Stew - Soft rice pancakes with coconut milk stew
                - Chettinad Chicken - Spicy Tamil Nadu delicacy with roasted spices
                - Avial - Mixed vegetables in coconut and yogurt sauce
                - Filter Coffee - Traditional South Indian filter coffee
                - Tender Coconut Water - Fresh from Kerala coconuts
                
                WRITING STYLE:
                - Evoke memories of home for South Indians
                - Educate North Indians about authentic South Indian cuisine
                - Highlight health benefits and fresh ingredients
                - Include brief cultural stories behind dishes
                - Mention chef's regional expertise
                - Add mouth-watering sensory descriptions
                
                TARGET EMOTIONS:
                - Nostalgia for South Indians away from home
                - Curiosity for those new to authentic South Indian food
                - Trust through traditional preparation methods
                - Excitement about discovering new flavors
                """
    
    return team.create_content(menu_brief, "menu_descriptions")

def create_corporate_catering_content() -> Dict[str, Any]:
    """Create B2B content for corporate catering"""
    
    team = ContentCreationTeam()
    
    corporate_brief = """
                        CORPORATE CATERING CONTENT - SPICE ROUTE
                        
                        TARGET: BKC offices, IT companies, consulting firms, banks
                        
                        CORPORATE CATERING SERVICES:
                        - Executive lunch boxes (₹150-250 per person)
                        - Team lunch catering for meetings and events
                        - Festival celebration catering (Onam, Pongal, etc.)
                        - Weekly/monthly corporate meal subscriptions
                        - Coffee and snacks for meetings
                        
                        VALUE PROPOSITIONS FOR CORPORATES:
                        - On-time delivery guaranteed
                        - GST invoicing and corporate billing
                        - Customizable for dietary restrictions
                        - Bulk order discounts
                        - Advanced ordering through WhatsApp Business
                        - Nutrition information for health-conscious teams
                        
                        CONTENT NEEDED:
                        - Email pitch to corporate HR teams
                        - Corporate catering brochure content
                        - LinkedIn posts targeting business owners
                        - WhatsApp Business templates for corporate inquiries
                        
                        CORPORATE PAIN POINTS TO ADDRESS:
                        - Limited healthy lunch options in BKC
                        - Long queues at popular restaurants
                        - Expensive corporate catering from 5-star hotels
                        - Repetitive food options for team lunches
                        - Complicated ordering and billing processes
                        """
    
    return team.create_content(corporate_brief, "corporate_catering")

if __name__ == "__main__":
    
    async def run_restaurant_examples():
        """Run all restaurant content creation examples"""
        
        print("Mumbai Restaurant Content Creation Examples")
        print("=" * 50)
        
        try:
            # Main social media campaign
            print("\n1 Creating Social Media Campaign...")
            social_results = await create_restaurant_content()
            print(f"- Social media campaign: {social_results.get('status', 'completed')}")
            
            # Menu descriptions
            print("\n2 Creating Menu Descriptions...")
            menu_results = create_additional_restaurant_content()
            print(f"- Menu descriptions: {menu_results.get('status', 'completed')}")
            
            # Corporate catering
            print("\n3 Creating Corporate Catering Content...")
            corporate_results = create_corporate_catering_content()
            print(f"- Corporate catering: {corporate_results.get('status', 'completed')}")
            
            print("\nAll restaurant content examples completed!")
            print(f"4 Check output directory for generated content")
            
        except Exception as e:
            print(f"Error running examples: {e}")
            print("Make sure to set your API key in environment variables")
    
    # Run examples
    asyncio.run(run_restaurant_examples())