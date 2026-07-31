# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: PromoPlanner
def load_profiles():
    profiles = []
    path = os.path.join(BASE_DIR, 'profiles.json')
    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
            for p in data.get('profiles', []):
                profiles.append(p)
    return profiles

def save_profiles(profiles):
    path = os.path.join(BASE_DIR, 'profiles.json')
    with open(path, 'w') as f:
        json.dump({'profiles': profiles}, f, indent=2)

class UserProfiles:
    _instance = None
    
    def __init__(self):
        self.profiles = load_profiles() if not self._loaded else list(self.profiles)
        self._loaded = True
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = UserProfiles()
        return cls._instance
    
    def add_profile(self, name, role='user', budget_limit=None):
        for p in self.profiles:
            if p['name'] == name:
                raise ValueError(f'Профиль "{name}" уже существует')
        self.profiles.append({'name': name, 'role': role, 'budget_limit': budget_limit})
        save_profiles(self.profiles)
    
    def remove_profile(self, name):
        for i, p in enumerate(self.profiles):
            if p['name'] == name:
                self.profiles.pop(i)
                save_profiles(self.profiles)
                return True
        return False
    
    def get_profile(self, name):
        for p in self.profiles:
            if p['name'] == name:
                return dict(p)
        return None
    
    def list_profiles(self):
        return [dict(p) for p in self.profiles]
