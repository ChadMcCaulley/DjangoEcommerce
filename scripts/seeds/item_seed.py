import json
import os
from datetime import datetime
from core.models import (
    Item, ItemVariant
)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
seed_dir = os.path.join(base_dir, "seeds/movie_seed.json")
