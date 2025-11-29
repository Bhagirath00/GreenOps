# Cell 1: Installation & Setup
!pip install -U -q google-generativeai requests numpy matplotlib folium

import os
import time
import json
import requests
import asyncio
import numpy as np  # Added for Cell 3
import matplotlib.pyplot as plt  # Added for Cell 10
import folium  # Added for Cell 11
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
from google.ai.generativelanguage import Part, FunctionResponse
from IPython.display import display, Image # Added for Cell 10

print("✅ Dependencies installed and libraries imported.")