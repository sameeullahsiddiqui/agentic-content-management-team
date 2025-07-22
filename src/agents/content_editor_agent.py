"""
Content Editor Agent for AutoGen Content Team India
Specializes in editing and refining content for Indian markets

Author: Samee Ullah Siddiqui
Repository: https://github.com/sameeullahsiddiqui/agentic-content-management-team
"""

import re
import string
from typing import Dict, Any, List, Optional, Tuple
from base_agent import BaseAgent


class ContentEditorAgent(BaseAgent):
    """
    Content Editor Agent - Reviews and refines content for Indian audiences
    Ensures quality, cultural appropriateness, and local relevance
    """

    def __init__(
        self,
        llm_config: Dict[str, Any],
        agent_config: Optional[Dict[str, Any]] = None,
        regional_config: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize Content Editor Agent

        Args:
            llm_config: LLM configuration
            agent_config: Agent-specific configuration
            regional_config: Indian market configuration
        """
        super().__init__(
            name="ContentEditor",
            agent_type="assistant",
            llm_config=llm_config,
            system_message=self.get_system_message(),
            agent_config=agent_config,
            regional_config=regional_config,
        )

        # Editor-specific attributes
        self.editing_standards = self._get_editing_standards()
        self.indian_style_guide = self._get_indian_style_guide()
        self.cultural_sensitivity_rules = self._get_cultural_sensitivity_rules()
        self.readability_guidelines = self._get_readability_guidelines()
        self.fact_check_sources = self._get_indian_fact_check_sources()

    def get_system_message(self) -> str:
        """Get the system message for Content Editor"""
        return """You are a meticulous content editor with deep expertise in Indian markets, cultural nuances, and digital communication standards. Your role is to transform good content into exceptional, culturally resonant content that engages Indian audiences effectively.

                    CORE EDITING RESPONSIBILITIES:
                    - Grammar, spelling, punctuation, and language accuracy for Indian English
                    - Cultural appropriateness and sensitivity across diverse Indian communities
                    - Fact-checking with specific focus on Indian market data and statistics
                    - Tone consistency and brand voice alignment for Indian audiences
                    - Readability optimization for diverse education levels and demographics
                    - Local compliance with Indian advertising standards (ASCI guidelines)
                    - Mobile-first content structure for Indian consumption patterns

                    INDIAN MARKET EDITING EXPERTISE:
                    - Indian English conventions, spellings, and linguistic preferences
                    - Cultural references verification and appropriateness assessment
                    - Regional sensitivity across different Indian states and communities
                    - Hindi phrase integration and transliteration accuracy
                    - Festival and seasonal content timing and cultural accuracy
                    - Local business context and market dynamics understanding
                    - Price formatting, currency representation, and number systems (lakh, crore)

                    QUALITY ASSURANCE STANDARDS:
                    - Readability: Target 8th grade level for maximum accessibility
                    - Cultural Sensitivity: 95%+ appropriateness score across all communities
                    - Factual Accuracy: Verify all Indian market data, statistics, and references
                    - Mobile Optimization: 85%+ mobile readability score
                    - Engagement Optimization: Clear structure with scannable format
                    - Local Relevance: Include specific Indian examples and contextual references

                    EDITING PROCESS WORKFLOW:
                    1. **Initial Review**: Overall content structure, flow, and completeness
                    2. **Language Editing**: Grammar, spelling, clarity, and Indian English conventions
                    3. **Cultural Verification**: Sensitivity check and appropriateness across regions
                    4. **Fact Checking**: Verify all claims, statistics, and Indian market references
                    5. **Readability Enhancement**: Simplify complex sentences, improve flow
                    6. **Mobile Optimization**: Ensure short paragraphs, clear headers, scannable format
                    7. **Final Polish**: Brand voice consistency, call-to-action optimization

                    INDIAN ENGLISH STYLE GUIDELINES:
                    - Use Indian spelling conventions (realise, colour, centre) where natural
                    - Include appropriate Hindi words when they add cultural authenticity
                    - Use Indian numbering systems (₹1,50,000 instead of ₹150,000)
                    - Reference Indian time zones (IST) and business hours appropriately
                    - Include culturally familiar analogies and references
                    - Use respectful address forms when addressing audiences

                    CULTURAL SENSITIVITY REQUIREMENTS:
                    - Ensure inclusive representation across all Indian states and communities
                    - Avoid stereotypes about any region, religion, caste, or economic group
                    - Use balanced examples from different parts of India
                    - Respect religious sentiments and cultural practices
                    - Include diverse perspectives in testimonials and case studies
                    - Consider joint family structures in consumer-focused content

                    READABILITY OPTIMIZATION TECHNIQUES:
                    - Convert complex sentences into 2-3 shorter sentences
                    - Use active voice instead of passive voice wherever possible
                    - Replace jargon with simple, commonly understood terms
                    - Add transition words to improve flow between sentences
                    - Create bullet points and numbered lists for complex information
                    - Use descriptive headers and subheaders for easy navigation

                    MOBILE-FIRST EDITING APPROACH:
                    - Keep paragraphs to 2-4 sentences maximum
                    - Use short sentences (15-20 words average)
                    - Create white space with line breaks and bullet points
                    - Ensure content flows logically on small screens
                    - Make call-to-actions clearly visible and actionable
                    - Optimize for voice search queries common in India

                    FACT-CHECKING PRIORITIES:
                    - Verify all statistics about Indian market, demographics, and economy
                    - Check accuracy of company information and success stories
                    - Validate festival dates, cultural references, and regional information
                    - Confirm pricing, availability, and service delivery claims
                    - Cross-reference industry data with reliable Indian sources
                    - Ensure compliance with current Indian regulations and standards

                    BRAND VOICE CONSISTENCY:
                    - Maintain consistent tone throughout all content pieces
                    - Ensure messaging aligns with Indian consumer psychology
                    - Balance professional credibility with approachable warmth
                    - Include trust-building elements important to Indian consumers
                    - Adapt formality level based on platform and audience
                    - Incorporate community and family values where appropriate

                    COLLABORATION APPROACH:
                    - Provide specific, actionable feedback to Content Writers
                    - Coordinate with SEO Specialist for keyword integration without compromising readability
                    - Work with Brand Strategist to ensure strategic message alignment
                    - Respond constructively to Project Manager feedback and priorities
                    - Suggest improvements that enhance both quality and cultural resonance

                    OUTPUT STANDARDS:
                    - Return edited content with clear improvement explanations
                    - Highlight significant changes and reasoning behind edits
                    - Provide readability scores and cultural appropriateness assessments
                    - Suggest alternative phrasings for better local market fit
                    - Include recommendations for visual elements or supporting content
                    - Offer platform-specific optimization suggestions

                    CONTINUOUS IMPROVEMENT:
                    - Stay updated with evolving Indian digital communication trends
                    - Learn from audience feedback and engagement metrics
                    - Adapt editing approach based on regional performance data
                    - Incorporate new cultural insights and market developments
                    - Refine editing standards based on successful content patterns

                    Remember: Your goal is to ensure every piece of content not only meets professional editing standards but also resonates authentically with Indian audiences, respects cultural values, and drives meaningful engagement across diverse demographics."""

    def get_specialization(self) -> List[str]:
        """Get list of Content Editor specializations"""
        return [
            "indian_english_editing",
            "cultural_sensitivity_review",
            "readability_optimization",
            "mobile_first_editing",
            "fact_checking_indian_market",
            "brand_voice_consistency",
            "asci_compliance_review",
            "regional_content_adaptation",
            "hindi_phrase_integration",
            "festival_content_accuracy",
            "consumer_psychology_alignment",
            "trust_building_optimization",
        ]

    def edit_content(
        self, content: str, content_type: str, target_audience: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Main editing function that processes content comprehensively"""

        editing_result = {
            "original_content": content,
            "edited_content": "",
            "improvements_made": [],
            "quality_scores": {},
            "recommendations": [],
            "cultural_assessment": {},
            "readability_metrics": {},
        }

        # Step 1: Initial content analysis
        initial_analysis = self._analyze_content_structure(content)

        # Step 2: Grammar and language editing
        grammar_edited = self._edit_grammar_and_language(content)
        editing_result["improvements_made"].extend(grammar_edited["changes"])

        # Step 3: Cultural sensitivity review
        cultural_review = self._review_cultural_sensitivity(grammar_edited["content"])
        editing_result["cultural_assessment"] = cultural_review["assessment"]

        # Step 4: Readability optimization
        readability_optimized = self._optimize_readability(cultural_review["content"])
        editing_result["readability_metrics"] = readability_optimized["metrics"]

        # Step 5: Indian market relevance enhancement
        market_enhanced = self._enhance_indian_market_relevance(
            readability_optimized["content"]
        )

        # Step 6: Mobile optimization
        mobile_optimized = self._optimize_for_mobile(market_enhanced["content"])

        # Step 7: Final polish and quality check
        final_content = self._final_polish(mobile_optimized["content"], content_type)

        editing_result["edited_content"] = final_content["content"]
        editing_result["quality_scores"] = self._calculate_quality_scores(
            final_content["content"]
        )
        editing_result["recommendations"] = self._generate_recommendations(
            editing_result
        )

        return editing_result

    def _get_editing_standards(self) -> Dict[str, Dict[str, Any]]:
        """Define comprehensive editing standards"""
        return {
            "grammar_and_language": {
                "grammar_accuracy": {
                    "target": 99,
                    "critical_errors": [
                        "subject_verb_disagreement",
                        "tense_inconsistency",
                    ],
                },
                "spelling_accuracy": {"target": 100, "dictionary": "indian_english"},
                "punctuation": {"target": 98, "style": "oxford_comma_optional"},
                "sentence_structure": {
                    "avg_words_per_sentence": 15,
                    "max_words_per_sentence": 25,
                },
            },
            "readability": {
                "flesch_kincaid_grade": {"target": 8.0, "maximum": 10.0},
                "sentence_length": {"average": 15, "maximum": 25},
                "paragraph_length": {"sentences": 4, "words": 75},
                "syllable_complexity": {"avg_syllables_per_word": 1.5},
            },
            "cultural_appropriateness": {
                "sensitivity_score": {"minimum": 95},
                "inclusive_language": {"required": True},
                "regional_balance": {"multiple_regions": True},
                "religious_sensitivity": {"required": True},
            },
            "indian_market_relevance": {
                "local_examples": {"minimum": 1, "preferred": 3},
                "indian_statistics": {"verification": "required"},
                "cultural_references": {"accuracy": "mandatory"},
                "regional_adaptation": {"consideration": "required"},
            },
            "mobile_optimization": {
                "paragraph_length": {"max_sentences": 4},
                "line_length": {"max_characters": 65},
                "white_space": {"required": True},
                "scannable_format": {"headers_bullets": "required"},
            },
        }

    def _get_indian_style_guide(self) -> Dict[str, Any]:
        """Define Indian English style guide and conventions"""
        return {
            "spelling_conventions": {
                "british_vs_american": {
                    "prefer_british": [
                        "realise",
                        "colour",
                        "centre",
                        "honour",
                        "favour",
                    ],
                    "commonly_accepted_american": [
                        "organize",
                        "recognize",
                        "mobile",
                        "online",
                    ],
                },
                "indian_specific": {
                    "rupee_symbol": "₹ (before amount with space: ₹ 1,000)",
                    "number_format": "1,50,000 (Indian comma system)",
                    "large_numbers": "Use lakh and crore: ₹ 2.5 lakh, ₹ 10 crore",
                },
            },
            "hindi_integration": {
                "common_accepted_words": [
                    "chai",
                    "namaste",
                    "ji",
                    "sahab",
                    "madam",
                    "beta",
                    "didi",
                    "bhai",
                    "gharelu",
                    "desi",
                    "videshi",
                    "swadeshi",
                    "jugaad",
                    "aam aadmi",
                ],
                "business_terms": [
                    "vyavasaya",
                    "kaam",
                    "safalta",
                    "unnati",
                    "pragati",
                    "vikas",
                ],
                "usage_rules": {
                    "italicize": False,
                    "explain_on_first_use": "only_if_uncommon",
                    "natural_integration": True,
                },
            },
            "address_forms": {
                "respectful_terms": ["ji", "sahab", "madam", "sir", "aunty", "uncle"],
                "professional": ["Mr.", "Ms.", "Dr.", "Prof."],
                "casual_friendly": ["bhai", "didi", "friend", "buddy"],
            },
            "time_and_date": {
                "time_zone": "IST (Indian Standard Time)",
                "date_format": "DD/MM/YYYY or DD Month YYYY",
                "time_format": "12-hour with AM/PM",
                "business_hours": "10:00 AM - 7:00 PM IST",
            },
            "cultural_references": {
                "festivals": {
                    "major": ["Diwali", "Holi", "Eid", "Christmas", "Dussehra"],
                    "regional": ["Ganesh Chaturthi", "Durga Puja", "Onam", "Pongal"],
                    "usage": "Include significance, not just names",
                },
                "food_references": {
                    "pan_indian": ["chai", "roti", "rice", "dal", "sabzi"],
                    "regional": ["idli-sambar", "rajma-chawal", "dhokla", "biryani"],
                    "context": "Use food analogies for relatability",
                },
            },
        }

    def _get_cultural_sensitivity_rules(self) -> Dict[str, List[str]]:
        """Define cultural sensitivity guidelines"""
        return {
            "avoid_stereotypes": [
                "Regional stereotypes (Bengali fish-lovers, Punjabi party-lovers)",
                "Economic class generalizations",
                "Educational background assumptions",
                "Technology adoption assumptions based on age/location",
                "Gender role assumptions in professional contexts",
            ],
            "inclusive_language": [
                "Use 'Indian families' instead of 'Indian family' for broader appeal",
                "Include diverse regional examples in case studies",
                "Avoid assuming religious practices (not everyone celebrates all festivals)",
                "Use gender-neutral language where appropriate",
                "Include urban and rural perspectives when relevant",
            ],
            "respectful_references": [
                "Always capitalize religious terms and festivals",
                "Use full names for cities (Mumbai, not Bombay unless historical context)",
                "Respect linguistic diversity - mention multiple languages when relevant",
                "Acknowledge economic diversity without assumptions",
                "Include diverse age groups in examples and testimonials",
            ],
            "sensitive_topics": [
                "Avoid political party references unless absolutely necessary",
                "Handle religious references with equal respect for all faiths",
                "Be careful with caste-related content - focus on merit and achievement",
                "Avoid assumptions about family structures (nuclear vs joint families)",
                "Handle economic disparities sensitively - focus on solutions not problems",
            ],
        }

    def _get_readability_guidelines(self) -> Dict[str, Any]:
        """Define readability improvement guidelines"""
        return {
            "sentence_structure": {
                "ideal_length": "12-18 words",
                "maximum_length": "25 words",
                "structure_variety": "Mix simple, compound, and complex sentences",
                "active_voice_preference": "80% active voice minimum",
            },
            "vocabulary_choices": {
                "simple_alternatives": {
                    "utilize": "use",
                    "commence": "start",
                    "terminate": "end",
                    "facilitate": "help",
                    "endeavor": "try",
                    "Subsequently": "then",
                    "furthermore": "also",
                    "nevertheless": "however",
                },
                "indian_context_words": {
                    "prefer": ["shop", "store", "market", "vendor"],
                    "over": ["retailer", "merchant", "outlet", "establishment"],
                },
            },
            "paragraph_structure": {
                "ideal_sentences": "2-4 sentences",
                "maximum_sentences": "5 sentences",
                "maximum_words": "75 words",
                "topic_coherence": "One main idea per paragraph",
            },
            "formatting_for_readability": {
                "use_bullet_points": "For lists and multiple benefits",
                "use_numbered_lists": "For step-by-step processes",
                "use_headers": "Every 3-4 paragraphs maximum",
                "use_bold_text": "For key terms and important points (sparingly)",
            },
        }

    def _get_indian_fact_check_sources(self) -> Dict[str, List[str]]:
        """Define reliable sources for fact-checking Indian content"""
        return {
            "government_sources": [
                "Reserve Bank of India (RBI)",
                "Ministry of Statistics and Programme Implementation",
                "NITI Aayog reports",
                "Census of India",
                "Economic Survey reports",
            ],
            "business_statistics": [
                "NASSCOM reports",
                "CII (Confederation of Indian Industry)",
                "FICCI (Federation of Indian Chambers of Commerce)",
                "India Brand Equity Foundation (IBEF)",
                "Startup India reports",
            ],
            "market_research": [
                "Nielsen India",
                "KPMG India reports",
                "Ernst & Young India",
                "McKinsey India",
                "BCG India insights",
            ],
            "digital_and_tech": [
                "TRAI (Telecom Regulatory Authority)",
                "IT Ministry reports",
                "Digital India statistics",
                "IAMAI (Internet and Mobile Association)",
                "Google India reports",
            ],
        }

    def _analyze_content_structure(self, content: str) -> Dict[str, Any]:
        """Analyze overall content structure and organization"""

        paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
        sentences = [s.strip() for s in content.split(".") if s.strip()]

        analysis = {
            "total_words": len(content.split()),
            "total_sentences": len(sentences),
            "total_paragraphs": len(paragraphs),
            "avg_sentence_length": (
                sum(len(s.split()) for s in sentences) / len(sentences)
                if sentences
                else 0
            ),
            "avg_paragraph_length": (
                sum(len(p.split()) for p in paragraphs) / len(paragraphs)
                if paragraphs
                else 0
            ),
            "has_headers": bool(re.search(r"^#+\s", content, re.MULTILINE)),
            "has_bullet_points": bool(
                re.search(r"^\s*[•\-\*]\s", content, re.MULTILINE)
            ),
            "structure_issues": [],
        }

        # Identify structure issues
        if analysis["avg_sentence_length"] > 25:
            analysis["structure_issues"].append("Sentences too long for easy reading")

        if analysis["avg_paragraph_length"] > 100:
            analysis["structure_issues"].append(
                "Paragraphs too long for mobile reading"
            )

        if analysis["total_words"] > 200 and not analysis["has_headers"]:
            analysis["structure_issues"].append(
                "Long content needs headers for better navigation"
            )

        return analysis

    def _edit_grammar_and_language(self, content: str) -> Dict[str, Any]:
        """Edit grammar, spelling, and language issues"""

        edited_content = content
        changes_made = []

        # Common grammar fixes for Indian English
        grammar_fixes = {
            r"\bvery much\b": "very",
            r"\bgood enough\b": "sufficient",
            r"\btoo much\b": "excessive",
            r"\bonly and only\b": "only",
            r"\bdo one thing\b": "please",
            r"\bkinldy\b": "kindly",  # Common typo
            r"\bteh\b": "the",  # Common typo
            r"\brecieve\b": "receive",  # Common typo
            r"\baccommodate\b": "accommodate",  # Common typo
        }

        for pattern, replacement in grammar_fixes.items():
            if re.search(pattern, edited_content, re.IGNORECASE):
                edited_content = re.sub(
                    pattern, replacement, edited_content, flags=re.IGNORECASE
                )
                changes_made.append(
                    f"Fixed common error: '{pattern}' → '{replacement}'"
                )

        # Fix Indian number formatting
        # Convert international format to Indian format
        number_pattern = r"₹\s*(\d+),(\d{3}),(\d{3})\b"

        def indian_format(match):
            return f"₹ {match.group(1)},{match.group(2)},{match.group(3)}"

        if re.search(number_pattern, edited_content):
            edited_content = re.sub(number_pattern, indian_format, edited_content)
            changes_made.append("Converted to Indian number formatting")

        # Ensure proper capitalization for Indian terms
        indian_terms = {
            r"\bindia\b": "India",
            r"\bindian\b": "Indian",
            r"\bmumbai\b": "Mumbai",
            r"\bdelhi\b": "Delhi",
            r"\bbangalore\b": "Bangalore",
            r"\bchennai\b": "Chennai",
            r"\bdiwali\b": "Diwali",
            r"\bholi\b": "Holi",
        }

        for pattern, replacement in indian_terms.items():
            if re.search(pattern, edited_content):
                edited_content = re.sub(
                    pattern, replacement, edited_content, flags=re.IGNORECASE
                )
                changes_made.append(f"Capitalized Indian term: {replacement}")

        return {"content": edited_content, "changes": changes_made}

    def _review_cultural_sensitivity(self, content: str) -> Dict[str, Any]:
        """Review content for cultural sensitivity and appropriateness"""

        assessment = {
            "sensitivity_score": 100,
            "issues_found": [],
            "suggestions": [],
            "regional_balance": False,
            "inclusive_language": True,
        }

        content_lower = content.lower()

        # Check for potentially insensitive terms
        sensitive_terms = [
            "backward",
            "primitive",
            "uneducated",
            "illiterate",
            "poor people",
            "rich people",
            "typical indian",
            "all indians",
            "village people",
        ]

        for term in sensitive_terms:
            if term in content_lower:
                assessment["sensitivity_score"] -= 10
                assessment["issues_found"].append(
                    f"Potentially insensitive term: '{term}'"
                )
                assessment["suggestions"].append(
                    f"Replace '{term}' with more respectful language"
                )

        # Check for regional balance
        regions_mentioned = []
        indian_cities = [
            "mumbai",
            "delhi",
            "bangalore",
            "chennai",
            "kolkata",
            "hyderabad",
            "pune",
        ]
        for city in indian_cities:
            if city in content_lower:
                regions_mentioned.append(city)

        if len(regions_mentioned) >= 2:
            assessment["regional_balance"] = True
        elif len(regions_mentioned) == 1 and len(content.split()) > 200:
            assessment["suggestions"].append(
                "Consider adding examples from other Indian regions for better balance"
            )

        # Check for inclusive language
        exclusive_terms = ["guys", "manpower", "chairman"]
        inclusive_alternatives = ["everyone", "workforce", "chairperson"]

        for i, term in enumerate(exclusive_terms):
            if term in content_lower:
                assessment["inclusive_language"] = False
                assessment["suggestions"].append(
                    f"Replace '{term}' with '{inclusive_alternatives[i]}'"
                )

        return {"content": content, "assessment": assessment}

    def _optimize_readability(self, content: str) -> Dict[str, Any]:
        """Optimize content for better readability"""

        optimized_content = content
        improvements = []

        # Split long sentences
        sentences = content.split(".")
        optimized_sentences = []

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            words = sentence.split()
            if len(words) > 25:
                # Try to split at logical points
                split_points = ["and", "but", "however", "because", "since", "while"]
                best_split = None

                for point in split_points:
                    if point in sentence.lower():
                        split_index = sentence.lower().index(point)
                        if 10 < len(sentence[:split_index].split()) < 20:
                            best_split = split_index
                            break

                if best_split:
                    part1 = sentence[:best_split].strip()
                    part2 = sentence[best_split:].strip()
                    optimized_sentences.extend([part1, part2])
                    improvements.append(f"Split long sentence for better readability")
                else:
                    optimized_sentences.append(sentence)
            else:
                optimized_sentences.append(sentence)

        optimized_content = ". ".join(optimized_sentences)

        # Improve paragraph structure
        paragraphs = optimized_content.split("\n\n")
        optimized_paragraphs = []

        for paragraph in paragraphs:
            sentences_in_para = [s.strip() for s in paragraph.split(".") if s.strip()]

            if len(sentences_in_para) > 5:
                # Split long paragraphs
                mid_point = len(sentences_in_para) // 2
                para1 = ". ".join(sentences_in_para[:mid_point]) + "."
                para2 = ". ".join(sentences_in_para[mid_point:]) + "."
                optimized_paragraphs.extend([para1, para2])
                improvements.append("Split long paragraph for mobile readability")
            else:
                optimized_paragraphs.append(paragraph)

        optimized_content = "\n\n".join(optimized_paragraphs)

        # Calculate readability metrics
        words = optimized_content.split()
        sentences = [s for s in optimized_content.split(".") if s.strip()]

        metrics = {
            "avg_sentence_length": len(words) / len(sentences) if sentences else 0,
            "total_words": len(words),
            "total_sentences": len(sentences),
            "estimated_grade_level": (
                min(12, max(1, (len(words) / len(sentences)) - 5)) if sentences else 8
            ),
            "improvements_made": improvements,
        }

        return {"content": optimized_content, "metrics": metrics}

    def _enhance_indian_market_relevance(self, content: str) -> Dict[str, Any]:
        """Enhance content with Indian market context and examples"""

        enhanced_content = content
        enhancements = []

        # Add Indian examples if none exist
        if not self._has_indian_context(content):
            # Suggest where to add Indian examples
            suggestion = "\n\n💡 Editor's Note: Consider adding specific Indian examples, such as successful local businesses, relevant statistics, or cultural references to make this content more relatable to Indian audiences."
            enhanced_content += suggestion
            enhancements.append("Added suggestion for Indian context integration")

        # Ensure proper currency formatting
        currency_pattern = r"(\$\d+)"
        if re.search(currency_pattern, enhanced_content):
            enhanced_content = re.sub(
                currency_pattern, r"₹ \1 (equivalent)", enhanced_content
            )
            enhancements.append(
                "Added Indian currency context to international examples"
            )

        # Add cultural timing context if time-sensitive content
        time_patterns = ["deadline", "limited time", "expires soon", "last chance"]
        for pattern in time_patterns:
            if pattern in enhanced_content.lower():
                enhanced_content = enhanced_content.replace(pattern, f"{pattern} (IST)")
                enhancements.append("Added Indian time zone context")
                break

        return {"content": enhanced_content, "enhancements": enhancements}

    def _optimize_for_mobile(self, content: str) -> Dict[str, Any]:
        """Optimize content for mobile consumption"""

        mobile_optimized = content
        optimizations = []

        # Ensure short paragraphs
        paragraphs = mobile_optimized.split("\n\n")
        optimized_paragraphs = []

        for paragraph in paragraphs:
            word_count = len(paragraph.split())
            if word_count > 75:
                # Split into smaller chunks
                sentences = [s.strip() + "." for s in paragraph.split(".") if s.strip()]
                current_chunk = []
                current_word_count = 0

                for sentence in sentences:
                    sentence_words = len(sentence.split())
                    if current_word_count + sentence_words > 75 and current_chunk:
                        optimized_paragraphs.append(" ".join(current_chunk))
                        current_chunk = [sentence]
                        current_word_count = sentence_words
                    else:
                        current_chunk.append(sentence)
                        current_word_count += sentence_words

                if current_chunk:
                    optimized_paragraphs.append(" ".join(current_chunk))

                optimizations.append("Split long paragraph for mobile viewing")
            else:
                optimized_paragraphs.append(paragraph)

        mobile_optimized = "\n\n".join(optimized_paragraphs)

        # Add bullet points where appropriate
        list_indicators = [
            "benefits include",
            "features are",
            "we offer",
            "services include",
        ]
        for indicator in list_indicators:
            if indicator in mobile_optimized.lower():
                # Find the sentence and suggest bullet format
                pattern = f"{indicator}[^.]*\\."
                match = re.search(pattern, mobile_optimized, re.IGNORECASE)
                if match:
                    suggestion = f"\n\n📱 Mobile Optimization Suggestion: Consider converting the list after '{indicator}' into bullet points for better mobile readability."
                    mobile_optimized += suggestion
                    optimizations.append("Suggested bullet point formatting for mobile")
                    break

        return {"content": mobile_optimized, "optimizations": optimizations}

    def _final_polish(self, content: str, content_type: str) -> Dict[str, Any]:
        """Apply final polish and platform-specific optimizations"""

        polished_content = content
        polish_applied = []

        # Platform-specific optimizations
        if content_type == "social_media":
            # Ensure engaging opening
            if not re.match(r"^[🎯🚀💡🔥✨🎉]", polished_content):
                suggestion = "💡 Consider starting with an engaging emoji or hook for social media impact."
                polished_content = suggestion + "\n\n" + polished_content
                polish_applied.append("Added social media engagement suggestion")

        elif content_type == "email":
            # Ensure clear subject line suggestion
            if "subject" not in polished_content.lower():
                subject_suggestion = "\n\n📧 Suggested Subject Line: Include numbers, urgency, or local reference for better open rates in Indian market."
                polished_content += subject_suggestion
                polish_applied.append("Added email subject line guidance")

        elif content_type == "blog":
            # Ensure SEO-friendly structure
            if not re.search(r"^#+\s", polished_content, re.MULTILINE):
                header_suggestion = "\n\n📝 SEO Tip: Add relevant headers (H2, H3) with Indian keywords for better search visibility."
                polished_content += header_suggestion
                polish_applied.append("Added SEO header suggestion")

        # Final quality checks
        final_checks = self._perform_final_quality_checks(polished_content)

        return {
            "content": polished_content,
            "polish_applied": polish_applied,
            "final_quality": final_checks,
        }

    def _has_indian_context(self, content: str) -> bool:
        """Check if content contains Indian context"""
        indian_indicators = [
            "india",
            "indian",
            "mumbai",
            "delhi",
            "bangalore",
            "chennai",
            "rupee",
            "₹",
            "lakh",
            "crore",
            "diwali",
            "holi",
            "bollywood",
            "cricket",
            "chai",
            "namaste",
        ]

        content_lower = content.lower()
        return any(indicator in content_lower for indicator in indian_indicators)

    def _calculate_quality_scores(self, content: str) -> Dict[str, float]:
        """Calculate various quality scores for the content"""

        words = content.split()
        sentences = [s for s in content.split(".") if s.strip()]

        scores = {
            "readability_score": 0.0,
            "cultural_relevance": 0.0,
            "mobile_optimization": 0.0,
            "engagement_potential": 0.0,
            "overall_quality": 0.0,
        }

        # Readability score (based on sentence length and complexity)
        if sentences:
            avg_sentence_length = len(words) / len(sentences)
            readability = max(0, 100 - (avg_sentence_length - 15) * 3)
            scores["readability_score"] = min(100, readability)

        # Cultural relevance score
        if self._has_indian_context(content):
            scores["cultural_relevance"] = 85.0
        else:
            scores["cultural_relevance"] = 40.0

        # Mobile optimization score
        paragraphs = [p for p in content.split("\n\n") if p.strip()]
        if paragraphs:
            avg_para_length = sum(len(p.split()) for p in paragraphs) / len(paragraphs)
            mobile_score = max(0, 100 - (avg_para_length - 50) * 2)
            scores["mobile_optimization"] = min(100, mobile_score)

        # Engagement potential
        engagement_indicators = ["?", "!", "you", "your", "we", "our"]
        engagement_count = sum(
            content.lower().count(indicator) for indicator in engagement_indicators
        )
        scores["engagement_potential"] = min(100, engagement_count * 5)

        # Overall quality (weighted average)
        scores["overall_quality"] = (
            scores["readability_score"] * 0.3
            + scores["cultural_relevance"] * 0.3
            + scores["mobile_optimization"] * 0.2
            + scores["engagement_potential"] * 0.2
        )

        return scores

    def _generate_recommendations(self, editing_result: Dict[str, Any]) -> List[str]:
        """Generate specific recommendations for content improvement"""

        recommendations = []
        scores = editing_result["quality_scores"]

        if scores["readability_score"] < 80:
            recommendations.append(
                "Consider shortening sentences and using simpler vocabulary for better readability"
            )

        if scores["cultural_relevance"] < 70:
            recommendations.append(
                "Add more Indian examples, statistics, or cultural references to increase local relevance"
            )

        if scores["mobile_optimization"] < 80:
            recommendations.append(
                "Break long paragraphs into shorter chunks for better mobile reading experience"
            )

        if scores["engagement_potential"] < 60:
            recommendations.append(
                "Include more questions, direct address to readers, or interactive elements"
            )

        # Content-specific recommendations
        content = editing_result["edited_content"]

        if len(content.split()) > 500 and not re.search(
            r"^\s*[•\-\*]", content, re.MULTILINE
        ):
            recommendations.append(
                "Consider adding bullet points or numbered lists for easier scanning"
            )

        if "call" in content.lower() or "contact" in content.lower():
            recommendations.append(
                "Ensure contact methods include WhatsApp and local phone numbers for Indian market"
            )

        if "price" in content.lower() or "cost" in content.lower():
            recommendations.append(
                "Include Indian currency formatting and consider mentioning payment options like UPI"
            )

        return recommendations

    def _perform_final_quality_checks(self, content: str) -> Dict[str, bool]:
        """Perform final quality checks before content approval"""

        checks = {
            "no_spelling_errors": True,  # Simplified - would use spell checker in real implementation
            "proper_punctuation": bool(re.search(r"[.!?]", content.strip())),
            "consistent_tense": True,  # Simplified - would need NLP analysis
            "indian_currency_format": bool(re.search(r"₹\s*\d", content)),
            "mobile_friendly_paragraphs": all(
                len(p.split()) <= 100 for p in content.split("\n\n") if p.strip()
            ),
            "includes_call_to_action": bool(
                re.search(
                    r"(contact|call|visit|order|buy|click|share|comment)",
                    content,
                    re.IGNORECASE,
                )
            ),
            "culturally_appropriate": not any(
                term in content.lower()
                for term in ["backward", "primitive", "illiterate"]
            ),
        }

        return checks
