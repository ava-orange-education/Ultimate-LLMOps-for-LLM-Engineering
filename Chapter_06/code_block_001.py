class MemoryManager:
def __init__(self):
    	self.short_term = {}
    	self.long_term = self.load_long_term_memory()
	def remember(self, key, value, memory_type="short"):
    	if memory_type == "short":
        		self.short_term[key] = value
    	else:
        	self.long_term[key] = value
        	self.save_long_term_memory()
	def recall(self, key, memory_type="short"):
    	if memory_type == "short":
        		return self.short_term.get(key)
    	else:
        		return self.long_term.get(key)
	def load_long_term_memory(self):
        	with open('agent_memory.json', 'r') as f:
            		return json.load(f)
	def save_long_term_memory(self):
    		with open('agent_memory.json', 'w') as f:
        			json.dump(self.long_term, f)
class SmartSummarizationAgent:
	def __init__(self):
    	self.memory = MemoryManager()
    	self.preferences = {}
	def summarize_with_memory(self, document, user_id):
    	# Check if we've summarized for this user before
    	user_prefs = self.memory.recall(f"user_{user_id}_preferences", "long")
    	if user_prefs:
        	# Use learned preferences
        	summary_length = user_prefs.get("preferred_length", "medium")
    	else:
        	# Default settings
        	summary_length = "medium"
    	# Generate summary
    	summary = self.generate_summary(document, summary_length)
    	# Remember this interaction
    	self.memory.remember(f"last_summary_{user_id}", {
        	"document_length": len(document),
        	"summary_length": len(summary),
        	"timestamp": datetime.now().isoformat()
    	}, "long")
    	return summary
	def learn_user_preferences(self, user_id, feedback):
    	# Learn from user feedback
    	current_prefs = self.memory.recall(f"user_{user_id}_preferences", "long") or {}
    	if feedback == "too_long":
        		current_prefs["preferred_length"] = "short"
    	elif feedback == "too_short":
        		current_prefs["preferred_length"] = "long"
    	self.memory.remember(f"user_{user_id}_preferences", current_prefs, "long")