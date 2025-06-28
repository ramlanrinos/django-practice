from blog.models import Post, Category
from django.core.management.base import BaseCommand
from typing import Any
import random

class Command(BaseCommand):
    help = "This commands inserts posts data"

    def handle(self, *args: Any, **options: Any):
        # Post.objects.all().delete()

        titles = [
            "Quantum Glow Serum for Radiant Skin",
            "HyperSpeed Wireless Charging Pad",
            "EcoPulse Reusable Bamboo Toothbrush",
            "Starlight LED Smart Ceiling Fixture",
            "CloudComfort Memory Foam Pillow",
            "TurboFit Smart Resistance Bands",
            "AquaPure Portable Water Purifier",
            "NovaShield Anti-Theft Backpack",
            "SkyBreeze Compact Air Purifier",
            "FlexiCore Adjustable Laptop Stand",
            "SolarSpark Outdoor Lantern",
            "ZenFlow Aromatherapy Diffuser",
            "PowerGrip Magnetic Phone Mount",
            "VitaBlend Nutrient-Packed Smoothie Mix",
            "ArcticCool Cooling Bed Sheets",
            "StealthCam Wireless Security Camera",
            "PureWave Noise-Canceling Earbuds",
            "EcoChic Recycled Leather Wallet",
            "SmartSip Insulated Travel Mug",
            "LunaMist Hydrating Face Sprayer"
        ]

        contents = [
            "Lightweight serum with peptides and antioxidants for a youthful, glowing complexion.",
            "Ultra-fast 15W charger compatible with all Qi-enabled devices, sleek and compact.",
            "Sustainable toothbrush with soft bristles and ergonomic bamboo handle.",
            "App-controlled LED light with dimming and color-changing features for any mood.",
            "Contoured pillow for neck support and cooling gel for restful sleep.",
            "Set of 3 bands with built-in sensors to track workouts via app.",
            "USB-powered device removes 99.9 of contaminants for safe drinking water.",
            "Water-resistant bag with hidden zippers and USB charging port.",
            "HEPA filter purifier for clean air in small spaces, quiet and portable.",
            "Ergonomic aluminum stand with 6-angle adjustments for comfortable typing.",
            "Solar-powered lantern with 3 brightness modes, ideal for camping.",
            "Ultrasonic diffuser with 7 LED colors and 4 timer settings for relaxation.",
            "360° rotatable car mount with strong magnets for secure phone placement.",
            "Organic superfood powder with vitamins and protein for quick, healthy smoothies.",
            "Breathable, moisture-wicking sheets for a cool and comfortable sleep.",
            "1080p HD camera with night vision and motion detection, app-controlled.",
            "Wireless earbuds with 20-hour battery life and crisp audio quality.",
            "Slim, eco-friendly wallet with RFID protection and 8 card slots.",
            "16oz stainless steel mug keeps drinks hot or cold for 6 hours.",
            "Portable misting device with nano-technology for instant skin hydration."
        ]

        img_urls = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400"   
        ]

        categories = Category.objects.all()

        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Inserting data completed"))