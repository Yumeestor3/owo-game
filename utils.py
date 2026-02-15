import os
from datetime import datetime

def ensure_directories():
    """Pastikan folder ada"""
        if not os.path.exists("data"):
                os.makedirs("data")
                    if not os.path.exists("database"):
                            os.makedirs("database")

                            def truncate_message(text, max_length=200):
                                """Potong pesan jika terlalu panjang"""
                                    if len(text) > max_length:
                                            return text[:max_length-3] + "..."
                                                return text

                                                def get_timestamp():
                                                    """Dapatkan timestamp sekarang"""
                                                        return datetime.now().isoformat()

                                                        def format_number(num):
                                                            """Format angka dengan separator"""
                                                                return f"{num:,}"

                                                                def is_valid_username(username):
                                                                    """Validasi username"""
                                                                        if len(username) < 3:
                                                                                return False
                                                                                    if len(username) > 20:
                                                                                            return False
                                                                                                if not username.replace("_", "").replace("-", "").isalnum():
                                                                                                        return False
                                                                                                            return True

                                                                                                            def get_rarity_emoji(rarity):
                                                                                                                """Dapatkan emoji berdasarkan rarity"""
                                                                                                                    rarity_map = {
                                                                                                                                "common": "⚪",
                                                                                                                                        "uncommon": "🟢",
                                                                                                                                                "rare": "🔵",
                                                                                                                                                        "epic": "🟣",
                                                                                                                                                                "legendary": "🟡"
                                                                                                                    }
                                                                                                                        return rarity_map.get(rarity, "⚪")

                                                                                                                        def calculate_level_progress(exp, max_exp):
                                                                                                                            """Hitung progress level"""
                                                                                                                                progress = (exp / max_exp) * 100
                                                                                                                                    return min(100, progress)

                                                                                                                                    def get_health_status(hp, max_hp):
                                                                                                                                        """Dapatkan status kesehatan"""
                                                                                                                                            percentage = (hp / max_hp) * 100
                                                                                                                                                if percentage >= 75:
                                                                                                                                                        return "💚 Sehat"
                                                                                                                                                            elif percentage >= 50:
                                                                                                                                                                    return "💛 Sedang"
                                                                                                                                                                        elif percentage >= 25:
                                                                                                                                                                                return "🧡 Kritis"
                                                                                                                                                                                    else:
                                                                                                                                                                                            return "❤️ Sangat Kritis"

                                                                                                                                                                                            def log_action(user_id, action, details=""):
                                                                                                                                                                                                """Log aksi pemain"""
                                                                                                                                                                                                    timestamp = get_timestamp()
                                                                                                                                                                                                        log_message = f"[{timestamp}] User {user_id}: {action} - {details}"
                                                                                                                                                                                                            print(log_message)
                                                                                                                                                                                                                
                                                                                                                                                                                                                    # Simpan ke file log
                                                                                                                                                                                                                        with open("logs.txt", "a") as f:
                                                                                                                                                                                                                                f.write(log_message + "\n")

                                                                                                                                                                                                                                def create_csv_files():
                                                                                                                                                                                                                                    """Buat file CSV template"""
                                                                                                                                                                                                                                        import csv
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                # Items CSV
                                                                                                                                                                                                                                                    items_data = [
                                                                                                                                                                                                                                                                ["item_id", "nama", "emoji", "harga", "tipe", "efek_type", "efek_value", "rarity", "deskripsi"],
                                                                                                                                                                                                                                                                        [1, "Roti", "🍞", 50, "consumable", "heal", 20, "common", "Makanan sederhana"],
                                                                                                                                                                                                                                                                                [2, "Ramuan Hidup", "💊", 100, "consumable", "heal", 50, "common", "Ramuan ajaib"],
                                                                                                                                                                                                                                                    ]
                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                            with open("data/items.csv", "w", newline="") as f:
                                                                                                                                                                                                                                                                    writer = csv.writer(f)
                                                                                                                                                                                                                                                                            writer.writerows(items_data)
                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                    print("✅ CSV files created")

                                                                                                                                                                                                                                                                                    ensure_directories()
                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                    ]
                                                                                                                    }