import os
import sys

# Step 1: Add 'src' to Python path
sys.path.append(os.path.join(os.getcwd(), "src"))

# Step 2: Import logger
from text_summarization.logger import logger

# Step 3: Print and log
print(" main.py is running...")  # This prints to terminal
logger.info("welcome to the text summarization project.")

