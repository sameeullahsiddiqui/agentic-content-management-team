# Quick Start Guide - AutoGen Content Team India

Get up and running with AI-powered content creation for Indian markets in under 10 minutes!

## Super Quick Setup (2 minutes)

### 1. Clone and Install
```bash
git clone https://github.com/sameeullahsiddiqui/agentic-content-management-team.git
cd agentic-content-management-team
pip install -r requirements.txt
```

### 2. Set Your API Key
**Option A: OpenAI**
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

**Option B: Azure OpenAI**
```bash
export AZURE_OPENAI_API_KEY="your-azure-key"
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
export AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4"
```

### 3. Run Your First Content Creation
```bash
python main.py
```

**That's it!** Choose option 1 from the menu to create restaurant content.

---

## Quick Examples

### Mumbai Restaurant Campaign
```python
from src.content_team import ContentCreationTeam

# Auto-detects your API configuration
team = ContentCreationTeam()

# Create social media campaign
results = team.create_social_media_campaign("""
Create content for 'Spice Route', a South Indian restaurant in Mumbai's Bandra.
Target: Young professionals, ₹200-400 price range
Goal: Drive lunch traffic from BKC offices
""")
```

### Tech Startup Blog
```python
results = team.create_blog_article(
    topic="How AI is Transforming Rural Education in India",
    target_audience="Education policymakers and investors"
)
```

### E-commerce Festival Campaign
```python
results = team.create_content("""
Diwali sale campaign for ethnic wear platform
Target: Indian women 22-45, metro and tier-2 cities
Offer: 70% off, free shipping, authentic designs
""")
```

---

##  Configuration Options

### Environment Variables (.env)
```env
# Choose your LLM provider
OPENAI_API_KEY=your_key_here
# OR
AZURE_OPENAI_API_KEY=your_azure_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

# Customize for your market
TARGET_REGIONS=mumbai,delhi,bangalore
DEFAULT_LANGUAGE=english
INCLUDE_HINDI_PHRASES=true
```

### Agent Customization (config/agents.yaml)
```yaml
content_writer:
  temperature: 0.7  # Creativity level
  max_tokens: 2000  # Content length
  specializations:
    - indian_cultural_context
    - simple_english_writing
```

---

## Platform-Specific Content

### Social Media Campaigns
```python
team.create_social_media_campaign("your brief here")
```
**Generates:**
- Instagram posts with hashtags
- Facebook community content  
- LinkedIn professional posts
- WhatsApp Business messages

### Blog Articles
```python
team.create_blog_article("your topic", "target audience")
```
**Generates:**
- SEO-optimized headlines
- Indian market examples
- Cultural context integration
- Call-to-actions for Indian users

### Email Marketing
```python
team.create_email_campaign("campaign objective", "audience segment")
```
**Generates:**
- Welcome email series
- Festival campaign emails
- Customer retention content
- Mobile-optimized templates

---

## Indian Market Specialization

### Cultural Context
- Festival calendar integration (Diwali, Holi, Eid)
- Regional preferences (Mumbai vs Delhi vs Bangalore)
- Tier-2 and Tier-3 city considerations
- Hindi phrases and local references

### Business Context  
- UPI payment mentions
- WhatsApp Business integration
- Mobile-first optimization
- Indian pricing psychology (₹199 vs ₹200)

### Compliance
- ASCI advertising guidelines
- Consumer Protection Act compliance
- Data protection considerations
- Regional regulation awareness

---

## Pro Tips

### 1. Start with Templates
Use our industry-specific examples:
- `examples/mumbai_restaurant.py` - Food & beverage
- `examples/bangalore_startup.py` - Technology  
- `examples/diwali_campaign.py` - E-commerce

### 2. Customize Agent Behavior
Edit `config/agents.yaml` to:
- Adjust creativity levels (temperature)
- Set content length preferences
- Define regional focus areas
- Customize writing styles

### 3. Batch Content Creation
```python
# Create multiple content types at once
topics = ["AI in education", "Digital payments growth", "Startup funding trends"]
for topic in topics:
    team.create_blog_article(topic, "Indian businesses")
```

### 4. Cost Optimization
- Use `gpt-3.5-turbo` for simple tasks
- Set `max_tokens` appropriately  
- Cache results for similar requests
- Monitor usage with `team.get_performance_report()`

---

## Troubleshooting

### Common Issues

** "No LLM configuration found"**
```bash
# Make sure API key is set
echo $OPENAI_API_KEY
# or
echo $AZURE_OPENAI_API_KEY
```

** "AutoGen not installed"**
```bash
pip install pyautogen
# or for latest version
pip install autogen-agentchat autogen-ext[openai]
```

** "Permission denied on output directory"**
```bash
mkdir output
chmod 755 output
```

** API rate limits**
```bash
# Reduce concurrent requests
export RATE_LIMIT_PER_MINUTE=30
```

### Getting Help

1. **Check the logs**: Look in `output/` for error details
2. **GitHub Issues**: [Report bugs here](https://github.com/sameeullahsiddiqui/agentic-content-management-team/issues)
3. **Community**: Join our [Telegram group](https://t.me/autogen_india)
4. **Documentation**: See `docs/` folder for detailed guides

---

## Next Steps

### Beginner Path
1. Run the quick examples above
2. Try different content types (blog, social, email)
3. Customize agent settings
4. Review generated content quality

### Advanced Path  
1. Create custom agents for your industry
2. Add regional language support
3. Integrate with social media APIs
4. Set up performance monitoring

### Enterprise Path
1. Deploy on Azure/AWS infrastructure
2. Set up team collaboration workflows
3. Integrate with analytics platforms
4. Implement security and compliance measures

---

## Quick Reference

### Command Line Usage
```bash
python main.py                    # Interactive menu
python examples/mumbai_restaurant.py  # Specific example
python -m pytest tests/          # Run tests
```

### Python API
```python
from src.content_team import ContentCreationTeam

# Initialize with auto-detection
team = ContentCreationTeam()

# Or specify configuration
team = ContentCreationTeam({
    "provider": "azure",
    "api_key": "your-key",
    "endpoint": "your-endpoint",
    "model": "gpt-4.1"
})

# Create content
results = team.create_content("your brief", "content_type")
```

### File Structure
```
output/                    # Generated content
config/agents.yaml        # Agent configurations  
examples/                 # Ready-to-use examples
src/content_team.py       # Main library
docs/                     # Detailed documentation
```

---

**🌟 Star us on GitHub if this helps your business!**  
**Questions? Open an issue or join our community chat**

[Back to Main README](README.md) | [Full Documentation](docs/) | [Report Issues](https://github.com/sameeullahsiddiqui/agentic-content-management-team/issues)