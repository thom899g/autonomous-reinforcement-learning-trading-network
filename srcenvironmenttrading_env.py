"""
Reinforcement Learning Trading Environment
Implements Gymnasium interface for standardized RL training
Handles market simulation, portfolio management, and reward calculation
"""

import gymnasium as gym
import numpy as np
import pandas as pd
from typing import Tuple, Dict, Any, Optional
from dataclasses import dataclass
from loguru import logger
import warnings
from datetime import datetime

warnings.filterw