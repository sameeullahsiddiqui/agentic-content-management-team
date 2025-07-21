"""
Base Agent Class for AutoGen Content Team India
Provides common functionality for all specialized agents

Author: Samee Ullah Siddiqui
Repository: https://github.com/sameeullahsiddiqui/agentic-content-management-team
"""

import os
import json
import yaml
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from pathlib import Path
import autogen
from autogen import AssistantAgent, UserProxyAgent

class BaseAgent(ABC):
    
    def __init__(
        self,
        name: str,
        agent_type: str,
        llm_config: Dict[str, Any],
        system_message: str,
        agent_config: Optional[Dict[str, Any]] = None,
        regional_config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize base agent
        
        Args:
            name: Agent name
            agent_type: Type of agent (assistant/userproxy)
            llm_config: LLM configuration
            system_message: System message for the agent
            agent_config: Agent-specific configuration
            regional_config: Indian market configuration
        """
        self.name = name
        self.agent_type = agent_type
        self.llm_config = llm_config
        self.system_message = system_message
        self.agent_config = agent_config or {}
        self.regional_config = regional_config or self._load_default_regional_config()
        
        # Initialize agent
        self.agent = self._create_agent()
        
        # Performance tracking
        self.conversation_count = 0
        self.success_rate = 0.0
        self.average_response_time = 0.0
    
    @abstractmethod
    def get_system_message(self) -> str:
        """Get the system message for this agent"""
        pass
    
    @abstractmethod
    def get_specialization(self) -> List[str]:
        """Get list of agent specializations"""
        pass
    
    def _create_agent(self):
        """Create the AutoGen agent instance"""
        enhanced_system_message = self._enhance_system_message()
        
        if self.agent_type.lower() == "userproxy":
            return UserProxyAgent(
                name=self.name,
                system_message=enhanced_system_message,
                human_input_mode=self.agent_config.get("human_input_mode", "NEVER"),
                max_consecutive_auto_reply=self.agent_config.get("max_consecutive_auto_reply", 3),
                is_termination_msg=self._is_termination_msg,
                code_execution_config=self.agent_config.get("code_execution_config", {
                    "work_dir": "output",
                    "use_docker": False
                })
            )
        else:
            # Assistant agent
            enhanced_llm_config = self._enhance_llm_config()
            return AssistantAgent(
                name=self.name,
                system_message=enhanced_system_message,
                llm_config=enhanced_llm_config
            )
    
    def _enhance_system_message(self) -> str:
        """Enhance system message with Indian market context"""
        base_message = self.get_system_message()
        
        # Add Indian market context
        indian_context = self._get_indian_market_context()
        cultural_guidelines = self._get_cultural_guidelines()
        performance_standards = self._get_performance_standards()
        
        enhanced_message = f"""
                            {base_message}

                            INDIAN MARKET CONTEXT:
                            {indian_context}

                            CULTURAL GUIDELINES:
                            {cultural_guidelines}

                            PERFORMANCE STANDARDS:
                            {performance_standards}

                            REGIONAL CONFIGURATION:
                            - Target Regions: {', '.join(self.regional_config.get('target_regions', []))}
                            - Primary Language: {self.regional_config.get('languages', {}).get('primary', 'english')}
                            - Cultural Events: {', '.join(self.regional_config.get('cultural_context', {}).get('festivals', []))}
                            - Business Context: Indian startups, SMEs, and enterprises

                            Remember: Always create content that resonates with Indian audiences while maintaining high quality and cultural sensitivity.
                            """
        return enhanced_message
    
    def _enhance_llm_config(self) -> Dict[str, Any]:
        """Enhance LLM config with agent-specific settings"""
        config = self.llm_config.copy()
        
        # Apply agent-specific settings
        if "temperature" in self.agent_config:
            config["temperature"] = self.agent_config["temperature"]
        if "max_tokens" in self.agent_config:
            config["max_tokens"] = self.agent_config["max_tokens"]
        if "timeout" in self.agent_config:
            config["timeout"] = self.agent_config["timeout"]
        
        return config
    
    def _get_indian_market_context(self) -> str:
        """Get Indian market context string"""
        return """
            - India is a diverse market with 28 states, 8 union territories, and 22+ official languages
            - Mobile-first market with 80%+ users accessing content on mobile devices
            - Price-sensitive consumers who value quality and authenticity
            - Strong preference for local examples, case studies, and cultural references
            - Growing digital adoption across tier-2 and tier-3 cities
            - Family-oriented decision making in most purchase decisions
            - High importance of trust, social proof, and community recommendations
            - Seasonal content opportunities around festivals and cultural events
            """
    
    def _get_cultural_guidelines(self) -> str:
        """Get cultural guidelines for content creation"""
        return """
                - Use simple, accessible English (8th grade reading level)
                - Include relevant Hindi phrases where appropriate and natural
                - Respect all religions, castes, and communities equally
                - Avoid controversial political topics unless specifically required
                - Use Indian numbering system (lakh, crore) alongside international formats
                - Include diverse representation across different Indian states and cultures
                - Consider regional preferences and local customs
                - Use appropriate Indian festivals and celebrations as content hooks
                - Include success stories and examples from Indian businesses
                - Consider the joint family structure in consumer messaging
                """
    
    def _get_performance_standards(self) -> str:
        """Get performance standards for content quality"""
        return """
            - Content must be culturally appropriate and locally relevant
            - Readability score should target 8th grade level for accessibility
            - Include specific Indian examples, data, or case studies where possible
            - Optimize for mobile consumption (short paragraphs, bullet points)
            - Use active voice and conversational tone
            - Include clear call-to-actions appropriate for Indian market
            - Ensure compliance with Indian advertising standards (ASCI guidelines)
            - Fact-check all Indian market data and statistics
            - Use appropriate Indian English conventions and spellings
            - Consider voice search optimization (growing trend in India)
            """
    
    def _is_termination_msg(self, message) -> bool:
        """Check if message indicates conversation should terminate"""
        content = message.get("content", "").lower()
        termination_phrases = [
            "final content approved",
            "task completed", 
            "content ready for publication",
            "terminate",
            "all requirements met",
            "project completed successfully"
        ]
        return any(phrase in content for phrase in termination_phrases)
    
    def _load_default_regional_config(self) -> Dict[str, Any]:
        """Load default Indian regional configuration"""
        return {
            "target_regions": [
                "mumbai", "delhi", "bangalore", "pune", "hyderabad", "chennai",
                "kolkata", "ahmedabad", "surat", "jaipur", "lucknow", "kanpur"
            ],
            "languages": {
                "primary": "english",
                "secondary": "hindi",
                "regional": ["tamil", "bengali", "telugu", "marathi", "gujarati", "kannada"]
            },
            "cultural_context": {
                "festivals": ["diwali", "holi", "eid", "christmas", "dussehra", "ganesh_chaturthi"],
                "business_hours": "10:00-19:00",
                "currency": "INR",
                "date_format": "DD/MM/YYYY"
            },
            "market_segments": {
                "metros": ["mumbai", "delhi", "bangalore", "chennai", "kolkata", "hyderabad"],
                "tier2": ["pune", "ahmedabad", "surat", "jaipur", "lucknow", "kanpur"],
                "tier3": ["agra", "meerut", "rajkot", "kalyan", "vasai", "aurangabad"]
            }
        }
    
    def get_agent_info(self) -> Dict[str, Any]:
        """Get comprehensive agent information"""
        return {
            "name": self.name,
            "type": self.agent_type,
            "specializations": self.get_specialization(),
            "conversation_count": self.conversation_count,
            "success_rate": self.success_rate,
            "average_response_time": self.average_response_time,
            "llm_provider": self.llm_config.get("config_list", [{}])[0].get("api_type", "unknown"),
            "regional_focus": self.regional_config.get("target_regions", [])[:5]  # Top 5 regions
        }
    
    def update_performance_metrics(self, response_time: float, success: bool):
        """Update agent performance metrics"""
        self.conversation_count += 1
        
        # Update success rate
        if self.conversation_count == 1:
            self.success_rate = 1.0 if success else 0.0
        else:
            self.success_rate = (
                (self.success_rate * (self.conversation_count - 1) + (1.0 if success else 0.0)) 
                / self.conversation_count
            )
        
        # Update average response time
        if self.conversation_count == 1:
            self.average_response_time = response_time
        else:
            self.average_response_time = (
                (self.average_response_time * (self.conversation_count - 1) + response_time) 
                / self.conversation_count
            )
    
    def save_conversation_log(self, conversation_data: Dict[str, Any], output_dir: Path):
        """Save conversation log for this agent"""
        log_file = output_dir / f"{self.name.lower()}_conversation_log.json"
        
        log_data = {
            "agent_name": self.name,
            "agent_type": self.agent_type,
            "timestamp": conversation_data.get("timestamp"),
            "conversation": conversation_data.get("messages", []),
            "performance_metrics": {
                "conversation_count": self.conversation_count,
                "success_rate": self.success_rate,
                "average_response_time": self.average_response_time
            }
        }
        
        try:
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save conversation log for {self.name}: {e}")
    
    def get_cultural_insights(self, content_type: str) -> Dict[str, Any]:
        """Get cultural insights for specific content type"""
        insights = {
            "social_media": {
                "best_posting_times": "7-9 PM IST (peak engagement)",
                "popular_hashtags": ["#India", "#MadeInIndia", "#Digital India"],
                "cultural_hooks": ["festivals", "cricket", "bollywood", "family values"],
                "platform_preferences": {
                    "instagram": "Visual storytelling, reels, stories",
                    "facebook": "Community engagement, family content",
                    "linkedin": "Professional networking, thought leadership",
                    "whatsapp": "Personal communication, business updates"
                }
            },
            "blog_article": {
                "preferred_length": "1000-1500 words for Indian readers",
                "structure": ["hook", "problem", "solution", "Indian examples", "call-to-action"],
                "seo_keywords": "Include Indian city names and local terms",
                "examples": "Use Indian companies, entrepreneurs, and success stories"
            },
            "email_campaign": {
                "subject_lines": "Include numbers, urgency, and local references",
                "personalization": "Use first names and regional greetings",
                "timing": "Tuesday-Thursday, 10 AM - 2 PM IST",
                "mobile_optimization": "90% open emails on mobile"
            }
        }
        
        return insights.get(content_type, {})
    
    def validate_content_quality(self, content: str) -> Dict[str, Any]:
        """Validate content quality for Indian market"""
        quality_check = {
            "readability": self._check_readability(content),
            "cultural_appropriateness": self._check_cultural_sensitivity(content),
            "indian_references": self._check_indian_context(content),
            "mobile_optimization": self._check_mobile_friendliness(content),
            "call_to_action": self._check_cta_presence(content)
        }
        
        # Overall score
        scores = [score for score in quality_check.values() if isinstance(score, (int, float))]
        quality_check["overall_score"] = sum(scores) / len(scores) if scores else 0.0
        
        return quality_check
    
    def _check_readability(self, content: str) -> float:
        """Check content readability (simplified)"""
        # Simple readability check - count of short sentences vs long sentences
        sentences = content.split('.')
        short_sentences = sum(1 for s in sentences if len(s.split()) <= 15)
        total_sentences = len(sentences)
        
        if total_sentences == 0:
            return 0.0
            
        readability_score = (short_sentences / total_sentences) * 100
        return min(readability_score, 100.0)
    
    def _check_cultural_sensitivity(self, content: str) -> bool:
        """Check for cultural sensitivity (basic implementation)"""
        # Check for potentially insensitive terms
        sensitive_terms = [
            "backward", "primitive", "third world", "developing country" 
        ]
        
        content_lower = content.lower()
        return not any(term in content_lower for term in sensitive_terms)
    
    def _check_indian_context(self, content: str) -> bool:
        """Check if content includes Indian context"""
        indian_terms = [
            "india", "indian", "rupee", "₹", "lakh", "crore",
            "mumbai", "delhi", "bangalore", "chennai", "kolkata", "hyderabad",
            "diwali", "holi", "cricket", "bollywood"
        ]
        
        content_lower = content.lower()
        return any(term in content_lower for term in indian_terms)
    
    def _check_mobile_friendliness(self, content: str) -> float:
        """Check mobile-friendliness (simplified)"""
        # Check for short paragraphs and bullet points
        paragraphs = content.split('\n\n')
        short_paragraphs = sum(1 for p in paragraphs if len(p.split()) <= 50)
        
        if len(paragraphs) == 0:
            return 0.0
            
        mobile_score = (short_paragraphs / len(paragraphs)) * 100
        return min(mobile_score, 100.0)
    
    def _check_cta_presence(self, content: str) -> bool:
        """Check for call-to-action presence"""
        cta_phrases = [
            "contact us", "call now", "visit", "click here", "learn more",
            "get started", "sign up", "subscribe", "download", "book now"
        ]
        
        content_lower = content.lower()
        return any(phrase in content_lower for phrase in cta_phrases)

# Utility functions for agents
def load_agent_config(config_path: str = "config/agents.yaml") -> Dict[str, Any]:
    """Load agent configuration from YAML file"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Warning: Could not load agent config: {e}")
        return {}

def save_agent_config(config: Dict[str, Any], config_path: str = "config/agents.yaml"):
    """Save agent configuration to YAML file"""
    try:
        Path(config_path).parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Warning: Could not save agent config: {e}")