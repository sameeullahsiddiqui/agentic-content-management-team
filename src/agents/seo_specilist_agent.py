"""
SEO Specialist Agent for AutoGen Content Team India
Specializes in search engine optimization for Indian market

Author: Samee Ullah Siddiqui
Repository: https://github.com/sameeullahsiddiqui/agentic-content-management-team
"""

import re
from typing import Dict, Any, List, Optional, Tuple
from base_agent import BaseAgent


class SEOSpecialistAgent(BaseAgent):

    def __init__(
        self,
        llm_config: Dict[str, Any],
        agent_config: Optional[Dict[str, Any]] = None,
        regional_config: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize SEO Specialist Agent

        Args:
            llm_config: LLM configuration
            agent_config: Agent-specific configuration
            regional_config: Indian market configuration
        """
        super().__init__(
            name="SEOSpecialist",
            agent_type="assistant",
            llm_config=llm_config,
            system_message="",  # Will be set by get_system_message()
            agent_config=agent_config,
            regional_config=regional_config,
        )

        # SEO-specific attributes
        self.indian_keywords_db = self._load_indian_keywords()
        self.voice_search_patterns = self._get_voice_search_patterns()
        self.local_seo_factors = self._get_local_seo_factors()
        self.mobile_seo_guidelines = self._get_mobile_seo_guidelines()
        self.regional_search_trends = self._get_regional_search_trends()

    def get_system_message(self) -> str:
        """Get the system message for SEO Specialist"""
        return """You are an SEO specialist with deep expertise in Indian digital markets, local search behavior, and mobile-first optimization. Your role is to ensure content performs exceptionally well in Indian search engines and matches how Indians actually search for information online.

        CORE SEO EXPERTISE:
        - Indian search behavior patterns and query preferences
        - Hindi and regional language search optimization
        - Voice search optimization (fastest growing segment in India)
        - Local business SEO for Indian cities and regions
        - Mobile-first indexing optimization (critical for Indian market)
        - Cross-platform optimization (Google, YouTube, social platforms)
        - Regional search preferences and cultural search nuances

        INDIAN SEARCH BEHAVIOR UNDERSTANDING:
        - Indians often use conversational search queries ("best restaurant near me in Mumbai")
        - Voice search is growing 50% year-over-year, especially in regional languages
        - Mobile searches account for 80%+ of all searches in India
        - Local intent searches are extremely high ("near me", city names, landmarks)
        - Price-comparison searches are common ("cheap", "affordable", "best price")
        - Trust and reputation searches ("reviews", "genuine", "trusted")

        SEO OPTIMIZATION FOCUS AREAS:
        - Keyword research for Indian market with local search terms
        - Hindi transliteration and regional language considerations
        - Local pack optimization for Indian businesses
        - Featured snippet optimization for voice search
        - Mobile page speed and Core Web Vitals for Indian internet speeds
        - Schema markup for local businesses and Indian context
        - Google My Business optimization for Indian markets

        TECHNICAL SEO REQUIREMENTS:
        - Mobile-first indexing compliance (essential for Indian market)
        - Page speed optimization for varying internet speeds across India
        - Local schema markup with Indian address formats
        - Hreflang implementation for multilingual content
        - Internal linking strategy for topical authority
        - Image optimization with alt text including Indian keywords

        CONTENT SEO DELIVERABLES:
        - Primary and secondary keyword recommendations
        - Meta titles and descriptions optimized for Indian searches
        - Header structure (H1, H2, H3) with local relevance
        - Internal linking suggestions for Indian websites
        - Image alt-text with cultural context and local keywords
        - FAQ sections addressing common Indian search queries

        INDIAN MARKET SEO CONSIDERATIONS:
        - Include tier-2 and tier-3 city targeting for broader reach
        - Optimize for festival and seasonal searches throughout the year
        - Consider regional language transliteration in keyword strategy
        - Account for Indian social media search behavior patterns
        - Mobile page speed critical (average Indian mobile speed: 10-15 Mbps)
        - Local citations and directory listings for Indian businesses

        VOICE SEARCH OPTIMIZATION:
        - Target conversational keywords ("how to", "what is", "where can I")
        - Optimize for question-based queries common in Indian languages
        - Focus on local voice searches ("nearest", "around here", city names)
        - Include FAQ sections with natural language questions
        - Optimize for mobile voice search patterns
        - Consider Indian English accent and speech patterns

        LOCAL SEO SPECIALIZATION:
        - Google My Business optimization with Indian business categories
        - Local citation building in Indian directories
        - Review management and reputation optimization
        - Local keyword research including neighborhood and landmark names
        - Geographic targeting for multiple Indian cities
        - Local content creation for different regional markets

        KEYWORD RESEARCH METHODOLOGY:
        - Primary keyword: Main search term for the content topic
        - Secondary keywords: 3-5 supporting terms with search volume
        - Long-tail keywords: Specific Indian market queries
        - Local keywords: City, region, and neighborhood terms
        - Voice search keywords: Conversational and question-based
        - Competitor analysis: What works in Indian market
        - Seasonal keywords: Festival and event-based terms

        CONTENT OPTIMIZATION WORKFLOW:
        1. **Keyword Research**: Identify high-value Indian search terms
        2. **Title Optimization**: Create compelling, keyword-rich titles for Indian users
        3. **Meta Description**: Write click-worthy descriptions with local appeal
        4. **Header Structure**: Organize content with keyword-optimized headers
        5. **Content Integration**: Naturally integrate keywords without keyword stuffing
        6. **Internal Linking**: Connect to relevant Indian market content
        7. **Technical SEO**: Ensure mobile-first compliance and speed optimization

        MEASUREMENT AND ANALYTICS:
        - Track rankings for Indian keyword variations
        - Monitor local search visibility across target cities
        - Analyze voice search performance and queries
        - Measure mobile vs desktop performance in Indian market
        - Track seasonal and festival-related search performance
        - Monitor competitor performance in Indian SERPs

        COLLABORATION APPROACH:
        - Work with Content Writer to naturally integrate keywords
        - Coordinate with Content Editor to maintain readability while optimizing
        - Align with Brand Strategist for keyword-brand message consistency
        - Provide specific, actionable SEO recommendations to Project Manager
        - Balance SEO optimization with user experience and cultural relevance

        OUTPUT STANDARDS:
        - Provide specific keyword density recommendations (1-2% for primary keywords)
        - Include search volume estimates for Indian market when available
        - Suggest related topics for comprehensive content coverage
        - Recommend internal and external linking opportunities
        - Provide mobile optimization suggestions specific to Indian users
        - Include local SEO recommendations for business growth

        STAYING CURRENT:
        - Monitor Google algorithm updates affecting Indian market
        - Track emerging search trends in Indian languages
        - Stay updated with Indian digital behavior changes
        - Understand regional variations in search preferences
        - Keep current with voice search adoption patterns in India
        - Follow mobile-first indexing best practices for Indian market

        Remember: Your goal is to ensure content not only ranks well in Indian search results but also matches the actual search behavior and intent of Indian users, driving qualified traffic that converts to business value."""

    def get_specialization(self) -> List[str]:
        """Get list of SEO Specialist specializations"""
        return [
            "indian_keyword_research",
            "voice_search_optimization",
            "mobile_first_seo",
            "local_seo_indian_cities",
            "hindi_search_optimization",
            "regional_language_seo",
            "festival_seasonal_seo",
            "google_my_business_optimization",
            "indian_schema_markup",
            "mobile_page_speed_optimization",
            "indian_user_intent_analysis",
            "cross_platform_search_optimization",
        ]

    def _load_indian_keywords(self) -> Dict[str, List[str]]:
        """Load Indian market keyword database"""
        return {
            "high_volume_generic": [
                "best",
                "top",
                "near me",
                "in mumbai",
                "in delhi",
                "in bangalore",
                "cheap",
                "affordable",
                "price",
                "cost",
                "review",
                "genuine",
                "trusted",
                "online",
                "delivery",
                "home service",
                "booking",
            ],
            "business_types": {
                "restaurant": [
                    "restaurant near me",
                    "best food",
                    "home delivery",
                    "online order",
                    "veg restaurant",
                    "non veg",
                    "family restaurant",
                    "south indian food",
                    "north indian food",
                    "chinese food",
                    "fast food",
                    "tiffin service",
                ],
                "technology": [
                    "software company",
                    "app development",
                    "website design",
                    "digital marketing",
                    "cloud services",
                    "tech support",
                    "data recovery",
                    "computer repair",
                    "mobile app",
                    "web development",
                    "seo services",
                    "social media marketing",
                ],
                "ecommerce": [
                    "online shopping",
                    "cash on delivery",
                    "free delivery",
                    "discount",
                    "sale",
                    "offers",
                    "authentic products",
                    "genuine",
                    "original",
                    "return policy",
                    "customer service",
                    "fast shipping",
                ],
            },
            "local_modifiers": [
                "near me",
                "nearby",
                "in [city]",
                "around [area]",
                "[locality] में",
                "close to",
                "walking distance",
                "metro station",
                "bus stop",
                "market",
                "mall",
                "complex",
                "society",
                "colony",
            ],
            "voice_search_queries": [
                "how to",
                "what is",
                "where can i",
                "when does",
                "why should",
                "which is best",
                "tell me about",
                "find me",
                "show me",
                "book appointment",
                "order online",
                "call now",
            ],
            "trust_indicators": [
                "trusted",
                "genuine",
                "authentic",
                "verified",
                "certified",
                "licensed",
                "government approved",
                "iso certified",
                "reviews",
                "ratings",
                "testimonials",
                "customer feedback",
            ],
            "urgent_action": [
                "same day",
                "instant",
                "immediate",
                "urgent",
                "emergency",
                "24x7",
                "24 hours",
                "quick",
                "fast",
                "express",
                "rush",
            ],
            "price_related": [
                "cheap",
                "affordable",
                "low price",
                "discount",
                "offer",
                "free",
                "starting from",
                "budget",
                "economical",
                "value for money",
            ],
        }

    def _get_voice_search_patterns(self) -> Dict[str, List[str]]:
        """Get voice search optimization patterns"""
        return {
            "question_starters": [
                "how to",
                "what is",
                "where can",
                "when does",
                "why should",
                "which one",
                "who provides",
                "how much",
                "how many",
            ],
            "local_voice_queries": [
                "find [business] near me",
                "where is the nearest [business]",
                "call [business name]",
                "directions to [business]",
                "what time does [business] open",
                "is [business] open now",
            ],
            "conversational_patterns": [
                "I need",
                "I want",
                "I'm looking for",
                "show me",
                "find me",
                "book me",
                "order for me",
                "get me",
                "help me find",
            ],
            "indian_english_patterns": [
                "good [business] in [city]",
                "best [service] around here",
                "cheap [product] online",
                "home delivery [product]",
                "cash on delivery available",
            ],
        }

    def _get_local_seo_factors(self) -> Dict[str, Any]:
        """Get local SEO ranking factors for Indian market"""
        return {
            "google_my_business": {
                "importance": "critical",
                "factors": [
                    "Complete business information",
                    "Indian address format",
                    "Local phone number",
                    "Business hours in IST",
                    "Category selection",
                    "Regular posts and updates",
                    "Customer reviews and responses",
                    "Photos of business and products",
                ],
            },
            "local_citations": {
                "importance": "high",
                "indian_directories": [
                    "JustDial",
                    "Sulekha",
                    "IndiaMART",
                    "TradeIndia",
                    "99acres",
                    "MagicBricks",
                    "Zomato",
                    "Swiggy",
                ],
                "consistency_factors": [
                    "Business name spelling",
                    "Address format (Indian standard)",
                    "Phone number format (+91)",
                    "Website URL consistency",
                ],
            },
            "local_content": {
                "importance": "high",
                "content_types": [
                    "Location-based landing pages",
                    "Local event coverage",
                    "Regional festival content",
                    "Neighborhood guides",
                    "Local partnership announcements",
                ],
            },
            "reviews_and_ratings": {
                "importance": "critical",
                "platforms": [
                    "Google Reviews",
                    "Facebook Reviews",
                    "JustDial Reviews",
                    "Industry-specific platforms",
                    "Website testimonials",
                ],
                "management_strategy": [
                    "Encourage satisfied customers to leave reviews",
                    "Respond to all reviews professionally",
                    "Address negative feedback constructively",
                    "Use reviews as content for social proof",
                ],
            },
        }

    def _get_mobile_seo_guidelines(self) -> Dict[str, Any]:
        """Get mobile SEO guidelines for Indian market"""
        return {
            "page_speed": {
                "target_metrics": {
                    "first_contentful_paint": "< 1.8 seconds",
                    "largest_contentful_paint": "< 2.5 seconds",
                    "cumulative_layout_shift": "< 0.1",
                    "first_input_delay": "< 100 milliseconds",
                },
                "optimization_techniques": [
                    "Image compression and WebP format",
                    "Minify CSS and JavaScript",
                    "Use CDN for faster delivery",
                    "Optimize for 3G speeds (common in India)",
                    "Lazy loading for images and videos",
                ],
            },
            "mobile_usability": {
                "essential_factors": [
                    "Mobile-friendly design",
                    "Touch-friendly buttons and links",
                    "Readable font sizes without zooming",
                    "Proper viewport configuration",
                    "No horizontal scrolling required",
                ]
            },
            "user_experience": {
                "indian_mobile_behavior": [
                    "Thumb-friendly navigation",
                    "Quick loading on slower networks",
                    "Offline functionality where possible",
                    "Easy sharing on WhatsApp",
                    "Click-to-call functionality",
                ]
            },
        }

    def _get_regional_search_trends(self) -> Dict[str, Dict[str, List[str]]]:
        """Get regional search trends across Indian cities"""
        return {
            "mumbai": {
                "popular_keywords": ["mumbai", "bandra", "andheri", "powai", "thane"],
                "local_terms": [
                    "local train",
                    "station",
                    "western line",
                    "central line",
                ],
                "business_focus": ["finance", "bollywood", "textiles", "diamonds"],
            },
            "delhi": {
                "popular_keywords": ["delhi", "ncr", "gurgaon", "noida", "faridabad"],
                "local_terms": [
                    "metro",
                    "connaught place",
                    "karol bagh",
                    "lajpat nagar",
                ],
                "business_focus": ["government", "education", "automotive", "fashion"],
            },
            "bangalore": {
                "popular_keywords": [
                    "bangalore",
                    "bengaluru",
                    "koramangala",
                    "indiranagar",
                    "whitefield",
                ],
                "local_terms": ["tech park", "startup", "pub", "weather"],
                "business_focus": [
                    "technology",
                    "research",
                    "aerospace",
                    "biotechnology",
                ],
            },
            "chennai": {
                "popular_keywords": [
                    "chennai",
                    "madras",
                    "t nagar",
                    "anna nagar",
                    "velachery",
                ],
                "local_terms": ["beach", "temple", "filter coffee", "auto"],
                "business_focus": ["automobile", "healthcare", "education", "port"],
            },
            "hyderabad": {
                "popular_keywords": [
                    "hyderabad",
                    "secunderabad",
                    "hitech city",
                    "gachibowli",
                    "jubilee hills",
                ],
                "local_terms": ["biryani", "charminar", "tank bund", "metro"],
                "business_focus": [
                    "pharmaceuticals",
                    "biotechnology",
                    "information_technology",
                    "aerospace",
                ],
            },
        }

    def optimize_content_for_seo(
        self,
        content: str,
        target_keywords: List[str],
        content_type: str,
        regional_focus: List[str],
    ) -> Dict[str, Any]:
        """Main SEO optimization function"""

        seo_result = {
            "original_content": content,
            "optimized_content": "",
            "keyword_analysis": {},
            "seo_recommendations": [],
            "meta_elements": {},
            "technical_seo": {},
            "local_seo": {},
            "performance_predictions": {},
        }

        # Step 1: Keyword research and analysis
        keyword_analysis = self._analyze_keywords(
            target_keywords, regional_focus, content_type
        )
        seo_result["keyword_analysis"] = keyword_analysis

        # Step 2: Content optimization
        optimized_content = self._optimize_content_keywords(content, keyword_analysis)

        # Step 3: Meta elements creation
        meta_elements = self._create_meta_elements(
            optimized_content, keyword_analysis, regional_focus
        )
        seo_result["meta_elements"] = meta_elements

        # Step 4: Technical SEO recommendations
        technical_seo = self._generate_technical_seo_recommendations(
            content_type, regional_focus
        )
        seo_result["technical_seo"] = technical_seo

        # Step 5: Local SEO optimization
        local_seo = self._optimize_local_seo(optimized_content, regional_focus)
        seo_result["local_seo"] = local_seo

        # Step 6: Performance predictions
        performance = self._predict_seo_performance(keyword_analysis, regional_focus)
        seo_result["performance_predictions"] = performance

        seo_result["optimized_content"] = optimized_content
        seo_result["seo_recommendations"] = (
            self._generate_comprehensive_recommendations(seo_result)
        )

        return seo_result

    def _analyze_keywords(
        self, target_keywords: List[str], regional_focus: List[str], content_type: str
    ) -> Dict[str, Any]:
        """Analyze and expand keywords for Indian market"""

        analysis = {
            "primary_keywords": [],
            "secondary_keywords": [],
            "long_tail_keywords": [],
            "local_keywords": [],
            "voice_search_keywords": [],
            "seasonal_keywords": [],
            "keyword_difficulty": {},
        }

        # Expand primary keywords with Indian context
        for keyword in target_keywords[:3]:  # Top 3 as primary
            indian_variations = self._get_indian_keyword_variations(
                keyword, regional_focus
            )
            analysis["primary_keywords"].extend(indian_variations)

        # Generate secondary keywords
        business_type = self._detect_business_type(content_type)
        if business_type in self.indian_keywords_db["business_types"]:
            analysis["secondary_keywords"] = self.indian_keywords_db["business_types"][
                business_type
            ][:5]

        # Create local keywords
        for region in regional_focus:
            local_variations = [
                f"{keyword} in {region}",
                f"{keyword} {region}",
                f"best {keyword} {region}",
                f"{keyword} near {region}",
            ]
            analysis["local_keywords"].extend(local_variations)

        # Generate voice search keywords
        for keyword in analysis["primary_keywords"][:3]:
            voice_variations = [
                f"best {keyword} near me",
                f"how to find {keyword}",
                f"where can i get {keyword}",
                f"what is the cost of {keyword}",
            ]
            analysis["voice_search_keywords"].extend(voice_variations)

        # Add seasonal keywords (festivals, events)
        current_season = self._get_current_season_keywords()
        analysis["seasonal_keywords"] = current_season

        return analysis

    def _get_indian_keyword_variations(
        self, keyword: str, regional_focus: List[str]
    ) -> List[str]:
        """Get Indian market variations of a keyword"""
        variations = [keyword]

        # Add regional variations
        for region in regional_focus[:2]:  # Top 2 regions
            variations.extend(
                [f"{keyword} {region}", f"{keyword} in {region}", f"{region} {keyword}"]
            )

        # Add Indian market modifiers
        indian_modifiers = ["best", "top", "genuine", "trusted", "cheap", "affordable"]
        for modifier in indian_modifiers[:3]:
            variations.append(f"{modifier} {keyword}")

        # Add service-related variations
        service_modifiers = ["online", "home delivery", "near me", "booking", "service"]
        for modifier in service_modifiers[:2]:
            variations.append(f"{keyword} {modifier}")

        return variations

    def _detect_business_type(self, content_type: str) -> str:
        """Detect business type from content"""
        business_mapping = {
            "restaurant": "restaurant",
            "food": "restaurant",
            "tech": "technology",
            "software": "technology",
            "ecommerce": "ecommerce",
            "online": "ecommerce",
            "retail": "ecommerce",
        }

        content_lower = content_type.lower()
        for key, business_type in business_mapping.items():
            if key in content_lower:
                return business_type

        return "general"

    def _optimize_content_keywords(
        self, content: str, keyword_analysis: Dict[str, Any]
    ) -> str:
        """Optimize content with natural keyword integration"""

        optimized_content = content
        primary_keywords = keyword_analysis["primary_keywords"][:3]

        # Ensure primary keyword appears in first paragraph
        first_paragraph = optimized_content.split("\n\n")[0]
        if (
            primary_keywords
            and primary_keywords[0].lower() not in first_paragraph.lower()
        ):
            # Add keyword naturally to first paragraph
            first_sentence = first_paragraph.split(".")[0]
            enhanced_first = f"{first_sentence} focusing on {primary_keywords[0]}."
            optimized_content = optimized_content.replace(
                first_paragraph,
                first_paragraph.replace(first_sentence + ".", enhanced_first),
            )

        # Add secondary keywords throughout content
        secondary_keywords = keyword_analysis["secondary_keywords"][:3]
        paragraphs = optimized_content.split("\n\n")

        for i, paragraph in enumerate(paragraphs[1:], 1):  # Skip first paragraph
            if (
                i < len(secondary_keywords)
                and secondary_keywords[i - 1].lower() not in paragraph.lower()
            ):
                # Add keyword naturally
                sentences = paragraph.split(".")
                if len(sentences) > 1:
                    # Add to second sentence
                    enhanced_sentence = f"{sentences[1].strip()} This includes {secondary_keywords[i-1]}"
                    paragraphs[i] = paragraph.replace(sentences[1], enhanced_sentence)

        optimized_content = "\n\n".join(paragraphs)

        # Add long-tail keywords in FAQ or conclusion
        long_tail = keyword_analysis.get("long_tail_keywords", [])
        if long_tail and "frequently asked" not in optimized_content.lower():
            faq_section = self._create_faq_section(long_tail[:3])
            optimized_content += "\n\n" + faq_section

        return optimized_content

    def _create_faq_section(self, long_tail_keywords: List[str]) -> str:
        """Create FAQ section with long-tail keywords"""

        faq_section = "## Frequently Asked Questions\n\n"

        faq_templates = [
            "**Q: What is the best {keyword}?**\nA: The best {keyword} depends on your specific needs and location. We provide personalized recommendations based on your requirements.\n\n",
            "**Q: How much does {keyword} cost?**\nA: The cost of {keyword} varies based on several factors. Contact us for detailed pricing information.\n\n",
            "**Q: Where can I find {keyword} near me?**\nA: We offer {keyword} services across multiple locations. Use our location finder to find the nearest service center.\n\n",
        ]

        for i, keyword in enumerate(long_tail_keywords):
            if i < len(faq_templates):
                faq_section += faq_templates[i].format(keyword=keyword)

        return faq_section

    def _create_meta_elements(
        self, content: str, keyword_analysis: Dict[str, Any], regional_focus: List[str]
    ) -> Dict[str, str]:
        """Create SEO-optimized meta elements"""

        primary_keyword = (
            keyword_analysis["primary_keywords"][0]
            if keyword_analysis["primary_keywords"]
            else ""
        )
        region = regional_focus[0] if regional_focus else "India"

        # Meta title (50-60 characters)
        meta_title = f"{primary_keyword.title()} in {region} | Trusted Service Provider"
        if len(meta_title) > 60:
            meta_title = f"{primary_keyword.title()} {region} | Quality Service"

        # Meta description (150-160 characters)
        first_sentence = content.split(".")[0][:100]
        meta_description = f"{first_sentence}. Expert {primary_keyword} in {region}. Contact us for quality service and competitive prices."

        if len(meta_description) > 160:
            meta_description = f"Professional {primary_keyword} in {region}. Quality service, competitive prices. Contact us today for expert assistance."

        # Generate other meta elements
        meta_elements = {
            "title": meta_title,
            "description": meta_description,
            "keywords": ", ".join(
                keyword_analysis["primary_keywords"][:5]
                + keyword_analysis["local_keywords"][:3]
            ),
            "og_title": meta_title,
            "og_description": meta_description,
            "og_type": "website",
            "twitter_card": "summary",
            "twitter_title": meta_title,
            "twitter_description": meta_description[:140],  # Twitter limit
        }

        return meta_elements

    def _generate_technical_seo_recommendations(
        self, content_type: str, regional_focus: List[str]
    ) -> Dict[str, Any]:
        """Generate technical SEO recommendations"""

        return {
            "page_speed": {
                "priority": "critical",
                "recommendations": [
                    "Optimize images for WebP format (reduces size by 25-35%)",
                    "Implement lazy loading for images below the fold",
                    "Minify CSS and JavaScript files",
                    "Use CDN for faster content delivery across India",
                    "Optimize for 3G/4G speeds common in tier-2/3 cities",
                ],
            },
            "mobile_optimization": {
                "priority": "critical",
                "recommendations": [
                    "Ensure mobile-responsive design",
                    "Use large, touch-friendly buttons (minimum 44px)",
                    "Implement click-to-call functionality",
                    "Optimize forms for mobile input",
                    "Test on popular Indian mobile devices",
                ],
            },
            "schema_markup": {
                "priority": "high",
                "recommendations": [
                    "Implement LocalBusiness schema with Indian address format",
                    "Add Organization schema with contact information",
                    "Use Product schema for e-commerce items",
                    "Implement FAQ schema for voice search optimization",
                    "Add Review schema for customer testimonials",
                ],
            },
            "internal_linking": {
                "priority": "medium",
                "recommendations": [
                    "Link to location-specific pages for each target city",
                    "Create topic clusters around main services",
                    "Link to customer testimonials and case studies",
                    "Add breadcrumb navigation for better UX",
                    "Link to contact and booking pages from all content",
                ],
            },
        }

    def _optimize_local_seo(
        self, content: str, regional_focus: List[str]
    ) -> Dict[str, Any]:
        """Optimize for local SEO in Indian markets"""

        local_optimizations = {
            "google_my_business": {
                "optimization_checklist": [
                    "Complete business information with Indian address format",
                    "Add local phone number with +91 country code",
                    "Upload high-quality photos of business and products",
                    "Regular posts about services and offers",
                    "Respond to all customer reviews promptly",
                    "Add business hours in IST timezone",
                    "Select appropriate business categories",
                ]
            },
            "local_citations": {
                "recommended_directories": [
                    "JustDial - Primary Indian business directory",
                    "Sulekha - Local services directory",
                    "IndiaMART - B2B marketplace",
                    "Yellow Pages India - Traditional directory",
                    "Industry-specific directories",
                ],
                "citation_consistency": [
                    "Ensure consistent business name across all platforms",
                    "Use standard Indian address format",
                    "Maintain consistent phone number format",
                    "Keep website URL consistent everywhere",
                ],
            },
            "location_pages": {
                "recommendations": [
                    f"Create dedicated pages for each target city: {', '.join(regional_focus)}",
                    "Include local landmarks and neighborhoods in content",
                    "Add local customer testimonials and case studies",
                    "Include local contact information and directions",
                    "Optimize for local search terms and voice queries",
                ]
            },
            "local_content_strategy": {
                "content_ideas": [
                    "Local event participation and sponsorships",
                    "Regional festival offers and celebrations",
                    "Partnerships with local businesses",
                    "Community service initiatives",
                    "Local market insights and trends",
                ]
            },
        }

        return local_optimizations

    def _predict_seo_performance(
        self, keyword_analysis: Dict[str, Any], regional_focus: List[str]
    ) -> Dict[str, Any]:
        """Predict SEO performance based on optimization"""

        # Simplified performance prediction
        primary_keywords = len(keyword_analysis.get("primary_keywords", []))
        local_keywords = len(keyword_analysis.get("local_keywords", []))
        voice_keywords = len(keyword_analysis.get("voice_search_keywords", []))

        performance_score = min(
            100, (primary_keywords * 15) + (local_keywords * 10) + (voice_keywords * 5)
        )

        predictions = {
            "overall_seo_score": performance_score,
            "ranking_potential": {
                "local_searches": "High" if local_keywords > 10 else "Medium",
                "voice_searches": "High" if voice_keywords > 15 else "Medium",
                "mobile_searches": "High",  # Always high for Indian market
                "branded_searches": "Medium",
            },
            "expected_improvements": [
                f"20-30% increase in local search visibility for {', '.join(regional_focus[:2])}",
                "15-25% improvement in voice search rankings",
                "Improved mobile search performance and user experience",
                "Better featured snippet opportunities for FAQ content",
            ],
            "timeline_expectations": {
                "local_seo": "2-4 weeks for initial improvements",
                "organic_rankings": "3-6 months for significant movement",
                "voice_search": "1-3 months for optimization benefits",
                "technical_seo": "Immediate improvements after implementation",
            },
        }

        return predictions

    def _generate_comprehensive_recommendations(
        self, seo_result: Dict[str, Any]
    ) -> List[str]:
        """Generate comprehensive SEO recommendations"""

        recommendations = []

        # Keyword-based recommendations
        keyword_analysis = seo_result["keyword_analysis"]
        if len(keyword_analysis.get("primary_keywords", [])) < 3:
            recommendations.append(
                "Add more primary keywords focused on Indian market search terms"
            )

        if len(keyword_analysis.get("local_keywords", [])) < 5:
            recommendations.append(
                "Expand local keyword targeting for better regional visibility"
            )

        # Technical recommendations
        recommendations.extend(
            [
                "Implement mobile-first design optimized for Indian internet speeds",
                "Add structured data markup for better search result appearance",
                "Optimize images with Indian cultural context in alt text",
                "Create location-specific landing pages for each target city",
            ]
        )

        # Content recommendations
        recommendations.extend(
            [
                "Add FAQ section optimized for voice search queries",
                "Include customer testimonials with local context",
                "Create content around seasonal festivals and events",
                "Add internal links to related services and location pages",
            ]
        )

        # Local SEO recommendations
        recommendations.extend(
            [
                "Claim and optimize Google My Business listing",
                "Build citations in major Indian business directories",
                "Encourage customer reviews and respond promptly",
                "Create content about local community involvement",
            ]
        )

        return recommendations

    def _get_current_season_keywords(self) -> List[str]:
        """Get current seasonal keywords for Indian market"""
        # Simplified - would normally check actual dates
        seasonal_keywords = [
            "diwali offers",
            "festival sale",
            "monsoon special",
            "summer collection",
            "winter wear",
            "new year deals",
            "holi celebration",
            "eid special",
            "independence day offer",
            "wedding season",
            "back to school",
            "karva chauth",
        ]
        return seasonal_keywords

    def generate_content_headers(
        self, content: str, keyword_analysis: Dict[str, Any]
    ) -> List[str]:
        """Generate SEO-optimized headers for content"""

        primary_keywords = keyword_analysis.get("primary_keywords", [])
        secondary_keywords = keyword_analysis.get("secondary_keywords", [])

        headers = []

        # H1 - Main title with primary keyword
        if primary_keywords:
            headers.append(
                f"H1: Complete Guide to {primary_keywords[0].title()} in India"
            )

        # H2 - Major sections with secondary keywords
        if len(secondary_keywords) >= 2:
            headers.extend(
                [
                    f"H2: Why Choose {secondary_keywords[0].title()}?",
                    f"H2: Best {secondary_keywords[1].title()} Services in Your City",
                    f"H2: How to Find Reliable {primary_keywords[0] if primary_keywords else 'Service'} Providers",
                ]
            )

        # H3 - Subsections with long-tail keywords
        headers.extend(
            [
                "H3: Benefits for Indian Families",
                "H3: Pricing and Packages",
                "H3: Customer Reviews and Testimonials",
                "H3: Frequently Asked Questions",
                "H3: Contact Information and Booking",
            ]
        )

        return headers

    def create_local_seo_strategy(
        self, business_info: Dict[str, Any], regional_focus: List[str]
    ) -> Dict[str, Any]:
        """Create comprehensive local SEO strategy"""

        strategy = {
            "google_my_business_strategy": {
                "profile_optimization": [
                    "Complete all business information fields",
                    "Add high-quality photos (minimum 10 images)",
                    "Write compelling business description with keywords",
                    "Add relevant business attributes",
                    "Set accurate business hours and holiday schedules",
                    "Add products/services with descriptions",
                ],
                "posting_strategy": [
                    "Weekly posts about offers and updates",
                    "Event posts for festivals and special occasions",
                    "Product posts showcasing key services",
                    "Offer posts with clear call-to-actions",
                ],
                "review_management": [
                    "Respond to all reviews within 24 hours",
                    "Thank positive reviewers personally",
                    "Address negative reviews professionally",
                    "Encourage satisfied customers to leave reviews",
                ],
            },
            "local_keyword_strategy": {
                "primary_local_terms": [
                    f"{business_info.get('service', 'service')} in {city}"
                    for city in regional_focus
                ],
                "neighborhood_targeting": [
                    f"{business_info.get('service', 'service')} near {area}"
                    for area in ["me", "metro station", "mall", "market"]
                ],
                "service_area_keywords": [
                    f"best {business_info.get('service', 'service')} {city}"
                    for city in regional_focus
                ],
            },
            "citation_building_plan": {
                "tier_1_directories": [
                    "Google My Business",
                    "JustDial",
                    "Sulekha",
                    "Yellow Pages India",
                ],
                "industry_specific": [
                    "IndiaMART (B2B services)",
                    "Zomato (Food industry)",
                    "99acres (Real estate)",
                    "Naukri (Recruitment)",
                ],
                "local_directories": [
                    f"{city} business directory" for city in regional_focus
                ],
            },
            "content_localization": {
                "location_pages": [
                    f"Create dedicated page for {city} services"
                    for city in regional_focus
                ],
                "local_blog_topics": [
                    f"Top 10 {business_info.get('service', 'service')} providers in {regional_focus[0] if regional_focus else 'India'}",
                    f"How to choose {business_info.get('service', 'service')} in Indian metro cities",
                    f"Cost comparison of {business_info.get('service', 'service')} across Indian cities",
                ],
            },
        }

        return strategy

    def optimize_for_voice_search(
        self, content: str, target_audience: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Optimize content specifically for voice search"""

        voice_optimization = {
            "conversational_keywords": [],
            "question_based_content": [],
            "local_voice_queries": [],
            "mobile_voice_features": [],
            "structured_data_recommendations": [],
        }

        # Generate conversational keywords
        voice_optimization["conversational_keywords"] = [
            "how to find",
            "what is the best",
            "where can I get",
            "who provides",
            "when do you open",
            "how much does it cost",
        ]

        # Create question-based content suggestions
        business_type = target_audience.get("business_context", {}).get(
            "industry", "service"
        )
        voice_optimization["question_based_content"] = [
            f"What is the best {business_type} near me?",
            f"How much does {business_type} cost in India?",
            f"Who provides reliable {business_type} services?",
            f"When should I book {business_type} services?",
            f"Where can I find trusted {business_type} providers?",
        ]

        # Local voice queries
        voice_optimization["local_voice_queries"] = [
            "near me",
            "around here",
            "in my area",
            "closest to me",
            "within 5 km",
            "metro station nearby",
            "bus stop near",
        ]

        # Mobile voice features
        voice_optimization["mobile_voice_features"] = [
            "Click-to-call buttons prominently displayed",
            "Voice-friendly contact information",
            "Easy-to-pronounce business name",
            "Clear address with landmarks",
            "Operating hours clearly stated",
        ]

        # Structured data for voice search
        voice_optimization["structured_data_recommendations"] = [
            "FAQ schema for question-based content",
            "LocalBusiness schema with complete information",
            "Review schema for customer feedback",
            "Product/Service schema with pricing",
            "Event schema for special offers",
        ]

        return voice_optimization

    def analyze_competitor_seo(
        self, competitors: List[str], target_keywords: List[str]
    ) -> Dict[str, Any]:
        """Analyze competitor SEO strategies (simplified analysis)"""

        competitor_analysis = {
            "keyword_gaps": [],
            "content_opportunities": [],
            "technical_advantages": [],
            "local_seo_gaps": [],
            "recommendations": [],
        }

        # Simulated competitor analysis (in real implementation, would use SEO tools)
        competitor_analysis["keyword_gaps"] = [
            f"Long-tail keywords around '{target_keywords[0]} reviews'",
            f"Voice search terms for '{target_keywords[0]} near me'",
            f"Seasonal keywords for '{target_keywords[0]} festival offers'",
        ]

        competitor_analysis["content_opportunities"] = [
            "Create comprehensive FAQ section",
            "Add customer success stories with local context",
            "Develop location-specific service pages",
            "Create comparison guides for Indian market",
        ]

        competitor_analysis["technical_advantages"] = [
            "Faster page loading speeds for mobile users",
            "Better mobile user experience design",
            "More comprehensive structured data implementation",
            "Superior local SEO optimization",
        ]

        competitor_analysis["local_seo_gaps"] = [
            "Limited presence in tier-2 city directories",
            "Fewer customer reviews and ratings",
            "Missing location-specific content",
            "Weak Google My Business optimization",
        ]

        competitor_analysis["recommendations"] = [
            "Focus on long-tail keywords competitors are missing",
            "Create more comprehensive local content",
            "Improve technical SEO performance",
            "Build stronger local citation profile",
            "Enhance customer review generation strategy",
        ]

        return competitor_analysis

    def create_seo_content_calendar(
        self, business_info: Dict[str, Any], regional_focus: List[str]
    ) -> Dict[str, List[str]]:
        """Create SEO-focused content calendar for Indian market"""

        calendar = {
            "january": [
                "New Year business resolutions and goals",
                "Republic Day special offers and patriotic content",
                "Winter season service promotions",
                "Year-end review and customer testimonials",
            ],
            "february": [
                "Valentine's Day special services for couples",
                "Budget 2024 impact on industry analysis",
                "Spring season preparation content",
                "Customer success stories from previous year",
            ],
            "march": [
                "Holi festival special content and offers",
                "Financial year-end service promotions",
                "Women's Day celebration and recognition",
                "Spring cleaning and maintenance services",
            ],
            "april": [
                "New financial year business content",
                "Summer season preparation and services",
                "Gudi Padwa and regional new year celebrations",
                "Tax season service promotions",
            ],
            "may": [
                "Mother's Day special content and offers",
                "Summer vacation and travel-related services",
                "Labor Day recognition and worker appreciation",
                "Pre-monsoon preparation content",
            ],
            "june": [
                "Father's Day celebration content",
                "Monsoon preparation and safety tips",
                "Eid festival wishes and special offers",
                "Mid-year business review and goals",
            ],
            "july": [
                "Monsoon season services and solutions",
                "Guru Purnima education and learning content",
                "Independence Day preparation content",
                "Monsoon safety and maintenance tips",
            ],
            "august": [
                "Independence Day patriotic content and offers",
                "Raksha Bandhan family-focused content",
                "Janmashtami festival celebrations",
                "Back-to-school services and promotions",
            ],
            "september": [
                "Ganesh Chaturthi festival content and offers",
                "Teacher's Day educational content",
                "Post-monsoon maintenance and services",
                "Navratri festival preparation content",
            ],
            "october": [
                "Dussehra victory and success-themed content",
                "Pre-Diwali cleaning and preparation services",
                "Karva Chauth special offers for couples",
                "Festival season business promotions",
            ],
            "november": [
                "Diwali festival content and major promotions",
                "Children's Day family-focused content",
                "Bhai Dooj sibling celebration content",
                "Year-end service package promotions",
            ],
            "december": [
                "Christmas celebration and year-end offers",
                "New Year preparation and resolution content",
                "Winter season service promotions",
                "Annual review and customer appreciation",
            ],
        }

        # Customize calendar based on regional focus
        if "mumbai" in [region.lower() for region in regional_focus]:
            calendar["september"].append("Ganpati festival special Mumbai content")

        if "bengal" in [region.lower() for region in regional_focus] or "kolkata" in [
            region.lower() for region in regional_focus
        ]:
            calendar["october"].append("Durga Puja special Bengal-focused content")

        if "south" in [region.lower() for region in regional_focus] or any(
            city in ["chennai", "bangalore", "hyderabad"]
            for city in [r.lower() for r in regional_focus]
        ):
            calendar["april"].append("South Indian New Year celebrations")

        return calendar

    def generate_schema_markup(
        self, business_info: Dict[str, Any], content_type: str
    ) -> Dict[str, str]:
        """Generate structured data markup for Indian businesses"""

        schema_markup = {}

        # LocalBusiness Schema
        local_business_schema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": business_info.get("name", "Business Name"),
            "description": business_info.get(
                "description", "Professional services in India"
            ),
            "address": {
                "@type": "PostalAddress",
                "streetAddress": business_info.get("address", ""),
                "addressLocality": business_info.get("city", "Mumbai"),
                "addressRegion": business_info.get("state", "Maharashtra"),
                "postalCode": business_info.get("pincode", "400001"),
                "addressCountry": "IN",
            },
            "telephone": business_info.get("phone", "+91-98765-43210"),
            "url": business_info.get("website", ""),
            "openingHours": "Mo-Sa 10:00-19:00",
            "priceRange": business_info.get("price_range", "₹₹"),
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": business_info.get("latitude", "19.0760"),
                "longitude": business_info.get("longitude", "72.8777"),
            },
        }

        schema_markup["LocalBusiness"] = str(local_business_schema)

        # FAQ Schema for content with questions
        if "question" in content_type.lower() or "faq" in content_type.lower():
            faq_schema = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": f"What is the best {business_info.get('service', 'service')} in India?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f"The best {business_info.get('service', 'service')} depends on your specific needs and location. We provide personalized recommendations.",
                        },
                    }
                ],
            }
            schema_markup["FAQ"] = str(faq_schema)

        # Organization Schema
        organization_schema = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": business_info.get("name", "Business Name"),
            "url": business_info.get("website", ""),
            "logo": business_info.get("logo_url", ""),
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": business_info.get("phone", "+91-98765-43210"),
                "contactType": "customer service",
                "availableLanguage": ["English", "Hindi"],
            },
            "sameAs": [
                business_info.get("facebook_url", ""),
                business_info.get("twitter_url", ""),
                business_info.get("linkedin_url", ""),
            ],
        }

        schema_markup["Organization"] = str(organization_schema)

        return schema_markup

    def audit_current_seo(self, url: str, target_keywords: List[str]) -> Dict[str, Any]:
        """Audit current SEO performance (simplified analysis)"""

        audit_results = {
            "technical_seo": {
                "mobile_friendly": True,  # Would be checked via actual tools
                "page_speed_score": 75,  # Would be from PageSpeed Insights
                "https_enabled": True,
                "sitemap_present": True,
                "robots_txt_optimized": True,
            },
            "on_page_seo": {
                "title_optimized": False,
                "meta_description_present": True,
                "h1_tag_optimized": False,
                "keyword_density": 1.2,
                "internal_links": 5,
                "image_alt_tags": 60,  # Percentage
            },
            "local_seo": {
                "google_my_business_claimed": False,
                "local_citations": 3,
                "review_count": 12,
                "average_rating": 4.2,
                "location_pages": 0,
            },
            "content_quality": {
                "word_count": 850,
                "readability_score": 7.5,
                "indian_context": True,
                "call_to_action_present": True,
                "contact_info_visible": True,
            },
            "recommendations": [
                "Optimize title tags with primary keywords",
                "Improve page loading speed for mobile users",
                "Claim and optimize Google My Business listing",
                "Add more local citations in Indian directories",
                "Create location-specific landing pages",
                "Improve internal linking structure",
                "Add more customer reviews and testimonials",
            ],
            "priority_actions": [
                "Google My Business optimization (High Priority)",
                "Mobile page speed improvement (High Priority)",
                "Local citation building (Medium Priority)",
                "Content optimization for target keywords (Medium Priority)",
            ],
        }

        return audit_results
