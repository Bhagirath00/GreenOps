# Cell 1: Installation & Setup
!pip install -U -q google-generativeai requests numpy matplotlib folium

import os
import time
import json
import requests
import asyncio
import numpy as np  
import matplotlib.pyplot as plt  
import folium  
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
from google.ai.generativelanguage import Part, FunctionResponse
from IPython.display import display, Image 

print("✅ Dependencies installed and libraries imported.")