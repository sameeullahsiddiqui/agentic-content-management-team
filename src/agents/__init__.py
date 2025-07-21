"""
AutoGen Content Team India - Agents Package
All AI agents for content creation specialized for Indian markets

Author: Samee Ullah Siddiqui
Repository: https://github.com/sameeullahsiddiqui/agentic-content-management-team
"""

from base_agent import BaseAgent
from .project_manager_agent import ProjectManagerAgent
from .content_writer_agent import ContentWriterAgent
from .content_editor_agent import ContentEditorAgent
from .seo_specilist_agent import SEOSpecialistAgent
from .brand_strategist_agent import BrandStrategistAgent

__all__ = [
    "BaseAgent",
    "ProjectManagerAgent", 
    "ContentWriterAgent",
    "ContentEditorAgent",
    "SEOSpecialistAgent",
    "BrandStrategistAgent"
]

# Agent registry for easy access
AGENT_REGISTRY = {
    "project_manager": ProjectManagerAgent,
    "content_writer": ContentWriterAgent,
    "content_editor": ContentEditorAgent,
    "seo_specialist": SEOSpecialistAgent,
    "brand_strategist": BrandStrategistAgent
}

def get_agent_class(agent_type: str):
    """Get agent class by type name"""
    return AGENT_REGISTRY.get(agent_type.lower())

def list_available_agents():
    """List all available agent types"""
    return list(AGENT_REGISTRY.keys())

# Version info
__version__ = "1.0.0"
__author__ = "Samee Ullah Siddiqui"