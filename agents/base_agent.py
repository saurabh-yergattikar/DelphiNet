from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
import numpy as np
import pandas as pd
from enum import Enum

class AgentMode(Enum):
    DETECT = "detect"
    PREDICT = "predict" 
    PREVENT = "prevent"
    BROADCAST = "broadcast"

class BaseAgent(ABC):
    """Base class for all SF Neural Precog Network agents with level-up enhancements."""
    
    def __init__(self, name: str, threshold: float = 0.8):
        self.name = name
        self.threshold = threshold
        self.mode = AgentMode.DETECT
        self.confidence = 0.0
        self.level_up_features = {}
        
    def set_mode(self, mode: AgentMode):
        """Set agent operating mode."""
        self.mode = mode
        
    def get_confidence(self) -> float:
        """Get current confidence level."""
        return self.confidence
    
    def update_confidence(self, confidence: float):
        """Update confidence with threshold validation."""
        self.confidence = max(0.0, min(1.0, confidence))
        
    def meets_threshold(self) -> bool:
        """Check if confidence meets threshold for action."""
        return self.confidence >= self.threshold
    
    def add_level_up_feature(self, feature_name: str, feature_data: Any):
        """Add level-up enhancement feature."""
        self.level_up_features[feature_name] = feature_data
        
    def get_level_up_status(self) -> Dict[str, Any]:
        """Get current level-up feature status."""
        return {
            'agent': self.name,
            'mode': self.mode.value,
            'confidence': self.confidence,
            'threshold_met': self.meets_threshold(),
            'level_up_features': self.level_up_features
        }
    
    @abstractmethod
    def detect(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect issues or patterns in data."""
        pass
        
    @abstractmethod
    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Predict future outcomes or risks."""
        pass
        
    @abstractmethod
    def prevent(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate prevention strategies."""
        pass
        
    @abstractmethod
    def broadcast(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Broadcast findings to other agents."""
        pass
    
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute current mode with level-up enhancements."""
        if self.mode == AgentMode.DETECT:
            result = self.detect(data)
        elif self.mode == AgentMode.PREDICT:
            result = self.predict(data)
        elif self.mode == AgentMode.PREVENT:
            result = self.prevent(data)
        elif self.mode == AgentMode.BROADCAST:
            result = self.broadcast(data)
        else:
            raise ValueError(f"Unknown mode: {self.mode}")
            
        # Add level-up status to result
        result['level_up_status'] = self.get_level_up_status()
        return result 