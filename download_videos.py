import os
import yt_dlp
from yt_dlp.utils import download_range_func

output_dir = os.path.join("assets", "videos")
os.makedirs(output_dir, exist_ok=True)

# Konfigurasi video: nama, URL, start time (detik), end time (detik)
videos = [
    {
        "name": "jabar",
        "url": "https://www.youtube.com/watch?v=DoLRv-WknXU",
        "start": 15,   # Mulai detik 15
        "end": 35      # Selesai detik 35 (20 detik Tari Jaipong HD)
    },
    {
        "name": "jogja",
        "url": "https://www.youtube.com/watch?v=7w6x29DnKts",
        "start": 20,   # Mulai detik 20
        "end": 45      # Selesai detik 45 (25 detik Wayang Kulit HD)
    },
    {
        "name": "jatim",
        "url": "https://www.youtube.com/watch?v=fho5a1Ow71A",
        "start": 30,   # Mulai detik 30
        "end": 55      # Selesai detik 55 (25 detik Reog Ponorogo HD)
    },
    {
        "name": "keraton",
        "url": "https://www.youtube.com/watch?v=M3Nk-qfnGC4",
        "start": 10,   # Mulai detik 10
        "end": 35      # Selesai detik 35 (25 detik visual Keraton HD)
    }
]

for item in videos:
    print(f"\n Sedang mengunduh {item['name']} (HD, durasi {item['start']}s - {item['end']}s)...")
    
    ydl_opts = {
        # Ambil video kualitas tertinggi (1080p/720p) dalam format mp4
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best',
        'outtmpl': os.path.join(output_dir, f"{item['name']}.%(ext)s"),
        'overwrites': True,
        # Potong menit/detik langsung saat download:
        'download_ranges': download_range_func(None, [(item['start'], item['end'])]),
        'force_keyframes_at_cuts': True,
        # Bypass SABR streaming YouTube client mobile:
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'ios']
            }
        },
        'nocheckcertificate': True
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([item['url']])
    except Exception as e:
        print(f"Error {item['name']}: {e}")

print("\n Selesai! Semua video HD yang sudah terpotong rapi tersimpan di assets/videos/")