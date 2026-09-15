"""Konstanta terpusat untuk seluruh submission.

Semua nilai yang diwajibkan instruksi submission (ID model dan seed) dikunci di
sini supaya notebook dan aplikasi Streamlit memakai nilai yang persis sama.
"""

# --- Model wajib sesuai instruksi submission -------------------------------
MODEL_T2I = "stable-diffusion-v1-5/stable-diffusion-v1-5"
MODEL_INPAINT = "stable-diffusion-v1-5/stable-diffusion-inpainting"

# --- Seed wajib ------------------------------------------------------------
SEED_ASTRONAUT = 222  # Kriteria 1: text-to-image astronot di bulan
SEED_SATELLITE = 9    # Kriteria 2: inpainting satelit rusak

# --- Prompt Kriteria 1 -----------------------------------------------------
PROMPT_ASTRONAUT = (
    "2D digital art illustration of an astronaut in a white spacesuit "
    "standing on the surface of the moon, planet Earth visible in the starry "
    "sky above, flat vector style, clean lines, vibrant colors, "
    "highly detailed, artstation"
)

# CATATAN: ganti string ini dengan negative prompt persis dari instruksi
# submission bila redaksinya berbeda. Nilai di bawah mengikuti pembukaan yang
# diwajibkan ("photorealistic, realistic, photograph, ...").
NEGATIVE_PROMPT = (
    "photorealistic, realistic, photograph, photo, 3d render, hyperrealistic, "
    "blurry, low quality, low resolution, distorted, deformed, disfigured, "
    "bad anatomy, extra limbs, watermark, text, signature"
)

# --- Prompt Kriteria 2 -----------------------------------------------------
PROMPT_SATELLITE = (
    "a broken satellite crashed on the moon surface, damaged solar panels, "
    "torn metal panels, floating debris, 2D digital art illustration, "
    "same flat vector style, consistent lighting"
)

NEGATIVE_PROMPT_SATELLITE = (
    "photorealistic, realistic, photograph, blurry, low quality, "
    "distorted, deformed, watermark, text"
)

# --- Nilai default parameter inferensi ------------------------------------
DEFAULT_GUIDANCE_SCALE = 7.5
DEFAULT_NUM_INFERENCE_STEPS = 30
DEFAULT_HEIGHT = 512
DEFAULT_WIDTH = 512

# --- Scheduler yang wajib tersedia ----------------------------------------
SCHEDULER_CHOICES = ("Euler A", "DPM++", "DDIM")

# --- Lokasi output ---------------------------------------------------------
OUTPUT_DIR = "outputs"
