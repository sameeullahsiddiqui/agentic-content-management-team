"""
Agentic Content Creation Team

Author: Samee Ullah Siddiqui
Repository: https://github.com/sameeullahsiddiqui/agentic-content-management-team
"""

import os
import asyncio
from pathlib import Path
import sys
from typing import Dict, Any, Optional, List
import json
import autogen
from dotenv import load_dotenv
import yaml
from datetime import datetime

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root) + "/src/agents")

from project_manager_agent import ProjectManagerAgent
from content_writer_agent import ContentWriterAgent
from content_editor_agent import ContentEditorAgent
from seo_specilist_agent import SEOSpecialistAgent
from brand_strategist_agent import BrandStrategistAgent


class ContentCreationTeam:
    def __init__(self):

        self.work_dir = Path("output")
        self.work_dir.mkdir(exist_ok=True)

        self.llm_config = self._setup_llm_config()

        self.agent_config = self._load_agent_config()
        self.regional_config = self._load_regional_config()

        self.llm_provider = os.getenv("SELECTED_PROVIDER", "").lower()

        self._initialize_agents()

    def _initialize_agents(self):

        # Project Manager Agent (UserProxy with specialized configuration)
        self.project_manager = ProjectManagerAgent(
            llm_config=self.llm_config,
            agent_config=self.agent_config.get("project_manager", {}),
            regional_config=self.regional_config,
        )

        # Content Writer Agent
        self.content_writer = ContentWriterAgent(
            llm_config=self.llm_config,
            agent_config=self.agent_config.get("content_writer", {}),
            regional_config=self.regional_config,
        )

        # Content Editor Agent
        self.content_editor = ContentEditorAgent(
            llm_config=self.llm_config,
            agent_config=self.agent_config.get("content_editor", {}),
            regional_config=self.regional_config,
        )

        # SEO Specialist Agent
        self.seo_specialist = SEOSpecialistAgent(
            llm_config=self.llm_config,
            agent_config=self.agent_config.get("seo_specialist", {}),
            regional_config=self.regional_config,
        )

        # Brand Strategist Agent (New)
        self.brand_strategist = BrandStrategistAgent(
            llm_config=self.llm_config,
            agent_config=self.agent_config.get("brand_strategist", {}),
            regional_config=self.regional_config,
        )

        print(f"    Initialized specialized agents for Indian market content creation")

    def create_content(
        self, content_brief: str, content_type: str = "general"
    ) -> Dict[str, Any]:
        print(f"\nStarting content creation project...")

        enhanced_brief = ""
        groupchat = None

        try:

            # Step 1: Brand Strategist analyzes brand positioning requirements
            brand_analysis = self._get_brand_strategy_analysis(
                content_brief, content_type
            )

            # Step 2: Enhance brief with context and brand strategy
            enhanced_brief = self._enhance_brief_with_context(
                content_brief, content_type, brand_analysis
            )

            # Step 3: Project Manager initiates the workflow
            groupchat = autogen.GroupChat(
                agents=[
                    self.project_manager.agent,
                    self.content_writer.agent,
                    self.content_editor.agent,
                    self.seo_specialist.agent,
                    self.brand_strategist.agent,
                ],
                messages=[],
                max_round=100,
                speaker_selection_method="auto",  # or "round_robin" or custom
            )

            # Step 4: Create GroupChat Manager
            manager = autogen.GroupChatManager(
                groupchat=groupchat, llm_config=self.llm_config
            )

            # Step 5: Start the collaborative workflow
            self.project_manager.agent.initiate_chat(manager, message=enhanced_brief)

        except Exception as e:
            print(f"Error during content creation: {e}")
            raise ValueError("error: " + str(e))

            # Step 6: Extract and save results
        results = self._extract_and_save_results(
            enhanced_brief, content_type, groupchat, None
        )

        print("\nContent creation completed!")
        print(f"Check the output in: {self.work_dir}")

        return results

    def _get_brand_strategy_analysis(
        self, brief: str, content_type: str
    ) -> Dict[str, Any]:

        print(" Brand Strategist analyzing positioning requirements...")

        # Extract brand information from brief or use defaults
        brand_info = {
            "industry": self._extract_industry_from_brief(brief),
            "target_audience": self._extract_audience_from_brief(brief),
            "budget_range": "medium",  # Default or extract from brief
            "regional_focus": "pan_india",  # Based on regional config
        }

        brand_analysis = self.brand_strategist.analyze_brand_positioning(brand_info)

        print(
            f"    Brand strategy: {brand_analysis['positioning_strategy']['messaging_focus']}"
        )
        print(
            f"    Brand archetype: {brand_analysis['brand_archetype']['description']}"
        )

        return brand_analysis

    def _extract_industry_from_brief(self, brief: str) -> str:
        """Extract industry from content brief"""
        brief_lower = brief.lower()
        industry_keywords = {
            "technology": [
                "tech",
                "software",
                "digital",
                "app",
                "platform",
                "ai",
                "ml",
            ],
            "healthcare": [
                "health",
                "medical",
                "doctor",
                "hospital",
                "medicine",
                "wellness",
            ],
            "education": [
                "education",
                "learning",
                "school",
                "course",
                "training",
                "skill",
            ],
            "finance": [
                "finance",
                "banking",
                "investment",
                "money",
                "loan",
                "insurance",
            ],
            "food": ["food", "restaurant", "cuisine", "recipe", "cooking", "meal"],
            "retail": ["retail", "shopping", "store", "product", "sale", "customer"],
        }

        for industry, keywords in industry_keywords.items():
            if any(keyword in brief_lower for keyword in keywords):
                return industry

        return "general"

    def _extract_audience_from_brief(self, brief: str) -> str:
        """Extract target audience from content brief"""
        brief_lower = brief.lower()
        audience_keywords = {
            "young_professionals": [
                "professional",
                "career",
                "young",
                "graduate",
                "employee",
            ],
            "families_with_children": [
                "family",
                "children",
                "kids",
                "parent",
                "mother",
                "father",
            ],
            "seniors": ["senior", "elderly", "retirement", "pension", "mature"],
            "students": ["student", "college", "university", "academic", "study"],
            "entrepreneurs": ["entrepreneur", "business", "startup", "founder", "sme"],
        }

        for audience, keywords in audience_keywords.items():
            if any(keyword in brief_lower for keyword in keywords):
                return audience

        return "middle_class_families"

    def _enhance_brief_with_context(
        self, brief: str, content_type: str, brand_analysis: Dict[str, Any]
    ) -> str:

        regional_info = self.regional_config

        enhanced_brief = f"""
                            CONTENT CREATION PROJECT - INDIAN MARKET FOCUS
                            
                            ORIGINAL BRIEF: {brief}
                            
                            CONTENT TYPE: {content_type}
                            
                                                      
                            BRAND STRATEGY CONTEXT:
                            - Brand Positioning: {brand_analysis['positioning_strategy']['messaging_focus']}
                            - Brand Archetype: {brand_analysis['brand_archetype']['description']}
                            - Brand Voice: {', '.join(brand_analysis['messaging_framework']['tone_of_voice']['primary_characteristics'])}
                            - Cultural Hooks: {', '.join(brand_analysis['messaging_framework']['cultural_hooks'])}
                            - Trust Strategy: Focus on {brand_analysis['trust_building_strategy']['primary_focus'][0]['description'] if brand_analysis['trust_building_strategy']['primary_focus'] else 'relationship building'}
 
                            INDIAN MARKET CONTEXT:
                            - Target Regions: {', '.join(regional_info['target_regions'])}
                            - Primary Language: {regional_info['languages']['primary']}
                            - Cultural Context: Indian business ecosystem with focus on {', '.join(regional_info['cultural_context']['festivals'])}
                            - Currency: {regional_info['cultural_context']['currency']}
                            - Market Segments: Metro, Tier-2, and Tier-3 cities
                            
                            CONTENT REQUIREMENTS:
                            1. Use simple, accessible English (8th grade reading level)
                            2. Include relevant Indian examples and cultural references
                            3. Optimize for mobile-first consumption (80% of Indian users)
                            4. Consider regional variations and cultural sensitivities
                            5. Include appropriate call-to-actions for Indian market
                            6. Ensure compliance with Indian advertising guidelines
                            
                            COLLABORATION WORKFLOW:
                            1. ContentWriter: Create initial content with Indian context
                            2. ContentEditor: Review for quality, culture, and compliance
                            3. SEOSpecialist: Optimize for Indian search behavior
                            4. BrandStrategist: Ensure brand alignment and cultural fit
                            5. ProjectManager: Final review and approval
                            
                            LLM PROVIDER: {self.llm_provider.upper()}
                            
                            Please start with content creation. The team will collaborate until we achieve 
                            high-quality, culturally appropriate content for the Indian market.
                            """
        return enhanced_brief

    def _extract_and_save_results(
        self, brief: str, content_type: str, groupchat=None, final_messages=None
    ) -> Dict[str, Any]:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        results = {
            "brief": brief,
            "content_type": content_type,
            "timestamp": timestamp,
            "llm_provider": self.llm_provider,
            "agents_used": [
                "ProjectManager",
                "ContentWriter",
                "ContentEditor",
                "SEOSpecialist",
                "BrandStrategist",
            ],
            "status": "completed",
            "output_files": [],
            "conversation_stats": {},
            "final_content": {},
        }

        try:
            # Extract messages from GroupChat
            messages = []
            if groupchat and hasattr(groupchat, "messages"):
                messages = groupchat.messages
            elif final_messages:
                messages = final_messages

            # Analyze conversation statistics
            if messages:
                results["conversation_stats"] = {
                    "total_messages": len(messages),
                    "agents_participated": len(
                        set(msg.get("name", "Unknown") for msg in messages)
                    ),
                    "message_breakdown": {},
                }

                # Count messages per agent
                for msg in messages:
                    agent_name = msg.get("name", "Unknown")
                    if (
                        agent_name
                        not in results["conversation_stats"]["message_breakdown"]
                    ):
                        results["conversation_stats"]["message_breakdown"][
                            agent_name
                        ] = 0
                    results["conversation_stats"]["message_breakdown"][agent_name] += 1

            # Extract final content
            final_content = self._extract_final_campaign_content(messages)
            results["final_content"] = final_content

            # Save complete conversation log
            conversation_log_file = self.work_dir / f"conversation_log_{timestamp}.md"
            with open(conversation_log_file, "w", encoding="utf-8") as f:
                f.write("=" * 80 + "\n")
                f.write("AUTOGEN CONTENT CREATION TEAM - COMPLETE CONVERSATION LOG\n")
                f.write("=" * 80 + "\n\n")
                f.write(f"Brief: {brief}\n")
                f.write(f"Content Type: {content_type}\n")
                f.write(f"LLM Provider: {self.llm_provider}\n")
                f.write(f"Timestamp: {timestamp}\n")
                f.write(f"Total Messages: {len(messages)}\n\n")

                if messages:
                    f.write("CONVERSATION FLOW:\n")
                    f.write("-" * 50 + "\n\n")

                    for i, msg in enumerate(messages, 1):
                        agent_name = msg.get("name", "Unknown")
                        content = msg.get("content", "")
                        f.write(f"[Message {i}] {agent_name}:\n")
                        f.write("~" * 40 + "\n")
                        f.write(content)
                        f.write("\n\n")
                else:
                    f.write("No conversation messages found.\n")

            results["output_files"].append(str(conversation_log_file))

            # Save final campaign content separately
            if final_content.get("final_campaign"):
                campaign_file = self.work_dir / f"final_campaign_{timestamp}.md"
                with open(campaign_file, "w", encoding="utf-8") as f:
                    f.write("=" * 80 + "\n")
                    f.write("FINAL CAMPAIGN CONTENT\n")
                    f.write("=" * 80 + "\n\n")
                    f.write("ORIGINAL BRIEF:\n")
                    f.write("-" * 40 + "\n")
                    f.write(brief)
                    f.write("\n\n")
                    f.write("FINAL CAMPAIGN:\n")
                    f.write("-" * 40 + "\n")
                    f.write(final_content["final_campaign"])
                    f.write("\n\n")
                    f.write("=" * 80 + "\n")
                    f.write("CAMPAIGN METADATA:\n")
                    f.write("=" * 80 + "\n")
                    f.write(f"Content Type: {content_type}\n")
                    f.write(
                        f"Generated By: {final_content.get('generated_by', 'Multiple Agents')}\n"
                    )
                    f.write(
                        f"Word Count: {len(final_content['final_campaign'].split())}\n"
                    )
                    f.write(
                        f"Character Count: {len(final_content['final_campaign'])}\n"
                    )

                results["output_files"].append(str(campaign_file))
                print(f"✅ Final campaign saved to: {campaign_file}")

            # Save agent contributions breakdown
            if final_content.get("agent_contributions"):
                contributions_file = (
                    self.work_dir / f"agent_contributions_{timestamp}.json"
                )
                with open(contributions_file, "w", encoding="utf-8") as f:
                    json.dump(
                        final_content["agent_contributions"],
                        f,
                        indent=2,
                        ensure_ascii=False,
                    )

                results["output_files"].append(str(contributions_file))

            # Save project metadata with enhanced information
            metadata_file = self.work_dir / f"project_metadata_{timestamp}.json"
            with open(metadata_file, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2, ensure_ascii=False)

            results["output_files"].append(str(metadata_file))

            # Print summary
            print(f"\n📁 Results saved: {len(results['output_files'])} files")
            print(
                f"💬 Conversation: {results['conversation_stats'].get('total_messages', 0)} messages"
            )
            print(
                f"🤖 Agents participated: {results['conversation_stats'].get('agents_participated', 0)}"
            )

            if final_content.get("final_campaign"):
                word_count = len(final_content["final_campaign"].split())
                print(f"📝 Final campaign: {word_count} words")

        except Exception as e:
            print(f"❌ Could not save results: {e}")
            results["save_error"] = str(e)
            import traceback

            print(f"Full error: {traceback.format_exc()}")

        return results

    def _extract_final_campaign_content(self, messages: list) -> Dict[str, Any]:
        """Extract the final campaign content from conversation messages"""

        final_content = {
            "original_brief": "",
            "final_campaign": "",
            "last_message": "",
            "generated_by": "Unknown",
            "agent_contributions": {},
            "content_evolution": [],
        }

        if not messages:
            return final_content

        try:
            # Get original brief (first message)
            if messages:
                final_content["original_brief"] = messages[0].get("content", "")

            # Track each agent's contributions
            for msg in messages:
                agent_name = msg.get("name", "Unknown")
                content = msg.get("content", "")

                if agent_name not in final_content["agent_contributions"]:
                    final_content["agent_contributions"][agent_name] = []

                final_content["agent_contributions"][agent_name].append(
                    {
                        "content": content,
                        "length": len(content),
                        "word_count": len(content.split()),
                    }
                )

            # Get the last message
            final_content["last_message"] = messages[-1].get("content", "")
            final_content["generated_by"] = messages[-1].get("name", "Unknown")

            # Try to identify the most substantial final content
            # Look for the longest message from content creation agents
            content_agents = ["ContentWriter", "ContentEditor", "SEOSpecialist"]
            best_content = ""
            best_agent = ""

            for msg in reversed(messages):  # Start from the end
                agent_name = msg.get("name", "")
                content = msg.get("content", "")

                # Prioritize content from writing agents
                if agent_name in content_agents and len(content) > len(best_content):
                    best_content = content
                    best_agent = agent_name

            # If no content from writing agents, use the longest message overall
            if not best_content:
                for msg in messages:
                    content = msg.get("content", "")
                    if len(content) > len(best_content):
                        best_content = content
                        best_agent = msg.get("name", "Unknown")

            final_content["final_campaign"] = best_content
            if best_agent:
                final_content["generated_by"] = best_agent

            # Track content evolution (how content changed through the conversation)
            substantial_messages = [
                msg for msg in messages if len(msg.get("content", "")) > 100
            ]
            final_content["content_evolution"] = [
                {
                    "agent": msg.get("name", "Unknown"),
                    "length": len(msg.get("content", "")),
                    "preview": (
                        msg.get("content", "")[:100] + "..."
                        if len(msg.get("content", "")) > 100
                        else msg.get("content", "")
                    ),
                }
                for msg in substantial_messages
            ]

        except Exception as e:
            print(f"Error extracting final content: {e}")
            final_content["extraction_error"] = str(e)

        return final_content

    def _load_agent_config(self) -> Dict[str, Any]:

        config_file = Path("config/agents.yaml")
        if config_file.exists():
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    return yaml.safe_load(f)
            except Exception:
                pass

        # Default configuration
        return {
            "project_manager": {"temperature": 0.3, "max_tokens": 1000, "timeout": 120},
            "content_writer": {"temperature": 0.7, "max_tokens": 2000, "timeout": 180},
            "content_editor": {"temperature": 0.4, "max_tokens": 1500, "timeout": 150},
            "seo_specialist": {"temperature": 0.2, "max_tokens": 800, "timeout": 120},
        }

    def _load_regional_config(self) -> Dict[str, Any]:
        """Load regional configuration settings"""
        config_file = Path("config/regional_settings.yaml")
        if config_file.exists():
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    return yaml.safe_load(f)
            except Exception:
                pass

        # Default Indian market configuration
        return {
            "target_regions": [
                "mumbai",
                "delhi",
                "bangalore",
                "pune",
                "hyderabad",
                "chennai",
            ],
            "languages": {
                "primary": "english",
                "secondary": "hindi",
                "regional": ["tamil", "bengali", "telugu", "marathi"],
            },
            "cultural_context": {
                "festivals": ["diwali", "holi", "eid", "christmas", "dussehra"],
                "business_hours": "10:00-19:00",
                "currency": "INR",
                "date_format": "DD/MM/YYYY",
            },
            "market_segments": {
                "metros": [
                    "mumbai",
                    "delhi",
                    "bangalore",
                    "chennai",
                    "kolkata",
                    "hyderabad",
                ],
                "tier2": ["pune", "ahmedabad", "surat", "jaipur", "lucknow", "kanpur"],
                "tier3": ["agra", "meerut", "rajkot", "kalyan", "vasai", "aurangabad"],
            },
        }

    def _setup_llm_config(self) -> Dict[str, Any]:

        load_dotenv()

        provider = os.getenv("SELECTED_PROVIDER", "").lower()
        api_key = "your-api-key-here"

        if provider == "azure":
            api_key = os.getenv("AZURE_OPENAI_API_KEY")
            llm_config = {
                "config_list": [
                    {
                        "model": os.getenv(
                            "AZURE_OPENAI_DEPLOYMENT_MODEL", "gpt-35-turbo"
                        ),
                        "api_key": api_key,
                        "api_type": "azure",
                        "base_url": os.getenv("AZURE_OPENAI_ENDPOINT"),
                        "api_version": os.getenv(
                            "AZURE_OPENAI_API_VERSION", "2023-05-15"
                        ),
                    }
                ],
                "temperature": float(os.getenv("AZURE_TEMPERATURE", 0.7)),
                "timeout": 120,
            }

        elif provider == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            llm_config = {
                "config_list": [
                    {
                        "model": os.getenv("OPENAI_MODEL", "gpt-4"),
                        "api_key": api_key,
                        "api_type": "openai",
                    }
                ],
                "temperature": float(os.getenv("OPENAI_TEMPERATURE", 0.7)),
                "timeout": 120,
            }

        elif provider == "lmstudio":
            api_key = os.getenv("LMSTUDIO_API_KEY")
            price_str = os.getenv("LMSTUDIO_PRICE", "0.0,0.0")
            price = list(map(float, price_str.split(",")))

            llm_config = {
                "config_list": [
                    {
                        "model": os.getenv("LMSTUDIO_MODEL", "llama-2-7b-chat"),
                        "base_url": os.getenv(
                            "LMSTUDIO_BASE_URL", "http://127.0.0.1:1234/v1"
                        ),
                        "api_key": api_key,
                        "api_type": os.getenv("LMSTUDIO_API_TYPE", "openai"),
                        "max_tokens": int(os.getenv("LMSTUDIO_MAX_TOKENS", 2048)),
                        "price": price,
                    }
                ],
                "temperature": float(os.getenv("LMSTUDIO_TEMPERATURE", 0.7)),
                "timeout": 300,
            }

        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")

        if not api_key or api_key == "your-api-key-here":
            raise ValueError("Please provide a valid API key for the LLM provider.")

        return llm_config

    def _check_termination(self, message) -> bool:
        """Check if conversation should be terminated"""
        content = message.get("content", "").lower()
        termination_phrases = [
            "final content approved",
            "terminate",
            "task completed",
            "content ready for publication",
            "all requirements met",
        ]
        return any(phrase in content for phrase in termination_phrases)

    def create_social_media_campaign(self, campaign_brief: str) -> Dict[str, Any]:
        """Specialized method for social media content creation"""
        print(f"\n  Creating social media campaign...")

        enhanced_brief = f"""
                        SOCIAL MEDIA CAMPAIGN PROJECT - INDIAN MARKET
                        
                        Brief: {campaign_brief}
                        
                        DELIVERABLES REQUIRED:
                        1. Instagram Posts (3-5 posts with captions and hashtags)
                        - Carousel posts for educational content
                        - Story templates with Indian design elements
                        - Reel scripts with trending Indian audio/music suggestions
                        
                        2. LinkedIn Professional Content
                        - Thought leadership posts for Indian business community
                        - Company update templates
                        - Industry insight posts with Indian market data
                        
                        3. Facebook Posts for Broader Reach
                        - Community-focused content
                        - Event promotion templates
                        - Customer testimonial formats
                        
                        4. Twitter/X Content
                        - Thread templates on relevant topics
                        - Quick tips and insights
                        - Live-tweeting templates for Indian events
                        
                        5. WhatsApp Business Messages
                        - Customer communication templates
                        - Promotional message formats
                        - Order confirmation and support templates
                        
                        INDIAN SOCIAL MEDIA REQUIREMENTS:
                        - Use trending Indian hashtags and topics
                        - Include festival and cultural tie-ins
                        - Optimize for peak Indian social media hours (7-9 PM)
                        - Consider regional language hashtags
                        - Include appropriate emojis for Indian audience
                        - Account for Indian social media consumption patterns
                        - Include call-to-actions relevant to Indian users (UPI payments, WhatsApp contact)
                        
                        Platform-specific optimization for Indian users:
                        - Instagram: Visual storytelling with Indian aesthetics
                        - LinkedIn: Professional networking in Indian business context
                        - Facebook: Community building and local engagement
                        - Twitter: Real-time engagement with Indian trends
                        - WhatsApp: Personal, direct communication style
                        """

        return self.create_content(enhanced_brief, "social_media_campaign")

    def create_blog_article(
        self,
        topic: str,
        target_audience: str = "Indian businesses",
        word_count: int = 1500,
    ) -> Dict[str, Any]:
        """Specialized method for blog article creation"""
        print(f"\n📰 Creating blog article...")

        blog_brief = f"""
        BLOG ARTICLE PROJECT - INDIAN MARKET FOCUS
        
        Topic: {topic}
        Target Audience: {target_audience}
        Word Count: {word_count} words
        
        ARTICLE STRUCTURE REQUIREMENTS:
        1. Compelling headline optimized for Indian search behavior
        2. Meta description (150-160 characters) with Indian keywords
        3. Introduction with Indian market context and statistics
        4. Main content sections with clear headers (H2, H3)
        5. Indian case studies and examples throughout
        6. Actionable takeaways relevant to Indian business environment
        7. Conclusion with clear call-to-action for Indian readers
        8. Suggested internal linking topics for Indian websites
        
        CONTENT REQUIREMENTS:
        - Include recent Indian market data and statistics
        - Reference successful Indian companies and entrepreneurs
        - Address common challenges faced by Indian businesses
        - Provide solutions relevant to Indian market conditions
        - Include cultural context and local insights
        - Optimize for Indian search queries and voice search
        
        SEO OPTIMIZATION:
        - Primary keyword research for Indian market
        - Secondary keyword integration throughout content
        - Local SEO considerations for Indian cities
        - Image suggestions with Indian context
        - FAQ section addressing common Indian market questions
        
        EXPERTISE AREAS TO COVER:
        - Market insights specific to India
        - Regulatory and compliance considerations
        - Cost-effective solutions for Indian businesses
        - Technology adoption trends in India
        - Success stories from Indian market
        """

        return self.create_content(blog_brief, "blog_article")

    def create_email_campaign(
        self, campaign_objective: str, audience_segment: str
    ) -> Dict[str, Any]:
        """Specialized method for email marketing campaigns"""
        print(f"\n📧 Creating email campaign...")

        email_brief = f"""
        EMAIL MARKETING CAMPAIGN - INDIAN AUDIENCE
        
        Campaign Objective: {campaign_objective}
        Audience Segment: {audience_segment}
        
        EMAIL SERIES DELIVERABLES:
        1. Welcome Email Series (3-5 emails)
        2. Promotional Campaign Emails
        3. Newsletter Template
        4. Abandoned Cart Recovery (for e-commerce)
        5. Customer Retention Emails
        6. Festival/Seasonal Campaign Emails
        
        INDIAN EMAIL MARKETING CONSIDERATIONS:
        - Mobile-first design (90% of Indians check email on mobile)
        - Hindi subject lines where appropriate
        - Regional festival greetings and offers
        - UPI payment integration mentions
        - WhatsApp contact options
        - Local delivery and support information
        
        CONTENT ELEMENTS:
        - Personalized greetings with Indian cultural context
        - Local testimonials and success stories
        - Region-specific offers and promotions
        - Cultural holidays and festival acknowledgments
        - Trust signals important to Indian consumers
        - Clear value propositions in Indian context
        
        COMPLIANCE REQUIREMENTS:
        - CAN-SPAM compliance
        - Indian data protection considerations
        - Unsubscribe options in local languages
        - Contact information with Indian address
        """

        return self.create_content(email_brief, "email_campaign")

    def analyze_competitor_content(
        self, competitor_info: str, analysis_focus: str
    ) -> Dict[str, Any]:
        """Analyze competitor content and provide strategic insights"""
        print(f"\n🔍 Analyzing competitor content...")

        analysis_brief = f"""
        COMPETITOR CONTENT ANALYSIS - INDIAN MARKET
        
        Competitor Information: {competitor_info}
        Analysis Focus: {analysis_focus}
        
        ANALYSIS DELIVERABLES:
        1. Content Strategy Assessment
           - Content types and formats used
           - Publishing frequency and timing
           - Engagement levels and audience response
        
        2. Cultural Adaptation Analysis
           - How well competitor adapts to Indian culture
           - Regional customization strategies
           - Festival and seasonal content approach
        
        3. SEO and Digital Marketing Assessment
           - Keyword strategy for Indian market
           - Social media presence and engagement
           - Local SEO and business listings
        
        4. Opportunities and Gaps
           - Underserved audience segments
           - Content gaps in Indian market
           - Improvement opportunities
        
        5. Strategic Recommendations
           - Content differentiation strategies
           - Cultural positioning opportunities
           - Market penetration tactics
        
        INDIAN MARKET ANALYSIS FOCUS:
        - Regional market penetration
        - Cultural sensitivity and adaptation
        - Price positioning and value communication
        - Trust building strategies
        - Community engagement approaches
        - Festival and seasonal marketing effectiveness
        """

        return self.create_content(analysis_brief, "competitor_analysis")

    def get_performance_report(self) -> Dict[str, Any]:
        """Generate performance report of content creation activities"""
        output_files = list(self.work_dir.glob("*.json"))

        report = {
            "total_projects": len(output_files),
            "llm_provider": self.llm_provider,
            "output_directory": str(self.work_dir),
            "agents_configured": len(self.agent_config),
            "regional_settings": self.regional_config["target_regions"],
            "recent_projects": [],
        }

        # Add recent project information
        for file_path in sorted(output_files, reverse=True)[:5]:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    project_data = json.load(f)
                    report["recent_projects"].append(
                        {
                            "timestamp": project_data.get("timestamp"),
                            "content_type": project_data.get("content_type"),
                            "status": project_data.get("status"),
                            "brief_preview": project_data.get("brief", "")[:100]
                            + "...",
                        }
                    )
            except Exception:
                continue

        return report


def create_content_team_with_openai(
    api_key: str, model: str = "gpt-4"
) -> ContentCreationTeam:
    """
    Create ContentCreationTeam with OpenAI configuration

    Args:
        api_key: OpenAI API key
        model: Model name (default: gpt-4)

    Returns:
        Configured ContentCreationTeam instance
    """
    llm_config = {"provider": "openai", "api_key": api_key, "model": model}
    return ContentCreationTeam(llm_config)


def create_content_team_with_azure(
    api_key: str, endpoint: str, model: str, api_version: str = "2024-02-15-preview"
) -> ContentCreationTeam:
    """
    Create ContentCreationTeam with Azure OpenAI configuration

    Args:
        api_key: Azure OpenAI API key
        endpoint: Azure OpenAI endpoint URL
        model: model/model name
        api_version: API version (default: 2024-02-15-preview)

    Returns:
        Configured ContentCreationTeam instance
    """
    llm_config = {
        "provider": "azure",
        "api_key": api_key,
        "endpoint": endpoint,
        "model": model,
        "api_version": api_version,
    }
    return ContentCreationTeam(llm_config)
