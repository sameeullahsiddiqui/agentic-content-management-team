"""
Content Writer Agent for AutoGen Content Team India
Specializes in creating engaging content for Indian markets

Author: Samee Ullah Siddiqui
Repository: https://github.com/sameeullahsiddiqui/agentic-content-management-team
"""

import re
import random
from typing import Dict, Any, List, Optional, Tuple
from base_agent import BaseAgent


class ContentWriterAgent(BaseAgent):
    """
    Content Writer Agent - Creates engaging content for Indian audiences
    Specializes in cultural adaptation and local market understanding
    """

    def __init__(
        self,
        llm_config: Dict[str, Any],
        agent_config: Optional[Dict[str, Any]] = None,
        regional_config: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize Content Writer Agent

        Args:
            llm_config: LLM configuration
            agent_config: Agent-specific configuration
            regional_config: Indian market configuration
        """
        super().__init__(
            name="ContentWriter",
            agent_type="assistant",
            llm_config=llm_config,
            system_message=self.get_system_message(),
            agent_config=agent_config,
            regional_config=regional_config,
        )

        # Writer-specific attributes
        self.writing_styles = self._get_writing_styles()
        self.indian_examples_db = self._load_indian_examples()
        self.cultural_hooks = self._get_cultural_hooks()
        self.hindi_phrases = self._get_common_hindi_phrases()
        self.content_templates = self._get_content_templates()

    def get_system_message(self) -> str:
        """Get the system message for Content Writer"""
        return """You are a skilled content writer specializing in Indian markets with deep cultural understanding and expertise in creating engaging, locally relevant content.

                    STRICT RULES:
                    - Write ONLY creative marketing content
                    - NO code, NO programming, NO API calls, NO technical solutions
                    - NO mentions of "import", "requests", "API", "execute", or programming terms
                    - Focus on persuasive, engaging written content only
                    - Keep responses under 100 words unless specifically asked for longer content
                    - Always end with TERMINATE when you finish writing content

                    CORE EXPERTISE:
                    - Indian cultural context and regional nuances across 25+ cities
                    - Multi-generational audience communication (Gen Z, Millennials, Gen X, Boomers)
                    - Cross-cultural adaptation for metro, tier-2, and tier-3 cities
                    - Hindi/English code-switching that feels natural and appropriate
                    - Indian business ecosystem understanding (startups, SMEs, family businesses, MNCs)
                    - Local success stories, case studies, and market insights
                    - Festival and seasonal content integration

                    WRITING STYLE REQUIREMENTS:
                    - Simple, conversational English accessible to 8th grade reading level
                    - Culturally sensitive and locally relevant throughout
                    - Emotionally engaging with authentic Indian references
                    - Action-oriented with clear value propositions
                    - Optimized for mobile-first consumption patterns
                    - Inclusive representation across different Indian communities

                    CONTENT SPECIALIZATIONS:
                    - Social Media Content: Instagram posts, Facebook community content, LinkedIn professional posts, WhatsApp Business messages
                    - Blog Articles: Thought leadership, how-to guides, industry insights, local market analysis
                    - Email Marketing: Welcome series, promotional campaigns, newsletters, customer retention
                    - Website Copy: Landing pages, product descriptions, about us, service pages
                    - Marketing Materials: Brochures, flyers, presentations, sales collateral
                    - Video Scripts: YouTube content, Instagram reels, educational videos

                    INDIAN MARKET INTEGRATION REQUIREMENTS:
                    - Include specific Indian examples, data points, and case studies
                    - Reference successful Indian companies, entrepreneurs, and brands
                    - Use appropriate regional context based on target audience location
                    - Integrate relevant festivals, cultural events, and seasonal themes
                    - Consider joint family decision-making in consumer messaging
                    - Include trust-building elements important to Indian consumers
                    - Use Indian numbering systems (lakh, crore) alongside international formats
                    - Reference local challenges and provide India-specific solutions

                    CULTURAL ADAPTATION GUIDELINES:
                    - Respect all religions, castes, and communities equally
                    - Use inclusive language that represents diverse Indian demographics
                    - Avoid controversial political topics unless specifically required
                    - Include appropriate Hindi phrases only when natural and value-adding
                    - Consider regional food preferences, traditions, and customs
                    - Reference popular Indian entertainment (Bollywood, cricket, local festivals)
                    - Use Indian time references (IST) and local business hours
                    - Include references to Indian payment methods (UPI, digital wallets) when relevant

                    MOBILE-FIRST OPTIMIZATION:
                    - Write short paragraphs (2-4 sentences maximum)
                    - Use bullet points and numbered lists for easy scanning
                    - Create clear, descriptive headers and subheaders
                    - Ensure content flows well on small screens
                    - Use active voice and conversational tone
                    - Include relevant emojis for social media content
                    - Structure content for quick consumption and sharing

                    CONTENT QUALITY STANDARDS:
                    - Every piece must include at least one specific Indian example or reference
                    - Language should be accessible to audiences with varying English proficiency
                    - Content must be factually accurate with current Indian market data
                    - Include clear call-to-actions appropriate for Indian consumer behavior
                    - Ensure content is shareable and encourages engagement
                    - Maintain brand voice consistency while adapting for local market
                    - Optimize for voice search queries common in India

                    COLLABORATION APPROACH:
                    - Work closely with Editor for quality refinement
                    - Coordinate with SEO Specialist for keyword integration
                    - Align with Brand Strategist for positioning consistency
                    - Respond constructively to Project Manager feedback
                    - Iterate content based on cultural sensitivity reviews
                    - Provide multiple content variations when requested

                    OUTPUT FORMAT:
                    - Provide content in requested format (social post, blog article, email, etc.)
                    - Include relevant hashtags for social media content
                    - Suggest accompanying visuals or multimedia elements
                    - Provide content length that matches platform requirements
                    - Include cultural context explanations when using specific regional references
                    - Offer alternative versions for different audience segments when appropriate

                    Remember: Your goal is to create content that not only informs and engages but also feels authentically Indian while being accessible to diverse audiences across the country."""

    def get_specialization(self) -> List[str]:
        """Get list of Content Writer specializations"""
        return [
            "indian_cultural_adaptation",
            "multi_regional_content",
            "social_media_writing",
            "blog_article_creation",
            "email_marketing_copy",
            "website_content_writing",
            "hindi_english_integration",
            "festival_seasonal_content",
            "mobile_first_writing",
            "local_business_storytelling",
            "consumer_psychology_writing",
            "cross_generational_communication",
        ]

    def _get_writing_styles(self) -> Dict[str, Dict[str, Any]]:
        """Define different writing styles for various content types"""
        return {
            "social_media": {
                "tone": "casual_friendly",
                "sentence_length": "short",
                "emoji_usage": "frequent",
                "hashtag_count": "8-15",
                "call_to_action": "direct_engaging",
                "max_length": 280,
                "features": [
                    "trending_topics",
                    "user_generated_content",
                    "community_building",
                ],
            },
            "blog_article": {
                "tone": "informative_conversational",
                "sentence_length": "varied",
                "emoji_usage": "minimal",
                "hashtag_count": "0-3",
                "call_to_action": "informative_helpful",
                "max_length": 2000,
                "features": ["data_driven", "case_studies", "actionable_insights"],
            },
            "email_marketing": {
                "tone": "personal_professional",
                "sentence_length": "medium",
                "emoji_usage": "moderate",
                "hashtag_count": "0-2",
                "call_to_action": "clear_action_oriented",
                "max_length": 500,
                "features": ["personalization", "segmentation", "urgency_creation"],
            },
            "website_copy": {
                "tone": "professional_trustworthy",
                "sentence_length": "medium_to_long",
                "emoji_usage": "rare",
                "hashtag_count": "0",
                "call_to_action": "conversion_focused",
                "max_length": 1000,
                "features": ["seo_optimized", "trust_building", "benefit_focused"],
            },
            "whatsapp_business": {
                "tone": "personal_helpful",
                "sentence_length": "very_short",
                "emoji_usage": "frequent",
                "hashtag_count": "0-1",
                "call_to_action": "immediate_response",
                "max_length": 160,
                "features": [
                    "quick_updates",
                    "personal_touch",
                    "instant_communication",
                ],
            },
        }

    def _load_indian_examples(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load database of Indian examples and case studies"""
        return {
            "successful_companies": [
                {
                    "name": "Flipkart",
                    "industry": "E-commerce",
                    "story": "Started in Bangalore, became India's leading e-commerce platform",
                    "founded": 2007,
                },
                {
                    "name": "Zomato",
                    "industry": "Food Tech",
                    "story": "From Delhi startup to global food delivery platform",
                    "founded": 2008,
                },
                {
                    "name": "Paytm",
                    "industry": "Fintech",
                    "story": "Revolutionized digital payments in India",
                    "founded": 2010,
                },
                {
                    "name": "Ola",
                    "industry": "Mobility",
                    "story": "Made ride-sharing accessible across Indian cities",
                    "founded": 2010,
                },
                {
                    "name": "BYJU'S",
                    "industry": "Edtech",
                    "story": "Transformed online learning for Indian students",
                    "founded": 2011,
                },
                {
                    "name": "Swiggy",
                    "industry": "Food Delivery",
                    "story": "Bangalore-based food delivery revolution",
                    "founded": 2014,
                },
                {
                    "name": "Freshworks",
                    "industry": "SaaS",
                    "story": "Chennai-based global software success",
                    "founded": 2010,
                },
            ],
            "entrepreneurs": [
                {
                    "name": "Sachin Bansal",
                    "company": "Flipkart",
                    "achievement": "Built India's largest e-commerce platform",
                },
                {
                    "name": "Deepinder Goyal",
                    "company": "Zomato",
                    "achievement": "Transformed food discovery and delivery",
                },
                {
                    "name": "Vijay Shekhar Sharma",
                    "company": "Paytm",
                    "achievement": "Pioneered digital payments in India",
                },
                {
                    "name": "Bhavish Aggarwal",
                    "company": "Ola",
                    "achievement": "Revolutionized urban mobility",
                },
                {
                    "name": "Byju Raveendran",
                    "company": "BYJU'S",
                    "achievement": "Made quality education accessible",
                },
                {
                    "name": "Sriharsha Majety",
                    "company": "Swiggy",
                    "achievement": "Redefined food delivery experience",
                },
            ],
            "market_statistics": [
                {
                    "metric": "Digital Payment Growth",
                    "value": "300% year-over-year",
                    "source": "RBI Data 2024",
                },
                {
                    "metric": "Internet Users",
                    "value": "750+ million",
                    "source": "TRAI Report 2024",
                },
                {
                    "metric": "Smartphone Penetration",
                    "value": "85% in urban areas",
                    "source": "GSMA Intelligence",
                },
                {
                    "metric": "E-commerce Growth",
                    "value": "₹7.5 lakh crore market",
                    "source": "IBEF Report",
                },
                {
                    "metric": "UPI Transactions",
                    "value": "10+ billion monthly",
                    "source": "NPCI Data",
                },
                {
                    "metric": "Startup Funding",
                    "value": "$25+ billion in 2024",
                    "source": "VCCEdge Data",
                },
            ],
            "cultural_references": [
                {
                    "festival": "Diwali",
                    "business_angle": "Festival shopping season, gifting culture, family celebrations",
                },
                {
                    "festival": "Holi",
                    "business_angle": "Color themes, celebration products, community events",
                },
                {
                    "festival": "Eid",
                    "business_angle": "Festive wear, food specialties, family gatherings",
                },
                {
                    "festival": "Ganesh Chaturthi",
                    "business_angle": "Community celebrations, eco-friendly products, regional focus",
                },
                {
                    "festival": "Durga Puja",
                    "business_angle": "Eastern India focus, cultural events, artistic themes",
                },
                {
                    "event": "Cricket World Cup",
                    "business_angle": "National unity, sports marketing, viewing parties",
                },
                {
                    "event": "Bollywood Releases",
                    "business_angle": "Entertainment marketing, celebrity endorsements",
                },
                {
                    "trend": "Work from Home",
                    "business_angle": "Digital tools, home office setups, productivity",
                },
            ],
        }

    def _get_cultural_hooks(self) -> Dict[str, List[str]]:
        """Get cultural hooks for different contexts"""
        return {
            "family_values": [
                "Made with the care of a mother's cooking",
                "Bringing families together since [year]",
                "Trusted by generations of Indian families",
                "Where tradition meets innovation",
                "Built for the Indian family",
            ],
            "progress_and_tradition": [
                "Rooted in tradition, powered by technology",
                "Ancient wisdom, modern solutions",
                "Honoring our heritage while embracing the future",
                "Traditional values, contemporary approach",
                "Where culture meets innovation",
            ],
            "community_and_belonging": [
                "Join the community of successful Indians",
                "Connecting India, one story at a time",
                "Building a stronger India together",
                "Your local neighborhood partner",
                "Made by Indians, for Indians",
            ],
            "aspirational_growth": [
                "Rise with India's growth story",
                "Unlock your potential in New India",
                "Be part of India's digital revolution",
                "Dream big, achieve bigger",
                "Your success is India's success",
            ],
            "trust_and_authenticity": [
                "Trusted by 1 crore+ Indians",
                "Authentic quality you can rely on",
                "Transparent pricing, honest service",
                "Built on trust, powered by excellence",
                "Your trusted Indian partner",
            ],
        }

    def _get_common_hindi_phrases(self) -> Dict[str, Dict[str, str]]:
        """Get common Hindi phrases with context"""
        return {
            "greetings": {
                "namaste": "Universal respectful greeting",
                "sat sri akal": "Punjabi greeting for North India",
                "vanakkam": "Tamil greeting for South India",
                "adaab": "Urdu greeting, widely understood",
            },
            "expressions": {
                "bahut achha": "Very good/excellent",
                "kya baat hai": "How wonderful/impressive",
                "shandar": "Fantastic/amazing",
                "zabardast": "Tremendous/awesome",
                "kamaal": "Amazing/wonderful",
                "ekdum": "Absolutely/completely",
            },
            "business_terms": {
                "vyavasaya": "Business",
                "safalta": "Success",
                "pragati": "Progress",
                "vikas": "Development",
                "unnati": "Advancement",
                "lakshya": "Goal/target",
            },
            "emotional_connectors": {
                "dil se": "From the heart",
                "sachchi": "Truly/genuinely",
                "asli": "Real/authentic",
                "vishwas": "Trust/faith",
                "bharosa": "Confidence/trust",
                "izzat": "Respect/honor",
            },
        }

    def _get_content_templates(self) -> Dict[str, Dict[str, str]]:
        """Get content templates for different types"""
        return {
            "instagram_post": {
                "structure": "[Hook] + [Value/Story] + [Call to Action] + [Hashtags]",
                "example": "🎯 Did you know? [Interesting fact about India/business]\n\n[2-3 sentences explaining the value/story]\n\n💡 [Actionable tip or insight]\n\n👇 Share your experience in comments!\n\n#IndianBusiness #Startup #DigitalIndia",
            },
            "linkedin_post": {
                "structure": "[Professional Hook] + [Industry Insight] + [Indian Context] + [Professional CTA]",
                "example": "The Indian startup ecosystem is witnessing unprecedented growth...\n\n[Professional insight with data]\n\n[Relevant example from Indian market]\n\nWhat's your take on this trend? Share your thoughts below.",
            },
            "blog_intro": {
                "structure": "[Relatable Problem] + [Indian Context] + [Solution Preview] + [Article Promise]",
                "example": "If you're a business owner in [Indian city], you've probably faced [common problem]. With India's [relevant trend/statistic], this challenge has become even more pressing.\n\nIn this article, we'll explore [solution] that has helped [number]+ Indian businesses [achieve result].",
            },
            "whatsapp_message": {
                "structure": "[Personal Greeting] + [Brief Value] + [Clear Action]",
                "example": "Hi [Name] 👋\n\n[Brief update/offer in 1-2 lines]\n\n[Clear action step]\n\nReply STOP to unsubscribe.",
            },
        }

    def generate_content_by_type(
        self,
        content_type: str,
        brief: str,
        target_audience: Dict[str, Any],
        regional_focus: List[str],
    ) -> Dict[str, Any]:
        """Generate content based on type and requirements"""

        content_generators = {
            "social_media_campaign": self._generate_social_media_campaign,
            "blog_article": self._generate_blog_article,
            "email_campaign": self._generate_email_campaign,
            "website_content": self._generate_website_content,
            "product_description": self._generate_product_description,
            "whatsapp_business": self._generate_whatsapp_content,
        }

        generator = content_generators.get(content_type, self._generate_general_content)
        return generator(brief, target_audience, regional_focus)

    def _generate_social_media_campaign(
        self, brief: str, target_audience: Dict[str, Any], regional_focus: List[str]
    ) -> Dict[str, Any]:
        """Generate comprehensive social media campaign"""

        # Extract business details from brief
        business_info = self._extract_business_info(brief)
        content_style = self.writing_styles["social_media"]

        campaign = {
            "instagram_posts": self._create_instagram_posts(
                business_info, target_audience, regional_focus
            ),
            "facebook_posts": self._create_facebook_posts(
                business_info, target_audience, regional_focus
            ),
            "linkedin_posts": self._create_linkedin_posts(
                business_info, target_audience, regional_focus
            ),
            "whatsapp_messages": self._create_whatsapp_messages(
                business_info, target_audience, regional_focus
            ),
            "hashtag_strategy": self._create_hashtag_strategy(
                business_info, regional_focus
            ),
            "posting_schedule": self._create_posting_schedule(regional_focus),
            "content_themes": self._suggest_content_themes(
                business_info, target_audience
            ),
        }

        return campaign

    def _create_instagram_posts(
        self,
        business_info: Dict[str, Any],
        target_audience: Dict[str, Any],
        regional_focus: List[str],
    ) -> List[Dict[str, Any]]:

        posts = []

        # Post 1: Introduction/Welcome Post
        regional_greeting = self._get_regional_greeting(regional_focus)
        posts.append(
            {
                "type": "introduction",
                "caption": f"""🎉 {regional_greeting}! Welcome to {business_info.get('name', 'our business')}!

                        We're excited to serve the amazing {', '.join(regional_focus[:2])} community with {business_info.get('offering', 'our premium services')}.

                        ✨ What makes us special?
                        • {business_info.get('usp_1', 'Authentic quality you can trust')}
                        • {business_info.get('usp_2', 'Made with love for Indian families')}
                        • {business_info.get('usp_3', 'Affordable prices, premium experience')}

                        Join our growing family of {self._get_customer_count()} happy customers! 

                        👇 Tell us what you'd like to see more of!

                        #Welcome #NewBeginnings #{"".join([city.title() for city in regional_focus[:2]])} #IndianBusiness #QualityFirst #TrustWorthy #MadeInIndia #LocalBusiness""",
                "visual_suggestion": "Warm, welcoming image with Indian cultural elements and business branding",
                "best_time": "7:00 PM IST (peak engagement time)",
                "engagement_strategy": "Ask followers about their preferences to boost comments",
            }
        )

        # Post 2: Behind-the-Scenes/Story Post
        cultural_hook = random.choice(self.cultural_hooks["family_values"])
        posts.append(
            {
                "type": "behind_the_scenes",
                "caption": f"""👥 Meet the heart behind {business_info.get('name', 'our brand')}!

                        {cultural_hook} - that's what drives us every single day.

                        From our {business_info.get('location', 'local')} kitchen/workshop to your home, every {business_info.get('product', 'product')} is crafted with:
                        🤲 Traditional methods passed down through generations
                        ❤️ Love and attention to detail
                        🏆 Quality that makes your family proud

                        Did you know? We source our {business_info.get('key_ingredient', 'ingredients')} directly from {business_info.get('source_location', 'local farmers')}, ensuring freshness and supporting our Indian community.

                        That's the {business_info.get('name', 'our')} promise - authentic, reliable, and rooted in Indian values!

                        Share this if you believe in supporting local Indian businesses! 🇮🇳

                        #BehindTheScenes #IndianValues #Authentic #LocalSupport #QualityMatters #{"".join([city.title() for city in regional_focus[:1]])}Story #ProudlyIndian #FamilyBusiness""",
                "visual_suggestion": "Behind-the-scenes photos showing preparation/creation process with Indian aesthetics",
                "best_time": "6:30 PM IST (after work hours)",
                "engagement_strategy": "Share authentic story to build emotional connection",
            }
        )

        # Post 3: Customer Testimonial/Social Proof
        testimonial = self._create_authentic_testimonial(business_info, regional_focus)
        posts.append(
            {
                "type": "customer_testimonial",
                "caption": f"""⭐ Real Stories, Real Happiness! ⭐

                        "{testimonial['quote']}"
                        - {testimonial['customer_name']}, {testimonial['location']}

                        Stories like these make our day! 😊 When {testimonial['customer_name']} tried our {business_info.get('product', 'service')} for the first time, they were amazed by the {testimonial['highlight']}.

                        This is exactly why we do what we do - to bring joy, quality, and trust to every Indian family.

                        🙏 Thank you {testimonial['customer_name']} for being part of our journey!

                        👥 Have you tried us yet? Share your experience in the comments!

                        #CustomerLove #Testimonial #HappyCustomers #{"".join([city.title() for city in regional_focus[:1]])}Reviews #Trusted #QualityExperience #IndianFamilies #Grateful""",
                "visual_suggestion": "Customer photo or testimonial graphic with Indian design elements",
                "best_time": "8:00 PM IST (social proof works well in evening)",
                "engagement_strategy": "Encourage other customers to share their experiences",
            }
        )

        # Post 4: Educational/Value-Added Content
        educational_content = self._create_educational_content(
            business_info, target_audience
        )
        posts.append(
            {
                "type": "educational",
                "caption": f"""📚 Did You Know? Interesting Facts About {business_info.get('industry', 'Our Industry')}!

                    {educational_content['fact_1']} 🤔

                    {educational_content['fact_2']} 💡

                    {educational_content['fact_3']} 🇮🇳

                    This is why choosing the right {business_info.get('product_category', 'product')} matters for your family!

                    At {business_info.get('name', 'our company')}, we ensure:
                    ✅ {educational_content['benefit_1']}
                    ✅ {educational_content['benefit_2']}
                    ✅ {educational_content['benefit_3']}

                    💬 Which fact surprised you the most? Let us know!

                    #DidYouKnow #EducationalContent #IndianMarket #SmartChoices #InformedDecisions #{"".join([city.title() for city in regional_focus[:1]])}Facts #KnowledgeSharing #ValueEducation""",
                "visual_suggestion": "Infographic with Indian color scheme and easy-to-read facts",
                "best_time": "12:00 PM IST (lunch break engagement)",
                "engagement_strategy": "Ask questions to encourage educational discussions",
            }
        )

        # Post 5: Special Offer/Call-to-Action
        offer_details = self._create_compelling_offer(business_info, regional_focus)
        posts.append(
            {
                "type": "promotional_offer",
                "caption": f"""🎉 {offer_details['festival_hook']} Special Offer! 🎉

                        {offer_details['urgency_creator']} 

                        🔥 Special {offer_details['festival_name']} Offer:
                        • {offer_details['discount']} off on all {business_info.get('products', 'items')}
                        • {offer_details['bonus_offer']}
                        • {offer_details['free_service']}

                        Only for our {', '.join(regional_focus)} family! ❤️

                        Why choose us this {offer_details['festival_name']}?
                        ✨ Guaranteed satisfaction
                        ✨ Same-day delivery in {regional_focus[0] if regional_focus else 'your city'}
                        ✨ Trusted by {self._get_customer_count()}+ families

                        📱 Order now: {offer_details['contact_method']}
                        🚚 Free delivery on orders above {offer_details['free_delivery_threshold']}

                        ⏰ Offer valid till {offer_details['expiry_date']}

                        Don't miss out! Share with your family and friends! 

                        #SpecialOffer #{"".join(offer_details['festival_name'].split())} #LimitedTime #{"".join([city.title() for city in regional_focus[:1]])}Offer #SameDay Delivery #TrustedBrand #FamilyOffer""",
                "visual_suggestion": "Eye-catching promotional graphic with festival colors and clear offer details",
                "best_time": "7:30 PM IST (prime decision-making time)",
                "engagement_strategy": "Create urgency and encourage immediate action",
            }
        )

        return posts

    def _create_facebook_posts(
        self,
        business_info: Dict[str, Any],
        target_audience: Dict[str, Any],
        regional_focus: List[str],
    ) -> List[Dict[str, Any]]:

        posts = []

        # Community-focused post
        posts.append(
            {
                "type": "community_engagement",
                "content": f"""🏘️ Proud to be part of the {', '.join(regional_focus)} community!

                            When we started {business_info.get('name', 'our business')} {business_info.get('years_ago', '5')} years ago, our dream was simple - to serve our local community with {business_info.get('offering', 'quality products')} that Indian families deserve.

                            Today, thanks to your incredible support, we've:
                            • Served {self._get_customer_count()}+ happy families
                            • Created {business_info.get('jobs_created', '25')} local jobs
                            • Partnered with {business_info.get('local_suppliers', '15')} local suppliers
                            • Contributed to {business_info.get('community_initiatives', 'various community initiatives')}

                            This is what community support looks like! 💪

                            Every purchase you make supports local employment, helps us source from regional suppliers, and strengthens our beautiful {regional_focus[0] if regional_focus else 'local'} economy.

                            Thank you for being part of our journey. Here's to building a stronger, more prosperous community together! 🙏

                            What do you love most about our local {regional_focus[0] if regional_focus else 'area'} community? Share in the comments below! 👇""",
                "engagement_tactics": [
                    "Ask community-related questions",
                    "Share local success stories",
                    "Tag local businesses",
                ],
                "best_time": "6:00 PM IST",
            }
        )

        # Event/Festival post
        current_festival = self._get_current_or_upcoming_festival()
        posts.append(
            {
                "type": "festival_celebration",
                "content": f"""🎊 {current_festival['greeting']} to all our wonderful customers! 🎊

                        {current_festival['significance']}

                        This {current_festival['name']}, we're celebrating with our community by:
                        🎁 Special {current_festival['name']} collection featuring {business_info.get('festival_products', 'traditional favorites')}
                        🏠 Free home delivery for all festival orders
                        👥 Supporting {current_festival['charity_angle']} in our neighborhood
                        🎉 Spreading joy with special prices for families

                        {current_festival['cultural_message']}

                        Visit us at {business_info.get('address', 'our store')} or call {business_info.get('phone', 'us')} for your {current_festival['name']} needs!

                        May this {current_festival['name']} bring prosperity, happiness, and good health to all families! 🙏

                        Share your {current_festival['name']} celebrations with us using #{current_festival['hashtag']}{business_info.get('name', '').replace(' ', '')}!""",
                "engagement_tactics": [
                    "Festival wishes",
                    "Share festival photos",
                    "Community celebration",
                ],
                "best_time": f"{current_festival['optimal_posting_time']}",
            }
        )

        # Customer success story (detailed)
        success_story = self._create_detailed_customer_story(
            business_info, regional_focus
        )
        posts.append(
            {
                "type": "detailed_testimonial",
                "content": f"""👨‍👩‍👧‍👦 Customer Spotlight: The {success_story['family_name']} Family Story

                                We love sharing stories of how our {business_info.get('products', 'products')} have made a difference in our customers' lives!

                                Meet {success_story['customer_name']} from {success_story['location']}:

                                "{success_story['detailed_story']}"

                                {success_story['transformation_details']}

                                What touched us most was when {success_story['customer_name']} said: "{success_story['emotional_quote']}"

                                This is exactly why we're passionate about what we do - creating positive impacts in real Indian families' lives! ❤️

                                {success_story['business_learning']}

                                Thank you {success_story['customer_name']} for trusting us with your family's {business_info.get('need_category', 'needs')}!

                                Have a similar story? We'd love to hear from you! Comment below or send us a message. 📩""",
                "engagement_tactics": [
                    "Personal stories",
                    "Emotional connection",
                    "Invite story sharing",
                ],
                "best_time": "7:00 PM IST",
            }
        )

        return posts

    def _create_linkedin_posts(
        self,
        business_info: Dict[str, Any],
        target_audience: Dict[str, Any],
        regional_focus: List[str],
    ) -> List[Dict[str, Any]]:

        posts = []

        # Industry insight post
        posts.append(
            {
                "type": "industry_insight",
                "content": f"""📈 The {business_info.get('industry', 'Indian business')} landscape is evolving rapidly.

                                Key trends we're observing in {', '.join(regional_focus[:2])}:

                                1️⃣ Digital-first approach: {self._get_industry_stat_1(business_info)}
                                2️⃣ Local sourcing preference: {self._get_industry_stat_2(business_info)}
                                3️⃣ Quality consciousness: {self._get_industry_stat_3(business_info)}

                                At {business_info.get('name', 'our company')}, we've adapted by:
                                • Implementing digital solutions for seamless customer experience
                                • Building strong partnerships with local {business_info.get('supplier_type', 'suppliers')}
                                • Maintaining uncompromised quality standards

                                The result? {business_info.get('growth_metric', '200% growth')} in the past {business_info.get('growth_period', '2 years')} and {self._get_customer_count()}+ satisfied customers.

                                What trends are you seeing in your industry? Let's discuss in the comments.

                                #IndianBusiness #GrowthStrategy #LocalBusiness #DigitalTransformation #QualityFirst""",
                "engagement_type": "professional_discussion",
                "best_time": "10:00 AM IST",
            }
        )

        # Entrepreneurial journey post
        posts.append(
            {
                "type": "entrepreneurial_story",
                "content": f"""🚀 From idea to impact: Our {business_info.get('years_in_business', '5')}-year journey

                            When I started {business_info.get('name', 'this venture')} in {business_info.get('founding_location', regional_focus[0] if regional_focus else 'India')}, the vision was clear: {business_info.get('founding_vision', 'to serve Indian families with authentic, quality products')}.

                            The challenges were real:
                            • Limited initial capital
                            • Building trust in a competitive market  
                            • Understanding diverse regional preferences across {', '.join(regional_focus)}
                            • Scaling operations while maintaining quality

                            Key learnings that shaped our success:

                            1. **Customer-first approach**: Every decision was evaluated against "Does this serve our customers better?"

                            2. **Local adaptation**: What works in Mumbai might need adjustment for Pune or Nashik.

                            3. **Team building**: Hiring people who believe in the mission, not just the paycheck.

                            4. **Continuous learning**: The Indian market teaches you something new every day.

                            Today, we're proud to serve {self._get_customer_count()}+ families and employ {business_info.get('team_size', '50')}+ people locally.

                            To fellow entrepreneurs: What's the most valuable lesson your journey has taught you?

                            #Entrepreneurship #IndianStartup #SmallBusiness #LocalImpact #BusinessJourney #LessonsLearned""",
                "engagement_type": "entrepreneurial_community",
                "best_time": "2:00 PM IST",
            }
        )

        return posts

    def _create_whatsapp_messages(
        self,
        business_info: Dict[str, Any],
        target_audience: Dict[str, Any],
        regional_focus: List[str],
    ) -> List[Dict[str, Any]]:

        messages = []

        # Welcome message
        messages.append(
            {
                "type": "welcome_series",
                "message": f"""🙏 Welcome to {business_info.get('name', 'our business')} family!

            Thank you for your interest in our {business_info.get('main_product', 'products')}. 

            Quick benefits for you:
            ✅ {business_info.get('benefit_1', 'Premium quality guaranteed')}
            ✅ {business_info.get('benefit_2', 'Free delivery in ' + (regional_focus[0] if regional_focus else 'your area'))}
            ✅ {business_info.get('benefit_3', '24/7 customer support')}

            📱 Save our number for:
            • Quick orders
            • Daily updates  
            • Special offers

            Reply HI to get started! 😊""",
                "timing": "Immediate after signup",
                "follow_up": "Send after 2 hours if no response",
            }
        )

        # Daily/Weekly update
        messages.append(
            {
                "type": "regular_update",
                "message": f"""🌅 Good morning! 

            Today's special from {business_info.get('name')}:

            🔥 {business_info.get('daily_special', 'Fresh batch ready')}
            💰 Special price: {business_info.get('special_price', '₹999')} (Save ₹{business_info.get('savings', '200')})
            🚚 Free delivery till 8 PM

            Order now: Reply ORDER
            More info: Reply INFO

            Have a great day! ☀️""",
                "timing": "8:00 AM IST",
                "frequency": "Weekly",
            }
        )

        # Festival/Special occasion
        current_festival = self._get_current_or_upcoming_festival()
        messages.append(
            {
                "type": "festival_offer",
                "message": f"""🎉 {current_festival['greeting']}! 

            Special {current_festival['name']} offer just for you:

            🎁 {business_info.get('festival_offer', '30% OFF')} on all {business_info.get('products')}
            🚀 FREE gift with every order
            📦 Same day delivery guaranteed

            Valid only today! 

            Order: Reply YES
            Details: Reply INFO

            Celebrate this {current_festival['name']} with quality! 🙏""",
                "timing": f"{current_festival['message_timing']}",
                "urgency": "High",
            }
        )

        return messages

    def _extract_business_info(self, brief: str) -> Dict[str, Any]:
        """Extract business information from content brief"""
        brief_lower = brief.lower()

        # Extract business name
        name_patterns = [
            r"restaurant name:\s*([^,\n]+)",
            r"business:\s*([^,\n]+)",
            r"company:\s*([^,\n]+)",
        ]
        business_name = "Your Business"
        for pattern in name_patterns:
            match = re.search(pattern, brief_lower)
            if match:
                business_name = match.group(1).strip().title()
                break

        # Extract location
        location_patterns = [
            r"location:\s*([^,\n]+)",
            r"based in:\s*([^,\n]+)",
            r"in\s+([a-z]+(?:\s+[a-z]+)*),",
        ]
        location = "India"
        for pattern in location_patterns:
            match = re.search(pattern, brief_lower)
            if match:
                location = match.group(1).strip().title()
                break

        # Extract price range
        price_match = re.search(r"₹(\d+)-(\d+)", brief)
        price_range = price_match.group(0) if price_match else "₹200-500"

        # Extract target audience age
        age_match = re.search(r"(\d+)-(\d+)", brief)
        target_age = (
            f"{age_match.group(1)}-{age_match.group(2)}" if age_match else "25-35"
        )

        return {
            "name": business_name,
            "location": location,
            "price_range": price_range,
            "target_age": target_age,
            "industry": self._detect_industry(brief_lower),
            "offering": self._extract_offering(brief_lower),
            "usp_1": self._extract_usp(brief_lower, 1),
            "usp_2": self._extract_usp(brief_lower, 2),
            "usp_3": self._extract_usp(brief_lower, 3),
        }

    def _detect_industry(self, brief_lower: str) -> str:
        """Detect industry from brief"""
        industries = {
            "restaurant": ["restaurant", "food", "cafe", "dining", "cuisine"],
            "technology": ["tech", "software", "app", "digital", "ai", "startup"],
            "ecommerce": ["ecommerce", "online store", "retail", "shopping"],
            "education": ["education", "school", "training", "course", "learning"],
            "healthcare": ["healthcare", "medical", "clinic", "hospital", "wellness"],
        }

        for industry, keywords in industries.items():
            if any(keyword in brief_lower for keyword in keywords):
                return industry
        return "general"

    def _extract_offering(self, brief_lower: str) -> str:
        """Extract main offering from brief"""
        if "restaurant" in brief_lower or "food" in brief_lower:
            return "authentic cuisine and dining experience"
        elif "tech" in brief_lower or "software" in brief_lower:
            return "innovative technology solutions"
        elif "ecommerce" in brief_lower:
            return "quality products with convenient shopping"
        elif "education" in brief_lower:
            return "comprehensive learning solutions"
        else:
            return "premium products and services"

    def _extract_usp(self, brief_lower: str, usp_number: int) -> str:
        """Extract unique selling propositions"""
        usps = {
            "restaurant": [
                "Authentic recipes from traditional Indian kitchens",
                "Fresh ingredients sourced daily from local markets",
                "Family-friendly atmosphere with quick service",
            ],
            "technology": [
                "Cutting-edge solutions built for Indian market",
                "24/7 customer support in multiple languages",
                "Affordable pricing with enterprise-grade quality",
            ],
            "ecommerce": [
                "Wide selection of authentic Indian products",
                "Free delivery across major Indian cities",
                "Easy returns and genuine quality guarantee",
            ],
        }

        industry = self._detect_industry(brief_lower)
        industry_usps = usps.get(
            industry,
            [
                "Trusted quality you can depend on",
                "Customer-first approach with personalized service",
                "Competitive pricing with premium experience",
            ],
        )

        return industry_usps[min(usp_number - 1, len(industry_usps) - 1)]
