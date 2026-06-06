# ============================================
# MODUL DATA PARAMETER
# Menyimpan data sampling dan baku mutu
# EcoSurface v1.0
# ============================================

# Dictionary untuk Panduan Sampling
# Struktur: key = nama parameter, value = detail panduan
sampling_data = {
    "pH": {
        "wadah": "Botol Polietilen (PE) atau Botol Kaca",
        "volume": "500 mL",
        "pengawet": "Tidak ada",
        "penyimpanan": "4°C (Dingin)",
        "holding_time": "14 Hari",
        "catatan": "Ukur segera setelah pengambilan. Hindari agitasi kuat."
    },
    "Suhu": {
        "wadah": "Botol Kaca Amber",
        "volume": "1000 mL",
        "pengawet": "Tidak ada",
        "penyimpanan": "In Situ / Segera diukur",
        "holding_time": "Segera",
        "catatan": "Ukur langsung di lokasi menggunakan termometer."
    },
    "TSS": {
        "wadah": "Botol Polietilen (PE)",
        "volume": "1000 mL",
        "pengawet": "Tidak ada",
        "penyimpanan": "4°C",
        "holding_time": "14 Hari",
        "catatan": "Sampel jangan disaring di lapangan, bawa seluruhnya ke lab."
    },
    "TDS": {
        "wadah": "Botol Polietilen (PE)",
        "volume": "500 mL",
        "pengawet": "Tidak ada",
        "penyimpanan": "4°C",
        "holding_time": "28 Hari",
        "catatan": "Pastikan botol bersih sebelum pengambilan."
    },
    "DO": {
        "wadah": "Botol Kaca (dengan penutup Fuller)",
        "volume": "300 mL",
        "pengawet": "Reagen Winkler (MnSO4 + Alkali-Azida)",
        "penyimpanan": "4°C (Gelap)",
        "holding_time": "4-8 Jam",
        "catatan": "Hindari gelembung udara saat pengambilan sampel."
    },
    "BOD": {
        "wadah": "Botol Kaca Amber / PE",
        "volume": "1000 mL",
        "pengawet": "Tidak ada (Tanpa penambahan kimia)",
        "penyimpanan": "4°C",
        "holding_time": "48 Jam (Maks 72 Jam)",
        "catatan": "Inkubasi segera di lab pada suhu 20°C selama 5 hari."
    },
    "COD": {
        "wadah": "Botol Polietilen (PE)",
        "volume": "500 mL",
        "pengawet": "H2SO4 (Asam Sulfat) hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "28 Hari",
        "catatan": "Sampel harus segera didinginkan setelah pengambilan."
    },
    "Nitrat": {
        "wadah": "Botol Polietilen (PE)",
        "volume": "500 mL",
        "pengawet": "Tidak ada",
        "penyimpanan": "4°C",
        "holding_time": "48 Jam",
        "catatan": "Pendingkan analisis jika > 48 jam."
    },
    "Nitrit": {
        "wadah": "Botol Polietilen (PE)",
        "volume": "500 mL",
        "pengawet": "Tidak ada",
        "penyimpanan": "4°C",
        "holding_time": "48 Jam",
        "catatan": "Hindari paparan cahaya langsung."
    },
    "Amonia": {
        "wadah": "Botol Polietilen (PE)",
        "volume": "500 mL",
        "pengawet": "H2SO4 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "28 Hari",
        "catatan": "Ditambahkan untuk mencegah degradasi biologis."
    },
    "Fosfat": {
        "wadah": "Botol Polietilen (PE)",
        "volume": "500 mL",
        "pengawet": "Tidak ada",
        "penyimpanan": "4°C",
        "holding_time": "28 Hari",
        "catatan": "Cuci botol terlebih dahulu dengan HCl."
    },
    "Sulfat": {
        "wadah": "Botol Polietilen (PE)",
        "volume": "500 mL",
        "pengawet": "Tidak ada",
        "penyimpanan": "4°C",
        "holding_time": "28 Hari",
        "catatan": "Simpan di tempat sejuk."
    },
    "Klorida": {
        "wadah": "Botol Polietilen (PE)",
        "volume": "500 mL",
        "pengawet": "Tidak ada",
        "penyimpan": "4°C",
        "holding_time": "28 Hari",
        "catatan": "Tidak ada catatan khusus."
    },
    "Total Coliform": {
        "wadah": "Botol Steril",
        "volume": "500 mL",
        "pengawet": "Natrium Thiosulfat (untuk netralisir klor)",
        "penyimpanan": "4°C",
        "holding_time": "24 Jam",
        "catatan": "Jaga sterilitas sampel."
    },
    "Fecal Coliform": {
        "wadah": "Botol Steril",
        "volume": "500 mL",
        "pengawet": "Natrium Thiosulfat",
        "penyimpanan": "4°C",
        "holding_time": "24 Jam",
        "catatan": "Jaga sterilitas sampel."
    },
    "Besi (Fe)": {
        "wadah": "Botol Polietilen (PE) / Botol Kaca",
        "volume": "500 mL",
        "pengawet": "HNO3 (Asam Nitrat) hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "6 Bulan",
        "catatan": "Cuci botol terlebih dahulu dengan HCl."
    },
    "Mangan (Mn)": {
        "wadah": "Botol Polietilen (PE)",
        "volume": "500 mL",
        "pengawet": "HNO3 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "6 Bulan",
        "catatan": "Tidak ada catatan khusus."
    }
}

# Dictionary Baku Mutu
# Struktur: key = nama parameter, value = nilai baku mutu (mg/L)
# Logika: "max" = hasil harus <= baku mutu | "min" = hasil harus >= baku mutu (khusus DO)
baku_mutu = {
    "pH": {"nilai": 9, "jenis": "max"},
    "Suhu": {"nilai": 45, "jenis": "max"},
    "TSS": {"nilai": 100, "jenis": "max"},
    "TDS": {"nilai": 1000, "jenis": "max"},
    "DO": {"nilai": 4, "jenis": "min"},  # DO harus >= (minimum)
    "BOD": {"nilai": 30, "jenis": "max"},
    "COD": {"nilai": 50, "jenis": "max"},
    "Nitrat": {"nilai": 20, "jenis": "max"},
    "Nitrit": {"nilai": 1, "jenis": "max"},
    "Amonia": {"nilai": 10, "jenis": "max"},
    "Fosfat": {"nilai": 5, "jenis": "max"},
    "Sulfat": {"nilai": 400, "jenis": "max"},
    "Klorida": {"nilai": 600, "jenis": "max"},
    "Total Coliform": {"nilai": 10000, "jenis": "max"},
    "Fecal Coliform": {"nilai": 1000, "jenis": "max"},
    "Besi (Fe)": {"nilai": 5, "jenis": "max"},
    "Mangan (Mn)": {"nilai": 2, "jenis": "max"}
}

# Daftar parameter yang tersedia untuk dropdown
list_parameter = [
    "pH", "Suhu", "TSS", "TDS", "DO", "BOD", "COD", 
    "Nitrat", "Nitrit", "Amonia", "Fosfat", "Sulfat", 
    "Klorida", "Total Coliform", "Fecal Coliform", 
    "Besi (Fe)", "Mangan (Mn)"
]
