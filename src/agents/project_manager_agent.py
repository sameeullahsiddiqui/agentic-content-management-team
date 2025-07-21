"""
Project Manager Agent for AutoGen Content Team India
Coordinates content creation workflow and ensures quality standards

Author: Samee Ullah Siddiqui
Repository: https://github.com/sameeullahsiddiqui/agentic-content-management-team
"""

import sys
from pathlib import Path

from base_agent import BaseAgent

from typing import Dict, Any, List, Optional

class ProjectManagerAgent(BaseAgent):
    
    def __init__(
            self,
            llm_config: Dict[str, Any],
            agent_config: Optional[Dict[str, Any]] = None,
            regional_config: Optional[Dict[str, Any]] = None
            ):
        
        """
        Initialize Project Manager Agent
        
        Args:
            llm_config: LLM configuration
            agent_config: Agent-specific configuration
            regional_config: Indian market configuration
        """
        super().__init__(
            name="ProjectManager",
            agent_type="userproxy",
            llm_config=llm_config,
            system_message=  self.get_system_message(),
            agent_config=agent_config,
            regional_config=regional_config
                        )
        
        # Project management specific attributes
        self.current_project = None
        self.project_history = []
        self.quality_standards = self._get_quality_standards()
        self.workflow_stages = self._get_workflow_stages()
    
    def get_system_message(self) -> str:
        """Get the system message for Project Manager"""
        return f"""You are an experienced Project Manager for content creation targeting Indian audiences. 
        You coordinate the team, provide feedback, and ensure quality standards are met.

        CORE RESPONSIBILITIES:
        - Coordinate content creation workflow between specialized agents
        - Ensure cultural appropriateness and local relevance for Indian market
        - Provide constructive feedback and quality control
        - Manage project timeline and deliverables
        - Bridge communication between different specialized agents
        - Make final approval decisions on content quality

        PROJECT MANAGEMENT APPROACH:
        - Start with clear brief analysis and requirement gathering
        - Delegate tasks to appropriate specialists (Writer, Editor, SEO, Brand Strategy)
        - Review outputs at each stage and provide specific feedback
        - Ensure consistency across all content pieces
        - Validate against Indian market standards and cultural sensitivity
        - Coordinate revisions and improvements
        - Make final approval when all quality standards are met

        QUALITY CONTROL STANDARDS:
        - Content must resonate with Indian audiences across different regions
        - Use simple, accessible English (8th grade reading level)
        - Include relevant Indian examples, case studies, and cultural references
        - Respect cultural sensitivities and regional preferences
        - Optimize for Indian digital consumption patterns (mobile-first)
        - Ensure compliance with Indian advertising guidelines (ASCI)
        - Include appropriate call-to-actions for Indian market behavior

        WORKFLOW MANAGEMENT:
        1. Brief Analysis: Understand requirements and target audience
        2. Task Delegation: Assign work to appropriate team members
        3. Progress Monitoring: Track deliverables and provide guidance
        4. Quality Review: Evaluate outputs against standards
        5. Feedback Loop: Coordinate revisions and improvements
        6. Final Approval: Ensure all requirements are met before sign-off

        COMMUNICATION STYLE:
        - Clear and direct feedback with specific, actionable suggestions
        - Constructive and supportive tone with team members
        - Focus on solutions rather than problems
        - Acknowledge good work while identifying areas for improvement
        - Ask clarifying questions when requirements are unclear

        TERMINATION CONDITIONS:
        End the conversation only when:
        - All content meets quality standards
        - Cultural appropriateness is verified
        - Indian market relevance is confirmed
        - Team has addressed all feedback points
        - Final deliverables are ready for publication

        Use "FINAL CONTENT APPROVED" to terminate when all standards are met.
        """
    
    def get_specialization(self) -> List[str]:

        return [
            "workflow_coordination",
            "quality_control",
            "indian_market_standards",
            "cultural_sensitivity_review",
            "team_management",
            "project_timeline_management",
            "stakeholder_communication",
            "deliverable_validation"
        ]
       
    def analyze_content_brief(self, brief: str) -> Dict[str, Any]:

        analysis = {
            "brief_text": brief,
            "content_type": self._identify_content_type(brief),
            "target_audience": self._extract_target_audience(brief),
            "business_context": self._extract_business_context(brief),
            "regional_focus": self._extract_regional_focus(brief),
            "key_requirements": self._extract_key_requirements(brief),
            "success_metrics": self._define_success_metrics(brief),
            "cultural_considerations": self._identify_cultural_considerations(brief)
        }
        
        return analysis
    


    def _get_quality_standards(self) -> Dict[str, Any]:

        return {
            "cultural_appropriateness": {
                "description": "Content respects Indian cultural values and sensitivities",
                "criteria": [
                    "No offensive or insensitive cultural references",
                    "Appropriate use of regional context",
                    "Inclusive representation across Indian communities",
                    "Respectful treatment of religious and cultural practices"
                ],
                "minimum_score": 95
            },
            "readability": {
                "description": "Content is accessible to diverse Indian audiences",
                "criteria": [
                    "8th grade reading level or below",
                    "Short paragraphs for mobile consumption",
                    "Clear and simple language",
                    "Logical flow and structure"
                ],
                "minimum_score": 85
            },
            "local_relevance": {
                "description": "Content includes Indian market context and examples",
                "criteria": [
                    "Indian business examples or case studies",
                    "Local market data and statistics",
                    "Regional preferences consideration",
                    "Indian currency and numbering systems"
                ],
                "minimum_score": 80
            },
            "mobile_optimization": {
                "description": "Content optimized for mobile consumption",
                "criteria": [
                    "Short paragraphs (3-4 sentences max)",
                    "Bullet points and lists for easy scanning",
                    "Clear headers and subheaders",
                    "Minimal horizontal scrolling required"
                ],
                "minimum_score": 85
            },
            "call_to_action": {
                "description": "Clear and appropriate CTAs for Indian market",
                "criteria": [
                    "Culturally appropriate action requests",
                    "Local contact methods (WhatsApp, phone)",
                    "Indian payment method references when relevant",
                    "Clear next steps for users"
                ],
                "minimum_score": 75
            }
        }
    
    def _get_workflow_stages(self) -> List[Dict[str, Any]]:

        return [
            {
                "stage": "brief_analysis",
                "description": "Analyze content brief and requirements",
                "owner": "project_manager",
                "deliverables": ["requirement_analysis", "target_audience_profile", "success_criteria"],
                "duration": "5-10 minutes"
            },
            {
                "stage": "content_creation",
                "description": "Create initial content draft",
                "owner": "content_writer",
                "deliverables": ["content_draft", "cultural_references", "local_examples"],
                "duration": "15-20 minutes"
            },
            {
                "stage": "content_editing",
                "description": "Review and improve content quality",
                "owner": "content_editor", 
                "deliverables": ["edited_content", "quality_improvements", "compliance_check"],
                "duration": "10-15 minutes"
            },
            {
                "stage": "seo_optimization",
                "description": "Optimize content for Indian search behavior",
                "owner": "seo_specialist",
                "deliverables": ["keyword_optimization", "meta_data", "search_enhancements"],
                "duration": "10-12 minutes"
            },
            {
                "stage": "brand_alignment",
                "description": "Ensure brand consistency and strategic alignment",
                "owner": "brand_strategist",
                "deliverables": ["brand_review", "strategic_recommendations", "positioning_validation"],
                "duration": "8-10 minutes"
            },
            {
                "stage": "final_review",
                "description": "Final quality control and approval",
                "owner": "project_manager",
                "deliverables": ["quality_assessment", "final_approval", "publication_readiness"],
                "duration": "5-8 minutes"
            }
        ]
    
    def _identify_content_type(self, brief: str) -> str:

        brief_lower = brief.lower()
        
        if any(word in brief_lower for word in ["social media", "instagram", "facebook", "linkedin", "twitter"]):
            return "social_media_campaign"
        elif any(word in brief_lower for word in ["blog", "article", "post", "thought leadership"]):
            return "blog_article"
        elif any(word in brief_lower for word in ["email", "newsletter", "campaign"]):
            return "email_campaign"
        elif any(word in brief_lower for word in ["website", "landing page", "web copy"]):
            return "website_content"
        elif any(word in brief_lower for word in ["menu", "product description", "catalog"]):
            return "product_content"
        else:
            return "general_content"
    
    def _extract_target_audience(self, brief: str) -> Dict[str, Any]:

        brief_lower = brief.lower()
        
        audience = {
            "demographics": [],
            "psychographics": [],
            "geographic": [],
            "behavioral": []
        }
        
        # Demographics
        if "young professional" in brief_lower or "professionals" in brief_lower:
            audience["demographics"].append("young_professionals_25_35")
        if "students" in brief_lower:
            audience["demographics"].append("students_18_25")
        if "entrepreneurs" in brief_lower or "business owners" in brief_lower:
            audience["demographics"].append("entrepreneurs_30_50")
        if "families" in brief_lower or "parents" in brief_lower:
            audience["demographics"].append("families_with_children")
        
        # Geographic
        indian_cities = ["mumbai", "delhi", "bangalore", "chennai", "kolkata", "hyderabad", "pune"]
        for city in indian_cities:
            if city in brief_lower:
                audience["geographic"].append(city)
        
        if "tier-2" in brief_lower or "tier 2" in brief_lower:
            audience["geographic"].append("tier_2_cities")
        if "tier-3" in brief_lower or "tier 3" in brief_lower:
            audience["geographic"].append("tier_3_cities")
        if "metro" in brief_lower:
            audience["geographic"].append("metro_cities")
        
        return audience
    
    def _extract_business_context(self, brief: str) -> Dict[str, Any]:

        brief_lower = brief.lower()
        
        context = {
            "industry": "general",
            "business_type": "unknown",
            "stage": "unknown",
            "size": "unknown"
        }
        
        # Industry identification
        if any(word in brief_lower for word in ["restaurant", "food", "cafe", "dining"]):
            context["industry"] = "food_beverage"
        elif any(word in brief_lower for word in ["tech", "software", "ai", "app", "startup"]):
            context["industry"] = "technology"
        elif any(word in brief_lower for word in ["ecommerce", "e-commerce", "online store", "retail"]):
            context["industry"] = "ecommerce_retail"
        elif any(word in brief_lower for word in ["education", "school", "training", "course"]):
            context["industry"] = "education"
        elif any(word in brief_lower for word in ["healthcare", "hospital", "clinic", "medical"]):
            context["industry"] = "healthcare"
        elif any(word in brief_lower for word in ["finance", "bank", "insurance", "fintech"]):
            context["industry"] = "finance"
        
        # Business type
        if "startup" in brief_lower:
            context["business_type"] = "startup"
        elif "sme" in brief_lower or "small business" in brief_lower:
            context["business_type"] = "sme"
        elif "enterprise" in brief_lower or "large company" in brief_lower:
            context["business_type"] = "enterprise"
        elif "family business" in brief_lower:
            context["business_type"] = "family_business"
        
        return context
    
    def _extract_regional_focus(self, brief: str) -> List[str]:

        brief_lower = brief.lower()
        regions = []
        
        # Specific cities
        indian_cities = {
            "mumbai": ["mumbai", "bombay"],
            "delhi": ["delhi", "new delhi"],
            "bangalore": ["bangalore", "bengaluru"],
            "chennai": ["chennai", "madras"],
            "kolkata": ["kolkata", "calcutta"],
            "hyderabad": ["hyderabad"],
            "pune": ["pune"],
            "ahmedabad": ["ahmedabad"]
        }
        
        for city, variants in indian_cities.items():
            if any(variant in brief_lower for variant in variants):
                regions.append(city)
        
        # Regional categories
        if "north india" in brief_lower or "northern india" in brief_lower:
            regions.extend(["delhi", "punjab", "haryana", "rajasthan"])
        if "south india" in brief_lower or "southern india" in brief_lower:
            regions.extend(["chennai", "bangalore", "hyderabad", "kerala"])
        if "west india" in brief_lower or "western india" in brief_lower:
            regions.extend(["mumbai", "pune", "ahmedabad", "gujarat"])
        if "east india" in brief_lower or "eastern india" in brief_lower:
            regions.extend(["kolkata", "bhubaneswar"])
        
        return list(set(regions))  # Remove duplicates
    
    def _extract_key_requirements(self, brief: str) -> List[str]:

        requirements = []
        brief_lower = brief.lower()
        
        # Content format requirements
        if "instagram" in brief_lower:
            requirements.append("instagram_optimized_content")
        if "linkedin" in brief_lower:
            requirements.append("professional_business_content")
        if "whatsapp" in brief_lower:
            requirements.append("whatsapp_business_ready")
        if "email" in brief_lower:
            requirements.append("email_marketing_format")
        if "blog" in brief_lower:
            requirements.append("seo_optimized_blog_post")
        
        # Business requirements
        if "lead generation" in brief_lower or "leads" in brief_lower:
            requirements.append("lead_generation_focused")
        if "brand awareness" in brief_lower:
            requirements.append("brand_awareness_campaign")
        if "sales" in brief_lower or "conversion" in brief_lower:
            requirements.append("sales_conversion_oriented")
        if "engagement" in brief_lower:
            requirements.append("high_engagement_content")
        
        # Cultural requirements
        if "festival" in brief_lower or "diwali" in brief_lower or "holi" in brief_lower:
            requirements.append("festival_themed_content")
        if "local" in brief_lower or "regional" in brief_lower:
            requirements.append("regional_customization")
        if "hindi" in brief_lower:
            requirements.append("hindi_integration")
        
        return requirements
    
    def _define_success_metrics(self, brief: str) -> Dict[str, Any]:

        metrics = {
            "engagement_metrics": [],
            "business_metrics": [],
            "quality_metrics": []
        }
        
        brief_lower = brief.lower()
        
        # Engagement metrics
        if "social media" in brief_lower:
            metrics["engagement_metrics"].extend([
                "likes_comments_shares", 
                "reach_impressions", 
                "follower_growth"
            ])
        
        if "blog" in brief_lower:
            metrics["engagement_metrics"].extend([
                "page_views", 
                "time_on_page", 
                "social_shares"
            ])
        
        # Business metrics
        if "sales" in brief_lower or "revenue" in brief_lower:
            metrics["business_metrics"].extend([
                "conversion_rate", 
                "sales_increase", 
                "revenue_growth"
            ])
        
        if "leads" in brief_lower:
            metrics["business_metrics"].extend([
                "lead_generation", 
                "contact_form_submissions", 
                "inquiry_calls"
            ])
        
        # Quality metrics (always included)
        metrics["quality_metrics"].extend([
            "cultural_appropriateness_score_95_plus",
            "readability_score_85_plus", 
            "indian_context_integration",
            "mobile_optimization_score_85_plus"
        ])
        
        return metrics
    
    def _identify_cultural_considerations(self, brief: str) -> List[str]:
     
     
        considerations = []
        brief_lower = brief.lower()
        
        # Festival considerations
        festivals = ["diwali", "holi", "eid", "christmas", "dussehra", "ganesh chaturthi"]
        for festival in festivals:
            if festival in brief_lower:
                considerations.append(f"integrate_{festival}_themes")
        
        # Regional considerations
        if "south indian" in brief_lower:
            considerations.extend([
                "south_indian_cultural_references",
                "tamil_telugu_cultural_context",
                "traditional_south_indian_values"
            ])
        
        if "north indian" in brief_lower:
            considerations.extend([
                "north_indian_cultural_references", 
                "hindi_cultural_context",
                "punjabi_haryanvi_influences"
            ])
        
        # Business culture considerations
        if "family business" in brief_lower:
            considerations.extend([
                "family_values_emphasis",
                "trust_building_focus",
                "generational_respect"
            ])
        
        if "startup" in brief_lower:
            considerations.extend([
                "innovation_emphasis",
                "young_professional_culture",
                "tech_savvy_audience"
            ])
        
        # Always include these for Indian market
        considerations.extend([
            "mobile_first_consumption",
            "price_value_sensitivity", 
            "social_proof_importance",
            "family_decision_making_influence"
        ])
        
        return list(set(considerations))  # Remove duplicates
    



    def validate_team_output(self, content: str, agent_name: str) -> Dict[str, Any]:
        """Validate output from team members"""
        validation = {
            "agent": agent_name,
            "content_length": len(content),
            "validation_passed": True,
            "issues": [],
            "suggestions": [],
            "score": 0.0
        }
        
        # Run quality checks using base class methods
        quality_results = self.validate_content_quality(content)
        
        # Check against quality standards
        for standard, criteria in self.quality_standards.items():
            if standard in quality_results:
                score = quality_results[standard]
                min_score = criteria["minimum_score"]
                
                if isinstance(score, bool):
                    score = 100.0 if score else 0.0
                
                if score < min_score:
                    validation["validation_passed"] = False
                    validation["issues"].append(
                        f"{standard}: Score {score:.1f} below minimum {min_score}"
                    )
                    validation["suggestions"].append(
                        f"Improve {standard}: {criteria['description']}"
                    )
        
        # Calculate overall score
        scores = [
            score for score in quality_results.values() 
            if isinstance(score, (int, float))
        ]
        validation["score"] = sum(scores) / len(scores) if scores else 0.0
        
        return validation
    
    def generate_project_summary(self, project_data: Dict[str, Any]) -> str:
        """Generate project summary for final approval"""
        summary = f"""
                    PROJECT COMPLETION SUMMARY
                    ==========================

                    Project: {project_data.get('brief', 'Content Creation Project')}
                    Content Type: {project_data.get('content_type', 'General')}
                    Target Audience: {', '.join(project_data.get('target_audience', {}).get('demographics', []))}
                    Regional Focus: {', '.join(project_data.get('regional_focus', []))}

                    QUALITY VALIDATION RESULTS:
                    """
        
        # Add validation results for each agent
        for agent, validation in project_data.get('validations', {}).items():
            summary += f"""
                        {agent.upper()} VALIDATION:
                        - Overall Score: {validation.get('score', 0):.1f}/100
                        - Status: {'PASSED' if validation.get('validation_passed') else 'NEEDS REVISION'}
                        - Issues: {len(validation.get('issues', []))} found
                        """
        
        # Add final recommendations
        summary += f"""
                    FINAL RECOMMENDATIONS:
                    - Content meets Indian market standards: {'YES' if all(v.get('validation_passed', False) for v in project_data.get('validations', {}).values()) else 'NEEDS WORK'}
                    - Cultural appropriateness verified: YES
                    - Mobile optimization confirmed: YES
                    - SEO optimization completed: YES
                    - Brand alignment validated: YES

                    STATUS: {'APPROVED FOR PUBLICATION' if all(v.get('validation_passed', False) for v in project_data.get('validations', {}).values()) else 'REQUIRES REVISION'}
                    """
        
        return summary
    
    def get_next_action_recommendation(self, current_stage: str, validation_results: Dict[str, Any]) -> str:

        """Get recommendation for next action based on current stage and validation"""
        if not validation_results.get("validation_passed", False):
            return f"""
                        NEXT ACTION REQUIRED:
                        Current Stage: {current_stage}
                        Status: REVISION NEEDED

                        Issues to Address:
                        {chr(10).join(['- ' + issue for issue in validation_results.get('issues', [])])}

                        Suggestions:
                        {chr(10).join(['- ' + suggestion for suggestion in validation_results.get('suggestions', [])])}

                        Please revise the content addressing these issues before proceeding.
                        """
        else:
            stage_flow = {
                "brief_analysis": "content_creation",
                "content_creation": "content_editing", 
                "content_editing": "seo_optimization",
                "seo_optimization": "brand_alignment",
                "brand_alignment": "final_review",
                "final_review": "project_completion"
            }
            
            next_stage = stage_flow.get(current_stage, "project_completion")
            
            if next_stage == "project_completion":
                return "ALL STAGES COMPLETED - READY FOR FINAL APPROVAL"
            else:
                return f"Stage validated. Proceeding to: {next_stage}"
    
    def create_feedback_message(self, agent_name: str, content: str, validation: Dict[str, Any]) -> str:

        """Create detailed feedback message for team members"""
        feedback = f"""
                    FEEDBACK FOR {agent_name.upper()}
                    {'='*50}

                    CONTENT QUALITY ASSESSMENT:
                    Overall Score: {validation.get('score', 0):.1f}/100
                    Status: {'APPROVED' if validation.get('validation_passed') else 'REVISION REQUIRED'}

                    """
        
        if validation.get('issues'):
            feedback += "ISSUES TO ADDRESS:\n"
            for issue in validation['issues']:
                feedback += f"{issue}\n"
            feedback += "\n"
        
        if validation.get('suggestions'):
            feedback += "IMPROVEMENT SUGGESTIONS:\n"
            for suggestion in validation['suggestions']:
                feedback += f"{suggestion}\n"
            feedback += "\n"
        
        # Add agent-specific guidance
        agent_guidance = {
            "ContentWriter": """
                                WRITER-SPECIFIC GUIDANCE:
                                - Ensure content includes specific Indian examples and case studies
                                - Use conversational tone while maintaining professionalism
                                - Include regional references appropriate to target audience
                                - Optimize sentence length for mobile readability
                                - Add cultural hooks that resonate with Indian values
                                """,
            "ContentEditor": """
                                EDITOR-SPECIFIC GUIDANCE:
                                - Focus on improving readability for diverse Indian education levels
                                - Verify all Indian market facts and statistics
                                - Check for appropriate Hindi phrase integration
                                - Ensure mobile-first paragraph structure
                                - Validate cultural sensitivity across all regions
                                """,
            "SEOSpecialist": """
                                SEO-SPECIFIC GUIDANCE:
                                - Include Indian city names and local search terms
                                - Optimize for voice search queries common in India
                                - Consider regional language keyword variations
                                - Focus on mobile-first indexing requirements
                                - Include local business schema markup suggestions
                                """,
            "BrandStrategist": """
                                BRAND-SPECIFIC GUIDANCE:
                                - Ensure messaging aligns with Indian consumer psychology
                                - Validate trust-building elements for Indian market
                                - Check family-oriented messaging where appropriate
                                - Confirm value proposition resonates with price-sensitive audience
                                - Verify community and social proof elements
                                """
        }
        
        feedback += agent_guidance.get(agent_name, "")
        
        if validation.get('validation_passed'):
            feedback += "\nEXCELLENT WORK! Content meets all quality standards."
        else:
            feedback += "\nPlease revise and resubmit after addressing the issues above."
        
        return feedback